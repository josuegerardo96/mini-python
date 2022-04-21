from miParserVisitor import *
from miParserParser import *

class AContextual(miParserVisitor):
    def visitProgramAST(self, ctx: miParserParser.ProgramASTContext):
        return super().visitProgramAST(ctx)

    def visitStatement(self, ctx: miParserParser.StatementContext):
        return super().visitStatement(ctx)

    def visitDefStatementAST(self, ctx: miParserParser.DefStatementASTContext):
        return super().visitDefStatementAST(ctx)

# meter todos el código, todos los visits

# para leer el token
    #ctx.IDENTIFIER().symbol
    #ctx.IDENTIFIER().getSymbol()

#buscar no pide token pide texto
    # ctx.IDENTIFIER().symbol.text
    # ctx.IDENTIFIER().symbol.text()

# para reportar errores, necesitamos guardar errores sintacticos, de alcance
# podríamos guardarlos en una lista, despues de hacer la visita en en el main ver si
# la lista está vacía o no
    # ctx.IDENTIFIER().symbol.line
    # ctx.IDENTIFIER().symbol.column

# openScope insertar 