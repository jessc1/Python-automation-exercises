data=[
    (1000, 10),
    (2000, 17),
    (2500, 170),
    (2500, -170),
]

# The header for reference
print('Revenue | Profit | Percent')

TEMPLATE = '{revenue: >7,} | {profit:>+6} | {percent:>7.2%}'

# Print the data rows
for revenue, profit in data:
    row = TEMPLATE.format(revenue=revenue, profit=profit, percent=profit/revenue)
    print(row)