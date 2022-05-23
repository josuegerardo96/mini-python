from miParserVisitor import  miParserVisitor
from miParserLexer import  miParserLexer
from miParserParser import miParserParser

from antlr4 import *
class codeGen(miParserVisitor):

    class Instr:
        def __init__(self, i, a):
            self.instr = i
            self.arg = a

    def __init__(self):
        self.codigo = []
        self.instActual = 0
        self.variablesLocalesDefinidas = []

    def generate(self, instr, arg):
        self.codigo.append(codeGen.Instr(instr, arg))
        self.instActual += 1

    def printCode(self):
        print("----- CODIGO GENERADO ------\n")
        for x in self.codigo:
            print(x.instr, end = '')
            if (x.arg):
                print(" " + x.arg)
            else:
                print("")

    def agregarVariableDefinida(self, nombre, lista):
        if (self.buscarVariableDefinida(nombre,lista) == False):
            lista.append(nombre)

    def buscarVariableDefinida(self, nombre, lista):
        for v in lista:
            if v == nombre:
                return True
        return False

    def visitProgramAST(self, ctx: miParserParser.ProgramASTContext):
        super().visitProgramAST(ctx)
        self.printCode()
        return self.codigo


    # Visit a parse tree produced by miParserParser#defST.
    def visitDefST(self, ctx:miParserParser.DefSTContext):
        return super().visitDefStatementAST(ctx)


    # Visit a parse tree produced by miParserParser#ifST.
    def visitIfST(self, ctx:miParserParser.IfSTContext):
        return super().visitIfStatementAST(ctx)


    # Visit a parse tree produced by miParserParser#returnST.
    def visitReturnST(self, ctx:miParserParser.ReturnSTContext):
        return super().visitReturnStatementAST(ctx)


    # Visit a parse tree produced by miParserParser#printST.
    def visitPrintST(self, ctx:miParserParser.PrintSTContext):
        return super().visitPrintStatementAST(ctx)


    # Visit a parse tree produced by miParserParser#whileST.
    def visitWhileST(self, ctx:miParserParser.WhileSTContext):
        return super().visitWhileStatementAST(ctx)


    # Visit a parse tree produced by miParserParser#forST.
    def visitForST(self, ctx:miParserParser.ForSTContext):
        return super().visitForStatementAST(ctx)


    # Visit a parse tree produced by miParserParser#assignST.
    def visitAssignST(self, ctx:miParserParser.AssignSTContext):
        return super().visitAssignStatementAST(ctx)


    # Visit a parse tree produced by miParserParser#functionST.
    def visitFunctionST(self, ctx:miParserParser.FunctionSTContext):
        return super().visitFunctionCallStatementAST(ctx)


    # Visit a parse tree produced by miParserParser#expressionST.
    def visitExpressionST(self, ctx:miParserParser.ExpressionSTContext):
        return super().visitExpressionAST(ctx)


    # Visit a parse tree produced by miParserParser#defStatementAST.
    def visitDefStatementAST(self, ctx:miParserParser.DefStatementASTContext):
        #return super().visitDefStatementAST(ctx)
        self.generate("DEF", ctx.IDENTIFIER().getText())
        if (ctx.argList()):
            self.visit(ctx.argList())

        self.visit(ctx.sequence())
        if (ctx.IDENTIFIER().getText() == "Main"):
            self.generate("END", None)
        else:
            self.generate("RETURN", None)
        self.variablesLocalesDefinidas = []
        return None


    # Visit a parse tree produced by miParserParser#argListAST.
    def visitArgListAST(self, ctx:miParserParser.ArgListASTContext):
        #return super().visitArgListAST(ctx)

        for i in ctx.IDENTIFIER():
            self.generate("PUSH_LOCAL", i.getText())
            self.agregarVariableDefinida(i.getText(), self.variablesLocalesDefinidas)
        return None


    # Visit a parse tree produced by miParserParser#ifStatementAST.
    def visitIfStatementAST(self, ctx:miParserParser.IfStatementASTContext):
        #return super().visitIfStatementAST(ctx)

        self.visit(ctx.expression())
        etiq1 = self.instActual
        self.generate("JUMP_IF_FALSE", "0")
        self.visit(ctx.sequence(0))
        if (ctx.ELSE()):
            etiq2 = self.instActual
            self.generate("JUMP_ABSOLUTE", "0")
            self.codigo[etiq1].arg = str(self.instActual)
            self.visit(ctx.sequence(1))
            self.codigo[etiq2].arg = str(self.instActual)
        else:
            self.codigo[etiq1].arg = str(self.instActual)
        return None


    # Visit a parse tree produced by miParserParser#whileStatementAST.
    def visitWhileStatementAST(self, ctx:miParserParser.WhileStatementASTContext):
        #return super().visitWhileStatementAST(ctx)

        etiq1 = self.instActual
        self.generate("JUMP_ABSOLUTE", "0")
        etiq2 = self.instActual
        self.visit(ctx.sequence())
        self.codigo[etiq1].arg = str(self.instActual)
        self.visit(ctx.expression())
        self.generate("JUMP_IF_TRUE", str(etiq2))

        return None


    # Visit a parse tree produced by miParserParser#forStatementAST.
    def visitForStatementAST(self, ctx:miParserParser.ForStatementASTContext):
        return super().visitForStatementAST(ctx)


    # Visit a parse tree produced by miParserParser#returnStatementAST.
    def visitReturnStatementAST(self, ctx:miParserParser.ReturnStatementASTContext):
        #return super().visitReturnStatementAST(ctx)
        self.visit(ctx.expression())
        self.generate("RETURN_VALUE", None)
        return None


    # Visit a parse tree produced by miParserParser#printStatementAST.
    def visitPrintStatementAST(self, ctx:miParserParser.PrintStatementASTContext):
        #return super().visitPrintStatementAST(ctx)

        self.visit(ctx.expression())
        self.generate("LOAD_GLOBAL", "print")
        self.generate("CALL_FUNCTION", "1")
        return None


    # Visit a parse tree produced by miParserParser#assignStatementAST.
    def visitAssignStatementAST(self, ctx:miParserParser.AssignStatementASTContext):
        #return super().visitAssignStatementAST(ctx)

        if (self.buscarVariableDefinida(ctx.IDENTIFIER().getText(), self.variablesLocalesDefinidas) == False):
            self.generate("PUSH_LOCAL", ctx.IDENTIFIER().getText())  # NO DEBERÍA HACERSE SIEMPRE EL PUSH
            self.agregarVariableDefinida(ctx.IDENTIFIER().getText(), self.variablesLocalesDefinidas)
        self.visit(ctx.expression())
        self.generate("STORE_FAST", ctx.IDENTIFIER().getText())
        return None


    # Visit a parse tree produced by miParserParser#functionCallStatementAST.
    def visitFunctionCallStatementAST(self, ctx:miParserParser.FunctionCallStatementASTContext):
        return super().visitFunctionCallStatementAST(ctx)

        """cant_params = 0
        if (ctx.expressionList()):
            cant_params = self.visit(ctx.expressionList())
        self.generate("LOAD_GLOBAL", ctx.IDENTIFIER().getText())
        self.generate("CALL_FUNCTION", str(cant_params))
        return None"""


    # Visit a parse tree produced by miParserParser#expressionStatementAST.
    def visitExpressionStatementAST(self, ctx:miParserParser.ExpressionStatementASTContext):
        return super().visitExpressionStatementAST(ctx)


    # Visit a parse tree produced by miParserParser#sequenceAST.
    def visitSequenceAST(self, ctx:miParserParser.SequenceASTContext):
        return super().visitSequenceAST(ctx)


    # Visit a parse tree produced by miParserParser#moreStatementsAST.
    def visitMoreStatementsAST(self, ctx:miParserParser.MoreStatementsASTContext):
        return super().visitMoreStatementsAST(ctx)


    # Visit a parse tree produced by miParserParser#expressionAST.
    def visitExpressionAST(self, ctx:miParserParser.ExpressionASTContext):
        return super().visitExpressionAST(ctx)

        """self.visit(ctx.getChild(0))
        i = 1
        while i < len(ctx.children):
            oper = ctx.children[i]
            i += 1
            self.visit(ctx.getChild(i))
            self.generate("COMPARE_OP", oper.getText())
            i += 1

        return None"""


    # Visit a parse tree produced by miParserParser#comparisonAST.
    def visitComparisonAST(self, ctx:miParserParser.ComparisonASTContext):
        return super().visitComparisonAST(ctx)


    # Visit a parse tree produced by miParserParser#additionExpressionAST.
    def visitAdditionExpressionAST(self, ctx:miParserParser.AdditionExpressionASTContext):
        return super().visitAdditionExpressionAST(ctx)

        """self.visit(ctx.getChild(0))
        i = 1
        while i < len(ctx.children):
            oper = ctx.children[i]
            i += 1
            self.visit(ctx.getChild(i))
            if (oper.getText() == "+"):
                self.generate("BINARY_ADD", None)
            elif (oper.getText() == "-"):
                self.generate("BINARY_SUBSTRACT", None)
            i += 1

        return None"""


    # Visit a parse tree produced by miParserParser#additionFactorAST.
    def visitAdditionFactorAST(self, ctx:miParserParser.AdditionFactorASTContext):
        #return super().visitAdditionExpressionAST(ctx)

        #self.visit(ctx.getChild(0)) pasar esto al otro visit y luego tiene que llamar a esta función
        # actualizar indices ?
        i = 1
        while i < len(ctx.children):
            oper = ctx.children[i]
            i += 1
            self.visit(ctx.getChild(i))
            if (oper.getText() == "+"):
                self.generate("BINARY_ADD", None)
            elif (oper.getText() == "-"):
                self.generate("BINARY_SUBSTRACT", None)
            i += 1

        return None


    # Visit a parse tree produced by miParserParser#multiplicationExpressionAST.
    def visitMultiplicationExpressionAST(self, ctx:miParserParser.MultiplicationExpressionASTContext):
        return super().visitMultiplicationExpressionAST(ctx)


    # Visit a parse tree produced by miParserParser#multiplicationFactorAST.
    def visitMultiplicationFactorAST(self, ctx:miParserParser.MultiplicationFactorASTContext):
        return super().visitMultiplicationFactorAST(ctx)


    # Visit a parse tree produced by miParserParser#elementExpressionAST.
    def visitElementExpressionAST(self, ctx:miParserParser.ElementExpressionASTContext):
        return super().visitElementExpressionAST(ctx)


    # Visit a parse tree produced by miParserParser#elementAccessAST.
    def visitElementAccessAST(self, ctx:miParserParser.ElementAccessASTContext):
        return super().visitElementAccessAST(ctx)


    # Visit a parse tree produced by miParserParser#expressionListAST.
    def visitExpressionListAST(self, ctx:miParserParser.ExpressionListASTContext):
        return super().visitExpressionListAST(ctx)

        """for e in ctx.expression():
            self.visit(e)
        return len(ctx.expression())"""


    # Visit a parse tree produced by miParserParser#moreExpressionsAST.
    def visitMoreExpressionsAST(self, ctx:miParserParser.MoreExpressionsASTContext):
        return super().visitMoreExpressionsAST(ctx)


    # Visit a parse tree produced by miParserParser#integerPrimitiveExpressionAST.
    def visitIntegerPrimitiveExpressionAST(self, ctx:miParserParser.IntegerPrimitiveExpressionASTContext):
        self.generate("LOAD_CONST", ctx.INTEGER().getText())
        return None


    # Visit a parse tree produced by miParserParser#floatPrimitiveExpressionAST.
    def visitFloatPrimitiveExpressionAST(self, ctx:miParserParser.FloatPrimitiveExpressionASTContext):
        return super().visitFloatPrimitiveExpressionAST(ctx)


    # Visit a parse tree produced by miParserParser#charconstPrimitiveExpressionAST.
    def visitCharconstPrimitiveExpressionAST(self, ctx:miParserParser.CharconstPrimitiveExpressionASTContext):
        return super().visitCharconstPrimitiveExpressionAST(ctx)

    # Visit a parse tree produced by miParserParser#stringPrimitiveExpressionAST.
    def visitStringPrimitiveExpressionAST(self, ctx:miParserParser.StringPrimitiveExpressionASTContext):
        #return super().visitStringPrimitiveExpressionAST(ctx)

        self.generate("LOAD_CONST", ctx.STRING().getText())
        return None


    # Visit a parse tree produced by miParserParser#identifierPrimitiveExpressionAST.
    def visitIdentifierPrimitiveExpressionAST(self, ctx:miParserParser.IdentifierPrimitiveExpressionASTContext):
        #return super().visitIdentifierPrimitiveExpressionAST(ctx)

        if (ctx.expressionList()==None):
            #deberíamos saber si es FAST o GLOBAL
            self.generate("LOAD_FAST",ctx.IDENTIFIER().getText())
        else:
            cant_params = self.visit(ctx.expressionList())
            self.generate("LOAD_GLOBAL", ctx.IDENTIFIER().getText())
            self.generate("CALL_FUNCTION", str(cant_params))
        return None


    # Visit a parse tree produced by miParserParser#parenthesisPrimitiveExpressionAST.
    def visitParenthesisPrimitiveExpressionAST(self, ctx:miParserParser.ParenthesisPrimitiveExpressionASTContext):
        return super().visitParenthesisPrimitiveExpressionAST(ctx)


    # Visit a parse tree produced by miParserParser#listexpressionPrimitiveExpressionAST.
    def visitListexpressionPrimitiveExpressionAST(self, ctx:miParserParser.ListexpressionPrimitiveExpressionASTContext):
        return super().visitListexpressionPrimitiveExpressionAST(ctx)


    # Visit a parse tree produced by miParserParser#lenparenthesisPrimitiveExpressionAST.
    def visitLenparenthesisPrimitiveExpressionAST(self, ctx:miParserParser.LenparenthesisPrimitiveExpressionASTContext):
        return super().visitLenparenthesisPrimitiveExpressionAST(ctx)


    # Visit a parse tree produced by miParserParser#listExpressionAST.
    def visitListExpressionAST(self, ctx:miParserParser.ListExpressionASTContext):
        return super().visitListExpressionAST(ctx)
