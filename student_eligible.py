# write a program to check a student can eligible to Reach next Level or not ?
#***************CONDITION***************************************.
#Here our objective is pass mark in individual subject is 32 ?
# student total mark must be greater than equal to magic number then student can go next level ?
#if student have mora than 3 back paper then he/she can not move next level ?

list1=[]
count=0
pamk=32
Name=input("Enter your name: ")
math=int(input("Enter your Math mark: "))
if math<=32:
    chance=input("Do you want re-attempt?").lower()
    if chance=="yes":
        math1=int(input("Enter your math result: "))
        if pamk>=math1:
            list1.append(math)
            print("you have give back paper")
            count += 1
        else:
            list1.append(math1)
    else:
        list1.append(math)
        print("you have give back paper")
        count += 1
else:
    list1.append(math)

eng=int(input("Enter your english mark: "))
if eng<=32:
    chance = input("Do you want re-attempt?").lower()
    if chance == "yes":
        eng1= int(input("Enter your math result: "))
        if pamk >= eng1:
            list1.append(eng)
            print("you have give back paper")
            count += 1
        else:
            list1.append(eng1)
    else:
        list1.append(eng)
        print("you have give back paper")
        count+=1
else:
    list1.append(eng)

pyt=int(input("Enter your python mark: "))
if pyt<=32:
    chance = input("Do you want re-attempt?").lower()
    if chance == "yes":
        pyt1 = int(input("Enter your math result: "))
        if pamk >= pyt1:
            list1.append(pyt)
            print("you have give back paper")
            count += 1
        else:
            list1.append(pyt1)
    else:
        list1.append(pyt)
        print("you have give back paper")
        count += 1
else:
    list1.append(pyt)

jav=int(input("Enter your Java mark: "))
if jav<=32:
    chance = input("Do you want re-attempt?").lower()
    if chance == "yes":
        jav1 = int(input("Enter your math result: "))
        if pamk >= jav1:
            list1.append(jav)
            print("you have give back paper")
            count += 1
        else:
            list1.append(jav1)
    else:
        list1.append((jav))
        print("you have give back paper")
        count += 1
else:
    list1.append(jav)

sum1=sum(list1)
if count<=2:
    if sum1 >=140:
        print(f'Dear {Name} you have succesfully complet!!! Welcome to next level !!!!!')
        print(f'Magic mark is 140 and you got {sum1}')
        print(f'you have back paper is {count}')
    else:
        print(f'Dear {Name} You are Fail!! ')
        print(f'Magic mark is 140 and you got {sum1}')
        print(f'you have back paper is {count}')
        print(f'You need give all the exam in next phase!!!')
else:
    print(f'Dear {Name} You are Fail!! ')
    print(f'you have back paper is {count}')
    print(f'You need give all the exam in next phase!!!')
