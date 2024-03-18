import typing
import abstract_logger
from megalogged import MegaLoggedItem

class MegaLogger:
    """
    MegaLogger class
    """

    def __init__(
        self,
        check_abstract_base_class: bool = True,
        print_yield: bool = False,
    ) -> None:
        """
        Constructor

        :param check_abstract_base_class: boolean,
        if true check whether the correct MegaLogger
         abstract classes have been used

        :param print_yield: boolean,
        if true, prints the immediate handlers in the terminal
        """
        self._list_instant_handlers: typing.List[
            abstract_logger.AbstractInstant
        ] = []
        self._list_delayed_handlers: typing.List[
            abstract_logger.AbstractDelayed
        ] = []
        self.check_abstract_base_class: bool = check_abstract_base_class
        self.print_yield: bool = print_yield

    def add_instant_handlers(
        self, handler: abstract_logger.AbstractInstant
    ) -> None:
        """
        Add a handler to the list of instant handler list

        :param handler: Handler
        """
        if self.check_abstract_base_class:
            assert isinstance(handler, abstract_logger.AbstractInstant)
        self._list_instant_handlers.append(handler)

    def add_delayed_handlers(
        self, handler: abstract_logger.AbstractDelayed
    ) -> None:
        """
        Add a handler to the list of delayed handler list

        :param handler: Handler
        """
        if self.check_abstract_base_class:
            assert isinstance(handler, abstract_logger.AbstractDelayed)
        self._list_delayed_handlers.append(handler)

    def add_item(
        self,
        item_logged: MegaLoggedItem,
        message: typing.Optional[str] = None,
        **kwargs
    ):
        """
        Add the item item_logged with the message argument message.

        :param item_logged: Item to log (must be a subclass of MegaLoggedItem)

        :param message: text

        :param kwargs:
        """
        if self.check_abstract_base_class:
            assert isinstance(item_logged, MegaLoggedItem)

        for logger_i in self._list_delayed_handlers:
            logger_i.log_item(item_logged, message=message, **kwargs)
        if self.print_yield:
            list_return = []
            for logger_j in self._list_instant_handlers:
                list_return.append(
                    logger_j.log_item(item_logged, message=message, **kwargs)
                )
            if len(list_return) != 0:
                print(list_return)
        else:
            for logger_j in self._list_instant_handlers:
                logger_j.log_item(item_logged, message=message, **kwargs)

    def add_item_lists(
        self,
        list_items: typing.List[MegaLoggedItem],
        message: typing.Optional[str] = None,
        **kwargs
    ) -> None:
        """
        Same as add_item, but with a list

        :param list_items: List of items (subclass of MegaLoggedItem)

        :param message: string

        :param kwargs:
        """
        for item_i in list_items:
            self.add_item(item_logged=item_i, message=message, **kwargs)

    def add_item_tuple(
        self,
        list_items_tuple: typing.List[
            typing.Tuple[MegaLoggedItem, typing.Optional[str]]
        ],
        **kwargs
    ):
        for item_i, message_i in list_items_tuple:
            self.add_item(item_logged=item_i, message=message_i, **kwargs)

    def yield_results(self, **kwargs):
        for logger_j in self._list_delayed_handlers:
            logger_j.yield_results(**kwargs)
