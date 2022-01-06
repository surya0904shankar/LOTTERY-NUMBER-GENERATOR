def lottery():
    lot=[]
    print("WELCOME USER TO BINGO LOTTERY")
    print("----------------------------------------------------------------------")
    k=int(input("enter '1' to choose your number enter\n'2' for the system to generate a number for you"))
    print("----------------------------------------------------------------------")
    if k==1:
        flag=0
        while flag!=1:
            user=int(input("enter a 6 DIGIT NUMBER for BINGO LOTTERY selection"))
            if len(str(user))!=6:
                print("invalid digit entered, digit count is not 6 please choose again!")
                continue
            elif len(str(user))==6:
                if user not in lot:
                    lot.append(user)
                    flag+=1
                elif user in lot:
                    print("the number already exixts please choose another number")
                    continue
    elif k==2:
        import random
        found=0
        user=random.randint(100000,999999)
        while found!=1:
            if user not in lot:
                lot.append(user)
                found+=1
            elif user in lot:
                continue
    k=str(user)
    print("----------------------------------------------------------------------")
    print("your BINGO LOTTERY number is:",user)
    print("----------------------------------------------------------------------") 
    mail=input("enter your mail id:")
    import smtplib
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("suryalicdb@gmail.com","Lic@1234")
    p=("Congrats on choosing your lottery number from BINGO LOTTRIES")
    s.sendmail("suryalicdb@gmail.com",mail,p)
    print("email sent")
    s.quit() 
lottery()
