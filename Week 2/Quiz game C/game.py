while 1==1:
    point=0
    val = input('Quiz game\nFor start press 1  otherwise  press 2\n')
    if val == '1':
        print("\nok boss\n\nWhich is the first letter in afabet?\n\nChoose:\n\n1) b\n2) c\n3) a\n")
        que=input()
        if que==3:
            point+=1
            print("\n\nmmm yess you got one point baby\n\n\n")
        else:
            print('nice idiot')
        print("\n\nWhich is the second letter in afabet?\n\nChoose:\n\n1) b\n2) c\n3) a\n")
        qee=input()
        if qee==1:
            point+=1
            print('you are like a genius, one more point for you\n\n\n')
        else:
            print("go home\n\n")
        print("1+2=?\n\nChoose:\n\n1) 1\n2) 2\n3) 3\n")
        res=input('')
        if res=='3':
            point+=1
            print("\nnice work Einstein\n\n")
            print(point)
        else:
            print("\ngo to school\n\n")
        print('\nYOU GOT',point,'POINTS\n\nTHE GAME WILL RESTART\n\n')
    else:
        print('idiot')
        break
