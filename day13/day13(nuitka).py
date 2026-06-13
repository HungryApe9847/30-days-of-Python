#Example code
import random
from art import text2art
length = 5
width = 5
grid = [["."for x in range(length)] for y in range(width)]
moves = 0

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Player:
    global grid
    def __init__(self, name):
        self.name = name
        self.pos = Vector2(random.randint(0, length-1), random.randint(0, width-1))
    def move(self, direction):
        global grid
        if direction == "n":
            if self.pos.y > 0:
                self.pos.y -= 1
            else:
                print("You walk into a wall.")
        if direction == "s":
            if self.pos.y < width-1:
                self.pos.y += 1
            else:
                print("You walk into a wall.")
        if direction == "w":
            if self.pos.x > 0:
                self.pos.x -= 1
            else:
                print("You walk into a wall.")
        if direction == "e":
            if self.pos.x < length-1:
                self.pos.x += 1
            else:
                print("You walk into a wall.")

        grid = [["." for x in range(length)] for y in range(width)]
        grid[player.pos.y][player.pos.x] = "P"

def draw_grid():
    global grid
    for row in grid:
        print("  ".join(row))

print(text2art("Treasure      Hunter!"))
username = input("What is your name? ")
player = Player(username)
while True:
    treasure_pos = Vector2(random.randint(0, length-1), random.randint(0, width-1))
    if treasure_pos.x != player.pos.x and treasure_pos.y != player.pos.y:
        break
print("The aim of the game is to find the treasure. Walk around until you see it.")

grid[player.pos.y][player.pos.x] = "P"
draw_grid()
while True:
    grid = [["." for x in range(length)] for y in range(width)]
    player.move(input("type n, e, s, or w to move: "))
    draw_grid()
    if player.pos.x == treasure_pos.x and player.pos.y == treasure_pos.y:
        moves += 1
        print(f"You found the treasure in {moves} turns!")
        print(text2art("You      win!"))
        break
    else:
        moves += 1
        print(f"No treasure here! Keep looking! (turn: {moves})")