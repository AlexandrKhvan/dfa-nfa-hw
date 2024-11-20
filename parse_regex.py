import sys
from antlr4 import InputStream, CommonTokenStream
from RegexLexer import RegexLexer
from RegexParser import RegexParser
from antlr4.error.ErrorListener import ErrorListener

class RegexErrorListener(ErrorListener):
    def __init__(self):
        super(RegexErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_message = f"Syntax error at line {line}, column {column}: {msg}"
        self.errors.append(error_message)

def parse_regex(input_regex):
    input_stream = InputStream(input_regex)
    lexer = RegexLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = RegexParser(stream)

    error_listener = RegexErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    tree = parser.regex()
    if error_listener.errors:
        '''
        for error in error_listener.errors:
            print(error, file=sys.stderr)
        '''
        return None
    return tree