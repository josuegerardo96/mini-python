# Generated from C:/Users/Meih55/Desktop/mini-python\miParser.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .miParserParser import miParserParser
else:
    from miParserParser import miParserParser

# This class defines a complete generic visitor for a parse tree produced by miParserParser.

class miParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by miParserParser#programAST.
    def visitProgramAST(self, ctx:miParserParser.ProgramASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#statement.
    def visitStatement(self, ctx:miParserParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#defStatementAST.
    def visitDefStatementAST(self, ctx:miParserParser.DefStatementASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#argListAST.
    def visitArgListAST(self, ctx:miParserParser.ArgListASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#moreArgsAST.
    def visitMoreArgsAST(self, ctx:miParserParser.MoreArgsASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#ifStatementAST.
    def visitIfStatementAST(self, ctx:miParserParser.IfStatementASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#whileStatementAST.
    def visitWhileStatementAST(self, ctx:miParserParser.WhileStatementASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#forStatementAST.
    def visitForStatementAST(self, ctx:miParserParser.ForStatementASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#returnStatementAST.
    def visitReturnStatementAST(self, ctx:miParserParser.ReturnStatementASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#printStatementAST.
    def visitPrintStatementAST(self, ctx:miParserParser.PrintStatementASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#assignStatementAST.
    def visitAssignStatementAST(self, ctx:miParserParser.AssignStatementASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#functionCallStatementAST.
    def visitFunctionCallStatementAST(self, ctx:miParserParser.FunctionCallStatementASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#expressionStatementAST.
    def visitExpressionStatementAST(self, ctx:miParserParser.ExpressionStatementASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#sequenceAST.
    def visitSequenceAST(self, ctx:miParserParser.SequenceASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#moreStatementsAST.
    def visitMoreStatementsAST(self, ctx:miParserParser.MoreStatementsASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#expressionAST.
    def visitExpressionAST(self, ctx:miParserParser.ExpressionASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#comparisonAST.
    def visitComparisonAST(self, ctx:miParserParser.ComparisonASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#additionExpressionAST.
    def visitAdditionExpressionAST(self, ctx:miParserParser.AdditionExpressionASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#additionFactorAST.
    def visitAdditionFactorAST(self, ctx:miParserParser.AdditionFactorASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#multiplicationExpressionAST.
    def visitMultiplicationExpressionAST(self, ctx:miParserParser.MultiplicationExpressionASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#multiplicationFactorAST.
    def visitMultiplicationFactorAST(self, ctx:miParserParser.MultiplicationFactorASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#elementExpressionAST.
    def visitElementExpressionAST(self, ctx:miParserParser.ElementExpressionASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#elementAccessAST.
    def visitElementAccessAST(self, ctx:miParserParser.ElementAccessASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#expressionListAST.
    def visitExpressionListAST(self, ctx:miParserParser.ExpressionListASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#moreExpressionsAST.
    def visitMoreExpressionsAST(self, ctx:miParserParser.MoreExpressionsASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#integerPrimitiveExpressionAST.
    def visitIntegerPrimitiveExpressionAST(self, ctx:miParserParser.IntegerPrimitiveExpressionASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#floatPrimitiveExpressionAST.
    def visitFloatPrimitiveExpressionAST(self, ctx:miParserParser.FloatPrimitiveExpressionASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#charconstPrimitiveExpressionAST.
    def visitCharconstPrimitiveExpressionAST(self, ctx:miParserParser.CharconstPrimitiveExpressionASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#stringPrimitiveExpressionAST.
    def visitStringPrimitiveExpressionAST(self, ctx:miParserParser.StringPrimitiveExpressionASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#identifierPrimitiveExpressionAST.
    def visitIdentifierPrimitiveExpressionAST(self, ctx:miParserParser.IdentifierPrimitiveExpressionASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#parenthesisPrimitiveExpressionAST.
    def visitParenthesisPrimitiveExpressionAST(self, ctx:miParserParser.ParenthesisPrimitiveExpressionASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#listexpressionPrimitiveExpressionAST.
    def visitListexpressionPrimitiveExpressionAST(self, ctx:miParserParser.ListexpressionPrimitiveExpressionASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#lenparenthesisPrimitiveExpressionAST.
    def visitLenparenthesisPrimitiveExpressionAST(self, ctx:miParserParser.LenparenthesisPrimitiveExpressionASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#listExpressionAST.
    def visitListExpressionAST(self, ctx:miParserParser.ListExpressionASTContext):
        return self.visitChildren(ctx)



del miParserParser