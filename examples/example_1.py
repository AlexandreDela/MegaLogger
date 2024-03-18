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