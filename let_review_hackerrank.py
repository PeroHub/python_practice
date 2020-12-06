""" Task
Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each name queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for name is not found, print Not found instead.

Note: Your phone book should be a Dictionary/Map/HashMap data structure."""

import sys

n = int(sys.stdin.readline().strip())
phoneBook = dict()

for i in range(0, n):
    entry = sys.stdin.readline().strip().split(' ')
    phoneBook[entry[0]] = entry[1]

query = sys.stdin.readline().strip()
while query:
    phoneNumber = phoneBook.get(query)
    if phoneNumber:
        print(query + '=' + phoneNumber)
    else:
        print('Not found')
    query = sys.stdin.readline().strip()