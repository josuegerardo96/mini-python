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
        self.visit(ctx.singleCommand)
        return None
        #return super().visitProgramAST(ctx)

    """def visitStatement(self, ctx: miParserParser.StatementContext):
        self.visit(ctx.singleCommand(0))
        for i in range (1,ctx.singleCommand().size()-1):   #Como poner el <=
                                                           #Filtrar?
            self.visit(ctx.singleCommand(i))
        return None
        #return super().visitStatement(ctx)
    """

    def visitDefST(self, ctx: miParserParser.DefSTContext):
        #Adaptado del visitLetSC

        self.laTabla.openScope()
        self.visit(ctx.declaration)
        self.visit(ctx.singleCommand)
        self.laTabla.closeScope()
        return None

        #return super().visitDefST(ctx)

    def visitIfST(self, ctx: miParserParser.IfSTContext):
        return None
        #return super().visitIfST(ctx)

    def visitReturnST(self, ctx: miParserParser.ReturnSTContext):
        return None
        #return super().visitReturnST(ctx)

    def visitPrintST(self, ctx: miParserParser.PrintSTContext):
        return super().visitPrintST(ctx)
        """No sabemos adaptarlo"""

    def visitWhileST(self, ctx: miParserParser.WhileSTContext):
        return None
        #return super().visitWhileST(ctx)

    def visitForST(self, ctx: miParserParser.ForSTContext):
        #Adaptado del visitBlockSC
        self.visit(ctx.command)
        return None
        #return super().visitForST(ctx)

    def visitAssignST(self, ctx: miParserParser.AssignSTContext):
        #Adaptado del visitAssignSC
        tipoExpr= self.visit(ctx.expression)
        e= self.visit(ctx.ident)
        if e!=None:
            if tipoExpr!= -1:
                if e.type != tipoExpr:
                    self.errorMsgs.append("tipos incompatibles en asignacion")
        else:
            self.errorMsgs.append("el id no esta declarado")
        return None

        #return super().visitAssignST(ctx)

    def visitFunctionST(self, ctx: miParserParser.FunctionSTContext):
        #Adaptado del visitCallSC
        self.visit((ctx.functionCallStatement))
        return None
        #return super().visitFunctionST(ctx)

    def visitExpressionST(self, ctx: miParserParser.ExpressionSTContext):
        return super().visitExpressionST(ctx)
        """No sabemos adaptarlo"""

    def visitDefStatementAST(self, ctx: miParserParser.DefStatementASTContext):
        return super().visitDefStatementAST(ctx)
    """No sabemos adaptarlo"""

    def visitArgListAST(self, ctx: miParserParser.ArgListASTContext):
        #Adaptado del paramDecls
        self.visit(ctx.idDeclaration(0))
        for i in range(1,ctx.idDeclaration.size()-1):
            self.visit(ctx.idDeclaration(i))
        return ctx.idDeclaration
        #return super().visitArgListAST(ctx)

    def visitMoreArgsAST(self, ctx: miParserParser.MoreArgsASTContext):
        return super().visitMoreArgsAST(ctx)
    """No sabemos adaptarlo"""

    def visitIfStatementAST(self, ctx: miParserParser.IfStatementASTContext):
        return super().visitIfStatementAST(ctx)

    def visitWhileStatementAST(self, ctx: miParserParser.WhileStatementASTContext):
        return super().visitWhileStatementAST(ctx)

    def visitForStatementAST(self, ctx: miParserParser.ForStatementASTContext):
        return super().visitForStatementAST(ctx)

    def visitReturnStatementAST(self, ctx: miParserParser.ReturnStatementASTContext):
        return super().visitReturnStatementAST(ctx)

    def visitPrintStatementAST(self, ctx: miParserParser.PrintStatementASTContext):
        return super().visitPrintStatementAST(ctx)

    def visitAssignStatementAST(self, ctx: miParserParser.AssignStatementASTContext):
        # poner la tabla aquí
        self.laTabla
        print(ctx.IDENTIFIER().symbol.text)
        return super().visitAssignStatementAST(ctx)


    def visitFunctionCallStatementAST(self, ctx: miParserParser.FunctionCallStatementASTContext):
        return super().visitFunctionCallStatementAST(ctx)

    def visitExpressionStatementAST(self, ctx: miParserParser.ExpressionStatementASTContext):
        return super().visitExpressionStatementAST(ctx)

    def visitSequenceAST(self, ctx: miParserParser.SequenceASTContext):
        return super().visitSequenceAST(ctx)

    def visitMoreStatementsAST(self, ctx: miParserParser.MoreStatementsASTContext):
        return super().visitMoreStatementsAST(ctx)

    def visitExpressionAST(self, ctx: miParserParser.ExpressionASTContext):
        return super().visitExpressionAST(ctx)

    def visitComparisonAST(self, ctx: miParserParser.ComparisonASTContext):
        return super().visitComparisonAST(ctx)

    def visitAdditionExpressionAST(self, ctx: miParserParser.AdditionExpressionASTContext):
        return super().visitAdditionExpressionAST(ctx)

    def visitAdditionFactorAST(self, ctx: miParserParser.AdditionFactorASTContext):
        return super().visitAdditionFactorAST(ctx)

    def visitMultiplicationExpressionAST(self, ctx: miParserParser.MultiplicationExpressionASTContext):
        return super().visitMultiplicationExpressionAST(ctx)

    def visitMultiplicationFactorAST(self, ctx: miParserParser.MultiplicationFactorASTContext):
        return super().visitMultiplicationFactorAST(ctx)

    def visitElementExpressionAST(self, ctx: miParserParser.ElementExpressionASTContext):
        return super().visitElementExpressionAST(ctx)

    def visitElementAccessAST(self, ctx: miParserParser.ElementAccessASTContext):
        return super().visitElementAccessAST(ctx)

    def visitExpressionListAST(self, ctx: miParserParser.ExpressionListASTContext):
        return super().visitExpressionListAST(ctx)

    def visitMoreExpressionsAST(self, ctx: miParserParser.MoreExpressionsASTContext):
        return super().visitMoreExpressionsAST(ctx)

    def visitIntegerPrimitiveExpressionAST(self, ctx: miParserParser.IntegerPrimitiveExpressionASTContext):
        return super().visitIntegerPrimitiveExpressionAST(ctx)

    def visitFloatPrimitiveExpressionAST(self, ctx: miParserParser.FloatPrimitiveExpressionASTContext):
        return super().visitFloatPrimitiveExpressionAST(ctx)

    def visitCharconstPrimitiveExpressionAST(self, ctx: miParserParser.CharconstPrimitiveExpressionASTContext):
        return super().visitCharconstPrimitiveExpressionAST(ctx)

    def visitStringPrimitiveExpressionAST(self, ctx: miParserParser.StringPrimitiveExpressionASTContext):
        return super().visitStringPrimitiveExpressionAST(ctx)

    def visitIdentifierPrimitiveExpressionAST(self, ctx: miParserParser.IdentifierPrimitiveExpressionASTContext):
        return super().visitIdentifierPrimitiveExpressionAST(ctx)

    def visitParenthesisPrimitiveExpressionAST(self, ctx: miParserParser.ParenthesisPrimitiveExpressionASTContext):
        return super().visitParenthesisPrimitiveExpressionAST(ctx)

    def visitListexpressionPrimitiveExpressionAST(self,
                                                  ctx: miParserParser.ListexpressionPrimitiveExpressionASTContext):
        return super().visitListexpressionPrimitiveExpressionAST(ctx)

    def visitLenparenthesisPrimitiveExpressionAST(self,
                                                  ctx: miParserParser.LenparenthesisPrimitiveExpressionASTContext):
        return super().visitLenparenthesisPrimitiveExpressionAST(ctx)

    def visitListExpressionAST(self, ctx: miParserParser.ListExpressionASTContext):
        return super().visitListExpressionAST(ctx)


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