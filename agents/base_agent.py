from abc import ABC, abstractmethod

class BaseAgent(ABC):
    """Abstract base class for snake game agents."""

    @abstractmethod
    def choose_direction(self, snake, apple, width, height, current_direction, wrap):
        """
        Decide next move for the snake.
        :param snake: list of (x,y) tuples representing the snake body (head last)
        :param apple: (x,y) tuple for apple position
        :param width: board width
        :param height: board height
        :param current_direction: (dx,dy) tuple of current movement
        :param wrap: whether the board wraps around edges
        :return: new direction (dx,dy)
        """
        pass
