class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            rowList = [s for s in row if s != '.']
            #print(rowList) 
            if (len(rowList) != len(set(rowList))):
                return False
            
        for i in range(9):
            colList = [row[i] for row in board if row[i] != '.']
            #print(colList)
            if (len(colList) != len(set(colList))):
                return False
                 
        for j in range(0, 9, 3):
            small1, small2, small3 = [], [], []
            for row in board[j+0:j+3]:
                small1 += [num for num in row[0:3] if num != '.'] 
                small2 += [num for num in row[3:6] if num != '.']
                small3 += [num for num in row[6:] if num != '.']
            #print(small1)
            #print(small2)
            #print(small3)
            if len(small1) != len(set(small1)):
                return False
            if len(small2) != len(set(small2)):
                return False
            if len(small3) != len(set(small3)):
                return False
        return True