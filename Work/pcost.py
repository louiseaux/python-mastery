# pcost.py
#
# Exercise 1.3

def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename, 'r') as f:
        for line in f:
            fields = line.split()
            try:
                nshares = int(fields[1])
                price = float(fields[2])
                total_cost += nshares * price

            # This catches errors in int() and float() conversions above
            except ValueError as e:
                print(f"Couldn't parse: {repr(line)}")
                print(f"Reason: {e}")

    return total_cost

if __name__ == '__main__':
    print(portfolio_cost('../Data/portfolio.dat'))