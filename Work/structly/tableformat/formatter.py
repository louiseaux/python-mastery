# formatter.py
#
# Exercise 9.3

__all__ = [ 'create_formatter', 'print_table' ]

from abc import ABC, abstractmethod

def print_table(records, fields, formatter):
    if not isinstance(formatter, TableFormatter):
        raise TypeError('Expected a TableFormatter')
    
    # Print the table headers in a 10-character wide field
    formatter.headings(fields)

    # Output the table contents
    for r in records:
        rowdata = [ getattr(r, fieldname) for fieldname in fields ]
        formatter.row(rowdata)

class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        pass
    
    @abstractmethod
    def row(self, rowdata):
        pass

from .formats.text import TextTableFormatter
from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter

class ColumnFormatMixin:
    formats = []
    def row(self, rowdata):
        rowdata = [ (fmt % d) for fmt, d in zip(self.formats, rowdata) ]
        super().row(rowdata)
    
class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([ h.upper() for h in headers ])

def create_formatter(name, column_formats=None, upper_headers=None):
    if name == 'text':
        formatter_cls = TextTableFormatter
    elif name == 'csv':
        formatter_cls = CSVTableFormatter
    elif name == 'html':
        formatter_cls = HTMLTableFormatter
    else:
        raise RuntimeError('Unknown format %s' % name)
    
    if column_formats:
        class formatter_cls(ColumnFormatMixin, formatter_cls):
            formats = column_formats
    
    if upper_headers:
        class formatter_cls(UpperHeadersMixin, formatter_cls):
            pass

    return formatter_cls()