import numpy as np
#This is the file for reading the data from the file

#Given the file name, this function will read the data from the file
#  and return it as a numpy array
def read_mat_file(file,type=float):
    return np.loadtxt(file,dtype=type)
#This function will read the data from the file from the given data type
# and return it as a numpy array
def read_mat(type='original'):
        file="inDrop1_data/inDrop1"

        dict = {
        'original':".txt",
        'cp10k':"_cp10k.txt",
        'HEG':"_HEG.txt",
        'logcp10k':"_logcp10k.txt",
        'sqrtcp10k':"_sqrtcp10k.txt"
        }
        file+=dict[type]
        return read_mat_file(file,float)