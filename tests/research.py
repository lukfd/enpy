import json
import csv
import pandas as pd

# read json
with open('./filetest/train.json') as f:
  train = json.load(f)

###### nodes.csv

ingredients = []
# for each object get index ingredients
# then add it to the ingredients array
# filter the one that appear in more than one
for i in range (0,len(train)):
    for j in train[i]['ingredients']:
        ingredients.append(j)
# eliminates duplicates
ingredients = list(dict.fromkeys(ingredients))
# write the file
with open('./nodes.csv', 'w', newline='') as csvfile:
    fieldnames = ['id']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range (1,len(ingredients)+1):
        writer.writerow({'id': str(i)})

####### edges.csv

# find out how the ingredients are connected
# between recepies

# write the file
with open('./edges.csv', 'w', newline='') as csvfile2:
    fieldnames = ['From','To']
    writer = csv.DictWriter(csvfile2, fieldnames=fieldnames)
    writer.writeheader()

    for x in range (1,len(ingredients)+1):
        #print(x)
        # for each recepie
        for i in range (0,len(train)):
            if ingredients[x-1] in train[i]['ingredients']:
                for to in train[i]['ingredients']:
                    # then x is connected to all those ingredients
                    index = ingredients.index(to) + 1
                    # From = x and To = index
                    if x != index:
                        writer.writerow({'From': str(x),'To': str(index)})


############# FOR NAMES
# with open('./names.csv', 'w', newline='') as csvfile3:
#     fieldnames = ['number', 'name']
#     writer = csv.DictWriter(csvfile3, fieldnames=fieldnames)

#     writer.writeheader()
#     for i in range (1, len(ingredients)+1):
#         writer.writerow({'number': str(i), 'name': str(ingredients[i-1])})


##### FOR DUPLICATES
# with open('1.csv','r') as in_file, open('2.csv','w') as out_file:
#     seen = set() # set for fast O(1) amortized lookup
#     for line in in_file:
#         if line in seen: continue # skip duplicate

#         seen.add(line)
#         out_file.write(line)