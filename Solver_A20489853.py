import collections
import time


class Solver:

    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.nodes = 0

    def brute_force(self):
        # Get set of empty cells
        variables = self.get_vars()

        # check every possible board arrangement
        def check_permutations(var):
            if var >= len(variables):
                return False

            (r, c) = variables[var]
            for num in range(1, 10):
                self.nodes += 1
                self.puzzle.board[r][c] = str(num)
                self.puzzle.pprint()
                check_permutations(var+1)
                if self.valid_move():
                    return True

        check_permutations(0)

    def backtracking(self):
        # Get set of empty cells
        variables = self.get_vars()
        variables.reverse()

        # recurse until solved
        def solve_further():
            if len(variables) == 0:
                return
            r, c = variables.pop()

            for num in range(1, 10):
                self.nodes += 1
                self.puzzle.board[r][c] = str(num)
                if self.valid_move():
                    self.puzzle.pprint()
                    solve_further()
                if self.is_solved():
                    return
            self.puzzle.board[r][c] = 'X'
            variables.append((r, c))

        solve_further()

    def mrv_heuristics(self):
        # Generate set of all filled cells on board
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        blocks = collections.defaultdict(set)

        for row in range(9):
            for col in range(9):
                curr = self.puzzle.board[row][col]
                if curr == 'X':
                    continue
                rows[row].add(curr)
                cols[col].add(curr)
                blocks[(row // 3, col // 3)].add(curr)

        # Get a mapping of all empty cells to their minimum domain
        variables = []
        mappings = {}
        for row in range(9):
            for col in range(9):
                if self.puzzle.board[row][col] == 'X':
                    domain = []
                    for i in range(1, 10):
                        if str(i) not in rows[row] or str(i) not in cols[col] or str(i) not in blocks[(row // 3, col // 3)]:
                            domain.append(str(i))
                    if len(domain) == 1:
                        self.puzzle.board[row][col] = domain.pop()  # plug the value in immediately if only 1 remains
                    else:
                        mappings.setdefault((row, col), domain)
                        variables.append((row, col))
        variables.reverse()

        # If the puzzle is solved, print and return
        if len(variables) == 0:
            self.puzzle.pprint()
            return

        # Apply backtracking over remaining domain values
        def solve_further():
            if len(variables) == 0:
                return
            r, c = variables.pop()

            for num in mappings[(r, c)]:
                self.nodes += 1
                self.puzzle.board[r][c] = str(num)
                if self.valid_move():
                    self.puzzle.pprint()
                    solve_further()
                if self.is_solved():
                    return
            self.puzzle.board[r][c] = 'X'
            variables.append((r, c))

        solve_further()

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

    def get_vars(self):
        lst = []
        for row in range(9):
            for col in range(9):
                if self.puzzle.board[row][col] == 'X':
                    lst.append((row, col))
        return lst
