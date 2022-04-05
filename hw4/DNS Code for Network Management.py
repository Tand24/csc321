
"""
#Import needed modules
import pandas as pd
import socket
    
#Pandas reads the file and seperates it, global variables are under
x = pd.read_csv("domains.tsv", sep = '\t')['domain']
doc = {}
docHost = {}

for i in range(len(x)): #goes through x, where i is the iterantion number
    temp = [] #resets the temp var after every iteration
    try:
        long = socket.getaddrinfo(str(x[i]),443) 
        for b in range(len(long)):
            temp.append(long[b][4]) 
        doc[x[i]] = temp 
        
    except Exception as e:
        #Gives error message for websites that are no longer functioning
        print("\nERROR PRESENT: "+str(e)+'\n')

print(doc)
    
for l in doc: #goes through every key/vlaue of dictionary 'doc'
    try:
        #sets the name of the site to the key and adds the value of the extra bits
        docHost[l] = socket.gethostbyaddr(str(doc[l][0][0]))
        docHost[l] = docHost[l][0] #removes the extra bits, leaves host name
        
    except Exception as e:
        #Gives error message the IPs that do not produce a host name
        print("Error : ", e)

for y in docHost: #goes thorough every key/value in dictionary 'docHost'
    doc[y].append(docHost[y]) #adds the host name from docHost to the matching key of doc

print(doc) #prints the final dictionary of the site name, IP, and host name respectivly. 

