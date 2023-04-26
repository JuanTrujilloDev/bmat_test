import uuid
from typing import Any, Dict, List, TextIO

import pandas as pd

default_cols = ["Song", "Date", "Number of Plays"]


class FileOpener:
    def open(self, file_dir: str) -> TextIO:
        """Opens a file from file directory
        and return a file handle.

        Time complexity: O(1)
        """
        file_handle = open(file_dir, "r+")
        return file_handle


class FileCloser:
    def close(self, file_handle: TextIO) -> None:
        """Closes a file handle.

        Time complexity: O(1)
        """
        file_handle.close()


class CsvHandler:
    def get_csv(
        self,
        file_handle: TextIO,
        delimiter: str = ",",
        required_columns: List[str] = default_cols,
    ) -> pd.DataFrame:
        """Extracts data from a csv file
        and returns a pandas dataframe.

        Time complexity: O(n)
        """
        required_columns = required_columns
        csv_data = pd.read_csv(
            file_handle, delimiter=delimiter, usecols=required_columns
        )
        return csv_data


class TotalNumberPlaysPerSong:
    def total_number_per_song(self, csv_data: pd.DataFrame) -> pd.DataFrame:
        """Groups songs by date and sums ceach play per day
        then returns a dataframe with the result.

        Time complexity: O(N+K)
        N would be the number of rows in the dataframe that get grouped by columns.
        K would be the number of resulting groups that get summed.
        """
        data = csv_data.groupby(["Song", "Date"]).sum()
        return data


class GroupSongsPlaysPerDay:
    def generate_csv(
        self,
        file_dir: str,
        delimiter: str = ",",
        required_columns: List[str] = default_cols,
    ) -> Any:
        """Generates a csv file with the total number of plays per song.
        The file is saved in the same directory as the original file.

        The resulting function has the following time complexity:
        O(N+K) + O(N) + O(1) + O(1) + O(1) = O(2N+K) ≈ O(N+K)
        """
        file_handle = FileOpener().open(file_dir)
        csv_data = CsvHandler().get_csv(file_handle, delimiter, required_columns)
        total_number_per_song = TotalNumberPlaysPerSong().total_number_per_song(
            csv_data
        )
        FileCloser().close(file_handle)
        return total_number_per_song.to_csv()
