from miParserVisitor import *
from miParserParser import *
from TablaSimbolos import *
from antlr4 import *

class AContextual(miParserVisitor):
    def __init__(self):
        self.errorMsgs= []
        self.laTabla= TablaSimbolos()
        self.laTabla.openScope()

    def hasErrors(self):
        return len(self.errorMsgs) > 0

    def printErrors(self):
        if not self.hasErrors:
            return "0 errors"
        builder= ''
        for i in self.errorMsgs:
            builder+= '\n'
        return builder

    def visitProgramAST(self, ctx: miParserParser.ProgramASTContext):
        i = ctx.statement()
        for e in range(len(i)):
            self.visit(ctx.statement(e))
        return None

    #def visitStatement(self, ctx: miParserParser.StatementContext):
        #self.visit(ctx.singleCommand(0))
        #for i in range (1,ctx.singleCommand().size()-1):   #Como poner el <=
                                                           #Filtrar?
        #    self.visit(ctx.singleCommand(i))
    #    return None
        #return super().visitStatement(ctx)


    def visitDefST(self, ctx: miParserParser.DefSTContext):
        return super().visitDefST(ctx)

    def visitDefStatementAST(self, ctx: miParserParser.DefStatementASTContext):
        self.laTabla.openScope()
        self.laTabla.insertar(ctx.IDENTIFIER(), self.visit(ctx.argList()), True, ctx)
        self.visit(ctx.sequence())
        self.laTabla.closeScope()
        return None
    #variable es False
    #metodo es True

    def visitIfST(self, ctx: miParserParser.IfSTContext):
        return super().visitIfST(ctx)

    def visitReturnST(self, ctx: miParserParser.ReturnSTContext):
        return super().visitReturnST(ctx)

    def visitPrintST(self, ctx: miParserParser.PrintSTContext):
        return super().visitPrintST(ctx)

    def visitWhileST(self, ctx: miParserParser.WhileSTContext):
        return super().visitWhileST(ctx)

    def visitForST(self, ctx: miParserParser.ForSTContext):
        return super().visitForST(ctx)

    def visitAssignST(self, ctx: miParserParser.AssignSTContext):
        return super().visitAssignST(ctx)

    def visitFunctionST(self, ctx: miParserParser.FunctionSTContext):
        return super().visitFunctionST(ctx)

    def visitExpressionST(self, ctx: miParserParser.ExpressionSTContext):
        return super().visitExpressionST(ctx)

    def visitArgListAST(self, ctx: miParserParser.ArgListASTContext):
        self.laTabla.openScope()
        e= ctx.IDENTIFIER()
        for i in range(len(e)):
            self.laTabla.insertar(self.visit(ctx.IDENTIFIER(i)), ctx.COMA(i), False, ctx)
        self.laTabla.closeScope()
        return None

    def visitIfStatementAST(self, ctx: miParserParser.IfStatementASTContext):
        x = ctx.expression()
        y = ctx.sequence()
        self.visit(x)
        for j in range (len(y)):
            self.visit(ctx.sequence(j))
        return None

    def visitWhileStatementAST(self, ctx: miParserParser.WhileStatementASTContext):
        self.visit(ctx.expression())
        self.visit(ctx.sequence())
        return None

    def visitForStatementAST(self, ctx: miParserParser.ForStatementASTContext):
        self.visit(ctx.expression())
        self.visit(ctx.sequence())
        return None

    def visitReturnStatementAST(self, ctx: miParserParser.ReturnStatementASTContext):
        self.visit(ctx.expression())
        return None

    def visitPrintStatementAST(self, ctx: miParserParser.PrintStatementASTContext):
        self.visit(ctx.expression())
        return None

    def visitAssignStatementAST(self, ctx: miParserParser.AssignStatementASTContext):
        self.laTabla.openScope()
        self.laTabla.insertar(self.visit(ctx.IDENTIFIER()), None,  False, ctx)
        self.visit(ctx.expression())
        self.laTabla.closeScope()
        #print(ctx.IDENTIFIER().symbol.text)
        return None


    def visitFunctionCallStatementAST(self, ctx: miParserParser.FunctionCallStatementASTContext):
        self.visit(ctx.primitiveExpression())
        self.visit(ctx.expressionList())
        return None

    def visitExpressionStatementAST(self, ctx: miParserParser.ExpressionStatementASTContext):
        self.visit(ctx.expressionList())
        return None

    def visitSequenceAST(self, ctx: miParserParser.SequenceASTContext):
        self.visit(ctx.moreStatements())
        return None

    def visitMoreStatementsAST(self, ctx: miParserParser.MoreStatementsASTContext):
        self.visit(ctx.statement())
        e= ctx.moreStatements()
        for i in range(len(e)):
            self.visit(ctx.moreStatements(i))
        return None

    def visitExpressionAST(self, ctx: miParserParser.ExpressionASTContext):
        self.visit(ctx.additionExpression())
        self.visit(ctx.comparison())
        return None

    def visitComparisonAST(self, ctx: miParserParser.ComparisonASTContext):
        e= ctx.additionExpression()
        for i in range(len(e)):
            self.visit(ctx.additionExpression(i))
        return None

    def visitAdditionExpressionAST(self, ctx: miParserParser.AdditionExpressionASTContext):
        self.visit(ctx.multiplicationExpression())
        self.visit(ctx.additionFactor())
        return None

    def visitAdditionFactorAST(self, ctx: miParserParser.AdditionFactorASTContext):
        e= ctx.multiplicationExpression()
        for i in range(len(e)):
            self.visit(ctx.multiplicationExpression(i))
        return None

    def visitMultiplicationExpressionAST(self, ctx: miParserParser.MultiplicationExpressionASTContext):
        self.visit(ctx.elementExpression())
        self.visit(ctx.multiplicationFactor())
        return None

    def visitMultiplicationFactorAST(self, ctx: miParserParser.MultiplicationFactorASTContext):
        e= ctx.elementExpression()
        for i in range(len(e)):
            self.visit(ctx.elementExpression(i))
        return None

    def visitElementExpressionAST(self, ctx: miParserParser.ElementExpressionASTContext):
        self.visit(ctx.primitiveExpression())
        self.visit(ctx.elementAccess())
        return None

    def visitElementAccessAST(self, ctx: miParserParser.ElementAccessASTContext):
        e= ctx.expression()
        for i in range(len(e)):
            self.visit(ctx.expression(i))
        return None

    def visitExpressionListAST(self, ctx: miParserParser.ExpressionListASTContext):
        self.visit(ctx.expression())
        self.visit(ctx.moreExpressions())
        return None

    def visitMoreExpressionsAST(self, ctx: miParserParser.MoreExpressionsASTContext):
        e= ctx.expression()
        for i in range(len(e)):
            self.visit(ctx.expression(i))
        return None

    def visitIntegerPrimitiveExpressionAST(self, ctx: miParserParser.IntegerPrimitiveExpressionASTContext):
        return None

    def visitFloatPrimitiveExpressionAST(self, ctx: miParserParser.FloatPrimitiveExpressionASTContext):
        return None

    def visitCharconstPrimitiveExpressionAST(self, ctx: miParserParser.CharconstPrimitiveExpressionASTContext):
        return None

    def visitStringPrimitiveExpressionAST(self, ctx: miParserParser.StringPrimitiveExpressionASTContext):
        return None

    def visitIdentifierPrimitiveExpressionAST(self, ctx: miParserParser.IdentifierPrimitiveExpressionASTContext):
        self.laTabla.openScope()
        self.laTabla.insertar(ctx.IDENTIFIER(), ctx.expressionList(), True, ctx)
        self.laTabla.closeScope()
        return None

    def visitParenthesisPrimitiveExpressionAST(self, ctx: miParserParser.ParenthesisPrimitiveExpressionASTContext):
        self.visit(ctx.expression())
        return None

    def visitListexpressionPrimitiveExpressionAST(self, ctx: miParserParser.ListexpressionPrimitiveExpressionASTContext):
        self.visit(ctx.listExpression())
        return None

    def visitLenparenthesisPrimitiveExpressionAST(self, ctx: miParserParser.LenparenthesisPrimitiveExpressionASTContext):
        self.visit(ctx.expression())
        return None

    def visitListExpressionAST(self, ctx: miParserParser.ListExpressionASTContext):
        self.visit(ctx.expressionList())
        return None


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