def solve_four_queens():
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True
    
    def backtrack(board, row):
        if row == 4:
            solutions.append(board.copy())
            return
        
        for col in range(4):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(board, row + 1)
                board[row] = -1
    
    solutions = []
    backtrack([-1] * 4, 0)
    return solutions

def print_board(solution):
    for row in range(4):
        line = ""
        for col in range(4):
            if solution[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

def main():
    solutions = solve_four_queens()
    
    print(f"Задача: расставить 4 ферзя на доске 4x4")
    print(f"Найдено решений: {len(solutions)}\n")
    
    for i, sol in enumerate(solutions):
        print(f"Решение {i + 1}:")
        print(f"Позиции по рядам: {sol}")
        print_board(sol)

if __name__ == "__main__":
    main()