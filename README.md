# enpy

**Python library for converting datasets to edges and nodes csv files for network analysis (in particular iGraph)**

Version: 1.0.0

also available at: [https://test.pypi.org/project/edges-nodes-py/1.0.0/](https://test.pypi.org/project/edges-nodes-py/1.0.0/)
----

# Description

This python library is for getting the data from a dataset and creating two csv files (or other extentions in the future) that will be used as *Edges* and *Node* (also called Links and Verticies) in Network Analysis which can be done in [iGraph](https://igraph.org/). 

# Installation

**requirements:** Python 3
Fork the project or

`git clone https://github.com/lukfd/enpy.git`

OR

`python -m pip install --index-url https://test.pypi.org/simple/ --no-deps edges-nodes-py`

# Tutorial

First import the python object from the package.

```
from enpy import Enpy
```

if you have installed from github also add to the top `import sys` and `sys.path.insert(1, './enpy')`. Also run your script in the base directory.

Initialize the Enpy object
```
# 1. Creating Enpy Object
enpyObj = Enpy.Enpy('./path/dataset.json')
```

Then call functions to create the files `edges.csv` and `nodes.csv`.

```
# first print version and test it
enpyObj.test()

# Create nodes.csv
enpyObj.getNodesJson2Csv('./path/nodes.csv', 'name_of_the_json_array', 'id')

# save names of each edges
enpyObj.getNamesJson2Csv('./path/nodes_name.csv', 'name_of_the_json_array')

# Create nodes.csv
enpyObj.getEdgesJson2Csv('./path/edges.csv', 'name_of_the_json_array')
```

to have a full understanding, read the Documentation or read the `example.py` code.

# Documentation

The package *enpy* is a collection of functions within a class! So remember to import and create the object Enpy.

the Enpy object needs to be initialize by passing the file name of your dataset (for this version 1.0.0 it can only be a json file)

**CLASS' FUNCTIONS**
- Creates the csv file for the nodes of the network. It **expects** the path of to where to write the csv file and the name of the array where the possible nodes can be in the json object. By defaul it will name the column header to *id*.
```
getNodesJson2Csv(self, output_path, from_name_array, name_of_col = 'id')
```

- Prints the read dataset as a python array. It **expects** the name of the array where the nodes are stored in the json object.
```
printDataset(self, from_name_array)
```

- Creates the csv file of all the names of the nodes in the network. It **expects** the path of to where to write the csv file and the name of the array where the possible nodes can be in the json object. By default the two header columns name that the csv file will have will be *number* and *name*.
```
getNamesJson2Csv(self, output_path, from_name_array, first_col_name = 'number', second_col_name = 'name')
```

- Prints to the terminal the name of a specific number of node or all the names of each node and their respective number. It **expects** the name of the array where the possible nodes can be in the json object. By defaul it sets the two header columns *name* and *number*. **For printing the name of a specific node's number** set `printNumber = ` the integer number (check `example.py`).
```
printNamesJson2Csv(self, from_name_array, first_col_name = 'number', second_col_name = 'name', printNumber = None)
```

- Creates the csv file of the Edges between the nodes. It **expects** the path of to where to write the csv file and the name of the array where the possible nodes can be in the json object. By defaul it sets the two header columns *From* and *To*.
```
getEdgesJson2Csv(self, output_path, from_name_array, name_of_col_one = 'From', name_of_col_two = 'To')
```

- Simply prints `enpy -- VERSION : 1.0.0` to terminal.
```
test()
```

### Types of dataset supported

**READ FROM A dataset's file extention:**
- json

In the `example.py` it is used a json with this structure:
```
[
 {
    "id": 10259,
    "cuisine": "greek",
    "ingredients": [
      "romaine lettuce",
      "black olives",
      "grape tomatoes",
      "garlic",
      "pepper",
      "purple onion",
      "seasoning",
      "garbanzo beans",
      "feta cheese crumbles"
    ]
  }
]
```
(For more insights on this json file read section *tests*)

So for this current version of the package (v 1.0.0) the dataset that you can work with need to be a *json* file object with an array of strings.

For the future we would need to make the package read also *csv*, *other formats of json files* and other *file type extentions*.

----
# About this project
Structure of the library:
```
├─ LICENSE
├─ README.md
│
├─ /enpy
│  ├─ Enpy.py
│  └─ __init__.py
│
├─ setup.py
└─/tests
   ├─ /filetest
   │  ├─ edges.csv
   │  ├─ nodes.csv
   │  ├─ nodes_name.csv
   │  └─ train.json
   │  
   ├─ example.py
   └─ test_to_implement.py
```

#### tests

I have used the tutorial example and the `example.py` code that I have used in my Network Model course. Me and my teamate have analyzed the data from the dataset of a list of recepies that contains a list of ingredients. The original dataset is available at [https://www.kaggle.com/kaggle/recipe-ingredients-dataset](https://www.kaggle.com/kaggle/recipe-ingredients-dataset). In the tutorial and in the example code we have used a smaller `train.json` dataset, which is composed as:

When I test on my local machined I had trouble importing the module. So I had to run the example.py from the base path. Then I had to have all the paths as `./tests/filetes/` as consequence.

#### Packages Dependancies

This python library depends on core python libraries *json* and *csv*.

#### To-do

- [ ] not inserting duplicate in `getEdgesJson2Csv` function
- [ ] expand readable file extentsion to csv
- [ ] make new tests
- [ ] clean up code
- [ ] better commenting

#### Other resources

- To learn more about statistical network modeling read [http://networksciencebook.com/](http://networksciencebook.com/)

- More about network visualization in *R* [https://kateto.net/network-visualization](https://kateto.net/network-visualization)

- learn more about json and csv python libraries here : [https://docs.python.org/3/library/json.html](https://docs.python.org/3/library/json.html), [https://docs.python.org/3/library/csv.html?highlight=csv#module-csv](https://docs.python.org/3/library/csv.html?highlight=csv#module-csv)

- How to publish in pypi [https://realpython.com/pypi-publish-python-package/](https://realpython.com/pypi-publish-python-package/)

#### Old issues

- Importing the module locally when I first tested (to have the directory named enpy and the module as consequence named Enpy.py). To read the issue read [https://stackoverflow.com/questions/65272979/importing-class-of-module-from-different-path-in-python-nameerror-name-enpy/65273026#65273026](https://stackoverflow.com/questions/65272979/importing-class-of-module-from-different-path-in-python-nameerror-name-enpy/65273026#65273026)