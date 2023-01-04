from queue import Queue
from dataclasses import dataclass
from datetime import date
from operator import index
from turtle import clear
import pandas as pd
from regex import P
from sympy import print_glsl

#Tkinter for choosing the file csv file to execute the code.
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

#below for clearing the terminal
import os

# Clearing the terminal before running the code.
clear = lambda:os.system('cls')
clear()

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

data_list = pd.read_csv(filename) # reads the excel file into pandas 

df = pd.DataFrame(data_list, columns= ['Date','Inbound','Outbound']) # converting Excel data into pandas data frame choosing the columns

df.fillna(0, inplace=True) # replacing Nan value with 0 

df.loc[(df['Outbound'] < 1000), 'Outbound'] = 0 # replacing any Outbound value less than 1000 to 0 

for i,index in df.iterrows():
        if df['Outbound'][i] == 0 :   #or df['Outbound'][i] <= 1000:
            
            print('-', df['Date'][i],sep = ' ')
            if df['Outbound'][i] != df['Outbound'][i + 1]:
                
                print('- Restored', df['Date'][i + 1], sep = ' ')
            else:
                pass
        else:
            pass

