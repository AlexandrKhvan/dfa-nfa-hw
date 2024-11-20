# Generated from Regex.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,8,43,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,
        1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,3,2,23,8,2,1,3,4,3,26,8,3,11,3,12,
        3,27,1,4,1,4,3,4,32,8,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,3,6,41,8,6,1,
        6,0,0,7,0,2,4,6,8,10,12,0,1,1,0,2,4,39,0,14,1,0,0,0,2,17,1,0,0,0,
        4,19,1,0,0,0,6,25,1,0,0,0,8,29,1,0,0,0,10,33,1,0,0,0,12,40,1,0,0,
        0,14,15,3,2,1,0,15,16,5,0,0,1,16,1,1,0,0,0,17,18,3,4,2,0,18,3,1,
        0,0,0,19,22,3,6,3,0,20,21,5,1,0,0,21,23,3,4,2,0,22,20,1,0,0,0,22,
        23,1,0,0,0,23,5,1,0,0,0,24,26,3,8,4,0,25,24,1,0,0,0,26,27,1,0,0,
        0,27,25,1,0,0,0,27,28,1,0,0,0,28,7,1,0,0,0,29,31,3,12,6,0,30,32,
        3,10,5,0,31,30,1,0,0,0,31,32,1,0,0,0,32,9,1,0,0,0,33,34,7,0,0,0,
        34,11,1,0,0,0,35,41,5,7,0,0,36,37,5,5,0,0,37,38,3,2,1,0,38,39,5,
        6,0,0,39,41,1,0,0,0,40,35,1,0,0,0,40,36,1,0,0,0,41,13,1,0,0,0,4,
        22,27,31,40
    ]

class RegexParser ( Parser ):

    grammarFileName = "Regex.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'|'", "'*'", "'+'", "'?'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "CHAR", "WS" ]

    RULE_regex = 0
    RULE_expression = 1
    RULE_alternation = 2
    RULE_concatenation = 3
    RULE_repetition = 4
    RULE_quantifier = 5
    RULE_atom = 6

    ruleNames =  [ "regex", "expression", "alternation", "concatenation", 
                   "repetition", "quantifier", "atom" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    CHAR=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RegexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(RegexParser.ExpressionContext,0)


        def EOF(self):
            return self.getToken(RegexParser.EOF, 0)

        def getRuleIndex(self):
            return RegexParser.RULE_regex

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegex" ):
                listener.enterRegex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegex" ):
                listener.exitRegex(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegex" ):
                return visitor.visitRegex(self)
            else:
                return visitor.visitChildren(self)




    def regex(self):

        localctx = RegexParser.RegexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_regex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.expression()
            self.state = 15
            self.match(RegexParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def alternation(self):
            return self.getTypedRuleContext(RegexParser.AlternationContext,0)


        def getRuleIndex(self):
            return RegexParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = RegexParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.alternation()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AlternationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.right = None # AlternationContext

        def concatenation(self):
            return self.getTypedRuleContext(RegexParser.ConcatenationContext,0)


        def alternation(self):
            return self.getTypedRuleContext(RegexParser.AlternationContext,0)


        def getRuleIndex(self):
            return RegexParser.RULE_alternation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlternation" ):
                listener.enterAlternation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlternation" ):
                listener.exitAlternation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlternation" ):
                return visitor.visitAlternation(self)
            else:
                return visitor.visitChildren(self)




    def alternation(self):

        localctx = RegexParser.AlternationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_alternation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.concatenation()
            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 20
                self.match(RegexParser.T__0)
                self.state = 21
                localctx.right = self.alternation()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConcatenationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def repetition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RegexParser.RepetitionContext)
            else:
                return self.getTypedRuleContext(RegexParser.RepetitionContext,i)


        def getRuleIndex(self):
            return RegexParser.RULE_concatenation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConcatenation" ):
                listener.enterConcatenation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConcatenation" ):
                listener.exitConcatenation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcatenation" ):
                return visitor.visitConcatenation(self)
            else:
                return visitor.visitChildren(self)




    def concatenation(self):

        localctx = RegexParser.ConcatenationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_concatenation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.repetition()
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==5 or _la==7):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepetitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.q = None # QuantifierContext

        def atom(self):
            return self.getTypedRuleContext(RegexParser.AtomContext,0)


        def quantifier(self):
            return self.getTypedRuleContext(RegexParser.QuantifierContext,0)


        def getRuleIndex(self):
            return RegexParser.RULE_repetition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepetition" ):
                listener.enterRepetition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepetition" ):
                listener.exitRepetition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepetition" ):
                return visitor.visitRepetition(self)
            else:
                return visitor.visitChildren(self)




    def repetition(self):

        localctx = RegexParser.RepetitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_repetition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.atom()
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 28) != 0):
                self.state = 30
                localctx.q = self.quantifier()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuantifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RegexParser.RULE_quantifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuantifier" ):
                listener.enterQuantifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuantifier" ):
                listener.exitQuantifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuantifier" ):
                return visitor.visitQuantifier(self)
            else:
                return visitor.visitChildren(self)




    def quantifier(self):

        localctx = RegexParser.QuantifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_quantifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 28) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.expr = None # ExpressionContext

        def CHAR(self):
            return self.getToken(RegexParser.CHAR, 0)

        def expression(self):
            return self.getTypedRuleContext(RegexParser.ExpressionContext,0)


        def getRuleIndex(self):
            return RegexParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = RegexParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_atom)
        try:
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.match(RegexParser.CHAR)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.match(RegexParser.T__4)
                self.state = 37
                localctx.expr = self.expression()
                self.state = 38
                self.match(RegexParser.T__5)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





