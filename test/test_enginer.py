from stockfish import Stockfish
import time

path_enginer = "<folder>/stockfish.exe"
enginer = Stockfish(path_enginer, parameters=dict(Threads=3, UCI_Elo=2000, Hash=16))
moves = []

while True:
    t0 = time.time()
    move = enginer.get_best_move()
    t1 = time.time()
    moves.append(move)
    try:
        enginer.set_position(moves)
    except ValueError:
        print("winner:", enginer.get_wdl_stats())
        quit()
    board = enginer.get_board_visual()
    print(board)
    print(move)
    print(round((t1-t0)*1000), "ms")
    time.sleep(1)