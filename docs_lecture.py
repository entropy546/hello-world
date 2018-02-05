#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 15:39:58 2018

@author: Francisco Romero
"""
import os
""""
input = the directory of a folder
output = a list with all the doc's names in the folder
this script read the names of the archives in a folder
and create a list of that names ( list with one column and x files 
depending on the dataset)

"""
direct = "/home/user/PDB_DB" ""# change the folder path for different cases
directory = os.fsencode(direct)

text_file = open("all_pdbs.txt","w")         # change the name of the txt archive
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".pdb"):
        text_file.write(str(filename)+"\n")   # this one makes only a column with the names of the dataset
text_file.close()
    