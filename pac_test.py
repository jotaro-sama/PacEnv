import pac_env

def printMatrix(mat):
    for row in mat:
        for elem in row:
            print(str(elem), end=" ")
        print("")

env = pac_env.PacEnv()
(screen, score, power) = env.reset()
done = False
info = ""

print("Score: " + str(score))
printMatrix(screen)

for i in range(100):
        action = env.action_space.sample()
        print(action)
        (screen, score, power), _, done, info = env.step("left")
        printMatrix(screen)
        print("Score: " + str(score) + ", Power :" + str(power))
        print(str(info["self.position"]) + ", pow_timeout: " + str(info["self.power_timeout"]))
        if done:
                print("Game Over! \n" + "Score: " + str(score))
                break

