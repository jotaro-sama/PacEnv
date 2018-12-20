import numpy as np 

class PacActionSpace(object):
    def __init__(self):
        self.moves = ["up", "left", "right", "dowm"]
    def sample():
        return np.random.choice(a=moves)

init_state = [
            ["W", "W", "W", "W", "W", "W", "W", "W"],
            ["W", ".", ".", "G", "G", ".", ".", "W"],
            ["W", ".", "W", "W", "W", "W", ".", "W"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["W", ".", "W", ".", " ", "W", ".", "W"],
            ["W", ".", "W", ".", ".", "W", ".", "W"],
            ["W", ".", ".", ".", "P", ".", ".", "W"],
            ["W", "W", "W", "W", "W", "W", "W", "W"]
        ]

class PacEnv():
    def __init__(self):
        self.level_state = init_state
        self.score = 0
        self.game_over = False
        self.action_space = PacActionSpace()
        self.position = (6, 4)
    def step(self, a):
        reward = 0.0
        if a not in self.action_space.moves:
            raise ValueError
        else:
            new_pos = 0, 0
            pos = self.position
            st = self.state

            if a=="up":
                new_pos = pos[0] - 1, pos[1]
            elif a=="left":
                new_pos = pos[0], pos[1] -1
            elif a=="right":
                new_pos = pos[0], pos[1] + 1
            elif a=="down":
                new_pos = pos[0] + 1, pos[1]

            if (new_pos[0] < 0):
                 new_pos[0] = 7
            if (new_pos[1] < 0):
                new_pos[1] = 7
            if (new_pos[0] > 7):
                new_pos[0] = 0
            if (new_pos[1] > 7):
                new_pos[1] = 0

            if st[new_pos[0]][new_pos[1]] == "G":
                self.game_over = True
            elif st[new_pos[0]][new_pos[1]] == ".":
                self.score += 1
                st[new_pos[0]][new_pos[1]] == "P"
                st[pos[0]][pos[1]] == " "
                self.position = new_pos
            elif st[new_pos[0]][new_pos[1]] == " ":
                st[new_pos[0]][new_pos[1]] == "P"
                st[pos[0]][pos[1]] == " "
                self.position = new_pos
        ob = (self.level_state, self.score)
        return ob, reward, self.game_over, {"self.position" : self.position}

    def reset(self):
        self.level_state = init_state
        self.score = 0
        self.game_over = False
        self.action_space = PacActionSpace()
        self.position = (6, 4)
        return (self.level_state, self.score)