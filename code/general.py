'''
                AI Agents for OpenAI gym: CS 182 Final Project
--------------------------------------------------------------------------------
                     Nathan Williams and Mike Kolor

To train a specific agent on a game, run the following in the command shell:

python lander.py/lake.py [agent] [timesteps]

[agent] specifies which agent to use.  The following codes are valid:
    ppo2
    ppo1
    a2c
    dqn
    acer
    acktr
    trpo

If an an invalid code or no code is provided, the game defaults to PPO2

[timesteps] specifies how many frames of training to run.  Provided values must
be integers, and the default value is 10,000

'''

import sys
import time

from ppo2 import ppo2
from ppo1 import ppo1
from a2c import a2c
from dqn import dqn
from acer import acer
from acktr import acktr
from trpo import trpo
from hardcode import hardcode
from random_agent import random_agent

def run(env_id, game):
    print("Selected game: {}.".format(env_id))

    # specify timesteps for training
    if len(sys.argv)<3:
        print("No timesteps specified; defaulting to 10,000.")
        timesteps = 10000
    else:
        try:
            timesteps = int(sys.argv[2])
            print("Training with {} timesteps".format(timesteps))
        except ValueError:
            print("Invalid timesteps; must be integer. Defaulting to 10,000.")
            timesteps = 10000

    # begin timer
    start_time = time.time()

    # select agent based on user input, and specify output directory, and run
    # training episodes
    if len(sys.argv)<2:
        print("No agent specified; defaulting to PPO2.")
        ppo2(env_id, "../data/ppo2_{}_{}".format(game,timesteps), timesteps)
    else:
        code = sys.argv[1]
        if code == "ppo2":
            print("PPO2 selected.")
            ppo2(env_id, "../data/ppo2_{}_{}".format(game,timesteps), timesteps)
        elif code == "ppo1":
            print("PPO1 selected.")
            ppo1(env_id, "../data/ppo1_{}_{}".format(game,timesteps), timesteps)
        elif code == "a2c":
            print("A2C selected.")
            a2c(env_id, "../data/a2c_{}_{}".format(game,timesteps), timesteps)
        elif code == "dqn":
            print("DQN selected.")
            dqn(env_id, "../data/dqn_{}_{}".format(game,timesteps), timesteps)
        elif code == "acer":
            print("ACER selected.")
            acer(env_id, "../data/acer_{}_{}".format(game,timesteps), timesteps)
        elif code == "acktr":
            print("ACKTR selected.")
            acktr(env_id, "../data/acktr_{}_{}".format(game,timesteps), timesteps)
        elif code == "trpo":
            print("TRPO selected.")
            trpo(env_id, "../data/trpo_{}_{}".format(game,timesteps), timesteps)
        elif code == "hardcode":
            print("Hard-coded policy selected.")
            if game == "lander":
                print("Hard-coded policy can only be run on FrozenLake8x8; switching environments.")
            hardcode("FrozenLake8x8-v0", "../data/hardcode_lake_{}".format(timesteps), timesteps)
        elif code == "random":
            print("Random agent selected.")
            random_agent(env_id, "../data/random_agent_{}_{}".format(game,timesteps), timesteps)
        else:
            print("Invalid code; defaulting to PPO2")
            ppo2(env_id, "../data/ppo2_{}_{}".format(game,timesteps), timesteps)

    # end timer and display output
    elapsed_time = time.time() - start_time
    print("Run complete!")
    print("Time elapsed: {}.".format(elapsed_time))
    print("See output directory for data.")
