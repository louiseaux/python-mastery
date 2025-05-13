# tableformat.py
#
# Exercise 3.2

def print_table(records, fields):
    # Print the table headers in a 10-character wide field
    print(' '.join('%10s' % fieldname for fieldname in fields))

    # Print the separator bars
    print(('-'*10 + ' ')*len(fields))

    # Output the table contents
    for record in records:
        print(' '.join('%10s' % getattr(record, fieldname) for fieldname in fields))