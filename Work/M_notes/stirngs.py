'''

1.4 Strings 

1 String operations :
    -Concatenation (+)
    -Length (len())
    -Membership test ( in , not in)
    -replication (*)
'''

'''
2.String Methods:
 s.endswith(suffix)     # Check if string ends with suffix
s.find(t)              # First occurrence of t in s
s.index(t)             # First occurrence of t in s
s.isalpha()            # Check if characters are alphabetic
s.isdigit()            # Check if characters are numeric
s.islower()            # Check if characters are lower-case
s.isupper()            # Check if characters are upper-case
s.join(slist)          # Join a list of strings using s as delimiter
s.lower()              # Convert to lower case
s.replace(old,new)     # Replace text
s.rfind(t)             # Search for t from end of string
s.rindex(t)            # Search for t from end of string
s.split([delim])       # Split string into list of substrings
s.startswith(prefix)   # Check if string starts with prefix
s.strip()              # Strip leading/trailing space
s.upper()  
    

'''
# ---------------------strip()----------------
#lstrip() rstrip()

I = 'String are immutable  '

j = I.strip()

print(j)

#-----------------.upper() , .lower()----------------

j = I.upper()
print(j)

j = I.lower()
print(j)

#endswith()

print(j.endswith('e'))

#-----------------join(s)----------------

#k = 'Every time we perform some operation a new string is created'
#k = 'Heck'
j = '-'.join(j)  #joins a list of string 
                
print(j)

#---------------------------split()------------------------
#splits string into a list of substrings using delimiter :

k = j.split(" ")    #here delimiter is space

print(k)


#-----------------STRING MUTABILITY-------------------

# Strings are read only , once created, the value can't be changed 

#All opertations and methods that manipulate strings always create new strings


#--------------------String conversions ----------------------

#---------------------str()--------------
#converts any value to a string

#--------------------Byte strings---------------

# A string of 8bit bytes enocountered with low-level I/O is written as:

data = b'Byte strings byte'

print(data)

# Most op are same but indexing gives kinda diff results

print(data[0])



#------------------CONVERSTION TO/FROM TEXT STRINGS----------------------------

#----------------------deconde() , encode()---------------------------


text = data.decode('utf-8') #bytes to text

data = text.encode('utf-8') #text to bytes

#other values can be : 'ascii' 'latin1'

#--------------------Raw string------------------

#raw strings are printed without interpreting backslash

direc = r'c:\\newdata'

#---------------------f-strings----------------
price = 90.908132
print(f"price must be : {price : 0.2f}")

