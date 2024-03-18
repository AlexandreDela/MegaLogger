Welcome to MegaLogger's documentation!
======================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

What is this?
-------------

This module is a module designed to help deal with object-oriented logging.

When you are dealing with real-life object, it can be more convenient to
have an object-oriented approach to keep all of the underlying data when
trying to log them.

Example of usecases:

1. Logging all of the unavailable items whose manufacturing company shut down
2. Logging the items that do not fit requirements
3. Logging the items that have incoherent state with another database

How to use?
-----------

Examples are available inside the **example** folder.

How does it work?
-----------------

The module :mod:`megalogger` is centered around few submodules:

1. The submodule :mod:`megalogged` gives the abstract class
for the item to be logged (the component).

2. The submodule :mod:`megalogging` gives the meta-logging manager.

3. The submodule :mod:`blueprints` gives
abstract classes that are partially-implemented handlers for various
usecases like Pandas Excel, Pandas ODS, Pandas SQL, Text Stream.

4. The submodule :mod:`abstract_logger` gives abstract loggers.

Short example
~~~~~~~~~~~~~

In this example, we will have 4 solar sensors objects represented by the
class Solar_Sensor (child of the abstract class
:class:`megalogged.MegaLoggedItemTuple` ) and
the blueprint for Pandas Excel (we will build MyPandasLogger, child of
:class:`blueprints.PandasExcelLoggerBlueprint` ).

We will iterate over each of the sensors to find those with power below
3 watts and log them out on an Excel sheet.

.. code:: python

    from src import megalogger
    class Solar_Sensor(megalogger.MegaLoggedItemTuple):
        def __init__(self,
                     power,
                     unique_id,
                     has_backsheet: bool):
            self.power = power
            self.life_expectancy = 10
            self.unique_id = unique_id
            self.has_backsheet: bool = has_backsheet

        def to_tuple(self,
                     **kwargs):
            return (self.power,
                    self.life_expectancy,
                    self.unique_id,
                    self.has_backsheet)


    class MyPandasLogger(megalogger.PandasExcelLoggerBlueprint):
        def add_item(self,
                     item,
                     message,
                     **kwargs):
            if isinstance(item, Solar_Sensor):
                tuple_equivalent = (*item.to_tuple(), message)
                self.internal_list_tuple.append(tuple_equivalent)
            else:
                raise TypeError()

    solar_sensor_a =\
        Solar_Sensor(power=54,unique_id="1454", has_backsheet=False)
    solar_sensor_b =\
        Solar_Sensor(power=2,unique_id="1457", has_backsheet=True)
    solar_sensor_c =\
        Solar_Sensor(power=3.6,unique_id="1462", has_backsheet=False)
    solar_sensor_d =\
        Solar_Sensor(power=1.7,unique_id="1469", has_backsheet=False)
    mylogger = MyPandasLogger()
    for solar_iter in [solar_sensor_a,
                       solar_sensor_b,
                       solar_sensor_c,
                       solar_sensor_d]:
        if solar_iter.power < 3:
            mylogger.add_item(solar_iter,
                              f"Invalid power {solar_iter.power};"
                              f" must be above 3 Watts")


    mylogger.yield_results(
        dict_elements_arguments={
            "EXCEL_LOCATION": "./test.xlsx",
            "PANDAS_COLUMNS": [
                "Power",
                "Life expectancy",
                "Unique ID",
                "Has backsheet ?",
                "Message"
            ]
        }
    )


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
