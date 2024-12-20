class Node:
    def __init__(self, type_, left=None, right=None, value=None):
        self.type = type_
        self.left = left
        self.right = right
        self.value = value

class Parser:
    def __init__(self, regex):
        self.regex = regex
        self.pos = 0
        self.current = self.regex[self.pos] if self.regex else None

    def advance(self):
        self.pos += 1
        if self.pos < len(self.regex):
            self.current = self.regex[self.pos]
        else:
            self.current = None

    def parse(self):
        node = self.parse_expr()
        if self.current is not None:
            raise Exception('Unexpected character at end of regex: ' + self.current)
        return node

    def parse_expr(self):
        left = self.parse_term()
        while self.current == '|':
            self.advance()
            right = self.parse_term()
            left = Node('|', left, right)
        return left

    def parse_term(self):
        left = self.parse_factor()
        while self.current is not None and self.current in 'ab':
            right = self.parse_factor()
            left = Node('concat', left, right)
        return left

    def parse_factor(self):
        node = self.parse_base()
        while self.current is not None and self.current in '*+?':
            op = self.current
            self.advance()
            node = Node(op, left=node)
        return node

    def parse_base(self):
        if self.current is not None and self.current in 'ab':
            node = Node('char', value=self.current)
            self.advance()
            return node
        else:
            raise Exception('Unexpected character: ' + (self.current if self.current else 'EOF'))

class Instruction:
    def __init__(self, op, arg1=None, arg2=None):
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2


class CodeGenerator:
    def __init__(self):
        self.instructions = []

    def new_instruction(self, op, arg1=None, arg2=None):
        instr = Instruction(op, arg1, arg2)
        self.instructions.append(instr)
        return len(self.instructions) - 1

    def generate(self, node):
        if node.type == 'char':
            self.new_instruction('char', node.value)
        elif node.type == 'concat':
            self.generate(node.left)
            self.generate(node.right)
        elif node.type == '|':
            split_idx = self.new_instruction('split', None, None)
            self.generate(node.left)
            jmp_idx = self.new_instruction('jmp', None)
            self.instructions[split_idx].arg1 = split_idx + 1
            self.instructions[split_idx].arg2 = len(self.instructions)
            self.generate(node.right)
            self.instructions[jmp_idx].arg1 = len(self.instructions)
        elif node.type == '*':
            start_idx = len(self.instructions)
            split_idx = self.new_instruction('split', None, None)
            self.instructions[split_idx].arg1 = split_idx + 1
            self.instructions[split_idx].arg2 = None  # Will be set later
            self.generate(node.left)
            self.new_instruction('jmp', start_idx)
            self.instructions[split_idx].arg2 = len(self.instructions)
        elif node.type == '+':
            start_idx = len(self.instructions)
            self.generate(node.left)
            split_idx = self.new_instruction('split', start_idx, len(self.instructions) + 1)
        elif node.type == '?':
            split_idx = self.new_instruction('split', None, None)
            self.instructions[split_idx].arg1 = split_idx + 1
            self.instructions[split_idx].arg2 = None  # Will be set later
            self.generate(node.left)
            self.instructions[split_idx].arg2 = len(self.instructions)
        else:
            raise Exception('Unknown node type: ' + node.type)

def run_vm(instructions, input_string):
    states = [(0, 0)]
    input_len = len(input_string)
    visited = set()
    while states:
        new_states = []
        for pc, idx in states:
            if (pc, idx) in visited:
                continue
            if pc >= len(instructions):
                continue
            visited.add((pc, idx))
            instr = instructions[pc]
            if instr.op == 'char':
                if idx < input_len and input_string[idx] == instr.arg1:
                    new_states.append((pc + 1, idx + 1))
            elif instr.op == 'match':
                if idx == input_len:
                    return True
            elif instr.op == 'jmp':
                new_states.append((instr.arg1, idx))
            elif instr.op == 'split':
                new_states.append((instr.arg1, idx))
                new_states.append((instr.arg2, idx))
        states = new_states
    return False
