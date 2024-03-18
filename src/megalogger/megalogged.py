from abc import ABC, abstractmethod


class MegaLoggedItem(ABC):
    """
    Master item that represents an object to be logged
    """

    @abstractmethod
    def __init__(self, **kwargs):
        """
        Constructor
        """


class MegaLoggedItemString(MegaLoggedItem):
    """
    Subclass of MegaLoggedItem that implements to_string
    """

    @abstractmethod
    def __init__(self):
        """
        Constructor
        """

    def to_string(self, **kwargs) -> str:
        """
        Returns the element as a string

        :param kwargs:

        :return: string
        """


class MegaLoggedItemTuple(MegaLoggedItem):
    """
    Subclass of MegaLoggedItem that implements to_tuple
    """

    @abstractmethod
    def __init__(self):
        """
        Constructor
        """

    def to_tuple(self, **kwargs):
        """
        Returns the element as a tuple of any length

        :param kwargs:

        :return: a list of tuples (of any length)

        """
