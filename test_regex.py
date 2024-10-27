import unittest
from regex import *
class TestRegexVM(unittest.TestCase):
    def test_simple_match(self):
        regex = 'ab'
        parser = Parser(regex)
        ast = parser.parse()
        codegen = CodeGenerator()
        codegen.generate(ast)
        codegen.new_instruction('match')
        instructions = codegen.instructions
        self.assertTrue(run_vm(instructions, 'ab'))
        self.assertFalse(run_vm(instructions, 'a'))
        self.assertFalse(run_vm(instructions, 'abc'))

    def test_alternation(self):
        regex = 'a|b'
        parser = Parser(regex)
        ast = parser.parse()
        codegen = CodeGenerator()
        codegen.generate(ast)
        codegen.new_instruction('match')
        instructions = codegen.instructions
        self.assertTrue(run_vm(instructions, 'a'))
        self.assertTrue(run_vm(instructions, 'b'))
        self.assertFalse(run_vm(instructions, 'ab'))

    def test_repetition(self):
        regex = 'a*'
        parser = Parser(regex)
        ast = parser.parse()
        codegen = CodeGenerator()
        codegen.generate(ast)
        codegen.new_instruction('match')
        instructions = codegen.instructions
        self.assertTrue(run_vm(instructions, ''))
        self.assertTrue(run_vm(instructions, 'a'))
        self.assertTrue(run_vm(instructions, 'aaaa'))
        self.assertFalse(run_vm(instructions, 'b'))

    def test_complex_expression(self):
        regex = 'a+b+'
        parser = Parser(regex)
        ast = parser.parse()
        codegen = CodeGenerator()
        codegen.generate(ast)
        codegen.new_instruction('match')
        instructions = codegen.instructions
        self.assertTrue(run_vm(instructions, 'ab'))
        self.assertTrue(run_vm(instructions, 'aaabbb'))
        self.assertTrue(run_vm(instructions, 'aab'))
        self.assertTrue(run_vm(instructions, 'abb'))
        self.assertFalse(run_vm(instructions, 'a'))
        self.assertFalse(run_vm(instructions, 'b'))
        self.assertFalse(run_vm(instructions, 'ba'))
        self.assertFalse(run_vm(instructions, 'aaabbba'))

    def test_question_mark(self):
        regex = 'a?b'
        parser = Parser(regex)
        ast = parser.parse()
        codegen = CodeGenerator()
        codegen.generate(ast)
        codegen.new_instruction('match')
        instructions = codegen.instructions
        self.assertTrue(run_vm(instructions, 'b'))
        self.assertTrue(run_vm(instructions, 'ab'))
        self.assertFalse(run_vm(instructions, 'aab'))
        self.assertFalse(run_vm(instructions, 'abb'))

if __name__ == '__main__':
    unittest.main()
