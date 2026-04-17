import sys
from antlr4 import FileStream, CommonTokenStream
from WhileLangLexer import WhileLangLexer
from WhileLangParser import WhileLangParser
from SemanticVisitor import SemanticVisitor


def main():
    if len(sys.argv) != 2:
        print('Uso: python main.py <archivo.txt>')
        sys.exit(1)

    input_path = sys.argv[1]
    input_stream = FileStream(input_path, encoding='utf-8')
    lexer = WhileLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = WhileLangParser(token_stream)
    tree = parser.program()

    visitor = SemanticVisitor()
    visitor.visit(tree)

    if visitor.errors:
        for error in visitor.errors:
            print(error)
    else:
        print('✓ Sin errores semánticos')


if __name__ == '__main__':
    main()
