def checkmate(board):
    if not isinstance(board, str):
        print("Error")
        return

    board = board.splitlines()
    n = len(board)

    if n == 0 or any(len(row) != n for row in board):
        print("Error")
        return

    king_pos = None
    king_count = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'K':
                king_pos = (i, j)
                king_count += 1

    if king_count != 1:
        print("Error")
        return

    kr, kc = king_pos

    for pr, pc in [(kr + 1, kc - 1), (kr + 1, kc + 1)]:
        if 0 <= pr < n and 0 <= pc < n and board[pr][pc] == 'P':
            print("Success")
            return

    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        r, c = kr+dr, kc+dc
        while 0 <= r < n and 0 <= c < n:
            piece = board[r][c]
            if piece not in "KPRBQ":
                r += dr; c += dc 
                continue
            if piece in ['R','Q']:
                print("Success")
                return
            break

    for dr, dc in [(-1,-1),(-1,1),(1,-1),(1,1)]:
        r, c = kr+dr, kc+dc
        while 0 <= r < n and 0 <= c < n:
            piece = board[r][c]
            if piece not in "KPRBQ":
                r += dr; c += dc
                continue
            if piece in ['B','Q']:
                print("Success")
                return
            break
    print("Fail")
