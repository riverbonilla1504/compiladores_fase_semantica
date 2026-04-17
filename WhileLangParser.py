# Generated from WhileLang.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,25,118,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,4,0,24,8,0,11,0,12,0,25,
        1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,36,8,1,1,2,1,2,1,2,1,2,1,2,1,
        2,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,5,5,57,8,5,
        10,5,12,5,60,9,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,5,6,70,8,6,10,6,
        12,6,73,9,6,1,6,1,6,1,6,1,6,5,6,79,8,6,10,6,12,6,82,9,6,1,6,3,6,
        85,8,6,1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,3,9,98,8,9,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,108,8,10,1,10,1,10,1,
        10,5,10,113,8,10,10,10,12,10,116,9,10,1,10,0,1,20,11,0,2,4,6,8,10,
        12,14,16,18,20,0,3,1,0,6,7,1,0,14,17,1,0,18,21,121,0,23,1,0,0,0,
        2,35,1,0,0,0,4,37,1,0,0,0,6,43,1,0,0,0,8,45,1,0,0,0,10,50,1,0,0,
        0,12,63,1,0,0,0,14,86,1,0,0,0,16,89,1,0,0,0,18,97,1,0,0,0,20,107,
        1,0,0,0,22,24,3,2,1,0,23,22,1,0,0,0,24,25,1,0,0,0,25,23,1,0,0,0,
        25,26,1,0,0,0,26,27,1,0,0,0,27,28,5,0,0,1,28,1,1,0,0,0,29,36,3,4,
        2,0,30,36,3,8,4,0,31,36,3,10,5,0,32,36,3,12,6,0,33,36,3,14,7,0,34,
        36,3,16,8,0,35,29,1,0,0,0,35,30,1,0,0,0,35,31,1,0,0,0,35,32,1,0,
        0,0,35,33,1,0,0,0,35,34,1,0,0,0,36,3,1,0,0,0,37,38,3,6,3,0,38,39,
        5,23,0,0,39,40,5,13,0,0,40,41,3,20,10,0,41,42,5,12,0,0,42,5,1,0,
        0,0,43,44,7,0,0,0,44,7,1,0,0,0,45,46,5,23,0,0,46,47,5,13,0,0,47,
        48,3,20,10,0,48,49,5,12,0,0,49,9,1,0,0,0,50,51,5,1,0,0,51,52,5,8,
        0,0,52,53,3,18,9,0,53,54,5,9,0,0,54,58,5,10,0,0,55,57,3,2,1,0,56,
        55,1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,58,59,1,0,0,0,59,61,1,0,0,
        0,60,58,1,0,0,0,61,62,5,11,0,0,62,11,1,0,0,0,63,64,5,2,0,0,64,65,
        5,8,0,0,65,66,3,18,9,0,66,67,5,9,0,0,67,71,5,10,0,0,68,70,3,2,1,
        0,69,68,1,0,0,0,70,73,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,74,
        1,0,0,0,73,71,1,0,0,0,74,84,5,11,0,0,75,76,5,3,0,0,76,80,5,10,0,
        0,77,79,3,2,1,0,78,77,1,0,0,0,79,82,1,0,0,0,80,78,1,0,0,0,80,81,
        1,0,0,0,81,83,1,0,0,0,82,80,1,0,0,0,83,85,5,11,0,0,84,75,1,0,0,0,
        84,85,1,0,0,0,85,13,1,0,0,0,86,87,5,4,0,0,87,88,5,12,0,0,88,15,1,
        0,0,0,89,90,5,5,0,0,90,91,5,12,0,0,91,17,1,0,0,0,92,98,3,20,10,0,
        93,94,3,20,10,0,94,95,7,1,0,0,95,96,3,20,10,0,96,98,1,0,0,0,97,92,
        1,0,0,0,97,93,1,0,0,0,98,19,1,0,0,0,99,100,6,10,-1,0,100,108,5,23,
        0,0,101,108,5,24,0,0,102,108,5,22,0,0,103,104,5,8,0,0,104,105,3,
        20,10,0,105,106,5,9,0,0,106,108,1,0,0,0,107,99,1,0,0,0,107,101,1,
        0,0,0,107,102,1,0,0,0,107,103,1,0,0,0,108,114,1,0,0,0,109,110,10,
        2,0,0,110,111,7,2,0,0,111,113,3,20,10,3,112,109,1,0,0,0,113,116,
        1,0,0,0,114,112,1,0,0,0,114,115,1,0,0,0,115,21,1,0,0,0,116,114,1,
        0,0,0,9,25,35,58,71,80,84,97,107,114
    ]

class WhileLangParser ( Parser ):

    grammarFileName = "WhileLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'while'", "'if'", "'else'", "'break'", 
                     "'continue'", "'int'", "'string'", "'('", "')'", "'{'", 
                     "'}'", "';'", "'='", "'>'", "'<'", "'=='", "'!='", 
                     "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "WHILE", "IF", "ELSE", "BREAK", "CONTINUE", 
                      "INT_TYPE", "STRING_TYPE", "LPAREN", "RPAREN", "LBRACE", 
                      "RBRACE", "SEMI", "ASSIGN", "GT", "LT", "EQ", "NE", 
                      "PLUS", "MINUS", "MULT", "DIV", "STRING", "ID", "NUMBER", 
                      "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_declaration = 2
    RULE_type = 3
    RULE_assignment = 4
    RULE_whileStatement = 5
    RULE_ifStatement = 6
    RULE_breakStatement = 7
    RULE_continueStatement = 8
    RULE_condition = 9
    RULE_expr = 10

    ruleNames =  [ "program", "statement", "declaration", "type", "assignment", 
                   "whileStatement", "ifStatement", "breakStatement", "continueStatement", 
                   "condition", "expr" ]

    EOF = Token.EOF
    WHILE=1
    IF=2
    ELSE=3
    BREAK=4
    CONTINUE=5
    INT_TYPE=6
    STRING_TYPE=7
    LPAREN=8
    RPAREN=9
    LBRACE=10
    RBRACE=11
    SEMI=12
    ASSIGN=13
    GT=14
    LT=15
    EQ=16
    NE=17
    PLUS=18
    MINUS=19
    MULT=20
    DIV=21
    STRING=22
    ID=23
    NUMBER=24
    WS=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(WhileLangParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(WhileLangParser.StatementContext,i)


        def getRuleIndex(self):
            return WhileLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = WhileLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self.statement()
                self.state = 25 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 8388854) != 0)):
                    break

            self.state = 27
            self.match(WhileLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(WhileLangParser.DeclarationContext,0)


        def assignment(self):
            return self.getTypedRuleContext(WhileLangParser.AssignmentContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(WhileLangParser.WhileStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(WhileLangParser.IfStatementContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(WhileLangParser.BreakStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(WhileLangParser.ContinueStatementContext,0)


        def getRuleIndex(self):
            return WhileLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = WhileLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.declaration()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.assignment()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.whileStatement()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 4)
                self.state = 32
                self.ifStatement()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 33
                self.breakStatement()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 34
                self.continueStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(WhileLangParser.TypeContext,0)


        def ID(self):
            return self.getToken(WhileLangParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(WhileLangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(WhileLangParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(WhileLangParser.SEMI, 0)

        def getRuleIndex(self):
            return WhileLangParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = WhileLangParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.type_()
            self.state = 38
            self.match(WhileLangParser.ID)
            self.state = 39
            self.match(WhileLangParser.ASSIGN)
            self.state = 40
            self.expr(0)
            self.state = 41
            self.match(WhileLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_TYPE(self):
            return self.getToken(WhileLangParser.INT_TYPE, 0)

        def STRING_TYPE(self):
            return self.getToken(WhileLangParser.STRING_TYPE, 0)

        def getRuleIndex(self):
            return WhileLangParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = WhileLangParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            _la = self._input.LA(1)
            if not(_la==6 or _la==7):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(WhileLangParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(WhileLangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(WhileLangParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(WhileLangParser.SEMI, 0)

        def getRuleIndex(self):
            return WhileLangParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = WhileLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(WhileLangParser.ID)
            self.state = 46
            self.match(WhileLangParser.ASSIGN)
            self.state = 47
            self.expr(0)
            self.state = 48
            self.match(WhileLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(WhileLangParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(WhileLangParser.LPAREN, 0)

        def condition(self):
            return self.getTypedRuleContext(WhileLangParser.ConditionContext,0)


        def RPAREN(self):
            return self.getToken(WhileLangParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(WhileLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(WhileLangParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(WhileLangParser.StatementContext,i)


        def getRuleIndex(self):
            return WhileLangParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = WhileLangParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_whileStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(WhileLangParser.WHILE)
            self.state = 51
            self.match(WhileLangParser.LPAREN)
            self.state = 52
            self.condition()
            self.state = 53
            self.match(WhileLangParser.RPAREN)
            self.state = 54
            self.match(WhileLangParser.LBRACE)
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8388854) != 0):
                self.state = 55
                self.statement()
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 61
            self.match(WhileLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(WhileLangParser.IF, 0)

        def LPAREN(self):
            return self.getToken(WhileLangParser.LPAREN, 0)

        def condition(self):
            return self.getTypedRuleContext(WhileLangParser.ConditionContext,0)


        def RPAREN(self):
            return self.getToken(WhileLangParser.RPAREN, 0)

        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(WhileLangParser.LBRACE)
            else:
                return self.getToken(WhileLangParser.LBRACE, i)

        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(WhileLangParser.RBRACE)
            else:
                return self.getToken(WhileLangParser.RBRACE, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(WhileLangParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(WhileLangParser.ELSE, 0)

        def getRuleIndex(self):
            return WhileLangParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = WhileLangParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(WhileLangParser.IF)
            self.state = 64
            self.match(WhileLangParser.LPAREN)
            self.state = 65
            self.condition()
            self.state = 66
            self.match(WhileLangParser.RPAREN)
            self.state = 67
            self.match(WhileLangParser.LBRACE)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8388854) != 0):
                self.state = 68
                self.statement()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 74
            self.match(WhileLangParser.RBRACE)
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 75
                self.match(WhileLangParser.ELSE)
                self.state = 76
                self.match(WhileLangParser.LBRACE)
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8388854) != 0):
                    self.state = 77
                    self.statement()
                    self.state = 82
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 83
                self.match(WhileLangParser.RBRACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(WhileLangParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(WhileLangParser.SEMI, 0)

        def getRuleIndex(self):
            return WhileLangParser.RULE_breakStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStatement" ):
                listener.enterBreakStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStatement" ):
                listener.exitBreakStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStatement" ):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)




    def breakStatement(self):

        localctx = WhileLangParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(WhileLangParser.BREAK)
            self.state = 87
            self.match(WhileLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(WhileLangParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(WhileLangParser.SEMI, 0)

        def getRuleIndex(self):
            return WhileLangParser.RULE_continueStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinueStatement" ):
                listener.enterContinueStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinueStatement" ):
                listener.exitContinueStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStatement" ):
                return visitor.visitContinueStatement(self)
            else:
                return visitor.visitChildren(self)




    def continueStatement(self):

        localctx = WhileLangParser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(WhileLangParser.CONTINUE)
            self.state = 90
            self.match(WhileLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WhileLangParser.RULE_condition

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ComparisonConditionContext(ConditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileLangParser.ConditionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(WhileLangParser.ExprContext,i)

        def GT(self):
            return self.getToken(WhileLangParser.GT, 0)
        def LT(self):
            return self.getToken(WhileLangParser.LT, 0)
        def EQ(self):
            return self.getToken(WhileLangParser.EQ, 0)
        def NE(self):
            return self.getToken(WhileLangParser.NE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonCondition" ):
                listener.enterComparisonCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonCondition" ):
                listener.exitComparisonCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonCondition" ):
                return visitor.visitComparisonCondition(self)
            else:
                return visitor.visitChildren(self)


    class ExprConditionContext(ConditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileLangParser.ConditionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(WhileLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprCondition" ):
                listener.enterExprCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprCondition" ):
                listener.exitExprCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprCondition" ):
                return visitor.visitExprCondition(self)
            else:
                return visitor.visitChildren(self)



    def condition(self):

        localctx = WhileLangParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.state = 97
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = WhileLangParser.ExprConditionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = WhileLangParser.ComparisonConditionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self.expr(0)
                self.state = 94
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 245760) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 95
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WhileLangParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class StringExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(WhileLangParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringExpr" ):
                listener.enterStringExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringExpr" ):
                listener.exitStringExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringExpr" ):
                return visitor.visitStringExpr(self)
            else:
                return visitor.visitChildren(self)


    class NumberExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(WhileLangParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpr" ):
                listener.enterNumberExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpr" ):
                listener.exitNumberExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExpr" ):
                return visitor.visitNumberExpr(self)
            else:
                return visitor.visitChildren(self)


    class ArithmeticExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(WhileLangParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(WhileLangParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(WhileLangParser.MINUS, 0)
        def MULT(self):
            return self.getToken(WhileLangParser.MULT, 0)
        def DIV(self):
            return self.getToken(WhileLangParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmeticExpr" ):
                listener.enterArithmeticExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmeticExpr" ):
                listener.exitArithmeticExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmeticExpr" ):
                return visitor.visitArithmeticExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(WhileLangParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(WhileLangParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(WhileLangParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class IdExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(WhileLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdExpr" ):
                listener.enterIdExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdExpr" ):
                listener.exitIdExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdExpr" ):
                return visitor.visitIdExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = WhileLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                localctx = WhileLangParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 100
                self.match(WhileLangParser.ID)
                pass
            elif token in [24]:
                localctx = WhileLangParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 101
                self.match(WhileLangParser.NUMBER)
                pass
            elif token in [22]:
                localctx = WhileLangParser.StringExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 102
                self.match(WhileLangParser.STRING)
                pass
            elif token in [8]:
                localctx = WhileLangParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 103
                self.match(WhileLangParser.LPAREN)
                self.state = 104
                self.expr(0)
                self.state = 105
                self.match(WhileLangParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 114
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = WhileLangParser.ArithmeticExprContext(self, WhileLangParser.ExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 109
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 110
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3932160) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 111
                    self.expr(3) 
                self.state = 116
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[10] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




