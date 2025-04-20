from .base_agent import BaseAgent

class HamiltonianAgent(BaseAgent):
    """Hamiltonian agent: follows a fixed Hamiltonian cycle covering all cells."""

    def choose_direction(self, snake, apple, width, height, current_direction, wrap):
        """Traverse the precomputed Hamiltonian cycle to update direction."""
        # TODO: implement Hamiltonian cycle traversal
        raise NotImplementedError
