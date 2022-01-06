from dataclasses import dataclass
from enum import Enum
import math

SPACE=' \n'
NUMBER='0123456789'
STRING='sincostgctgradlog^^'
CHARACTER='abcdefghijklmnopqrstuvwz'


# realizam clasa de tokenuri
class Type_Tokens( Enum):
    NUMBER = 1
    ADD = 2
    SUB = 3
    MUL = 4
    DIV = 5
    SIN = 6
    COS = 7
    CTG = 8
    TG = 9
    POWER = 10
    RAD = 11
    LOG = 12


@dataclass
class Token:
    type: Type_Tokens
    value: int = None


class Type_n(Enum):
    ADD = 1
    SUB = 2
    MUL = 3
    DIV = 4
    SIN = 5
    COS = 6
    CTG = 7
    TG = 8
    POWER = 9
    RAD = 10
    LOG = 11
    NUMBER = 12


@dataclass
class Node:
    type: Type_n
    left_child: any
    right_child: any
    value: int = None


class Lexer:
    def __init__(self):
        self.rpn_conv = TREE_Maker()

    def Give_token(self, expr):

        expr = self.rpn_conv.TREE(expr)
        list = []

        if expr:
            for fact in expr:
                if fact == "-":
                    list.append(Token(Type_Tokens.SUB))
                elif fact == "rad":
                    list.append(Token(Type_Tokens.RAD))
                elif fact == "log":
                    list.append(Token(Type_Tokens.LOG))
                elif fact == "+":
                    list.append(Token(Type_Tokens.ADD))
                elif fact == "*":
                    list.append(Token(Type_Tokens.MUL))
                elif fact == "/":
                    list.append(Token(Type_Tokens.DIV))
                elif fact.isdigit():
                    list.append(Token(Type_Tokens.NUMBER, int(fact)))
                elif fact == "^^":
                    list.append(Token(Type_Tokens.POWER))
                elif fact == "sin":
                    list.append(Token(Type_Tokens.SIN))
                elif fact == "cos":
                    list.append(Token(Type_Tokens.COS))
                elif fact == "tg":
                    list.append(Token(Type_Tokens.TG))
                elif fact == "ctg":
                    list.append(Token(Type_Tokens.CTG))

        return list

class TREE_Maker: #arborele e terminat
    def nextnode(self, exp_iter):
        try:
            return next(exp_iter)
        except StopIteration:
            return None

    def TREE(self, expression):
        tree = []
        if expression:
            iter_expr = iter(expression)
            paran = 0
            string_expr = self.nextnode(iter_expr)
            list_op = []

            while string_expr:
                if string_expr in SPACE:
                    string_expr = self.nextnode(iter_expr)
                    continue


                elif ")" ==string_expr:
                    while list_op and list_op[-1] != "(":
                        tree.append(list_op.pop())
                    if list_op:
                        list_op.pop()
                    string_expr = self.nextnode(iter_expr)
                    paran -= 1

                elif "("==string_expr:
                    list_op.append(string_expr)
                    string_expr = self.nextnode(iter_expr)
                    paran += 1


                elif string_expr in STRING:
                    text = ""
                    while string_expr != None and string_expr in STRING:
                        text += string_expr
                        string_expr = self.nextnode(iter_expr)

                    if "sin"==text:
                        list_op.append(text)
                    elif "cos"==text:
                        list_op.append(text)
                    elif "ctg"==text:
                        list_op.append(text)
                    elif "tg"==text:
                        list_op.append(text)
                    elif "rad"==text:
                        list_op.append(text)
                    elif "log"==text:
                        list_op.append(text)
                    elif "^^"==text:
                        list_op.append(text)
                    else:
                        print("Syntax error 1")
                        return []


                elif string_expr in NUMBER:
                    nr = ""
                    while string_expr != None and string_expr in NUMBER:
                        nr += string_expr
                        string_expr = self.nextnode(iter_expr)
                    tree.append(nr)



                elif string_expr in "+-*/"or string_expr in STRING:
                    if not list_op:
                        list_op.append(string_expr)
                    else:
                        while string_expr in "+-*/":
                            if list_op and string_expr in "+-" and( list_op[-1] in "+-*/" or list_op[-1] in STRING):
                                tree.append(list_op.pop())
                            elif list_op and string_expr in "*/" and ( list_op[-1] in "*/" or list_op[-1] in STRING):
                                tree.append(list_op.pop())
                            elif list_op and (string_expr in STRING) and (list_op[-1] in STRING):
                                tree.append(list_op.pop())

                            else:
                                list_op.append(string_expr)
                                break
                    string_expr = self.nextnode(iter_expr)
                else:
                    print("Is unknown character")
                    return []
            if paran != 0:
                print("Syntax error 1")
                return []
            while list_op:
                tree.append(list_op.pop())
        return tree


class Interpreter:
    def __init__(self):
        self.parser = Parser()

    def get_value(self, node):
        if  Type_n.MUL== node.type:
            return self.get_value(node.right_child) * self.get_value(node.left_child)
        elif  Type_n.SUB== node.type:
            return self.get_value(node.right_child) - self.get_value(node.left_child)
        elif Type_n.RAD== node.type:
            return math.sqrt(self.get_value(node.left_child))
        elif Type_n.LOG == node.type:
            return math.log10(self.get_value(node.left_child))
        elif  Type_n.DIV== node.type:
            return self.get_value(node.right_child) / self.get_value(node.left_child)
        elif  Type_n.NUMBER== node.type:
            return node.value
        elif  Type_n.ADD== node.type:
            return self.get_value(node.right_child) + self.get_value(node.left_child)
        elif Type_n.POWER == node.type:
            return self.get_value(node.right_child) ** self.get_value(node.left_child)
        elif Type_n.SIN == node.type:
            return math.sin(self.get_value(node.left_child))
        elif  Type_n.COS==node.type:
            return math.cos(self.get_value(node.left_child))
        elif  Type_n.TG== node.type:
            return math.tan(self.get_value(node.left_child))
        elif Type_n.CTG == node.type:
            return 1-math.tan(self.get_value(node.left_child))


    def rezolv(self, expression):
        rez = self.parser.parse(expression)
        if rez:
            if Type_n.NUMBER== rez.type:
                return rez.value
            try:
                return self.get_value(rez)
            except AttributeError:
                print("Syntax error")
        return ""


def main():

    inter = Interpreter()
    print()
    print("                             Interpretor matematic")
    print()
    print("Acest interpretor realizeaza operatii cu +,-,/,*,^^,radical,logaritm,cos,sin,tg,ctg.")
    print()
    expr = input("Expresie:  ")
    print("Rezultat: ", inter.rezolv(expr))


if __name__ == "__main__":
    main()
