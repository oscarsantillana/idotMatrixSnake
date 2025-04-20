from .base_agent import BaseAgent

class QLearningAgent(BaseAgent):
    """Q-learning agent: uses a tabular Q-table for state-action value estimates."""

    def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.1, log_file='snake_agent.log'):
        """Initialize learning rate, discount factor, exploration rate, and logging."""
        # TODO: set up Q-table and logger
        pass

    def choose_direction(self, snake, apple, width, height, current_direction, wrap):
        """Select action based on ε-greedy policy derived from Q-table."""
        # TODO: implement Q-learning decision logic
        raise NotImplementedError
