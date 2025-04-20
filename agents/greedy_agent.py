import logging
from .base_agent import BaseAgent

class GreedyAgent(BaseAgent):
    """Greedy agent: chooses move minimizing Manhattan distance to the apple."""

    def __init__(self, log_file='snake_agent.log'):
        self.logger = logging.getLogger('GreedyAgent')
        handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def choose_direction(self, snake, apple, width, height, current_direction, wrap):
        head = snake[-1]
        best_dir = current_direction
        min_dist = float('inf')
        # try all possible directions
        for d in [(1,0),(-1,0),(0,1),(0,-1)]:
            # avoid reversing
            if d == (-current_direction[0], -current_direction[1]):
                continue
            nx = head[0] + d[0]
            ny = head[1] + d[1]
            if wrap:
                nx %= width
                ny %= height
            else:
                if nx < 0 or nx >= width or ny < 0 or ny >= height:
                    continue
            if (nx, ny) in snake:
                continue
            dist = abs(nx - apple[0]) + abs(ny - apple[1])
            if dist < min_dist:
                min_dist = dist
                best_dir = d
        # log attempt
        self.logger.info(f"Head:{head} Apple:{apple} Chosen:{best_dir}")
        return best_dir
