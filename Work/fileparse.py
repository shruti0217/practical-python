# fileparse.py
#
# Exercise 3.3

import csv
import pprint

def parse_csv(filename,types = None, select=None, has_header = False , delimit = ','):
    '''
    Parse a csv file into a list of records.
    '''
    with open(filename, mode = 'r') as file:
        rows = csv.reader(file, delimiter = delimit)
        #header = next(rows)
        if not has_header: # if has_header is False
            record = []
           
           if types:
                for row in rows:
                    
                    record.append(tuple([types_c(row_c) for row_c,types_c in zip(row,types) ]))
            
            else:
                record = [tuple(row) for row in rows]
            print(record)
            return record

        #header = next(rows)
        if select :
            indices = [header.index(colname) for colname in select]
            header=select
        else :
            indices = []

        record = []
        for row in rows:
            if not row:
                continue
            if indices :
                row = [row[i] for i in indices]
            if types:
                row = [type_t(row_c) for type_t,row_c in zip(types,row)] # Will zip the type with row_column
            record.append(dict(zip(header,row)))
        print(record)          
        
parse_csv(r'Data/portfolio.csv')
