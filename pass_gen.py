import random

domain = [[]]*4
domain[0] = list(range(33,39)) #spcl
domain[1] = list(range(48,58)) #num
domain[2] = list(range(65,91)) #caps
domain[3] = list(range(97,123)) #lower
pass_len = raw_input("How big a password do you want: ")
generated_password = [None]*int(pass_len) #create an empty passwd of user input length
pos = 0
for pos in range(int(pass_len)):
    selected_type = random.choice(domain)
    selected_char = random.choice(selected_type)
    generated_password[pos] = chr(selected_char) #chr(int) gives corresponding char
print generated_password