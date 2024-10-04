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
