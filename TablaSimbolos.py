from miParserLexer import *
from miParserParser import *
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener




class TablaSimbolos:
    tabla= []
    nivelActual=0


class Ident:
    tok=None #Tipo token
    nivel=0
    valor=0
    params=[]
    isMethod=False
    declCtx= None #Tipo ParserRuleContext

    def __init__(self, t,  p, im, decl): # t tipo Token, tp tipo int, p tipo lista de Parser1.IdDeclarationContext, im tipo booleano, decl tipo ParserRuleContext
        self.tok=t
        nivel= self.nivelActual  ###Unresolved reference 'nivelActual'
        self.valor=0
        self.params=p
        self.isMethod=im
        self.declCtx=decl


    def setValue(self,v):
        self.valor=v

    def getNivel(self):
        return self.nivel

    def __int__(self):
        tabla=[]
        self.nivelActual=-1

    def insertar(self,id,p,im,decl): # id tipo Token, p tipo lista de Parser1.IdDeclarationContext, im tipo booleano, decl tipo ParserRuleContext
        self.i= Ident(id,p,im,decl)
        p.insert(0,self.i)

    def buscar(self, nombre):
        temp = None  # temp es tipo Ident
        for i in self.tabla:
            if i.__eq__(nombre):       #como hacer casting -> (((Ident)id).tok.getText().equals(nombre))
                return i
        return temp

    def openScope(self):
        self.nivelActual= self.nivelActual+1

    def closeScope(self):
        for i in self.tabla:
            if i.self.nivel==i.self.nivelActual:
                self.nivelActual=self.nivelActual-1

    def imprimir(self):
        print("----- INICIO TABLA ------")
        #for(i in self.tabla):