from miParserLexer import *
from miParserParser import *
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode


class Ident:
    tok=Token
    type=0
    nivel=0
    valor=0
    declCtx=ParserRuleContext

    def __init__(self, t, tp, decl):
        self.tok=t
        self.type=tp
        self.nivel= self.nivelActual
        self.valor=0


    class TablaSimbolos():
        tabla= LinkedList()
        nivelActual=0
        def __init__(self):
            self.nivelActual=0
            self.tabla=LinkedList()

    def setValue(self,v):
        self.valor=v

    def getNivel(self):
        return self.nivel
