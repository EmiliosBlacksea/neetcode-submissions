class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowsets = [set() for _ in range(9)]
        colsets = [set() for _ in range(9)]
        boxsets = [set() for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != ".":
                    number = board[i][j]
                    box = (i // 3) + 3 * (j // 3)
                    if (number in boxsets[box]) or (number in rowsets[i]) or (number in colsets[j]):
                        return False
                    rowsets[i].add(number)
                    colsets[j].add(number)
                    boxsets[box].add(number)
        return True