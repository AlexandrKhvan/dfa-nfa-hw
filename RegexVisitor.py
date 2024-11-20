# Generated from Regex.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RegexParser import RegexParser
else:
    from RegexParser import RegexParser

# This class defines a complete generic visitor for a parse tree produced by RegexParser.

class RegexVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RegexParser#regex.
    def visitRegex(self, ctx:RegexParser.RegexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegexParser#expression.
    def visitExpression(self, ctx:RegexParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegexParser#alternation.
    def visitAlternation(self, ctx:RegexParser.AlternationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegexParser#concatenation.
    def visitConcatenation(self, ctx:RegexParser.ConcatenationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegexParser#repetition.
    def visitRepetition(self, ctx:RegexParser.RepetitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegexParser#quantifier.
    def visitQuantifier(self, ctx:RegexParser.QuantifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegexParser#atom.
    def visitAtom(self, ctx:RegexParser.AtomContext):
        return self.visitChildren(ctx)



del RegexParser