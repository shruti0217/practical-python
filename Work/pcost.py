# pcost.py
#
# Exercise 1.27
#import gzip

import csv 

def portfolio_cost(path):
    Total_cost = 0.0
    with open(path,mode = 'r') as file:
        rows = csv.reader(file)     #will return a well formatted comma seperated list for each line 
        header = next(rows)

        for line in rows:
            for i in range(1,3):
                if line[i] == '':
                    line[i] == 0
            Total_cost = Total_cost + (int(line[1]) * float(line[2]))
    return Total_cost


#-------------exercise 2.15-----------------------#
#-Total cost using enumerator from Data/missing.csv
def port_cost(path):
    total = 0
    with open(path,mode = 'r') as f:
        f2 = csv.reader(f)
        print(f2)
        print(next(f2))
        #for i,line in enumerate(f2,start = 1) :
        for i,row in enumerate(f2):
                           
            print(row, i)
            
            ''' for i in row :
                 print(i)
            '''
            try :
                total+=float(row[2])*int(row[1])
                
            except ValueError:
                print(f"row{i}: Bad row :{row}")
        print(type(row))
        print(total)
#---------------------------------------------------#
             
                
        '''
            print(f"{i},{line}")
            print(f"{i},{line[3]}")
        '''   
        '''for j,word in enumerate(i):
                print(f"{j},{word}")
        '''   

#-------------------exercise 2.16-----------------------------#

def total_with_zip(path):
    with open(path, mode = 'r') as file:
        rows = csv.reader(file)
        header = next(rows)
        lis = []
        for row in rows:
            lis.append(dict(zip(header, row)))
        
        total = 0
        
        for i,r in enumerate(lis):
            #print(r)
            #print(r['shares'])
            try :
                total += int(r['shares']) * float(r['price'])
            except:
                continue 

        print(total)

#-------------------------------------------------------------#
'''
def portfolio_cost(path):
    Total_cost = 0.0
    

    #1 read file 
    #2 perform convertion and calculate the total amount 
    with open(path,mode = 'rt') as file  :
        header = next(file)   #doesn't make sense for me  
            #returns the next line in the file 
            #used to explicitly read or skip the line
        
        for line in file:
            line = line.strip().split(',')
            for j in range(1,3):
                if line[j] == '':
                    line[j] = 0.0
            print(line)
            Total_cost = Total_cost + (int(line[1])*float(line[2]))
   

    
    return Total_cost    
'''

import sys

if __name__ == '__main__':
    filename = ''
    '''
    if len(sys.argv) == 2:      #don't know what's up tf
        filename = sys.argv[1]
    if sys.argv == '':
        cost = portfolio_cost('Data/portfolio.csv')
    else :
        filename = int(input("Enter file name"))
        if filename == '\n':
            filename = 'Data/portfolio.csv'
    cost = portfolio_cost(filename)
    print(cost)
    '''
    '''if len(sys.argv) == 2:      # this all for when we run the program in terminal
        filename = sys.argv[1]
    else :
    '''


    #-------------exersise --------------------------#
    filename = 'Data/portfolio.csv'
    file2name = 'Data/missing.csv' 
    cost = portfolio_cost(filename)
    print(cost)
    #port_cost(file2name)
    print('exercise 2.16')
    total_with_zip(filename)
    print("part 2")
    total_with_zip(r'Data/portfoliodate.csv')
