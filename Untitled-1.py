import csv
"""""""""""
def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows =csv.reader(f)
        headers = next(rows)

        for line in rows:
            stock = {
                'name' : line[0],
                'shares' : int(line[1]),
                'price' : float(line[2]),
                }
            portfolio.append(stock)
    return portfolio

def read_prices(filename):
    prices = {}
    with open(filename) as f:
        rows= csv.reader(f)
        for line in rows:
            try:
                prices[line[0]] = float(line[1])
            except IndexError:
                pass
    return prices
portfolio = read_portfolio('C:/Users/user/portfolio.csv')
prices = read_prices('C:/Users/user/prices.csv')

"""""""""
portfolio=list()
prices=list()
with open('C:/Users/user/portfolio.csv', 'r') as file1:
    reader1 = csv.reader(file1)
    for row in reader1:
        portfolio.append(row)

with open('C:/Users/user/prices.csv', 'r') as file2:
    reader2 = csv.reader(file2)
    for row in reader2:
        prices.append(row)
total_cost = 0.0

total_value = 0.0
for s in portfolio:
    for a in range(1,len(portfolio)-1):
        total_cost +=float(portfolio[a][1])*float(portfolio[a][2])
print(total_cost)

