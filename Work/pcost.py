# pcost.py
#
# Exercise 1.27
import gzip

def portfolio_cost(path):
    Total_cost = 0.0

    #1 read file 
    #2 perform convertion and calculate the total amount 
    with gzip.open(path,mode = 'rt') as file :
        header = next(file)   #doesn't make sense for me  
                #returns the next line in the file 
                #used to explicitly read or skip the line
        
        for line in file:
            line = line.strip().split(',')
            Total_cost = Total_cost + (int(line[1])*float(line[2]))
    print(Total_cost)    

if __name__ == '__main__':
    portfolio_cost('practical_python/practical-python/Work/Data/portfolio.csv.gz')