import gym
import CrowdSim.envs as envs
from gym import envs
env = gym.make('CrowdSim-v0')
obs=env.reset()
print(obs)
# for _ in range(5):
#     env.render()
# env.step(env.action_space.sample()) # take a random action

envids = [spec.id for spec in envs.registry.all()]
print("NUM:",len(envids))
for envid in sorted(envids):
    print(envid)
