'''
Basic string operations does not support any kind of 
advance string matching . 

pythons re module is used for reg_Exp


'''

import re

text = 'Today is 01/03/2018 , there are 31 days in this month'

#-------------------------re.findall(r'exp',text)-----------------------------

date = re.findall(r'\d+/\d+/\d',text)

print(date)

date_modfi = '01/03/21'

#----------------------re.sub(r'exp_to_be_replaced',r'exp_to_change_to',string)-------------------------

modified_text = re.sub(r'(/d+)(/\d+)(/\d+)',r'\1-\3-\2',text)

#-------here we have to group them 
print(modified_text) #doesn't work :/



new_data = re.sub(r'(/d)+(/\d)+(/\d)',date_modfi,text) #this neither 

print(new_data)