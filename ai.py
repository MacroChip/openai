import gym
import universe  # register the universe environments
import random

FORWARD = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', False), ('KeyEvent', 'ArrowRight', False)]
RIGHT = [('KeyEvent', 'ArrowRight', True), ('KeyEvent', 'ArrowLeft', False)]
LEFT = [('KeyEvent', 'ArrowLeft', True), ('KeyEvent', 'ArrowRight', False)]

def main():
    env = gym.make('flashgames.CoasterRacer-v0')
    #env = gym.make('flashgames.DuskDrive-v0')
    env.configure(remotes=1)  # automatically creates a local docker container
    observation_n = env.reset()

    current_action = FORWARD
    action_n = [FORWARD for ob in observation_n]
    observation_n, reward_n, done_n, info = env.step(action_n)
    env.render()

    while True:
        current_action = determine_action(current_action, reward_n)
        action_n = [current_action for ob in observation_n]
        observation_n, reward_n, done_n, info = env.step(action_n)
        env.render()


def determine_action(current_action, reward_n):
    if (reward_n[0] > 0):
        next_action = current_action #keep doing what you are doing
    else:
        print("ACTION CHANGED")
        next_action = random.choice(list(filter(lambda x: x != current_action, [FORWARD, RIGHT, LEFT]))) #no rewards means we need to do something else
    return next_action

if __name__ == "__main__":
    main()
