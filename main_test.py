import unittest
from dfa import DFA
from nfa import NFA
from converter import nfa_to_dfa_converter

def load_automaton_from_file(filename, automaton_type):
    with open(filename, "r") as file:
        lines = file.readlines()
        n, m = int(lines[0].strip()), int(lines[1].strip())
        automaton = automaton_type(n, m)
        start_states = list(map(int, lines[3].strip().split()))
        automaton.fill_start_list(start_states if isinstance(automaton, NFA) else start_states[0])
        accepted_states = list(map(int, lines[4].strip().split()))
        automaton.fill_accepted_list(accepted_states)
        for line in lines[5:-1]:
            f, t, val = map(int, line.strip().split())
            automaton.fill_transitions_list(f, t, val)
        test_string = list(map(int, lines[-1].strip().split()))

    return automaton, test_string

def execute_automaton(filename, automaton_type):
    automaton, test_string = load_automaton_from_file(filename, automaton_type)
    return automaton.work(test_string)

class TestAutomaton(unittest.TestCase):
    def test_DFA_true(self):
        self.assertTrue(execute_automaton("dfa_test_true", DFA))

    def test_DFA_false(self):
        self.assertFalse(execute_automaton("dfa_test_false", DFA))

    def test_NFA_true(self):
        self.assertTrue(execute_automaton("nfa_test_true", NFA))

    def test_NFA_false(self):
        self.assertFalse(execute_automaton("nfa_test_false", NFA))

    def test_NFA_to_DFA(self):
        nfa, test_string = load_automaton_from_file("nfa_test_false", NFA)
        dfa = nfa_to_dfa_converter(nfa)
        self.assertEqual(nfa.work(test_string), dfa.work(test_string))

if __name__ == '__main__':
    unittest.main()