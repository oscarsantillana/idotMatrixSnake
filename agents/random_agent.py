from .base_agent import BaseAgent
import random

class RandomAgent(BaseAgent):
    """Random agent: picks a legal move uniformly at random."""

    def choose_direction(self, snake, apple, width, height, current_direction, wrap):
        """Select a random valid direction each turn."""
        # TODO: implement random move selection avoiding collisions
        raise NotImplementedError
