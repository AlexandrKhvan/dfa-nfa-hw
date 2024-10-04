class NFA:
    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.accepted = [False for _ in range(n)]
        self.transitions = [[[] for _ in range(m)] for __ in range(n)]
        self.start = []
    def fill_accepted_list(self, accepted_list):
        for q in accepted_list:
            assert 0 <= q < self.n
            self.accepted[q] = True
    def fill_transitions_list(self, _from: int, _to: int, symbol: int) -> None:
        assert 0 <= _from < self.n and 0 <= _to < self.n and 0 <= symbol < self.m
        self.transitions[_from][symbol].append(_to)
    def fill_start_list(self, start_list) -> None:
        assert all(0 <= x < self.n for x in start_list)
        self.start = start_list
    def work(self, arr):
        def dfs(current: int, index: int) -> bool:
            if index == len(arr):
                return self.accepted[current]
            for i in self.transitions[current][arr[index]]:
                if dfs(i, index + 1):
                    return True
            return False

        return any(dfs(start, 0) for start in self.start)
