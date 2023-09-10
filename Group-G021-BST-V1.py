#!/usr/bin/env python
# coding: utf-8

# In[1]:


def inputValidations(input_data = []):
    
    for x in input_data:
        if x.startswith("Dictionary."):
            continue
        elif x.startswith("addValue(Dictionary,"):
            continue
        elif x.startswith("print(Dictionary."):
            continue
        elif x.startswith("print(Dictionary["):
            continue
        else:
            writeException("Invalid Input. Pls check the line ..." + x)
    
    return "true"

def writeException (error_message):

    # Open the Output file and write the exceptions.
    try:
        out_file = open("outputPS09.txt", "w")
        out_file.write(error_message)
        out_file.close()
    except:
        print("Exception - " + error_message)
    finally:
        print("Exception Occured - " + error_message)
        raise Exception('Exception !')


# In[2]:


in_file_data = []
results=[]

try:
    in_file = open("inputPS09.txt", "r")
    for line in in_file:
        in_file_data.append(line)
                    
    if not in_file_data: 
        writeException("Input File is empty - Pls check the data")
    if in_file_data[0] == ' ':
        writeException("First line in the input file should have data")    
    in_file.close()
except FileNotFoundError:
        writeException("Input file inputPS09.txt not found in python working path")
except IOError:
        writeException("I/O Error. Pls check the input file inputPS09.txt and its content")
except:
        writeException("File open / read error system will stop processing")
finally:
    print("File Read Completed")

checkInput = inputValidations(in_file_data)

if checkInput != "true":
    writeException("Input Data Exception::::" + checkInput)
        


# In[3]:


class G021Dictionary:
    key = int()
    keylist = []
    valuelist = []
    value = None
    leftChild = None
    rightChild = None
    
    def __init__(self):
        pass

    def __getitem__(self, key):
        return self.getValue(key)

    def getValue(self, key):
        if self.key is not None:
            if key == self.key:
                return self.value
            if key < self.key and self.leftChild is not None:
                value = self.leftChild.getValue(key)
                if value is not None:
                    return value
            if key > self.key and self.rightChild is not None:
                value = self.rightChild.getValue(key)
                if value is not None:
                    return value
            else:
                return ""

    def setValue(self, key, value):
        self.key = key
        self.value = value
        self.leftChild = None
        self.rightChild = None

    def keys(self):
        key = self.key
        if key > 0:
            self.keylist.append(key)
        if self.leftChild is not None:
            self.leftChild.keys()
        if self.rightChild is not None:
            self.rightChild.keys()
        return self.keylist

    def values(self):
        value = self.value
        if self.key > 0:
            self.valuelist.append(value)
        if self.leftChild is not None:
            self.leftChild.values()
        if self.rightChild is not None:
            self.rightChild.values()

        return self.valuelist


# In[4]:


def validatekey(newkey):
    if isinstance(newkey, int) and newkey <= 0:
        print("Key should be greater then 0")
        exit()
    if not isinstance(newkey, int):
        print("Key should be integer")
        exit()


def addValue(root, newkey, newvalue):
    # if binary search tree is empty, create a new node and declare it as root

    validatekey(newkey)

    if root is None:
        root = G021Dictionary()
        root.setValue(newkey, newvalue)
        return root
    # if newValue is less than value of data in root, add it to left subtree and proceed recursively

    if newkey < root.key:
        root.leftChild = addValue(root.leftChild, newkey, newvalue)
    elif newkey == root.key:
        root.value = newvalue
    else:
        # if newValue is greater than value of data in root, add it to right subtree and proceed recursively
        root.rightChild = addValue(root.rightChild, newkey, newvalue)
    return root


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# In[5]:


Dictionary = G021Dictionary()


# In[7]:


from io import StringIO
import sys
import time
start_time = time.time()

i = 0;

try:
    out_file = open("outputPS09.txt", "w")
    
    for x in in_file_data:
        i = i + 1
        tmp = sys.stdout
        my_result = StringIO()
        sys.stdout = my_result
        if x.startswith("Dictionary."):
            x = "print("+x+")"
        exec(x)
        sys.stdout = tmp
        #print('VARIABLE:', my_result.getvalue())
        out_file.write(my_result.getvalue())
        print("Event " + str(i) + ": " + x)   
        
    #out_file.write("".join(results))
    # check for which worked
    
    print("Total time taken is -------- %s --------- seconds" % (time.time() - start_time))

    out_file.close()
except FileNotFoundError:
        print("Output file outputPS09.txt not found in python working path")
        raise Exception('Exception !')
except IOError:
        print("I/O Error. Pls check the input file outputPS09.txt and its content")
        raise Exception('Exception !')
except:
        print("Output file write error - Sytem will stop")
        raise Exception('Exception !')
finally:
    print("File write Completed")


# In[ ]:





# In[ ]:




