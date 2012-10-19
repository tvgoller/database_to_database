# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 15:37:05 2012

@author: whgoller
"""
import pyodbc # easy_install pyodbc

def connect(cnxn_string):
    print cnxn_string
    cnxn_string = cnxn_string.rstrip('\r\n')
    cnxn = pyodbc.connect(cnxn_string)
    cursor = cnxn.cursor()
    return cursor

def load_data(cxn,query):
    print query
    cxn.execute(query)
    rows = cxn.fetchall()
    print rows
    return rows

def save_data(cxn,rows,query):
    cxn.executemany(query,rows)
    cxn.commit()

def load_configuration(file_name):
    with open(file_name, 'rb') as file_input:
        list_of_all_lines = file_input.readlines()
        return list_of_all_lines
        
if __name__ == '__main__':
    config = load_configuration('example.txt')
    source_db = connect(config[0])
    rows = load_data(source_db,config[1])
    destination_db = connect(config[2])
    save_data(destination_db,rows,config[3])

