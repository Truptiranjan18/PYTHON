# Create a application to perform signup, signin, update password and exit.
user_dict={}
while True:
    print("1,signup")
    print("2,signin")
    print("3,Update password")
    print("4,Exit")
    opt=int(input("Enter option: "))
    if opt==1:
        uname=input("Enter Your Name: ")
        pwd=input("Enter Your Password: ")
        if uname in user_dict:
            print(f'{uname} already exists')
        else:
            user_dict[uname]=pwd
            print("User Registered...")
    elif opt==2:
        uname=input("UserName: ")
        if uname in user_dict:
            pwd=input("Password: ")
            p=user_dict[uname]
            if p==pwd:
                print(f"{uname} Welcome")
            else:
                print("Invalid Password")
        else:
            print("Invalid UserName")

    elif opt==3:
        uname=input("UserName: ")
        if uname in user_dict:
            opwd=input("old password")
            p=user_dict[uname]
            if p==opwd:
                npwd=input("New password: ")
                user_dict[uname]=npwd
                print("Password Updated")
            else:
                 print("Invalid Password")
        else:
            print("Invalid User Name")
    elif opt==4:
        print("Exit")
        break





