#!/usr/bin/python

import argparse

def find_max_profit(prices):
  if(len(prices)<2):
    return 0

  largest = None
  for i in range(len(prices)-2):
    price = prices[i]
    difference = max(*prices[i+1:]) - price
    if(largest == None or difference > largest):
      largest = difference

  return largest

print(find_max_profit([1050, 270, 1540, 3800, 2])) # 3530


# if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#  args = parser.parse_args()

#  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
