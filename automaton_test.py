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

    def test_DFA_minimization(self):
        dfa = DFA(6, 2)
        dfa.fill_start_list(0)
        dfa.fill_accepted_list([1, 3])
        dfa.fill_transitions_list(0, 1, 0)
        dfa.fill_transitions_list(0, 2, 1)
        dfa.fill_transitions_list(1, 1, 0)
        dfa.fill_transitions_list(1, 2, 1)
        dfa.fill_transitions_list(2, 3, 0)
        dfa.fill_transitions_list(2, 0, 1)
        dfa.fill_transitions_list(3, 3, 0)
        dfa.fill_transitions_list(3, 0, 1)
        dfa.fill_transitions_list(4, 5, 0)
        dfa.fill_transitions_list(4, 4, 1)
        dfa.fill_transitions_list(5, 5, 0)
        dfa.fill_transitions_list(5, 4, 1)
        minimized_dfa = dfa.minimize()
        self.assertTrue(minimized_dfa.n < dfa.n)

        test_strings = [
            [0],
            [1, 0],
            [1, 1],
            [0, 1, 0],
            [0, 1, 1],
        ]
        for s in test_strings:
            self.assertEqual(dfa.work(s), minimized_dfa.work(s))

    def test_same_DFA_equivalence(self):
        dfa1 = DFA(2, 2)
        dfa1.fill_start_list(0)
        dfa1.fill_accepted_list([0])
        dfa1.fill_transitions_list(0, 1, 0)
        dfa1.fill_transitions_list(0, 0, 1)
        dfa1.fill_transitions_list(1, 0, 0)
        dfa1.fill_transitions_list(1, 1, 1)

        dfa2 = DFA(2, 2)
        dfa2.fill_start_list(0)
        dfa2.fill_accepted_list([0])
        dfa2.fill_transitions_list(0, 1, 0)
        dfa2.fill_transitions_list(0, 0, 1)
        dfa2.fill_transitions_list(1, 0, 0)
        dfa2.fill_transitions_list(1, 1, 1)

        self.assertTrue(dfa1.is_equivalent_to(dfa2))

    def test_DFA_equivalence(self):
        dfa1 = DFA(2, 2)
        dfa1.fill_start_list(0)
        dfa1.fill_accepted_list([0])
        dfa1.fill_transitions_list(0, 1, 0)
        dfa1.fill_transitions_list(0, 0, 1)
        dfa1.fill_transitions_list(1, 0, 0)
        dfa1.fill_transitions_list(1, 1, 1)

        dfa2 = DFA(3, 2)
        dfa2.fill_start_list(0)
        dfa2.fill_accepted_list([0])
        dfa2.fill_transitions_list(0, 1, 0)
        dfa2.fill_transitions_list(0, 0, 1)
        dfa2.fill_transitions_list(1, 0, 0)
        dfa2.fill_transitions_list(1, 1, 1)
        dfa2.fill_transitions_list(2, 2, 0)
        dfa2.fill_transitions_list(2, 2, 1)

        self.assertTrue(dfa1.is_equivalent_to(dfa2))

    def test_DFA_accepts_all(self):
        dfa_all = DFA(1, 2)
        dfa_all.fill_start_list(0)
        dfa_all.fill_accepted_list([0])
        dfa_all.fill_transitions_list(0, 0, 0)
        dfa_all.fill_transitions_list(0, 0, 1)
        minimized_dfa_all=dfa_all.minimize()
        self.assertTrue(minimized_dfa_all.accepts_all())

        dfa_not_all = DFA(2, 2)
        dfa_not_all.fill_start_list(0)
        dfa_not_all.fill_accepted_list([1])
        dfa_not_all.fill_transitions_list(0, 1, 0)
        dfa_not_all.fill_transitions_list(0, 0, 1)
        dfa_not_all.fill_transitions_list(1, 1, 0)
        dfa_not_all.fill_transitions_list(1, 1, 1)
        minimized_dfa_not_all = dfa_not_all.minimize()
        self.assertFalse(minimized_dfa_not_all.accepts_all())

if __name__ == '__main__':
    unittest.main()