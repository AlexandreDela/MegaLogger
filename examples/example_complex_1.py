from src import megalogger
import typing
import pandas as pd


class ID_Item:
    def __init__(self,
                 plant,
                 revision,
                 configuration,
                 unique_id):
        self.plant = plant
        self.revision = revision
        self.configuration = configuration
        self.unique_id = unique_id

    def to_tuple(self) -> typing.Tuple[str, str, str, str]:
        return (self.plant, self.revision,
                self.configuration, self.unique_id)

    def to_string(self) -> str:
        return (f"<{self.plant}, {self.revision}, "
                f"{self.configuration}, {self.unique_id}>")


class Solar_Sensor(src.megalogger.megalogged.MegaLoggedItemTuple):
    def __init__(self,
                 power,
                 unique_id: ID_Item,
                 has_backsheet: bool):
        self.power = power
        self.life_expectancy: int = 10
        self.unique_id: ID_Item = unique_id
        self.has_backsheet: bool = has_backsheet

    def to_tuple(self):
        plant, revision, configuration, unique_id = (
            self.unique_id.to_tuple())
        return (self.power,
                self.life_expectancy,
                plant,
                revision,
                configuration,
                unique_id,
                self.has_backsheet)

class Wind_Turbine(src.megalogger.megalogged.MegaLoggedItemString):
    def __init__(self,
                 power,
                 turbine_company,
                 unique_id: ID_Item):
        self.power = power
        self.turbine_company = turbine_company
        self.unique_id : ID_Item = unique_id

    def to_string(self) -> str:
        plant, revision, configuration, unique_id = (
            self.unique_id.to_tuple())
        return (f"<{self.power}, {self.turbine_company}, {plant}"
                f", {revision}, {configuration} {unique_id}>")

class MyDelayedHandler(src.megalogger.abstract_logger.AbstractDelayed):
    def __init__(self):
        self.internal_list_tuple : typing.List = list()
        self.internal_list_string: typing.List[str] = list()


    def log_item(self,
                 item: typing.Union[
                     src.megalogger.megalogged.MegaLoggedItemTuple,
                     src.megalogger.megalogged.MegaLoggedItemString,
                 ],
                 message,
                 **kwargs) -> None:
        if isinstance(item, Solar_Sensor):
            tuple_equivalent = (*item.to_tuple(), message)
            self.internal_list_tuple.append(tuple_equivalent)
        elif isinstance(item, Wind_Turbine):
            if message is None:
                string_equivalent = item.to_string()
            else:
                string_equivalent = f"{item.to_string()},{message}"
            self.internal_list_string.append(string_equivalent)
        else:
            raise TypeError(f"Unknown item type {type(item)}")

    def yield_results(self,
                      dict_elements_arguments,
                      **kwargs):
        print(self.internal_list_tuple)
        df = pd.DataFrame.from_records(
            self.internal_list_tuple,
            columns=dict_elements_arguments["PANDAS_COLUMNS"]
        )
        df.to_excel(dict_elements_arguments["PANDAS"])

        with open(dict_elements_arguments["STRING"], "a") as f:
            f.write("\n".join(self.internal_list_string))


id_1 = ID_Item(
    plant="Plant Paris",
    unique_id="5154987",
    revision="B",
    configuration="RC 12.3"
)

id_2 = ID_Item(
    plant="Plant Saint-Denis",
    unique_id="5154989",
    revision="A",
    configuration="RC 9.5"
)
id_3 = ID_Item(
    plant="Plant Villetaneuse",
    unique_id="5154992",
    revision="C",
    configuration="RC 13.5"
)
id_4 = ID_Item(
    plant="Plant Enghien-les-Bains",
    unique_id="5154998",
    revision="G",
    configuration="RC 18.6"
)

solar_sensor_a = Solar_Sensor(
    power=54,
    unique_id=id_1,
    has_backsheet=True
)

solar_sensor_b = Solar_Sensor(
    power=2,
    unique_id=id_2,
    has_backsheet=False
)

wind_turbine_c = Wind_Turbine(
    power=1000,
    unique_id=id_3,
    turbine_company="Louisette"
)


wind_turbine_d = Wind_Turbine(
    power=750,
    unique_id=id_4,
    turbine_company="Maurice"
)

myhandler = MyDelayedHandler()

mylogger = megalogger.megalogger.MegaLogger(
    check_abstract_base_class=True,
    print_yield=True
)

mylogger.add_delayed_handlers(myhandler)

myhandler.log_item(solar_sensor_a, "Invalid power")
myhandler.log_item(solar_sensor_b, "Invalid plant format")
myhandler.log_item(wind_turbine_c, "Unrecognized Turbine Company")
myhandler.log_item(wind_turbine_d, "Invalid ID")

dict_data = {
    "PANDAS" : "./a.xlsx",
    "PANDAS_COLUMNS" : [
        "Power",
        "Life Expectancy",
        "Plant",
        "Revision",
        "Configuration",
        "Unique ID",
        "Has Backsheeet ?",
        "Message"
    ],
    "STRING": "./b.txt"
}

mylogger.yield_results(
    dict_elements_arguments=dict_data
)
