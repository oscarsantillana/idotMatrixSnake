import logging
import heapq
from .base_agent import BaseAgent

class AStarAgent(BaseAgent):
    """A* agent: finds optimal path to apple avoiding self-collision."""

    def __init__(self, log_file='snake_agent.log'):
        self.logger = logging.getLogger('AStarAgent')
        handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def heuristic(self, a, b, width, height, wrap):
        dx = abs(a[0] - b[0])
        dy = abs(a[1] - b[1])
        if wrap:
            dx = min(dx, width - dx)
            dy = min(dy, height - dy)
        return dx + dy

    def choose_direction(self, snake, apple, width, height, current_direction, wrap):
        head = snake[-1]
        obstacles = set(snake)
        frontier = []
        # state: (f=g+h, g, position, first_move)
        heapq.heappush(frontier, (self.heuristic(head, apple, width, height, wrap), 0, head, None))
        cost_so_far = {head: 0}
        first_move = None

        while frontier:
            f, g, current, first = heapq.heappop(frontier)
            if current == apple:
                first_move = first or current_direction
                break
            for d in [(1,0),(-1,0),(0,1),(0,-1)]:
                # avoid reversing on first move
                if current == head and d == (-current_direction[0], -current_direction[1]):
                    continue
                nx, ny = current[0] + d[0], current[1] + d[1]
                if wrap:
                    nx %= width; ny %= height
                else:
                    if nx < 0 or nx >= width or ny < 0 or ny >= height:
                        continue
                neighbor = (nx, ny)
                # treat apple as free
                if neighbor in obstacles and neighbor != apple:
                    continue
                new_cost = g + 1
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    pri = new_cost + self.heuristic(neighbor, apple, width, height, wrap)
                    heapq.heappush(frontier, (pri, new_cost, neighbor, d if first is None else first))
        if first_move is None:
            # no path found: keep current direction
            first_move = current_direction
        self.logger.info(f"Head:{head} Apple:{apple} Chosen:{first_move}")
        return first_move
