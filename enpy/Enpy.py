# Version 1.0.0 - Author: Luca Comba
# ENPY OBJ and FUNCTIONS

# Dependancies
import json
import csv

class Enpy:

    # Global Variables
    dataset = None

    # initialize class
    def __init__(self, file):
        self.readDataset(file)

    # Helper function
    def getArray(self, from_name_array):
        '''
        return array from the file
        '''
        array = []
        # for each object get index array
        # then add it to the array array
        # filter the one that appear in more than one
        for i in range (0,len(self.dataset)):
            for j in self.dataset[i][from_name_array]:
                array.append(j)
        return array

    # Functions
    def readDataset(self, file):
        '''
        READ DATA FILES AND STORE IT IN dataset
        now can be json
        '''
        with open(file) as f:
            self.dataset = json.load(f)

    def getNodesJson2Csv(self, output_path, from_name_array, name_of_col = 'id'):
        '''
        create csv file of nodes, structured like:
        
        *----*
        | id |
        ------
        | 1  |
        ------
        | 2  |     ...ect...
        ------    

        '''
        array = self.getArray(from_name_array)
        # eliminates duplicates
        array = list(dict.fromkeys(array))
        # write the file
        with open(output_path, 'w', newline='') as csvfile:
            fieldnames = [name_of_col]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for i in range (1,len(array)+1):
                writer.writerow({name_of_col: str(i)})

    def printDataset(self, from_name_array):
        '''
        printing the dataset read
        '''
        array = self.getArray(from_name_array)
        print(array)

    def getNamesJson2Csv(self, output_path, from_name_array, first_col_name = 'number', second_col_name = 'name'):
        '''
        create csv file of Names, structured like:
        
        *--------*------*
        | number | name |
        -----------------
        | 1      | ing1 |
        -----------------
        | 2      | ing2 |   ...ect...
        -----------------  

        '''
        array = self.getArray(from_name_array)

        with open(output_path, 'w', newline='') as csvfile:
            fieldnames = [first_col_name, second_col_name]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for i in range (1, len(array)+1):
                writer.writerow({first_col_name: str(i), second_col_name: str(array[i-1])})

    def printNamesJson2Csv(self, from_name_array, first_col_name = 'number', second_col_name = 'name', printNumber = None):
        '''
        print name of edges, structured like:
        
        number, name
        1, name1
        2, name2 

        '''
        array = self.getArray(from_name_array)

        # Printing header
        print(first_col_name + ', ' + second_col_name)
        
        if printNumber is None:
            for i in range (1, len(array)+1):
                print(str(i) + ', ' + str(array[i-1]))        
        else:
            print(str(printNumber) + ', ' + str(array[int(printNumber)-1])) 

    # EDGES Unweighted 
    def getEdgesJson2Csv(self, output_path, from_name_array, name_of_col_one = 'From', name_of_col_two = 'To'):
        '''
        find out how the NODES are connected
        between themselves (as array in recepies)

        create csv file of edges, structured like:
        
        *------*----*
        | From | To |
        -------------
        | 1    | 2  |
        -------------
        | 2    | 3  |   ...ect...
        -------------  

        '''
        array = self.getArray(from_name_array)
        # write the file
        with open(output_path, 'w', newline='') as csvfile2:
            fieldnames = [name_of_col_one,name_of_col_two]
            writer = csv.DictWriter(csvfile2, fieldnames=fieldnames)
            writer.writeheader()

            for x in range (1,len(array)+1):
                # for each recepie
                for i in range (0,len(self.dataset)):
                    if array[x-1] in self.dataset[i][from_name_array]:
                        for to in self.dataset[i][from_name_array]:
                            # then x is connected to all those array
                            index = array.index(to) + 1
                            # From = x and To = index
                            if x != index:
                                writer.writerow({name_of_col_one: str(x), name_of_col_two: str(index)})

    ### Other 2nd Functions

    def deleteDuplicatesCsv(self, infile_path, outfile_path):
        '''
        delete 
        '''
        ##### FOR DUPLICATES
        with open(infile_path,'r') as in_file, open(outfile_path,'w') as out_file:
            seen = set() # set for fast O(1) amortized lookup
            for line in in_file:
                if line in seen: continue # skip duplicate

                seen.add(line)
                out_file.write(line)

    # testing
    def test(self):
        print("enpy -- VERSION : 1.0.0")