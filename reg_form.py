import re
def email_check(email):
    k=0
    if len(email)>=6:
        if email[0].isalpha():
            if ('@' in email) and (email.count('@')==1):
                pattern,pattern1='\W@','@\W'
                match=re.findall(pattern,email)
                match1=re.findall(pattern1,email)
                if not(match or match1):
                    k=1
                    if k==1:
                        return True
                    else:
                        return False
                else:
                    print('special characters at the end of id or invalid domain name')
                    return False
            else:
                print("special character @ cant be used")
                return False
        else:
            print("starting character should be alphabet")
            return False
    else:
        print("enter valid email id")
        return False


def password_check(password):
    sp_char=['!','@','#','$','&','*','_','?','%','^','+','-','=','.',',','<','>','(',')']
    if (len(password)>5) and (len(password)<16):
        if re.search('[a-z]',password):
            if re.search('[A-Z]',password):
                if re.search('[0-9]',password):
                    for i in password:
                        if i in sp_char:
                            return True
                    else:
                        print("password must have atleast 1 special character")
                        return False
                else:
                    print("password must have atleast 1 digit")
                    return False
            else:
                print("password must have atleast 1 uppercase")
                return False
        else:
            print("password must have atleast 1 lowercase")
            return False
    else:
        print("password length should be 6 to 16 characters")
        return False

def registration():
    db=open("reg_data.txt",'r')
    db.close()
    print("Registration form")
    mail_id=input("Enter email id :")
    mail_ck=email_check(mail_id)
    if mail_ck:
        password = input("Create password :")
        pwd_ck=password_check(password)
        if pwd_ck:
            password1=input("Confirm password :")
            if password == password1:
                db = open('reg_data.txt', 'a')
                db.write(mail_id+ ',' + password+'\n')
                db.close()
                print("signed in successfully")
            else:
                print("password mismatch")
                registration()
        else:
            registration()
    else:
        registration()

def login():
    print('Login details')
    email=input('Enter registered mail id :')
    password=input('Enter your password :')
    db=open('reg_data.txt','r')
    d=[]
    f=[]
    for i in db:
        a,b=i.split(',')
        b=b.strip()
        d.append(a)
        f.append(b)
    data=dict(zip(d,f))

    if email in data.keys():
        if password == data[email]:
            print("logged in successfully")
        else:
            print("incorrect username or password")
            n=input("forgot password? (y/n)")
            if n=='y':
                mail_id=input("Enter your registered email id")
                if mail_id in data.keys():
                    print("your password is ",data[mail_id])
                else:
                    print("This id not registered")
                    startoff()
            elif n=='n':
                login()
            else:
                login()
    else:
        print("username does't exist")
        startoff()
def startoff():
    x=input('please press r for registration or l for login:')
    if x=='r':
        registration()
    elif x=='l':
        login()
    else:
        print("enter r or l:")

startoff()
