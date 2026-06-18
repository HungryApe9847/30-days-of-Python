import random
import time
from collections import deque

dq = deque()

class Player:
    def __init__(self, name, speed, strength, max_hp, spec_move):
        self.name = name
        self.speed = speed
        self.strength = strength
        self.max_hp = max_hp
        self.hp = self.max_hp
        self.spec_move = spec_move
    def attack(self, enemy):
        print(f"{self.name} attacks {enemy.name} for {self.strength} damage!")
        time.sleep(1)
        enemy.hp_change(0 - self.strength)
    def hp_change(self, damage):
        self.hp = self.hp + damage
        if self.hp <= 0:
            self.hp = 0
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print(f"{self.name}'s HP is now {self.hp}/{self.max_hp}.")
        time.sleep(1)
    def is_dead(self):
        return self.hp <= 0

class Enemy:
    def __init__(self, name, speed, strength, max_hp):
        self.name = name
        self.speed = speed
        self.strength = strength
        self.max_hp = max_hp
        self.hp = self.max_hp
    def hp_change(self, damage):
        self.hp = self.hp + damage
        if self.hp <= 0:
            self.hp = 0
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print(f"{self.name}'s HP is now {self.hp}/{self.max_hp}.")
        time.sleep(1)
    def attack(self, enemy):
        print(f"{self.name} attacks {enemy.name} for {self.strength} damage!")
        time.sleep(1)
        enemy.hp_change(0 - self.strength)
    def is_dead(self):
        return self.hp <= 0

class Combat:
    def __init__(self, player: Player, enemy: Enemy, dq: deque):
        self.player = player
        self.enemy = enemy
        self.dq = dq
    def combat(self):
        cooldown = 0
        while not player.is_dead() and not self.enemy.is_dead():
            turn = dq.pop()
            if turn == 1:
                print(f"\nIt's {self.player.name}'s turn!")
                time.sleep(1)
                if input("(A)Normal or (B)Special move? ").lower().strip() == "a":
                    self.player.attack(self.enemy)
                    cooldown -= 1
                else:
                    if cooldown <= 0.1:
                        self.player.attack(self.enemy)
                        dq.append(1)
                        cooldown = 1
                        print(f"{self.player.name} uses their special move: {self.player.spec_move}")
                        time.sleep(1)
                dq.appendleft(1)
            elif turn == 2:
                print(f"\nIt's {self.enemy.name}'s turn!")
                time.sleep(1)
                self.enemy.attack(self.player)
                dq.appendleft(2)
            else:
                print("Nobody's turn.")
        print()
        time.sleep(1)
        if self.enemy.is_dead():
            print("The player has won!")
        else:
            print("The enemy has won!")
    def start_combat(self):
        print(f"\n{self.enemy.name} enters the battle! HP: {self.enemy.hp}, Speed: {self.enemy.speed}, Strength: {self.enemy.strength}")
        time.sleep(1)
        if self.player.speed > self.enemy.speed:
            print(f"{self.player.name} is faster and goes first!")
            self.dq.append(1)
            self.dq.appendleft(2)
        else:
            print(f"{self.enemy.name} is faster and goes first!")
            self.dq.append(2)
            self.dq.appendleft(1)
        time.sleep(1)
        Combat.combat(self)


orc = Enemy("Orc", 10, 30, 50)
archer = Enemy("Archer", 50, 30, 30)
dragon = Enemy("Dragon", 50, 50, 50)
name = input("What is your name? ")
spec_move = random.choice(["Omega Slash!", "Giant Fireball of DOOOOM!", "Octuple frontflip kick!"])
player = Player(name, random.randint(1, 50), random.randint(5, 15), random.randint(40, 60), spec_move)
print(f"{player.name} enters the battle! HP: {player.hp}, Speed: {player.speed}, Strength: {player.strength}")
time.sleep(1)
combat = Combat(player, random.choice([orc, dragon, archer]), dq)
combat.start_combat()
