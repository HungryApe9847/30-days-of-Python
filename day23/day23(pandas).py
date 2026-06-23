# you will probably remember this code from the nuitka!

import pandas as pd
import random
from art import text2art
length = 5
width = 5
grid = [["."for x in range(length)] for y in range(width)]
moves = 0

try:
    save_data = pd.read_json("save_data.json", orient = "index")
    save_data_available = True
except FileNotFoundError:
    save_data_available = False

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Player:
    global grid
    def __init__(self, name, position):
        self.name = name
        self.pos = position
    def move(self, direction):
        global grid
        if direction == "save":
            if save_data_available:
                print("Saving progress to save_data.json...")
                save_dict = {
                    "player_pos": {"x": self.pos.x, "y": self.pos.y},
                    "treasure_pos": {"x": treasure_pos.x, "y": treasure_pos.y}
                }
                pd.DataFrame(save_dict).to_json("save_data.json", orient="columns")
                print("Game saved successfully!")
                return "saved"
            else:
                print("Save data not available.")
                return "saved"
        elif direction == "n":
            if self.pos.y > 0:
                self.pos.y -= 1

            else:
                print("You walk into a wall.")

        elif direction == "s":
            if self.pos.y < width-1:
                self.pos.y += 1

            else:
                print("You walk into a wall.")

        elif direction == "w":
            if self.pos.x > 0:
                self.pos.x -= 1

            else:
                print("You walk into a wall.")

        elif direction == "e":
            if self.pos.x < length-1:
                self.pos.x += 1

            else:
                print("You walk into a wall.")

        else:
            print("Invalid direction.")

        grid = [["." for x in range(length)] for y in range(width)]
        grid[player.pos.y][player.pos.x] = "P"
        return "moved"

def draw_grid():
    global grid
    for row in grid:
        print("  ".join(row))

print(text2art("Treasure      Hunter!"))
username = input("What is your name? ")
while True:
    loading = input("Do you want to load save data? ")
    if loading == "n":
        player = Player(username, Vector2(random.randint(0, length-1), random.randint(0, width-1)))
        while True:
            treasure_pos = Vector2(random.randint(0, length - 1), random.randint(0, width - 1))
            if treasure_pos.x != player.pos.x and treasure_pos.y != player.pos.y:
                break
        break
    elif loading == "y":
        if save_data_available:
            print("Loading save data...")
            px = int(save_data.loc["player_pos", "x"])
            py = int(save_data.loc["player_pos", "y"])
            tx = int(save_data.loc["treasure_pos", "x"])
            ty = int(save_data.loc["treasure_pos", "y"])
            player = Player(username, Vector2(px,py))
            treasure_pos = Vector2(tx,ty)
            print(f"Welcome back, {username}! Game loaded.")
            break
        else:
            print("Save data not available. Starting new save...")
            player = Player(username, Vector2(random.randint(0, length - 1), random.randint(0, width - 1)))
            while True:
                treasure_pos = Vector2(random.randint(0, length - 1), random.randint(0, width - 1))
                if treasure_pos.x != player.pos.x and treasure_pos.y != player.pos.y:
                    break

print("The aim of the game is to find the treasure. Walk around until you see it.")

grid[player.pos.y][player.pos.x] = "P"
draw_grid()
while True:
    grid = [["." for x in range(length)] for y in range(width)]
    status = player.move(input("type n, e, s, or w to move: "))
    if status == "saved":
        continue
    draw_grid()
    if player.pos.x == treasure_pos.x and player.pos.y == treasure_pos.y:
        moves += 1
        print(f"You found the treasure in {moves} turns!")
        print(text2art("You      win!"))
        break
    else:
        moves += 1
        print(f"No treasure here! Keep looking! (turn: {moves})")