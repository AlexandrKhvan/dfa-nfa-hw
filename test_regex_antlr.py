# test_regex.py

from parse_regex import parse_regex
from regex_ast_builder import RegexASTBuilder
from regex import *

def compile_and_run(regex, input_string):
    tree = parse_regex(regex)
    if not tree:
        print(f"Invalid regex: {regex}")
        return False

    ast_builder = RegexASTBuilder()
    try:
        ast = ast_builder.visit(tree)
    except Exception as e:
        print(f"Error building AST for regex: {regex}, Exception: {e}")
        return False

    if not ast:
        print(f"Error building AST for regex: {regex}")
        return False

    codegen = CodeGenerator()
    codegen.generate(ast)
    codegen.new_instruction('match')

    result = run_vm(codegen.instructions, input_string)
    return result

def test_regex_parsing():
    valid_regexes = [
        'a',
        'ab',
        'a|b',
        '(a)',
        'a*',
        'a+',
        'a?',
        '(a|b)*',
        'a(b|c)+d?',
        '((a)b)*c'
    ]

    invalid_regexes = [
        'a**',
        'a|',
        '*a',
        'a(b',
        'a(b|c',
        ')a(',
        'a++',
        'a(b))',
        'a(b|c))d',
        '(a|b'
    ]

    for regex in valid_regexes:
        tree = parse_regex(regex)
        assert tree is not None, f"Valid regex '{regex}' failed to parse."
        print(f"Successfully parsed valid regex: {regex}")

    for regex in invalid_regexes:
        tree = parse_regex(regex)
        assert tree is None, f"Invalid regex '{regex}' should not parse."
        print(f"Correctly rejected invalid regex: {regex}")
    print()
    print("All parsing tests passed.")
    print()

def test_vm():
    test_cases = [
        ('a', 'a', True),
        ('a', 'b', False),
        ('a|b', 'a', True),
        ('a|b', 'b', True),
        ('(a|b)*c', 'ababc', True),
        ('(a|b)*c', 'ababa', False),
        ('a+', 'aaaa', True),
        ('a+', '', False),
        ('a?', 'a', True),
        ('a?', '', True),
        ('a(b|c)+d?', 'abbd', True),
        ('a(b|c)+d?', 'acccd', True),
        ('a(b|c)+d?', 'ad', False),
        ('(a)', 'a', True),
        ('((a)b)*c', 'ababc', True),
        ('((a)b)*c', 'abc', True),
        ('((a)b)*c', 'ab', False),
    ]

    for regex, input_string, expected in test_cases:
        result = compile_and_run(regex, input_string)
        assert result == expected, f"Test failed for regex '{regex}' with input '{input_string}'"
        status = "passed" if result == expected else "failed"
        print(f"Test {status} for regex '{regex}' with input '{input_string}'")
    print()
    print("All VM tests passed.")

if __name__ == '__main__':
    test_regex_parsing()
    test_vm()