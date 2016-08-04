#!/usr/bin/python

import random
import string

filename   = 'password_list.txt'
print 'General parameters:'
pass_numb  = input('Number of passwords needed: ' )

print ''
print 'Dictionary Based Password Generation Parameters:'
word_count = input('Number of words use to generate passwords: ')

print ''
print 'Dictionary and Digit Based Password Generation Parameters:'
numb_count = input('digits needed to reach: ')
word_numb_count = input('Number of words used to generate password: ')

print ''
print 'Random Password Generation Parameters:'
char_count = input('Number of characters in passwords: ')
pass_list  = []


#------------------------------------------------------------------------------
f = open('words.txt', "r") ## open file with read only perm
dictionary = [line.rstrip('\n') for line in open('words.txt')] 
f.close()

f = open('words.txt', "r")
name_dictionary = [line.rstrip('\n') for line in open('words.txt')]
f.close()

#----------------------Dictionary based password:------------------------------
#---------with upper, lower numbers and punctuation----------------------------
def dict_pass_generator(size = word_count, words = dictionary):
    return "".join(random.choice(words) for _ in range(size))
    


for i in range(pass_numb):
    password = dict_pass_generator()
    password = "".join(random.choice([k.upper(), k]) for k in password)
    password = string.replace(password, 'e', '3', 3)
    password = string.replace(password, 'a', '@', 3)
    password = string.replace(password, 'i', '!', 3)
    password = string.replace(password, 'o', '0', 3)
    password = string.replace(password, 'l', '7', 3)
    password = string.replace(password, 's', '5', 3)
    pass_list.append(password)

#------------------------Name Dictionary Based Password-----------------------------
def pass_gen(size = word_numb_count, words = name_dictionary):
    return "".join(random.choice(words) for _ in range(size))

for i in range(pass_numb):
    mot_de_passe = pass_gen()
    pass_list.append(mot_de_passe)
    count = 0
    while count < numb_count + 1:
        mot_de_pass = mot_de_passe + str(count)
        pass_list.append(mot_de_pass)
        count += 1


#print 'pass'
#print passs
#---------------------------Random passwords:----------------------------------
def ran_pass_gen(size = char_count, chars = string.ascii_letters + string.digits + string.punctuation):
    return "".join(random.choice(chars) for _ in range(size))


for i in range(pass_numb):
    ran_pass = ran_pass_gen()
    ran_pass = "".join(random.choice([k.upper(), k]) for k in ran_pass)
    ran_pass = "".join(random.choice([k.lower(), k]) for k in ran_pass)
    pass_list.append(ran_pass)

#-------------------------Write passwords to file------------------------------

print pass_list

with open(filename,'w') as f:
    for s in pass_list:
        f.write(s + '\n')

print 'Done'
#----------------------------------------------------------------------
 
#usr = first_name + last_name + '@' + domain
#username_list.append(usr)
#print usr

#------------------------------------------------------------------------------
