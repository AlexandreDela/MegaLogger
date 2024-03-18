import typing
import sqlite3
import pandas as pd
from . import AbstractLogger, AbstractDelayed, AbstractInstant


class PandasExcelLoggerBlueprint(AbstractDelayed):
    """
    Blueprint for a log as the form of a Excel format
    using pandas and openpyxl
    """

    def __init__(self):
        self.internal_list_tuple = []

    def log_item(self, item, message, **kwargs):
        raise NotImplementedError

    def yield_results(self, dict_elements_arguments, **kwargs) -> None:
        """
        Pandas export to Excel

        :param dict_elements_arguments: Contains in key "PANDAS_COLUMNS"
        the columns to use for pd.DataFrame.from_records and in key
        "EXCEL_LOCATION" the Excel location.
        """
        df = pd.DataFrame.from_records(
            self.internal_list_tuple,
            columns=dict_elements_arguments["PANDAS_COLUMNS"],
        )
        df.to_excel(dict_elements_arguments["EXCEL_LOCATION"])


class PandasODSLoggerBlueprint(AbstractDelayed):
    """
    Blueprint for a log as the form of a ODS format
    using pandas
    """

    def __init__(self):
        self.internal_list_tuple = []

    def log_item(self, item, message, **kwargs):
        raise NotImplementedError

    def yield_results(self, dict_elements_arguments, **kwargs) -> None:
        """
        Pandas export to ODS

        :param dict_elements_arguments: Contains in key "PANDAS_COLUMNS"
        the columns to use for pd.DataFrame.from_records and in key
        "ODS_LOCATION" the ODS location.
        """
        df = pd.DataFrame.from_records(
            self.internal_list_tuple,
            columns=dict_elements_arguments["PANDAS_COLUMNS"],
        )
        with pd.ExcelWriter(
            dict_elements_arguments["ODS_LOCATION"], engine="odf"
        ) as odf_writer:
            df.to_excel(odf_writer)


class DelayedStreamLoggerBlueprint(AbstractDelayed):
    """
    Blueprint for a log as the form of a string dump in a text file
    """

    def __init__(self):
        self.internal_list_string = []

    def log_item(self, item, message, **kwargs):
        raise NotImplementedError

    def yield_results(self, dict_elements_arguments, **kwargs) -> None:
        """
        Pandas export to a text file

        :param dict_elements_arguments: Contains in key "OUTPUT_FILE"
         the output file location.
        """
        with open(
            dict_elements_arguments["OUTPUT_FILE"], "w", encoding="utf-8"
        ) as f:
            f.write("\n".join(self.internal_list_string))


class InstantStreamLoggerBlueprint(AbstractInstant):
    """
    Blueprint for a log as the form of an instant dump in a text file
    """

    def __init__(self):
        pass

    def log_item(self, item, message, **kwargs) -> str:
        """
        Basic implementation of the instant dump to file

        :param item:

        :param message:

        :param kwargs: Must contain the key "FILE_LOCATION"
        output file location.

        :return: string of log
        """
        string_return = f"Issue in object {item}: {message}"
        file_location = kwargs["FILE_LOCATION"]
        with open(file_location, "a", encoding="utf-8") as f:
            f.write(string_return)
        return string_return


class PandasSQLLoggerBlueprint(AbstractDelayed):
    """
    Blueprint for a log as the form of a SQL Table using pandas
    """

    def __init__(self):
        self.internal_list_tuple = []

    def log_item(self, item, message, **kwargs):
        raise NotImplementedError

    def yield_results(self, dict_elements_arguments, **kwargs) -> None:
        """
        Pandas export to SQL.
        By default, the behaviour when the path/table already exists
        is to append, but this can be modified internally.

        :param dict_elements_arguments: Contains in key "PANDAS_COLUMNS"
        the columns to use for pd.DataFrame.from_records, in key
        "SQL_FILE" the SQL file and in "SQL_TABLE" the table name.
        """
        df = pd.DataFrame.from_records(
            self.internal_list_tuple,
            columns=dict_elements_arguments["PANDAS_COLUMNS"],
        )
        sql_connector = sqlite3.connect(dict_elements_arguments["SQL_FILE"])
        sql_table = dict_elements_arguments["SQL_TABLE"]
        if_exists: typing.Literal["append", "replace", "fail"] = (
            "append"  # Behaviour when the table already exists
        )
        df.to_sql(sql_table, sql_connector, if_exists=if_exists)
