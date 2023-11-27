import sys
from time import time
from Board_A20489853 import Puzzle
from Solver_A20489853 import Solver

if __name__ == "__main__":

    # Verify CLI arguments
    if len(sys.argv) != 3:
        print("ERROR: Not enough/too many/illegal input arguments.")
        sys.exit()

    ALGO, FILENAME = sys.argv[1], sys.argv[2]

    if not (ALGO == "1" or ALGO == "2" or ALGO == "3" or ALGO == "4") or FILENAME.rfind("testcase"):
        print("ERROR: Not enough/too many/illegal input arguments.")
        sys.exit()

    # Print assignment information

    print(f"Last_Name, First_Name, AXXXXXXXX solution: \n"
          f"Input file: {FILENAME} \n")
        
    # Begin solving
    puzzle = Puzzle(FILENAME)
    solver = Solver(puzzle)

    if ALGO == "1":
        print("Algorithm: Brute Force Search")
        t0 = time()
        solver.brute_force()
        t1 = time()
    elif ALGO == "2":
        print("Algorithm: Constraint Satisfaction Problem Back-tracking Search")
        t0 = time()
        solver.backtracking()
        t1 = time()
    elif ALGO == "3":
        print("Algorithm: CSP with Forward-checking and MRV Heuristics")
        t0 = time()
        solver.mrv_heuristics()
        t1 = time()
    elif ALGO == "4":
        print("Solution Verification")
        val = solver.is_solved()
        print("This is a valid, solved Sudoku puzzle.") if val else print("This is NOT a solved Sudoku puzzle.")
        sys.exit()

    # Write puzzle back to CSV file (testcase#_solution.csv)
    puzzle.write_to(FILENAME)

    print(f"Number of search tree nodes generated: {solver.nodes} \n"
          f"Search Time: {t1 - t0} seconds")
