from .base_agent import BaseAgent

class MCTSAgent(BaseAgent):
    """Monte Carlo Tree Search agent: uses random rollouts to evaluate each action."""

    def choose_direction(self, snake, apple, width, height, current_direction, wrap):
        """Perform MCTS each turn to select the best move."""
        # TODO: implement Monte Carlo Tree Search
        raise NotImplementedError
