from checkmate import checkmate

def main():
    board2 = """\
R.
.K\
"""
    print("Board 2x2:")
    checkmate(board2)

    board4 = """\
R...
.K..
....
....\
"""
    print("Board 4x4:")
    checkmate(board4)

    board8 = """\
R.......
........
........
........
...K....
..B.....
........
........"""
    print("Board 8x8:")
    checkmate(board8)

if __name__ == "__main__":
    main()
