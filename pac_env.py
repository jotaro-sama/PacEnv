import numpy as np 

class PacActionSpace(object):
    moves = ["up", "left", "right", "down"]
    def sample(self):
        return np.random.choice(a=self.moves)

init_state = [
           ["W", "W", "W", "W", "W", "W", "W", "W"],
           ["W", ".", ".", "G", "G", ".", ".", "W"],
           ["W", ".", "W", "W", "W", "W", ".", "W"],
           [".", ".", ".", ".", ".", ".", ".", "."],
           ["W", ".", "W", "o", ".", "W", ".", "W"],
           ["W", ".", "W", ".", ".", "W", ".", "W"],
           ["W", ".", ".", ".", "P", ".", ".", "W"],
           ["W", "W", "W", "W", "W", "W", "W", "W"]
        ]

power_duration = 6

def CheckOver(level_matrix):
    over = True
    for line in level_matrix:
        if "." in line:
            over = False
    return over

class PacEnv():
    def __init__(self):
        self.state = init_state
        self.score = 0
        self.game_over = False
        self.action_space = PacActionSpace()
        self.position = [6, 4]
        self.power = False
        self.power_timeout = 0
    
    def step(self, a):
        reward = 0.0
        if a not in self.action_space.moves:
            raise ValueError
        else:
            pos = self.position
            new_pos = pos
            st = self.state

            if a=="up":
                new_pos = [pos[0] - 1, pos[1]]
            elif a=="left":
                new_pos = [pos[0], pos[1] -1]
            elif a=="right":
                new_pos = [pos[0], pos[1] + 1]
            elif a=="down":
                new_pos = [pos[0] + 1, pos[1]] 

            if (new_pos[0] < 0):
                 new_pos[0] = 7
            if (new_pos[1] < 0):
                new_pos[1] = 7
            if (new_pos[0] > 7):
                new_pos[0] = 0
            if (new_pos[1] > 7):
                new_pos[1] = 0

            if st[new_pos[0]][new_pos[1]] == "G":
                if not self.power:
                    self.game_over = True
                else:
                    self.score += 3
                    self.state[new_pos[0]][new_pos[1]] = "P"
                    self.state[pos[0]][pos[1]] = " "
                    self.position = new_pos
                    self.state = st
            elif st[new_pos[0]][new_pos[1]] == ".":
                self.score += 1
                self.state[new_pos[0]][new_pos[1]] = "P"
                self.state[pos[0]][pos[1]] = " "
                self.position = new_pos
                self.state = st
            elif st[new_pos[0]][new_pos[1]] == "o":
                self.score += 1
                self.state[new_pos[0]][new_pos[1]] = "P"
                self.state[pos[0]][pos[1]] = " "
                self.position = new_pos
                self.state = st
                self.power = True
                self.power_timeout = power_duration
            elif st[new_pos[0]][new_pos[1]] == " ":
                self.state[new_pos[0]][new_pos[1]] = "P"
                self.state[pos[0]][pos[1]] = " "
                self.position = new_pos
        if self.power:
            if self.power_timeout == 0:
                self.power = False
            else:
                self.power_timeout -= 1

        self.game_over = CheckOver(self.state)

        ob = (self.state, self.score, self.power)
        return ob, reward, self.game_over, {"self.position" : self.position, "self.power_timeout" : self.power_timeout}

    def reset(self):
        self.state = init_state
        self.score = 0
        self.game_over = False
        self.action_space = PacActionSpace()
        self.position = [6, 4]
        self.power = False
        self.power_timeout = 0
        return (self.state, self.score, self.power)