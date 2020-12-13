# ''' Local Test VERSION 1.0.0 '''
# import sys
# sys.path.insert(1, '../enpy')

from enpy import Enpy

# TESTING 

# 1. Creating Enpy Object
enpyObj = Enpy.Enpy('./tests/filetest/train.json')

# 2. Use it
# first print version and test it
enpyObj.test()

# Create nodes.csv
enpyObj.getNodesJson2Csv('./tests/filetest/nodes.csv', 'ingredients', 'id')

# save names of each edges
enpyObj.getNamesJson2Csv('./tests/filetest/nodes_name.csv', 'ingredients')

# print names of each edges
enpyObj.printNamesJson2Csv('ingredients',printNumber=10)

# Create nodes.csv
#enpyObj.getEdgesJson2Csv('./tests/filetest/edges.csv', 'ingredients')