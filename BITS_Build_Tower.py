#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# BITS Pilani is going to celebrate its 60th anniversary in a couple of years. 

# To mark the magical days at BITS Pilani, students are planning to construct a Tower. 

# This program is to engineer the tower construction in N days with following these pre-requisites: 
    # Every day you are provided with one disk of distinct size. 
    # The disk with larger sizes should be placed at the bottom of the tower. 
    # The disk with smaller sizes should be placed at the top of the tower. 

# The order in which tower must be constructed is as follows: 
    # You cannot put a new disk on the top of the tower until all the larger disks that are given to you get placed.


# In[ ]:


# Input processing

# Input file name inputPS07.txt

# Input accepted from the same path as this program exeuction

# Input file must have the following data
    # Total number of Days (N) to contruct the tower in line-1
    # Incoming Disk sizes (DS) are in line-2
    # 1 <= DS <= N
    # No duplicate DS in line-2
    


# In[ ]:


# Define all the common functions to be used in the program to build the tower

# Validate input for boundary conditions

def inputValidations(N,disk_array):
    
    #Validate if N is positive number and not Zero
    if N <= 0:
        return("Pls check N value. It must be greater than 0")
    
    #Validate if input number of days are not more than 10^10
    if N > 10 ** 10:
        return("Pls input N value less than or equal to 10^10 :: ")
        
    #Validate length of the data matches with the number of days
    if len(disk_array) != N: 
        return("Pls check the values for N and Disk array. It does not match :: ")
    
    # create a set from the list
    distinct_values = set(disk_array)
        
    # Check if any duplicates
    if len(disk_array) != len(distinct_values):
        return("Pls check - Duplicates found in the input list")
    
    # Validate if Maximum disk size is same as N
    if max(disk_array) != N:
        return("Max disk size must be same as N")
    
    return "true"

# Main logic to build the tower 

def buildTower (input_disks):
    print(input_disks)

    # Set the max disk size to the total number of days required to construct 
    max_disk = int(days_to_construct_tower)
    
    
    # Accumulation queue is the temporary queue to store the disks not in order
    accumulation_queue = [] 
    
    # Queue used to store day wise build plan
    build_queue = []

    # Function to store the accumulated disks which are pending to be deployed
    def enqueue_accumulation(disk):
        accumulation_queue.append(disk)

    # Function to store the daily build plan
    def enqueue_build(disk):
        build_queue.append(str(disk) + " ")

    # Formatting Function to store the calendar day
    def build_for_the_day(day):
        build_queue.append(str(day+1)+" > ")

    # Formatting Function to move the plan to next day
    def enqueue_nextday():
        build_queue.append("\n")

    
    # Process each disk in the queue one at a time till all the disks are processed
    for i in range(int(max_disk)):
        # If disk for the day is eligible to build for the day or eligible disks available in accumulation queue 
        if ((input_disks[i] == max_disk) 
        or  (max_disk in accumulation_queue) ):
            build_for_the_day(i)
            enqueue_build(max_disk)
            max_disk = max_disk - 1
            
            # Sort accumulation queue if disk available for build exist in accunulation queue for performance improvement
            if (max_disk in accumulation_queue):
                accumulation_queue = sorted(accumulation_queue)
            
            # If disk available to build exist in accumulation queue, then dequeue it to build queue
            for j in accumulation_queue[::-1]:
                if(j == max_disk):
                    enqueue_build(max_disk)
                    max_disk = max_disk - 1
                    del accumulation_queue[accumulation_queue.index(j)]
            
            enqueue_nextday()
        else:
            enqueue_accumulation(input_disks[i])
            build_for_the_day(i)
            enqueue_nextday()

    return build_queue    

# Common Function to write exceptions into output file 
def writeException (error_message):

    # Open the Output file and write the exceptions.
    try:
        out_file = open("outputPS07.txt", "w")
        out_file.write(error_message)
        out_file.close()
    except:
        print("Exception - " + error_message)
    finally:
        print("Exception Occured - " + error_message)
        raise Exception('Exception !')


# In[ ]:


# Open the input file, read, validate and assign to the processing variables.

try:
    in_file = open("inputPS07.txt", "r")
    in_file_data = []
    for line in in_file:
        in_file_data.append(line)
    if not in_file_data: 
        writeException("Input File is empty - Pls check the data")
    if in_file_data[0] == ' ':
        writeException("First line in the input file should have data")    
    in_file.close()
except FileNotFoundError:
        writeException("Input file inputPS07.txt not found in python working path")
except IOError:
        writeException("I/O Error. Pls check the input file inputPS07.txt and its content")
except:
        writeException("File open / read error system will stop processing")
finally:
    print("File Read Completed")

days_to_construct_tower = int(in_file_data[0])
disk_array = list(map(int, in_file_data[1].split()))

checkInput = inputValidations(days_to_construct_tower,disk_array)

if checkInput != "true":
    writeException("Input Data Exception::::" + checkInput)
        


# In[ ]:


# Call the main logic with the input disk array
towerDailyPlan = buildTower(disk_array)


# In[ ]:


# Open the Output file and write the results.

try:
    out_file = open("outputPS07.txt", "w")
    out_file.write("".join(towerDailyPlan))
    out_file.close()
except FileNotFoundError:
        print("Output file outputPS07.txt not found in python working path")
        raise Exception('Exception !')
except IOError:
        print("I/O Error. Pls check the input file outputPS07.txt and its content")
        raise Exception('Exception !')
except:
        print("Output file write error - Sytem will stop")
        raise Exception('Exception !')
finally:
    print("File write Completed")
    


# In[ ]:




