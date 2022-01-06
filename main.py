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
