from dfa import DFA
from nfa import NFA

def nfa_to_dfa_converter(nfa: NFA) -> DFA:
    n, m = nfa.n, nfa.m
    dfa = DFA(1 << n, m)
    dfa.fill_start_list(sum((1 << i) for i in nfa.start))
    for i in range(1 << n):
        for value in range(m):
            a = [0] * n
            for j in range(n):
                if i & (1 << j):
                    for b in nfa.transitions[j][value]:
                        a[b] = 1
            final = sum((1 << k) * a[k] for k in range(n))
            dfa.fill_transitions_list(i, final, value)

    dfa.fill_accepted_list([i for i in range(1 << n) if any((i & (1 << j)) and nfa.accepted[j] for j in range(n))])
    return dfa
