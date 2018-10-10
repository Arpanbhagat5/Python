str = raw_input("check for pallindrome (more than single char): ")
not_p = 0 
lt = 0
rt = len(str)-1
while(lt <= rt and not_p == 0):
    if str[lt] == str[rt]:
        lt = lt +1
        rt = rt -1
    else:
        not_p = 1
    
if not_p ==1:
    print("not pallindrome") 
else:
    print("Pallindrome")

