#!/usr/bin/env python

#------------------------------------------------------------------------------
# Author: Beheeder 
# Description: This script generates a list of usernames based on first, middle
# and lat name.
# ToDo: Add some randomization, add initial restriction to less than char in any
# name.

# Declare variables------------------------------------------------------------
first_name     = raw_input('insert first name: ')
middle_name    = raw_input('insert middle name: ')
last_name      = raw_input('insert last name: ')
domain         = raw_input('insert domain name: ')
numb           = input('insert number range: ')
while numb < 0:
    numb = input('ERROR!: Insert a positive value. ')

initial        = input('insert initials char number(e.g: if = 4 aplpha => alp): ')
while initial <= 0 > len(first_name) > len(last_name):
    initial = input('ERROR!: Insert a value greater than zero or less than the leght of the fisrt or last name. ')

print 'first'
print len(first_name)

print 'middle'
print len(middle_name)

print 'last'
print len(last_name)

username_list  = []
filename       = 'email_list.txt'

if middle_name == '':
    m_initial  = 0
else:
    m_initial  = initial

#------------------------------------------------------------------------------
usr = first_name + middle_name + last_name + '@' + domain
username_list.append(usr)

usr = first_name + middle_name + '@' + domain
username_list.append(usr)

usr = first_name + last_name + '@' + domain
username_list.append(usr)

usr = middle_name + '@' + domain
username_list.append(usr)

usr = middle_name + last_name + '@' + domain
username_list.append(usr)
#underscore
usr = first_name + '_' + middle_name + '_' + last_name + '@' + domain
username_list.append(usr)

usr = first_name + '_' + middle_name + '@' + domain
username_list.append(usr)

usr = first_name + '_' + last_name + '@' + domain
username_list.append(usr)

usr = middle_name + '_' + last_name + '@' + domain
username_list.append(usr)
# dot
usr = first_name + '.' + middle_name + '.' + last_name + '@' + domain
username_list.append(usr)

usr = first_name + '.' + middle_name + '@' + domain
username_list.append(usr)

usr = first_name + '.' + last_name + '@' + domain
username_list.append(usr)

usr = middle_name + '.' + last_name + '@' + domain
username_list.append(usr)


for _ in range(numb):
    usr = first_name + str(_) + '@' + domain
    username_list.append(usr)

    usr = first_name + middle_name + str(_) + '@' + domain
    username_list.append(usr)

    usr = first_name + last_name + str(_) + '@' + domain
    username_list.append(usr)

    usr = middle_name + str(_) + '@' + domain
    username_list.append(usr)

    usr = last_name + str(_) + '@' + domain
    username_list.append(usr)

    usr = middle_name + last_name + str(_) + '@' + domain
    username_list.append(usr)

    usr = first_name + middle_name + last_name + str(_) + '@' + domain
    username_list.append(usr)
#underscore
    usr = first_name + '_' + middle_name + str(_) + '@' + domain
    username_list.append(usr)

    usr = first_name + '_' + last_name + str(_) + '@' + domain
    username_list.append(usr)

    usr = middle_name + '_' + last_name + str(_) + '@' + domain
    username_list.append(usr)

    usr = first_name + '_' + middle_name + '_' +last_name + str(_) + '@' + domain
    username_list.append(usr)
#dot
    usr = first_name + '.' + middle_name + str(_) + '@' + domain
    username_list.append(usr)

    usr = first_name + '.' + last_name + str(_) + '@' + domain
    username_list.append(usr)

    usr = middle_name + '.' + last_name + str(_) + '@' + domain
    username_list.append(usr)

    usr = first_name + '.' + middle_name + '.' +last_name + str(_) + '@' + domain
    username_list.append(usr)

#------------------------------------------------------------------------------

for i in range(initial):
    for j in range(initial):
        if m_initial == 0:
            j = 0    
        for k in range(initial):
            if (i == 0 and j == 0 and k == 0): #(0,0,0)
                usr = first_name + middle_name[:j] + last_name[:k] + '@' + domain
                username_list.append(usr)

                usr = last_name + '@' + domain
                username_list.append(usr)

            elif (i == 0 and j ==0 and k != 0): #(0,0,k)
                
                usr = last_name[:k] + '@' + domain
                username_list.append(usr)

                usr = first_name + last_name[:k] + '@' + domain
                username_list.append(usr)

                usr = first_name + '_' + last_name[:k] + '@' + domain
                username_list.append(usr)

                usr = first_name + '.' + last_name[:k] + '@' + domain
                username_list.append(usr)

                for _ in range(numb):
                    usr = first_name + last_name[:k] + str(_) + '@' + domain
                    username_list.append(usr)

                    usr = first_name + '_' + last_name[:k] + str(_) + '@' + domain
                    username_list.append(usr)

                    usr = first_name + '.' + last_name[:k] + str(_) + '@' + domain
                    username_list.append(usr)
                   
# Using full midddle name combination
# add condition to fix abscence of middle name        <--------------- ERROR!!
                usr = middle_name + last_name[:k] + '@' + domain
                username_list.append(usr)

                usr = middle_name + '_' + last_name[:k] + '@' + domain
                username_list.append(usr)

                usr = middle_name + '.' + last_name[:k] + '@' + domain
                username_list.append(usr)

                usr = first_name + middle_name + last_name[:k] + '@' + domain
                username_list.append(usr)

                usr = first_name + middle_name + '_' + last_name[:k] + '@' + domain
                username_list.append(usr)

                usr = first_name + middle_name + '.' + last_name[:k] + '@' + domain
                username_list.append(usr)

                for _ in range(numb):
                    usr = first_name + middle_name + last_name[:k] + str(_) + '@' + domain
                    username_list.append(usr)

                    usr = first_name + '_' + middle_name + '_' + last_name[:k] + str(_) + '@' + domain
                    username_list.append(usr)

                    usr = first_name + '.' + middle_name + '.' + last_name[:k] + str(_) + '@' + domain
                    username_list.append(usr)

                    usr = middle_name + last_name[:k] + str(_) + '@' + domain
                    username_list.append(usr)

                    usr = middle_name + '_' + last_name[:k] + str(_) + '@' + domain
                    username_list.append(usr)

                    usr = middle_name + '.' + last_name[:k] + str(_) + '@' + domain
                    username_list.append(usr)
            
            elif (i == 0 and j !=0 and k == 0): #(0,j,0)
                usr = middle_name[:j] + '@' + domain
                username_list.append(usr)

                usr = first_name + middle_name[:j] + '@' + domain
                username_list.append(usr)

                usr = first_name + '_' + middle_name[:j] + '@' + domain
                username_list.append(usr)

                usr = first_name + '.' + middle_name[:j] + '@' + domain
                username_list.append(usr)

                for _ in range(numb):
                    usr = first_name + middle_name[:j] + str(_) + '@' + domain
                    username_list.append(usr)

                    usr = first_name + '_' + middle_name[:j] + str(_) + '@' + domain
                    username_list.append(usr)

                    usr = first_name + '.' + middle_name[:j] + str(_) + '@' + domain
                    username_list.append(usr)

                    usr = middle_name[:j] + str(_) + '@' + domain
                    username_list.append(usr)

            elif (i == 0 and j != 0 and k != 0): # (0,j,k)
                usr = middle_name[:j] + last_name[:k] + '@' + domain
                username_list.append(usr)

                usr = middle_name[:j] + '_' + last_name[:k] + '@' + domain
                username_list.append(usr)

                usr = middle_name[:j] + '.' + last_name[:k] + '@' + domain
                username_list.append(usr)

# Using full first name combination
                usr = first_name + middle_name[:j] + last_name[:k] + '@' + domain
                username_list.append(usr)

                usr = first_name + '_' + middle_name[:j] + '_' + last_name[:k] + '@' + domain
                username_list.append(usr)

                usr = first_name + '.' + middle_name[:j] + '.' + last_name[:k] + '@' + domain
                username_list.append(usr)

                for _ in range(numb):
                    usr = first_name + middle_name[:j] + last_name[:k] + str(_) + '@' + domain
                    username_list.append(usr)

                    usr = first_name + '_' + middle_name[:j] + '_' + last_name[:k] + str(_) + '@' + domain
                    username_list.append(usr)

                    usr = first_name + '.' + middle_name[:j] + '.' + last_name[:k] + str(_) + '@' + domain
                    username_list.append(usr)

                    usr = middle_name[:j] + last_name[:k] + str(_) + '@' + domain
                    username_list.append(usr)

                    usr = middle_name[:j] + '_' + last_name[:k] + str(_) + '@' + domain
                    username_list.append(usr)

                    usr = middle_name[:j] + '.' + last_name[:k] + str(_) + '@' + domain
                    username_list.append(usr)

            elif (i != 0 and j == 0 and k == 0 ): #(i,0,0)
                usr = first_name[:i] + middle_name[:j] + last_name[:k] + '@' + domain
                username_list.append(usr)

# using full last name combination
                usr = first_name[:i] + last_name + '@' + domain
                username_list.append(usr)

                usr = first_name[:i] +  '_' + last_name + '@' + domain
                username_list.append(usr)

                usr = first_name[:i] + '.' + last_name + '@' + domain
                username_list.append(usr)

                for _ in range(numb):
                    usr = first_name[:i] + last_name[:k] + str(_) + '@' + domain
                    username_list.append(usr)

                    usr = first_name[:i] + last_name + str(_) + '@' + domain
                    username_list.append(usr)

                    usr = first_name[:i] + '_' + last_name + str(_) + '@' + domain
                    username_list.append(usr)

                    usr = first_name[:i] + '.' + last_name + str(_) + '@' + domain
                    username_list.append(usr)
                
            elif (i != 0 and j != 0 and k == 0): #(i,j,0)
                usr = first_name[:i] + middle_name[:j] + '@' + domain
                username_list.append(usr)

                usr = first_name[:i] + '_' + middle_name[:j] + '@' + domain
                username_list.append(usr)

                usr = first_name[:i] + '.' + middle_name[:j] + '@' + domain
                username_list.append(usr) 
  
# Using full last name combination
                usr = first_name[:i] + middle_name[:j] + last_name + '@' + domain
                username_list.append(usr)

                usr = first_name[:i] + '_' + middle_name[:j] +  '_' + last_name + '@' + domain
                username_list.append(usr)

                usr = first_name[:i] + '.' + middle_name[:j] + '_' + last_name + '@' + domain
                username_list.append(usr)

                for _ in range(numb):
                    usr = first_name[:i] + middle_name[:j] + str(_) + '@' + domain
                    username_list.append(usr)

                    usr = first_name[:i] + '_' + middle_name[:j] + str(_) + '@' + domain
                    username_list.append(usr)

                    usr = first_name[:i] + '.' + middle_name[:j] + str(_) + '@' + domain
                    username_list.append(usr)

                    usr = first_name[:i] + middle_name[:j] + last_name + str(_) + '@' + domain
                    username_list.append(usr)

                    usr = first_name[:i] + '_' + middle_name[:j] + '_' + last_name + str(_) + '@' + domain
                    username_list.append(usr)

                    usr = first_name[:i] + '.' + middle_name[:j] + '.' + last_name + str(_) + '@' + domain
                    username_list.append(usr)

            elif (i != 0 and j == 0 and k != 0): #(i,0,k)
                usr = first_name[:i] + last_name[:k] + '@' + domain
                username_list.append(usr)

                usr = first_name[:i] + '_' + last_name[:k] + '@' + domain
                username_list.append(usr)

                usr = first_name[:i] + '.' + last_name[:k] + '@' + domain
                username_list.append(usr)

                for _ in range(numb):
                    usr = first_name[:i] + last_name[:k] + str(_) + '@' + domain
                    username_list.append(usr)

                    usr = first_name[:i] + '_' + last_name[:k] + str(_) + '@' + domain
                    username_list.append(usr)

                    usr = first_name[:i] + '.' + last_name[:k] + str(_) + '@' + domain
                    username_list.append(usr)

            else: #(i,j,k)
                usr = first_name[:i] + middle_name[:j] + last_name[:k] +'@' + domain
                username_list.append(usr)
    
                usr = first_name[:i] + '_' + middle_name[:j] + '_' + last_name[:k] + '@' + domain
                username_list.append(usr)
 
                usr = first_name[:i] + '.' + middle_name[:j] + '.' + last_name[:k] + '@' + domain
                username_list.append(usr)
                
                for _ in range(numb):

                    usr = first_name[:i] + middle_name[:j] + last_name[:k] + str(_) + '@' + domain
                    username_list.append(usr)

                    usr = first_name[:i] + '_' + middle_name[:j] + '_' + last_name[:k] + str(_) + '@' + domain
                    username_list.append(usr)

                    usr = first_name[:i] + '.' + middle_name[:j] + '.' + last_name[:k] + str(_) + '@' + domain
                    username_list.append(usr)

#------------------------------------------------------------------------------
with open(filename, 'w') as f:
    for s in username_list:
        f.write(s + '\n')

print 'done'
