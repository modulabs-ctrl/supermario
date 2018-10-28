__author__ = 'Wonseok Jung'
__maintainer__ = 'CTRL'
__date__ = '2018-10-28'

from nes_py.wrappers import BinarySpaceToDiscreteSpaceEnv
import gym_super_mario_bros
from ctrl_baselines import PPO2
from stable_baselines.common.policies import CnnPolicy
from stable_baselines.common.vec_env import DummyVecEnv

movements = [
    ['NOP'],
    ['A'],
    ['B'],
    ['right'],
    ['right', 'A'],
    ['right', 'B'],
    ['right', 'A', 'B'],
    ['left'],
    ['left', 'A'],
    ['left', 'B'],
    ['left', 'A', 'B'],
    #    ['down'],
    #    ['up']
]

_env = gym_super_mario_bros.make('SuperMarioBros-v0')
env = BinarySpaceToDiscreteSpaceEnv(_env, movements)
env = DummyVecEnv([lambda: env])

# 학습 과정을 보려면 render = True
model = PPO2(policy=CnnPolicy, env=env, verbose=1, render=True)
model.learn(total_timesteps=10000)

obs = env.reset()

while True:
    action, _info = model.predict(obs)

    obs, rewards, dones, info = env.step(action)
    print("학습끝")
    print(rewards)
    env.render()
