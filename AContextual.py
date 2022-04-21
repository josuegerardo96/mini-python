from miParserVisitor import *
from miParserParser import *

class AContextual(miParserVisitor):
    def visitProgramAST(self, ctx: miParserParser.ProgramASTContext):
        return super().visitProgramAST(ctx)

    def visitStatement(self, ctx: miParserParser.StatementContext):
        return super().visitStatement(ctx)

    def visitDefStatementAST(self, ctx: miParserParser.DefStatementASTContext):
        return super().visitDefStatementAST(ctx)
