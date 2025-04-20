from .base_agent import BaseAgent

class BFSAgent(BaseAgent):
    """BFS agent: uses breadth-first search to find the shortest path to the apple."""

    def choose_direction(self, snake, apple, width, height, current_direction, wrap):
        """Perform BFS each turn to locate the apple."""
        # TODO: implement BFS pathfinding
        raise NotImplementedError
