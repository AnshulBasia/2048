from random import randint
import time
"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    list1=[]
    if(len(line)==1):
        list1.append(line[0])
        return list1
    
    
    
    for num in range(len(line)):
        if(line[num]!=0):
            list1.append(line[num])
    index=0
    if(len(list1)==1):
        for num in range(1,len(line)):
              list1.append(0)
        return list1
    list2=[]
    
    while(index<len(list1)-1):
        if(list1[index+1]==list1[index]):
           list2.append(2*list1[index])
           index=index+2
           if(index+1==len(list1)):
            list2.append(list1[index])
           
        else:
           list2.append(list1[index])
           index=index+1
           if(index+1==len(list1)):
            list2.append(list1[index])
           
    list3=list2
    for num in range(len(list3),len(line)):
              list3.append(0)
    return list3
