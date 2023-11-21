import sys
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

    # just a helper for printing information about the algorithm
    algorithms = {
        "1": "Brute Force Search",
        "2": "Constraint Satisfaction Problem Back-tracking Search",
        "3": "CSP with Forward-checking and MRV Heuristics",
        "4": "Solution Verification"
    }

    print(f"Last_Name, First_Name, AXXXXXXXX solution: \n"
          f"Input file: {FILENAME} \n"
          f"Algorithm: {algorithms[ALGO]}")

    # Begin solver
    puzzle = Puzzle(FILENAME)
    solver = Solver(puzzle)
    solver.brute_force()
