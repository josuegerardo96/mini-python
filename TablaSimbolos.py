from miParserLexer import *
from miParserParser import *
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener




class TablaSimbolos:
#    tabla= []
#    nivelActual=0

    class Ident(self):  #tal vez poner slef.toko
        tok:Token
        def __init__(self, t,  p, im, decl, nivelActual): # t tipo Token, tp tipo int, p tipo lista de Parser1.IdDeclarationContext, im tipo booleano, decl tipo ParserRuleContext
            self.tok=t
            # este nivel actual no va a servir
            self.nivel = nivelActual  ###Unresolved reference 'nivelActual'
            self.valor=0
            self.params=p
            self.isMethod=im
            self.declCtx=decl

    def __int__(self):
        self.tabla=[]
        self.nivelActual=-1

    def insertar(self,id,p,im,decl): # id tipo Token, p tipo lista de Parser1.IdDeclarationContext, im tipo booleano, decl tipo ParserRuleContext
        i = Ident(id,p,im,decl, self.nivelActual)
        p.insert(0,i)

    def buscar(self, nombre):
        for i in self.tabla:
            if i.tok.text() == nombre:       #como hacer casting -> (((Ident)id).tok.getText().equals(nombre))
                return i.tok
        return None

    def openScope(self):
        self.nivelActual= self.nivelActual+1

    # version que el profe nos pasó, adaptarlo a nuestro proyecto
    def closeScope(self):
        self.tabla = list(filter(lambda x: x.nivel != self.nivelActual, self.tabla))
        self.nivelActual -= 1

    # esta es la función imprimir, se invoca print( str(la_tabla) )
    def __str__(self):
        str_list = []
        str_list.append("----- INICIO TABLA ------\n")
        for x in self.tabla:
            str_list.append(f'Nombre: {x.tok.text} - {x.nivel}\n')
        str_list.append("----- FIN TABLA ------\n")
        return ''.join(str_list)