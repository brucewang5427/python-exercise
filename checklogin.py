def checkname():
    persons=[{'name':'xingwen','age':25,'phone':'15212242569'},
           {'name':'chenggang wang','age':26,'phone':'15771557977'}]
    while True:
        name=input('please enter your name:')
        if name=='chenggang':
            count=0
            password=input('please enter your password: ')
            while password!='123' and count<6:
                password=input('wrong password, please enter again')
                count+=1
                
            else:
               print('welcome to login\n')
               name2=input('please enter the name you want to check: ')
               for person in persons:                
                   if name2==person['name']:
                       print('Name: {name}, Age: {age}, Phone: {phone}'.format(name=person['name'],age=person['age'], phone=person['phone']))
                       break
        else:
            print('sorry, user {0} not found'.format(name))
            break
            
if __name__=='__main__':
    checkname()
