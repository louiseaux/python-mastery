# csv.py
#
# Exercise 9.3

from ..formatter import TableFormatter

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))
    
    def row(self, rowdata):
        print(','.join(str(d) for d in rowdata))