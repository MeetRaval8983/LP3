"""A6: Backtracking 8 queens with first queen fixed at specified row/column."""
def solve(fixed_row,fixed_col):
    if not (0<=fixed_row<8 and 0<=fixed_col<8): raise ValueError('Positions must be 1..8')
    positions=[-1]*8;positions[fixed_row]=fixed_col
    def search(row):
        if row==8: return True
        if row==fixed_row:return search(row+1)
        for col in range(8):
            if all(other==-1 or (col!=other and abs(row-r)!=abs(col-other)) for r,other in enumerate(positions)):
                positions[row]=col
                if search(row+1):return True
                positions[row]=-1
        return False
    return positions if search(0) else None
if __name__=='__main__':
    row=int(input('First queen row 1..8 [1]: ') or '1')-1
    col=int(input('First queen column 1..8 [1]: ') or '1')-1
    result=solve(row,col)
    if result is None: print('No solution')
    else:
        for c in result: print(' '.join('Q' if j==c else '.' for j in range(8)))
