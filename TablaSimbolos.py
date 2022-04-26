from miParserLexer import *
from miParserParser import *
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener



class TablaSimbolos:

    class Ident:
        tok: Token
        def __init__(self, t,  p, im, decl, nivelActual):
            self.tok=t
            self.nivel = nivelActual
            self.valor=0
            self.params=p
            self.isMethod=im
            self.declCtx=decl

    def __int__(self):
        self.tabla=[]
        self.nivelActual=-1

    def insertar(self,id,p,im,decl):
        i = TablaSimbolos.Ident(id,p,im,decl, self.nivelActual)
        p.insert(0,i)

    def buscar(self, nombre):
        for i in self.tabla:
            if i.tok.text() == nombre:
                return i.tok
        return None

    def openScope(self):
        self.nivelActual= self.nivelActual+1


    def closeScope(self):
        self.tabla = list(filter(lambda x: x.nivel != self.nivelActual, self.tabla))
        self.nivelActual -= 1

    def __str__(self):
        str_list = []
        str_list.append("----- INICIO TABLA ------\n")
        for x in self.tabla:
            str_list.append(f'Nombre: {x.tok.text} - {x.nivel}\n')
        str_list.append("----- FIN TABLA ------\n")
        return ''.join(str_list)