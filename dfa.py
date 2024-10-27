from collections import deque
class DFA:
    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.accepted = [False for _ in range(n)]
        self.transitions = [[-1 for _ in range(m)] for _ in range(n)]
        self.start = -1
    def fill_accepted_list(self, accepted_list):
        for q in accepted_list:
            assert 0 <= q < self.n
            self.accepted[q] = True
    def fill_transitions_list(self, _from: int, _to: int, symbol: int) -> None:
        assert 0 <= _from < self.n and 0 <= _to < self.n and 0 <= symbol < self.m
        self.transitions[_from][symbol] = _to
    def fill_start_list(self, _start: int) -> None:
        assert 0 <= _start < self.n
        self.start = _start
    def work(self, arr):
        assert self.start != -1
        cur = self.start
        for val in arr:
            if self.transitions[cur][val] == -1:
                return False
            cur = self.transitions[cur][val]
        return self.accepted[cur]

    def remove_unreachable_states(self):
        reachable = [False] * self.n
        queue = [self.start]
        reachable[self.start] = True
        while queue:
            state = queue.pop(0)
            for symbol in range(self.m):
                next_state = self.transitions[state][symbol]
                if next_state != -1 and not reachable[next_state]:
                    reachable[next_state] = True
                    queue.append(next_state)

        state_mapping = {}
        new_index = 0
        for i in range(self.n):
            if reachable[i]:
                state_mapping[i] = new_index
                new_index += 1
        new_n = new_index
        new_transitions = [[-1 for _ in range(self.m)] for _ in range(new_n)]
        new_accepted = [False] * new_n
        for old_state, new_state in state_mapping.items():
            new_accepted[new_state] = self.accepted[old_state]
            for symbol in range(self.m):
                old_next_state = self.transitions[old_state][symbol]
                if old_next_state != -1 and old_next_state in state_mapping:
                    new_transitions[new_state][symbol] = state_mapping[old_next_state]
        self.n = new_n
        self.transitions = new_transitions
        self.accepted = new_accepted
        self.start = state_mapping[self.start]

    def minimize(self):
        self.remove_unreachable_states()
        partition = []
        accepting_states = set()
        non_accepting_states = set()
        for state in range(self.n):
            if self.accepted[state]:
                accepting_states.add(state)
            else:
                non_accepting_states.add(state)
        if accepting_states:
            partition.append(accepting_states)
        if non_accepting_states:
            partition.append(non_accepting_states)

        state_to_partition = {}
        for idx, group in enumerate(partition):
            for state in group:
                state_to_partition[state] = idx

        changed = True
        while changed:
            changed = False
            new_partition = []
            for group in partition:
                signatures = {}
                for state in group:
                    signature = []
                    for symbol in range(self.m):
                        next_state = self.transitions[state][symbol]
                        if next_state == -1:
                            signature.append(-1)
                        else:
                            signature.append(state_to_partition[next_state])
                    signature = tuple(signature)
                    if signature not in signatures:
                        signatures[signature] = set()
                    signatures[signature].add(state)
                for new_group in signatures.values():
                    new_partition.append(new_group)
                if len(signatures) > 1:
                    changed = True
            partition = new_partition
            state_to_partition = {}
            for idx, group in enumerate(partition):
                for state in group:
                    state_to_partition[state] = idx

        new_n = len(partition)
        new_transitions = [[-1 for _ in range(self.m)] for _ in range(new_n)]
        new_accepted = [False] * new_n
        new_start = state_to_partition[self.start]
        for idx, group in enumerate(partition):
            representative = next(iter(group))
            new_accepted[idx] = self.accepted[representative]
            for symbol in range(self.m):
                next_state = self.transitions[representative][symbol]
                if next_state != -1:
                    new_transitions[idx][symbol] = state_to_partition[next_state]
        minimized_dfa = DFA(new_n, self.m)
        minimized_dfa.transitions = new_transitions
        minimized_dfa.accepted = new_accepted
        minimized_dfa.start = new_start
        return minimized_dfa

    def is_equivalent_to(self, other_dfa):
        if self.m != other_dfa.m:
            return False

        minimized_self = self.minimize()
        minimized_other = other_dfa.minimize()

        if minimized_self.n != minimized_other.n:
            return False

        state_mapping = {}
        queue = deque()
        queue.append((minimized_self.start, minimized_other.start))
        state_mapping[minimized_self.start] = minimized_other.start

        while queue:
            s1, s2 = queue.popleft()
            if minimized_self.accepted[s1] != minimized_other.accepted[s2]:
                return False
            for symbol in range(self.m):
                n1 = minimized_self.transitions[s1][symbol]
                n2 = minimized_other.transitions[s2][symbol]
                if n1 == -1 and n2 == -1:
                    continue
                if n1 == -1 or n2 == -1:
                    return False
                if n1 in state_mapping:
                    if state_mapping[n1] != n2:
                        return False
                else:
                    state_mapping[n1] = n2
                    queue.append((n1, n2))
        if len(state_mapping) != minimized_self.n:
            return False
        return True

    def accepts_all(self):
        visited = [False] * self.n
        queue = deque()
        queue.append(self.start)
        visited[self.start] = True
        while queue:
            state = queue.popleft()
            if not self.accepted[state]:
                return False
            for symbol in range(self.m):
                next_state = self.transitions[state][symbol]
                if next_state == -1:
                    return False
                if not visited[next_state]:
                    visited[next_state] = True
                    queue.append(next_state)
        return True
