import csv
from typing import Any, List, TextIO


class FileOpener:
    def open(self, file_dir: str) -> TextIO:
        file_handle = open(file_dir, "r")
        return file_handle


class FileCloser:
    def close(self, file_handle: TextIO) -> None:
        file_handle.close()


class CsvHandler:
    def get_csv(self, file_handle: TextIO, delimiter: str) -> List[Any]:
        csv_data = csv.reader(file_handle, delimiter=delimiter)
        return list(csv_data)


class CsvReader:
    def read_csv(self, csv_data: List[Any]) -> None:
        for row in csv_data:
            print(row)


class CsvColumnReader:
    def read_csv_column(self, csv_data: List[Any], column: int) -> None:
        for row in csv_data:
            print(row[column])


file = FileOpener().open("songs.txt")
csv_data = CsvHandler().get_csv(file, ",")
CsvReader().read_csv(csv_data)
CsvColumnReader().read_csv_column(csv_data, 1)
FileCloser().close(file)
