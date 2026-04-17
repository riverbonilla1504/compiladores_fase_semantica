from antlr4 import ParseTreeVisitor
from WhileLangVisitor import WhileLangVisitor
from WhileLangParser import WhileLangParser

class SemanticVisitor(WhileLangVisitor):
    def __init__(self):
        self.scopes = []
        self.errors = []
        self.push_scope()

    def push_scope(self):
        self.scopes.append({})

    def pop_scope(self):
        if self.scopes:
            self.scopes.pop()

    def current_scope(self):
        return self.scopes[-1]

    def declare_variable(self, name, var_type, ctx):
        if name in self.current_scope():
            self.errors.append(f"Error semántico: redeclaración de variable '{name}' en el mismo scope en la línea {ctx.start.line}")
            return
        self.current_scope()[name] = var_type

    def resolve_variable(self, name, ctx):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        self.errors.append(f"Error semántico: variable no declarada '{name}' usada en la línea {ctx.start.line}")
        return None

    def visitProgram(self, ctx:WhileLangParser.ProgramContext):
        for statement in ctx.statement():
            self.visit(statement)
        return None

    def visitDeclaration(self, ctx:WhileLangParser.DeclarationContext):
        var_type = ctx.type_().getText()
        name = ctx.ID().getText()
        expr_type = self.visit(ctx.expr())

        if name in self.current_scope():
            self.errors.append(f"Error semántico: redeclaración de variable '{name}' en el mismo scope en la línea {ctx.start.line}")
            return None

        if expr_type is None:
            self.declare_variable(name, var_type, ctx)
            return None

        if expr_type != var_type:
            self.errors.append(
                f"Error semántico: asignación de tipo incompatible en la declaración de '{name}' (esperado {var_type}, obtenido {expr_type}) en la línea {ctx.start.line}"
            )
        self.declare_variable(name, var_type, ctx)
        return None

    def visitAssignment(self, ctx:WhileLangParser.AssignmentContext):
        name = ctx.ID().getText()
        var_type = self.resolve_variable(name, ctx)
        expr_type = self.visit(ctx.expr())

        if var_type is None or expr_type is None:
            return None

        if var_type != expr_type:
            self.errors.append(
                f"Error semántico: asignación de tipo incompatible en '{name}' (esperado {var_type}, obtenido {expr_type}) en la línea {ctx.start.line}"
            )
        return None

    def visitWhileStatement(self, ctx:WhileLangParser.WhileStatementContext):
        condition_type = self.visit(ctx.condition())
        if condition_type is None:
            condition_type = 'int'
        self.push_scope()
        for statement in ctx.statement():
            self.visit(statement)
        self.pop_scope()
        return None

    def visitIfStatement(self, ctx:WhileLangParser.IfStatementContext):
        self.visit(ctx.condition())
        if_statements = []
        else_statements = []
        in_else = False

        for child in ctx.getChildren():
            child_text = child.getText()
            if child_text == 'else':
                in_else = True
            elif hasattr(child, 'getRuleIndex') and child.getRuleIndex() == WhileLangParser.RULE_statement:
                if in_else:
                    else_statements.append(child)
                else:
                    if_statements.append(child)

        self.push_scope()
        for statement in if_statements:
            self.visit(statement)
        self.pop_scope()

        if else_statements:
            self.push_scope()
            for statement in else_statements:
                self.visit(statement)
            self.pop_scope()
        return None

    def visitBreakStatement(self, ctx:WhileLangParser.BreakStatementContext):
        return None

    def visitContinueStatement(self, ctx:WhileLangParser.ContinueStatementContext):
        return None

    def visitExprCondition(self, ctx:WhileLangParser.ExprConditionContext):
        expr_type = self.visit(ctx.expr())
        if expr_type != 'int':
            self.errors.append(
                f"Error semántico: condición debe ser de tipo int en la línea {ctx.start.line}, se obtuvo {expr_type}"
            )
        return 'int'

    def visitComparisonCondition(self, ctx:WhileLangParser.ComparisonConditionContext):
        left_type = self.visit(ctx.expr(0))
        right_type = self.visit(ctx.expr(1))
        if left_type != 'int' or right_type != 'int':
            self.errors.append(
                f"Error semántico: comparación solo permitida entre int en la línea {ctx.start.line} (tipos: {left_type}, {right_type})"
            )
        return 'int'

    def visitStringExpr(self, ctx:WhileLangParser.StringExprContext):
        return 'string'

    def visitNumberExpr(self, ctx:WhileLangParser.NumberExprContext):
        return 'int'

    def visitParenExpr(self, ctx:WhileLangParser.ParenExprContext):
        return self.visit(ctx.expr())

    def visitIdExpr(self, ctx:WhileLangParser.IdExprContext):
        return self.resolve_variable(ctx.ID().getText(), ctx)

    def visitArithmeticExpr(self, ctx:WhileLangParser.ArithmeticExprContext):
        left_type = self.visit(ctx.expr(0))
        right_type = self.visit(ctx.expr(1))
        operator = ctx.getChild(1).getText()

        if left_type is None or right_type is None:
            return None

        if operator == '+':
            if left_type == 'int' and right_type == 'int':
                return 'int'
            if left_type == 'string' and right_type == 'string':
                return 'string'
            self.errors.append(
                f"Error semántico: operador '+' solo permite int+int o string+string en la línea {ctx.start.line} (tipos: {left_type}, {right_type})"
            )
            return None

        if operator in ['-', '*', '/']:
            if left_type == 'int' and right_type == 'int':
                return 'int'
            self.errors.append(
                f"Error semántico: operador '{operator}' solo permite int*int/int/int o int-int en la línea {ctx.start.line} (tipos: {left_type}, {right_type})"
            )
            return None

        self.errors.append(f"Error semántico: operador desconocido '{operator}' en la línea {ctx.start.line}")
        return None
