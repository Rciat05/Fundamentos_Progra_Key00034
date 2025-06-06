import time
import os

def load_file():
    filepath = input("Enter the path of the file to load: ")

    file = open(filepath, 'r', encoding='utf-8')
    lines = file.readlines()
    file.close()

    return lines

def set_enviroment(raw_file):
    env = []
    for line in raw_file:
        line = line.strip()
        env.append([int(c) for c in line])
    return env
    
def print_env(env):
    for row in env:
        for cell in row:
            if cell == 1:
                print("▬", end="")
            else:
                print(' ', end="")
        print()

def counter_neighbors(env, x, y):
    l1 = [x-1, x, x+1 ]
    l2 = [y-1, y, y+1 ]
    count = 0
    for i in  l1:
        for i in l2:
            if i == x and j == y:
                continue
            if env[i][j] == 1:
                if count < 2 or count > 3:
                    env[i][j]
                count += 1
    return count


my_file = load_file()
print(my_file)
env = set_enviroment(my_file)
print_env(env)

# Simulacion

for generation in range(25):
    for i in range(1, len(env)-1):
        for j in range(i, len(env[0])- 1):

