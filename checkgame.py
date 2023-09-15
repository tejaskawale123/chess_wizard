import chess.pgn
import chess.engine

# Load the PGN file
pgn_file = open("game.pgn")
game = chess.pgn.read_game(pgn_file)

# Set up the board and the engine
board = game.board()
engine = chess.engine.SimpleEngine.popen_uci("C://Users//bhava//Desktop//Chess//stockfish_15.1_win_x64_avx2//stockfish_15.1_win_x64_avx2//stockfish-windows-2022-x86-64-avx2.exe")

# Iterate over the moves in the game
for move in game.mainline_moves():
    # Make the move and get the resulting board
    board.push(move)

    # Check if the move is a checkmate or a stalemate
    if board.is_checkmate():
        print(f"{board.turn} is checkmated!")
        break
    elif board.is_stalemate():
        print("Stalemate!")
        break

    # Evaluate the move
    info = engine.analyse(board, chess.engine.Limit(time=2.0))
    score = info["score"].relative.score(mate_score=1000000)

    # Classify the move
    if abs(score) > 500:
        classification = "Mistake"
    elif abs(score) > 100:
        classification = "Inaccuracy"
    else:
        classification = "Good Move"

    # Print the move and its classification
    print(f"{board.fullmove_number}. {move} ({classification})")

    # Print a suggestion
    # print("heelo")
    print(score)
    if classification == "Mistake":
        if score > 0:
            print("Suggestion: Consider playing a more defensive move.")
        else:
            print("Suggestion: Look for ways to attack or counterattack.")
    elif classification == "Inaccuracy":
        if score > 0:
            print("Suggestion: Consider playing a more aggressive move.")
        else:
            print("Suggestion: Look for ways to defend or consolidate your position.")
    elif classification == "Blunder":
        if score > 0:
            print("Suggestion: Consider playing a move that will force your opponent to defend.")
        else:
            print("Suggestion: Look for ways to save the situation or limit the damage.")
    else:
        print(classification)
    # Suggest the best move
    result = engine.play(board, chess.engine.Limit(time=2.0))
    print(f"Best move: {result.move}")

# Print the final board
print(board)

# Close the engine
engine.quit()
