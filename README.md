# Python3 iDotMatrix Snake Client

Interactive Snake game on the iDotMatrix LED matrix with support for pluggable AI agents and logging.

## Features

- Real‑time Snake game rendered on LED matrix device
- Pluggable agent framework (agents derive from `BaseAgent`)
- Built‑in agents:
  - GreedyAgent (min Manhattan distance)
  - AStarAgent (A* pathfinding)
  - LookaheadAgent (depth‑limited DFS)
  - RandomAgent (stub)
  - BFSAgent (stub)
  - HamiltonianAgent (stub)
  - MCTSAgent (stub)
  - QLearningAgent (stub)
  - DQNAgent (stub)
- Decision logging to `snake_agent.log`

## Installation

```bash
# clone repository
git clone https://github.com/<your‑username>/<repo‑name>.git
cd <repo‑name>

# create and activate Python 3 venv
python3 -m venv env
source env/bin/activate

# install dependencies
pip install -r requirements.txt
```

## Usage

```bash
# ensure device address is set (or use "auto")
export IDOTMATRIX_ADDRESS=<device_address>

# run game; choose an agent when prompted
python3 snake_game.py
```

When prompted for `Use agent?`, enter one of:
- `none` (manual keyboard/joystick control)
- `greedy`
- `astar`
- `lookahead`
- (any other stub agents once implemented)

## Logging

Agent decisions are appended to `snake_agent.log` with timestamp, head position, apple position, and chosen direction.

## Project Structure

```
├── snake_game.py       # main game loop
├── agents/             # agent implementations and stubs
│   ├── base_agent.py
│   ├── greedy_agent.py
│   ├── a_star_agent.py
│   ├── lookahead_agent.py
│   ├── random_agent.py  # stub
│   ├── bfs_agent.py     # stub
│   ├── hamiltonian_agent.py # stub
│   ├── mcts_agent.py    # stub
│   ├── q_learning_agent.py # stub
│   └── dqn_agent.py     # stub
└── requirements.txt     # Python dependencies
```

## License

MIT © 2025 <Your Name>