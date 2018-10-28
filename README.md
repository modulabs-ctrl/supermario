# supermario

## 기본 세팅

### 해당 repo clone 
```bash
$ git clone git+https://github.com/modulabs-ctrl/supermario.git
$ cd supermario 
```

### prerequisites 
Ubuntu 
```bash
$ sudo apt-get update && sudo apt-get install cmake libopenmpi-dev python3-dev zlib1g-dev
```

Mac OS
```bash
$ brew install cmake openmpi
```

### stable-baseline 설치
```bash
$ pip install stable-baselines
```

### gym-super-mario-bros 설치
```bash
$ pip install git+https://github.com/modulabs-ctrl/gym-super-mario-bros.git
```

## 추가된 Agents
### ppo2 agent (added by Wonseok Jung) 
- agents/ppo2_agent.py 
- ctrl_baselines/ppo2_render/ppo2_render.py

