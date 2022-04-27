print('Registration:')
us_name = input("set your username:")
pass_word = input("set your password:")

fil = open(f'{us_name}.txt','w')
fil.write(us_name)
fil.write('\n')
fil.write(pass_word)
fil.close()
print("Registration successful!")
print('Log in:')
username = input('enter your username:')
password = input('enter the password:')
flg = 0
newfile = open(f'{username}.txt','r')
for i in newfile.readlines():
    if i[:-2] == username:
        flg = 1
    elif i == pass_word:
        flg = 2
if flg == 2:
    print('log in succesful!')

newfile.close()