from abc import ABC, abstractmethod


class AbstractLogger(ABC):
    """
    Abstract object that represents a logger.
    """

    @abstractmethod
    def log_item(self, item, message, **kwargs):
        """
        Log method (abstract)

        :param item: item to log about

        :param message: message to print

        :param kwargs:

        :return:
        """


class AbstractInstant(AbstractLogger):
    """
    Subclass of AbstractLogger of when the abstract class that gives
     the result immediately
    """

    @abstractmethod
    def log_item(self, item, message, **kwargs):
        """
        Log method (abstract) instant

        :param item: item to log about

        :param message: message to print

        :param kwargs:

        :return: something to yield about (since it is instant)
        """


class AbstractDelayed(AbstractLogger):
    """
    Subclass of AbstractLogger of when the abstract class gives the result
    only at the end using yield_results
    """

    @abstractmethod
    def log_item(self, item, message, **kwargs) -> None:
        """
        Log method (abstract) delayed

        :param item: item to log about

        :param message: message to print

        :param kwargs:

        :return: None
        """

    @abstractmethod
    def yield_results(self, dict_elements_arguments, **kwargs):
        """
        This method is how the user wants to see the log file.

        See also blueprints.py that contains examples.

        :param dict_elements_arguments: Parameters for the method

        :param kwargs:

        :return:
        """
