# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Code by naryVip

import numpy as np
#Here 0 is referred as empty space.

arr = np.array(([2 ,1 ,3] , [6 ,5 ,4], [0 , 7, 8]))#Pre-defined as of now.
goal = np.array(([1 ,2 ,3] , [4 ,5 ,6], [7 ,8 ,0]))
#Temp(1 to 4) is used cuz there are 4 different moves (max) possible, the 4 stores in these temp.
temp4 = arr
temp3 = arr
temp2 = arr
temp1 = arr
print(arr)
#Zero position variables
space_row = 0
space_col = 0

def hueristic(nom):# Here the best choice is chosen which has less no misplaces elements as compared to goal state.
    global arr , goal ,temp1 , temp2 , temp3 , temp4
    temp = [temp1 , temp2 , temp3 , temp4]#Arrray consist of all 4 possible matrix
    misplace = []#This array stores the no of mismatches in each temp
    for i in range(nom , 4):
        temp.pop()#Here , if 2 movements then only 2 temps are stored , rest are popped, same for 3.
            
    #checking for the next state.       
    for i in temp:
        count = 0
        for j in range(3):
            for k in range(3):
                if i[j][k] != goal[j][k]:
                    count +=1
        misplace.append(count)
    
    min_count = min(misplace)#Takes which has min mis match
    index = misplace.index(min_count)#Matching Min value and matrix position in these 2 arrays
    arr = temp[index] #Arr is updated to next state near to goal state
    print("The updated matrix")
    print(arr)
    
    print()
    
    if 0 in misplace: #If any matrix has zero mismatches , then program stops.
        print("The goal state is reached")
    else:
        main()
        
        


def replace(array ,goal_pos ,i): #Here the empty space is moved
    global space_row , space_col ,temp1 ,temp2 ,temp3 , temp4 
    goal_row = goal_pos[0]
    goal_col = goal_pos[1]
    
    
    temp = array[space_row][space_col]
    array[space_row][space_col] = array[goal_row][goal_col]
    array[goal_row][goal_col] = temp
    #assigning/updating the value respectively
    if i == 0:    
        temp1 = array
    elif i == 1:
        temp2 = array
    elif i == 2:
        temp3 = array
    elif i ==3:    
        temp4 = array



    
def letsMove(possible_moves):#Here the different movement results in diff matrix , so max temp (1..4) matrix used. 
    global arr , space_row , space_col ,temp1 ,temp2 ,temp3 , temp4 
    nom = len(possible_moves)
    for i in range(nom):
        if i == 0: 
            replace(temp1 , possible_moves[i] ,i)
        #[program goes wrong here] : The main problem is here where the main array that is arr is getting copied from Temp1, seeking for the solution and will update ASAP
        elif i == 1:
            replace(temp2 , possible_moves[i] ,i)
        elif i == 2:
            replace(temp3 , possible_moves[i] ,i)
        elif i == 3:
            replace(temp4 , possible_moves[i] ,i)
    
    
    #print(temp1)
    #print(temp2)
    
    hueristic(nom)


    
    
def possibleMoves():#Checkinf for the possible moves from any position where empty space is.
    global arr , space_row , space_col
    possible_moves = []#THis stores the position(2d format) of possible movement of empty space.
    print()
    if( space_row + 1 <= 2 ):
        print("Down movement possible")
        possible_moves.append([space_row+1,space_col])
    if( space_row - 1 >= 0 ):
        print("Up movement possible")
        possible_moves.append([space_row-1,space_col])
    if( space_col + 1 <= 2 ):
        print("Right movement possible")
        possible_moves.append([space_row,space_col+1])
    if(space_col - 1 >= 0 ):
        print("Left movement possible")
        possible_moves.append([space_row,space_col-1])
    
    letsMove(possible_moves)
    

def main():
    global arr , space_row , space_col ,temp4 , temp3 ,temp2 ,temp1
    #This one for refreshing the value for next cycle with updated arr.
    temp4 = arr
    temp3 = arr
    temp2 = arr
    temp1 = arr
    
    for i in range(0 ,3):
        for j in range(0 ,3):
            if arr[i ,j] == 0:#For finding the position of empty space.
                space_row = i
                space_col = j
    
    possibleMoves()
    

main()  