import collections


class Solver:

    def __init__(self, puzzle):
        self.puzzle = puzzle

    def valid_move(self):
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        blocks = collections.defaultdict(set)

        for row in range(9):
            for col in range(9):
                curr = self.puzzle.board[row][col]
                if curr == 'X':
                    continue
                elif curr in rows[row] or curr in cols[col] or curr in blocks[(row // 3, col // 3)]:
                    return False
                rows[row].add(curr)
                cols[col].add(curr)
                blocks[(row // 3, col // 3)].add(curr)

        return True

    def brute_force(self):
        variables = []

        # get a set of all empty cells
        for row in range(9):
            for col in range(9):
                if self.puzzle.board[row][col] == 'X':
                    variables.append((row, col))

        # check every possible board arrangement
        def check_permutations(var):
            if var >= len(variables):
                return False

            (r, c) = variables[var]
            for num in range(1, 10):
                self.puzzle.board[r][c] = str(num)
                self.puzzle.pprint()
                check_permutations(var+1)
                if self.valid_move():
                    return True

        check_permutations(0)

    def backtracking(self):
        variables = []

        # get a set of all empty cells
        for row in range(9):
            for col in range(9):
                if self.puzzle.board[row][col] == 'X':
                    variables.append((row, col))
        variables.reverse()

        # recurse until solved
        def solve_further():
            pass

        solve_further()

    def is_solved(self):
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        blocks = collections.defaultdict(set)

        for row in range(9):
            for col in range(9):
                curr = self.puzzle.board[row][col]
                if curr == 'X':
                    return False
                elif curr in rows[row] or curr in cols[col] or curr in blocks[(row // 3, col // 3)]:
                    return False
                rows[row].add(curr)
                cols[col].add(curr)
                blocks[(row // 3, col // 3)].add(curr)

        return True
