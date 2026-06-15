import time
import chess
import random
from mistralai.client import Mistral
import dotenv
import os

dotenv.load_dotenv()
board = chess.Board()
client = Mistral(os.environ.get('API_KEY'))
player_turn = None
bot_color = None

def ai_question():
    global board, bot_color
    legal_moves = [move.uci() for move in board.legal_moves]
    prompt = f"""
    GOAL
    ---
    You are playing a chess game as {bot_color}. Your objective is to return legal chess moves. 
    Do not return any statements. You are a chess bot. Not an assistant.
    
    CHESS BOARD STATE
    ---
    FEN of current board: {board.fen()}
    ASCII of Current board: {board}

    
    
    LEGAL MOVES
    ---
    
    Legal Moves:
    {legal_moves}
    """
    inputs = [
        {"role":"user","content": prompt}
    ]

    response = client.beta.conversations.start(
        agent_id="ag_019ecc16c399712cb680462f95038420",
        agent_version=0,
        inputs=inputs,
    )
    print(response.outputs[0].content)
    return response.outputs[0].content

def ai_move():
    global board
    try:
        str_move = ai_question()
        move = chess.Move.from_uci(str_move)

        if move in board.legal_moves:
            board.push(move)
            return str_move
        else:
            print("Illegal move from the AI: ", move)
            return None
    except ValueError:
        print("Illegal UCI from the AI")
        return None

def player_move():
    while True:
        player_input = input("Input your move: ")
        try:
            move = chess.Move.from_uci(player_input)
            if move in board.legal_moves:
                board.push(move)
                break
            else:
                print("Illegal move from the player: ", move)
        except ValueError:
            print("Illegal UCI from the player")

def game():
    global board, player_turn
    player_turn = random.choice([True, False])
    if player_turn:
        print("Player is playing as whites.")
        bot_color = "blacks"
    else:
        print("Bot is playing as whites.")
        bot_color = "whites"
    while not board.is_game_over():
        print(f"{board}\n")
        if board.turn == player_turn:
            player_move()
        else:
            ai_move()
    if board.is_checkmate():
        if board.turn == player_turn:
            print("Bot wins by checkmate!")
        else:
            print("Player wins by checkmate!")
    elif board.is_insufficient_material():
        print("Draw by insufficient material!")
    elif board.is_repetition():
        print("Draw by repetition!")
    else:
        print("Draw by Stalemate!")

played = input("Have you played this before? (y/n)").lower().strip()
if played == "n":
    input("Press enter to start playing chess...")
    print("Enter moves in UCI format.")
    time.sleep(1)
    print("Examples:")
    time.sleep(1)
    print("  e2e4  (pawn from e2 to e4)")
    time.sleep(1)
    print("  g1f3  (knight from g1 to f3)")
    time.sleep(1)
    print("  e7e8q (promote to queen)")
    time.sleep(1)
    print("Good luck!!")
    input("Press enter to continue... ")
game()
if board.is_checkmate():
    if board.turn == player_turn:
        print("Player has won!")
    else:
        print("The bot has won!")
else:
    print("Draw!")

