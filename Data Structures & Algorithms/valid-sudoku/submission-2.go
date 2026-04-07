func isValidSudoku(board [][]byte) bool {
    rows := make(map[int]map[byte]bool)
    cols := make(map[int]map[byte]bool)

    type square struct {
        row int
        col int
    }

    squares := make(map[square]map[byte]bool)
    

    for r:=0; r<9; r++ {
        for c:=0; c<9; c++ {
            value := board[r][c]
            sq := square{r/3, c/3}
            if value == '.' {
                continue
            }
            if rows[r] == nil {
                rows[r] = make(map[byte]bool)
            }

            if cols[c] == nil {
                cols[c] = make(map[byte]bool)
            }

            if squares[sq] == nil {
                squares[sq] = make(map[byte]bool)
            }

            if rows[r][value] || cols[c][value] || squares[sq][value]  {
                return false
            }

            rows[r][value] = true
            cols[c][value] = true
            squares[sq][value] = true
        }
    }
    return true
}
