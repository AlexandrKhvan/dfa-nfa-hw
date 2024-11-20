from RegexParser import RegexParser
from RegexVisitor import RegexVisitor

class ASTNode:
    def __init__(self, type_, left=None, right=None, value=None):
        self.type = type_
        self.left = left
        self.right = right
        self.value = value

class RegexASTBuilder(RegexVisitor):
    def visitRegex(self, ctx: RegexParser.RegexContext):
        return self.visit(ctx.expression())

    def visitExpression(self, ctx: RegexParser.ExpressionContext):
        return self.visit(ctx.alternation())

    def visitAlternation(self, ctx: RegexParser.AlternationContext):
        left = self.visit(ctx.concatenation())
        if ctx.right:
            right = self.visit(ctx.right)
            return ASTNode('|', left, right)
        else:
            return left

    def visitConcatenation(self, ctx: RegexParser.ConcatenationContext):
        repetitions = ctx.repetition()
        if len(repetitions) == 1:
            return self.visit(repetitions[0])
        else:
            node = self.visit(repetitions[0])
            for rep_ctx in repetitions[1:]:
                next_node = self.visit(rep_ctx)
                node = ASTNode('concat', node, next_node)
            return node

    def visitRepetition(self, ctx: RegexParser.RepetitionContext):
        atom_node = self.visit(ctx.atom())
        if ctx.q:
            quant = ctx.q.getText()
            if quant == '*':
                return ASTNode('*', atom_node)
            elif quant == '+':
                return ASTNode('+', atom_node)
            elif quant == '?':
                return ASTNode('?', atom_node)
            else:
                raise Exception(f"Unknown quantifier: {quant}")
        else:
            return atom_node

    def visitAtom(self, ctx: RegexParser.AtomContext):
        if ctx.CHAR():
            return ASTNode('char', value=ctx.CHAR().getText())
        elif ctx.expr:
            return self.visit(ctx.expr)
        else:
            raise Exception("Invalid atom")