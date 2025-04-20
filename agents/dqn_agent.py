from .base_agent import BaseAgent

class DQNAgent(BaseAgent):
    """Deep Q-Network agent: uses a neural network to approximate Q-values."""

    def __init__(self, model=None, log_file='snake_agent.log'):
        """Initialize neural network model and logger."""
        # TODO: set up neural network model and logger
        pass

    def choose_direction(self, snake, apple, width, height, current_direction, wrap):
        """Select action by forwarding state through neural network."""
        # TODO: implement DQN action selection
        raise NotImplementedError
