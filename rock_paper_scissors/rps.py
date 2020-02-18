#!/usr/bin/python

import sys

def rock_paper_scissors(n: int) -> list:
   choices = ["rock", "paper", "scissors"]
   combinations = []

   def helper(b: int, result: list):
     if b == 0:
        combinations.append(result)
        return
    for i in choices:
        helper(b - 1, result + [i])
        helper(n, [])
   return combinations

print(rock_paper_scissors(1))
print(rock_paper_scissors(2))

# if __name__ == "__main__":
#  if len(sys.argv) > 1:
#    num_plays = int(sys.argv[1])
#    print(rock_paper_scissors(num_plays))
#  else:
#    print('Usage: rps.py [num_plays]')