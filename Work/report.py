#!/usr/bin/python3

# report.py
#
# Exercise 2.4

import csv
from pprint import pprint

def read_portfolio(path):
    #funtion will read the given portfolio file
    # and will return the the formatted content
    #so read and return the formatted content
    lis = []
    with open(path, mode = "r") as file:
        row = csv.reader(file) #csv.reader will return an object which will contain the collection of list of line which will be comma seperated list
        print(row)
        head = next(row) #next will actually kinda shifts the file pointer to the next line along with returning the content of the line that it was previously on 
        print(head)
        for i in row :
            #transformi(i)
            i[1] = int(i[1]) if i[1] !="" else 0
            i[2] = float(i[2]) if i[2] !="" else 0.0
            lis.append(dict(zip(head,i)))   #it worked....but how...shit
        print(lis)
        return (lis,head)

def Total_cost(info_list,head):
    total_cost = 0.0
    #for i in info_list:
    for i in info_list:
        #total_cost += i[head[1]]*i[head[2]]
        total_cost += i['shares'] * i['price'] 

    return total_cost

'''
def format(file_con,head):
    list = {}'''
'''
def transformi(i): # so funtions in py are always call by reference huh
    
    i[1] = int(i[1])
    i[2] = float(i[2])

'''
'''
def create_dic(line,head):
    dic = {}
    #print(head)
    for i,j in zip(line,head):
        dic[j] = i
    return dic
'''    


'''
def return_header(file_con):
    head = next(file_con)
    return head
throws value error 
'''    
#this function reads from the file prices.csv and returns a dictionary of stock - value pair
def read_prices(path):
    with open(path,mode = 'r') as file:
        rows = csv.reader(file)
        dic = {}
        
        for i in rows:
            #if i != []:
            try :
                #dic[i[0]] = float(dic[i[1]]) #how can you be this stupid bruh
                dic[i[0]] = float(i[1]) if i[1] != "" else 0.0
            #else :
            except:
                continue
    
        pprint(dic)
        return dic 
#this function will calculate the present value of the portfolio where the initial will take in the 
#the initial data of the portfolio and the new prices will take in the new values of stocks
def present_value_of_port(initial,new_prices):
    #lets first create a dic which will have the data of name and no_of shares in the portfolio with name share pair
    dic = {}
    for i in initial:
        #print(i['name'],i['shares'])
        dic[i['name']] = i['shares']
    print(dic)
    p_total = 0.0
    for i in dic.keys(): # returns stock names
        #print(i)
        p_total += dic[i] * new_prices[i]
    print(p_total)
    return p_total
    '''
    set_1  = dic.keys()
    print(set_1)
    set_2 = new_prices.keys()
    print(set_2)
    set_3 = set_1 & set_2    # kinda useless coz it just returns set_1 right? damn
    print(set_3)
    for i in set_3:
        print(dic[i],new_prices[i])
        p_total += dic[i] * new_prices[i]    
    '''




def make_report(dic_port,list_stocks):
    result = []
    change = 0
    print("Name\t\tshare\t\tprice\t\tchange")
    print("-------\t\t-------\t\t-------\t\t---------")
    for i in dic_port:
        change =  list_stocks[i['name']] - i['price'] 
        result.append((i['name'],i['shares'],i['price'],change))
    return result



if __name__ == "__main__":
    # I.Part one:
    #1 read the file
    file_con,head = read_portfolio(r"Data/portfolio.csv") 
    #head = return_header(file_con) this return an value error that says i/o operation on file so that means next works only when the file is open ?
    #2 format the data from the file in given format
    #done
    #3 calulate the total or perform the desired op
    port_value = Total_cost(file_con,head) # no need to pass head
    print(port_value)

    name,share,price = file_con[1].items()
    
    #print(name)
    #pprint(file_con)
    #print(file_con[1]['name'])
    #print(head)
    # II.part two:

    #1.read from the Data/prices.csv file and store the data in a dictionary with a name : value pair format
    present_price = read_prices(r"Data/prices.csv")
    

    #2.calculate the current value of portfolio and determine the gain/loss
    p_total = present_value_of_port(file_con,present_price)
    #check if gain or loss : 
    print(p_total - port_value) 
    
    
    if p_total > port_value :
        print(f"Gain  ")
    else :
        print("Loss")
    
    #3. Make a report that takes list of stocks and dictionary of prices as input 
    #and returns a list of tuples containing rows as (Name shares price change)
    report = make_report(file_con,present_price)
    for i in report:
        print('%10s\t%10d\t%10.2f\t%10.2f'% i)