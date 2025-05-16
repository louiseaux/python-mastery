# reader.py
#
# Exercise 5.1

import csv
from typing import Dict, List, TextIO

def csv_as_dicts(lines: TextIO, types: List[type], *, headers: List[str] | None = None) -> List[Dict]:
    '''
    Convert lines of CSV data into a list of dictionaries
    '''
    records: List = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = { name: func(val)
                   for name, func, val in zip(headers, types, row) }
        records.append(record)
    return records

def csv_as_instances(lines: TextIO, cls: type, *, headers: List[str] | None = None) -> List[type]:
    '''
    Convert lines of CSV data into a list of instances
    '''
    records: List = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records

def read_csv_as_dicts(filename: str, types: List[type], *, headers: List[str] | None = None) -> List[Dict]:
    '''
    Read CSV data into a list of dictionaries with optional type conversion
    '''
    with open(filename) as file:
        return csv_as_dicts(file, types, headers=headers)

def read_csv_as_instances(filename: str, cls: type, *, headers: List[str] | None = None) -> List[type]:
    '''
    Read CSV data into a list of instances
    '''
    with open(filename) as file:
        return csv_as_instances(file, cls, headers=headers)