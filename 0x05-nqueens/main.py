#!/usr/bin/python3
"""N queens puzzle"""

from typing import List
import sys


def solveNQueens(n: int) -> List[List[str]]:
    col = set()
    posDiag = set()  # r + c
    negDiag = set()  # r - c

    res = []
    board = [["." for _ in range(n)] for _ in range(n)]

    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return
  
        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue

            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "Q"

            backtrack(r + 1)

            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "."

    backtrack(0)
    return res

def convert_solution(board: List[str]) -> List[List[int]]:
    """Methode to convert board from list of str to List of int"""
    result = []
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == 'Q':
                result.append([r, c])
                break  # Move to the next row once the queen is found in the current row
    return result


def isvalidargs() -> int:
    """Methode to determins if args are valid
    And if the argv[1] is int and greater than 4"""
    # If the user called the program with the wrong number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    
    # N must be an integer greater or equal to 4
    try:
        n = int(sys.argv[1])
    except:
        print("N must be a number")
        exit(1)
    if n < 4:
        print("N must be at least 4")
        exit(1)

    return n


if __name__ == "__main__":
    solutions = solveNQueens(isvalidargs())
    converted_solutions = [convert_solution(board) for board in solutions]
    for solution in converted_solutions:
        print(solution)
