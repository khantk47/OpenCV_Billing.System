

def opening():
    print(" _______________________")
    print("|                       |")
    print("|  FreshCo Supermarket  |")
    print("|_______________________|")
    
def ownersmenu():  
    print("------------------------------")
    print("   -----MAIN MENU -----")
    print("------------------------------")
    print("      1.Owner's End       ")
    print("      2.Inventory         ")
    print("      3.Billing           ")
    print("      4.Analysis          ")
    print("      5.Print/Export(csv) ")
    print("      6.Visualization     ")
    print("      7.Exit              ")
    print(" ------------------------------")
    print(" ------------------------------")
def othersmenu():
    print("------------------------------")
    print("   ------MAIN MENU -------")
    print("------------------------------")
    print("      1.Inventory         ")
    print("      2.Billing           ")
    print("      3.Analysis          ")
    print("      4.Print/Export(csv) ")
    print("      5.Visualization     ")
    print("      6.Exit              ")
    print(" ------------------------------")
    print(" ------------------------------")
def owner():
    print("------------------------------")
    print("   ------OWNER'S MENU ----- ")
    print("------------------------------")
    print("    1.Owners Details   ")
    print("    2.License          ")
    print("    3.User Creation    ")
    print("    4.Employee Menu    ")
    print("    5.Exit             ")
    print(" ------------------------------")
    print(" ------------------------------")

#For getting only integer input    
def in_number(n):
    while True:
      try:
          num = int(input(n))
          break;
      except ValueError:
        print("Please input integer only...")
        continue
    return num

#Yes or No loop
def yorno(x):  
    while True:
      try:
        YorNo = input(x)
        if YorNo.upper() == "Y" or YorNo.upper() == "N" :          
          break;
        else:
          print("You have not entered the correct option(y/n)")
          continue
      except ValueError:
        print("You have not entered the correct option(y/n)")
        continue
    return YorNo

#Barcode scanning module-Helps us scan barcodes
def barcode():
    import cv2      #image processing and computer vision
    from pyzbar.pyzbar import decode  #barcode decoder
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)    
    cap.set(3,480)
    cap.set(4,320)
    
    camera = True
    a=""
    while camera == True:
        success, frame = cap.read()      
        
        for code in decode(frame):
            print("sadiq")
            a=code.data.decode('utf-8')
            #print (a)
            
            
    #        print(code.data.decode('utf-8'))
        #cv2.imshow('Please scan the Barcode and Press ESC key', frame)
        barcode_window='Please scan the Barcode and Press ESC key'
        cv2.imshow(barcode_window, frame)
        cv2.setWindowProperty(barcode_window,cv2.WND_PROP_TOPMOST,1)
        if cv2.waitKey(1) & 0xFF == 27:
            break
        with open("Sad_barcode_result.csv", mode ='w') as file:
                file.write(a)
        #cv2.waitKey(1)
        if len(a)!=0 :
            break
    cv2.destroyAllWindows()
    return (a)

    
def menu():
    while True:
        option=in_number("Choose an option : ")
    
    if option==1:
        print("Only access for owners")
        reuser="y"
        while reuser=="y":
            qnsuser=input("Enter the username: ")
            if qnsuser=="maytas123": 
                    repass="y"
                    while repass=="y":
                        qnspass=input("Enter the password: ")
                        if qnspass=="emerald":
                            print("Succesfully Authenciated")
                            repass=="n"
                            reuser="n"
                            break
                        else:
                            print("incorrect password")
                            repass=yorno("Do you want to try again(y/n): ")
            else:
                print("Incorrect Username")
                reuser=yorno("Do you want to try again(y/n): ")
        
    if option==2:
        reuser="y"
        while reuser=="y":
            qnsuser=input("Enter the username")
            if qnsuser=="maytas123" or qnsuser=="FreshCo123": 
                    repass="y"
                    while repass=="y":
                        qnspass=input("Enter the password: ")
                        if qnspass=="emerald" or qnspass=="ruby":
                            print("Succesfully Authenciated")
                            repass=="n"
                            reuser="n"
                            break
                        else:
                            print("incorrect password")
                            repass=yorno("Do you want to try again(y/n): ")
            else:
                print("Incorrect Username")
                reuser=yorno("Do you want to try again(y/n): ")
    if option==3:
        print("Thank you")
        
#Contains basic owners details
def owners_details():
    print("#1")
    print("Bussiness Owner: Tashin Khan")
    print("Bussiness name: FreshCo Supermarket ")
    print("Business type: Retail")
    print("Contact Number : 050-45678945")
    print("Email: tashinkhan123@gmail.com")
    print("Employer Identification Number :78546789")
    print("Bussiness location:Shop 3,Yarmookh Furniture bulding,Near old etisalat")
    print("Al Salam street, Fujairah ,UAE")
    print("-----------------------------------------------------------------")
    print("#2")
    print("Bussiness Owner: Mayookh Pramod")
    print("Bussiness name: FreshCo Supermarket ")
    print("Business type: Retail")
    print("Contact Number : 050-89675416")
    print("Email: mayookhpramodabc@gmail.com")
    print("Employer Identification Number :986985418")
    print("Bussiness location:1st floor, 107,Yarmookh Furniture bulding,Near old etisalat")
    print("Al Salam street, Fujairah ,UAE")
    
#Shop license details
def license1():
    lrechose="y"
    while lrechose=="y":
        print("------------------------------")
        print("   ------LICENSE MENU ----- ")
        print("------------------------------")
        print("     1.View                ")
        print("     2.Update              ")
        print("     3.Exit                ")
        print("------------------------------")
        print("------------------------------")
        option=in_number("Chose the required option: ")
        def plicense():
            print(" ___________________________")
            print("|                           |")
            print("|    Commercial License     |")
            print("|___________________________|")
            
            
            print("License No: 741852963")
            print("Trade Name: FreshCo                      ")
            print("issue date:",Issue_date)
            print("expiry date:",Expiry_date)
            print("Issue Place: Fujairah                       ")

            print("Establishment Date:  01-01-2021                      ")

            print("\n")
            print("Company Details")
            print(" ____________________________________________________________")
            print("|Partner| Nationality | Description      | No        | Shares|")
            print("|----------------------------------------------------|-------|")
            print("|Partner| Indian      | Tashin Khan      | 5005      |   50  |")
            print("|----------------------------------------------------|-------|")
            print("|Partner| Indian      | Mayookh Pramod   | 5008      |   50  |")
            print("|____________________________________________________|_______|")


            print("\nCommercial Activities: Fruits & vegetable sales, supermarket    ")
            print("Address     : Sakamkam,Fujairah         ")
            print("PO Box      : 11223")
            print("Telephone No:09-1112223")
            print("Fax no      :09-1112223")
        
        if option==2:
            global Issue_date
            Issue_date=input("Enter the new issue date(dd-mm-yyyy): " )
            global Expiry_date
            Expiry_date=input("Enter the new expiry date(dd-mm-yyyy): " )
            plicense()
            lrechose=yorno("Do you want to go to license menu again(y/n)")
            
        if option==1:
            Issue_date="02-08-2021 "
            Expiry_date="02-08-2022 "
            plicense()
            lrechose=yorno("Do you want to go to license menu again(y/n)")
            
        if option==3:
            print("thank you")
            lrechose="n"
            
#employee menu
def employee():
    erechose="y"
    while erechose=="y":
        print("------------------------------")
        print("  ------EMPLOYEE MENU ----- ")
        print("------------------------------")
        print("      1.Details             ")
        print("      2.Salary              ")
        print("      3.Exit                 ")
        print("------------------------------")
        print("------------------------------")
        import mysql.connector
        import pandas as pd
        global estatus
             
        mydb=mysql.connector.connect(host='localhost',user='root',passwd='tk47@tk47')
            
        mycursor=mydb.cursor()

        connection=mysql.connector.connect(host=' localhost',database='supermarket',user=' root',passwd='tk47@tk47')
        mycursor.execute('use supermarket;')
        
        option=int(in_number("Enter the required option: "))
        
        if option==1:
            empno=int(in_number("Enter the Employee Number: "))
            mycursor.execute("SELECT salary from employee where E_empno='%s';" %empno)
            sal_result= mycursor.fetchall()
            for x in sal_result:
                emp_sal=x[0]
            mycursor.execute("SELECT * from employee where E_empno='%s';" %empno)
            myresult = mycursor.fetchall()
            emp= pd.DataFrame(myresult,columns=['empno','Name','Nationality','Age','Salary','Contactno'])
            print(emp)
            erechose=yorno("Do you want to go to the Employee Menu again (y/n); ")
        
        elif option==2:
            empno=int(in_number("Enter the Employee Number: "))
            mycursor.execute("SELECT salary from employee where E_empno='%s';" %empno)
            sal_result= mycursor.fetchall()
            for x in sal_result:
                emp_sal=x[0]
            reloop="y"
            while reloop=="y":
                #name=input("Enter the employee name: ")
                mycursor.execute("SELECT E_empno from employee;")
                myresult = mycursor.fetchall()
                estatus= "N"
                from datetime import date
                import datetime
                today = date.today()
                    
                for x in myresult:
                    if x[0]==empno:
                       estatus= "Y"
                       mycursor.execute( "select empno,month,year,amount_paid,amount_left,status from salary where empno='%s';"%empno)
                       myresult = mycursor.fetchall()
                       sal= pd.DataFrame(myresult,columns=['Empno','Month','year','amount_paid','amount_left','status'])
                       print(sal)
                       month=input("Enter the month here: ")
                       year=int(in_number("Enter the year here: "))
                       datetime_object = datetime.datetime.strptime(month, "%b")
                       month_number = datetime_object.month
                       mycursor.execute("SELECT * from salary where month='%s' and year=%s and empno=%s;"%(month,year,empno))
                       myresult1 = mycursor.fetchall()
                       length=len(myresult1)
                       if length==1:
                           mycursor.execute("SELECT amount_paid from salary where month='%s' and year=%s and empno=%s;"%(month,year,empno))
                           y= str(mycursor.fetchall())
                           y=y.replace(',', '')
                           y=y.replace(')', '')
                           y=y.replace('(', '')
                           y=y.replace(']','')
                           y=y.replace('[','')
                           amount=int(in_number("Enter the amount to be paid"))
                           while int(y)+amount>emp_sal:
                               print("Amount exceeds salary limit,please try again")
                               amount=int(in_number("Enter the amount to be paid"))
                           if int(y)<emp_sal:
                               mycursor.execute("update salary set amount_paid=amount_paid+%s,amount_left= %s-amount_paid where month=%s and year=%s and empno=%s",(amount,emp_sal,month,year,empno))
                               mycursor.execute("commit;")
                           else:
                               print("you have aldready paid the salary")
                           
                           mycursor.execute("SELECT amount_left from salary where month='%s' and year=%s and empno='%s';"%(month,year,empno))
                           y= str(mycursor.fetchall())
                           y=y.replace(',', '')
                           y=y.replace(')', '')
                           y=y.replace('(', '')
                           y=y.replace(']','')
                           y=y.replace('[','')
                           
                           if int(y)==0:
                               mycursor.execute("update salary set status ='fully paid' where month='%s' and year=%s and empno='%s';" %(month,year,empno) )
                               mycursor.execute("commit;")
                           elif int(y)==emp_sal:
                               mycursor.execute("update salary set status ='unpaid' where month='%s' and year=%s and empno='%s';" %(month,year,empno) )
                               mycursor.execute("commit;")
                           else:
                               mycursor.execute("update salary set status ='partially paid' where month='%s' and year=%s and empno='%s';" %(month,year,empno) )
                               mycursor.execute("commit;")
                           erechose=yorno("Do you want to go to the Employee Menu again (y/n); ")    
                               
                       if length==0:
                           amount=int(in_number("Enter the amount to be paid"))
                           amount_left=emp_sal-amount
                           if amount_left==0:
                               status="unpaid"
                           elif amount_left>0 and amount_left<emp_sal:
                               status="partial paid"
                           else:
                               status="full paid"
                           mycursor.execute("insert into salary(empno,month,year,amount_paid,amount_left,status,paid_date,month_num) values(%s,%s,%s,%s,%s,%s,%s,%s);",(empno,month,year,amount,amount_left,status,today,month_number))
                           mycursor.execute("commit;")
                           erechose=yorno("Do you want to go to the Employee Menu again (y/n); ")
                if estatus=="Y":
                    break
                else:
                    print("Not an employee")
                    reloop=yorno("Do you want to try again(y/n): ")
                    
        elif option==3:
            estatus="n"
            print("thank you")
            break
#inventory menu -it helps to buy products and see sales and profits
def inventory():
    irechose="y"
    while irechose=="y":
        print("------------------------------")
        print("  ------INVENTORY MENU ----- ")
        print("------------------------------")
        print("     1.Sales            ")
        print("     2.Profits          ")
        print("     3.Add product      ")
        print("     4.Buy products     ")
        print("     5.Exit             ")
        print("------------------------------")
        print("------------------------------")
        
        import mysql.connector
        import pandas as pd
             
        mydb=mysql.connector.connect(host='localhost',user='root',passwd='tk47@tk47')
            
        mycursor=mydb.cursor()

        connection=mysql.connector.connect(host=' localhost',database='supermarket',user=' root',passwd='tk47@tk47')

        ioption=int(in_number("enter the required option: "))
        mycursor.execute('use supermarket;')
        if ioption==1:
            iloop="y"
            while iloop=="y":
                qnsid=in_number("enter the product id here: ")
                mycursor.execute("SELECT pid,product,unit_price,sold_qty,sales_value FROM supermarket where pid='%s';"%qnsid)
                myresult=mycursor.fetchall()
                emp= pd.DataFrame(myresult,columns=['PID','Product Name','Unit Price','Sold_Quantity','Sales value'])
                print(emp)
                for x in myresult:
                    print("No of units sold:",x[3])
                    print("Value of sales:",x[4],"dhs")
                iloop=yorno("Do you want to check for another product's sales(y/n):")
                if iloop=="n":
                    break
            irechose=yorno("Do you want to go to the Inventory Menu again (y/n); ")
        if ioption==2:
             iloop="y"
             while iloop=="y":
                qnsid=in_number("enter the product id here: ")
                mycursor.execute("SELECT pid,product,unit_price,sold_qty,inventory_value,sales_value FROM supermarket where pid='%s';"%qnsid)
                myresult=mycursor.fetchall()
                emp= pd.DataFrame(myresult,columns=['PID','Product Name','Unit Price','Sold_Quantity','Inventory Value','Sales value'])
                print(emp)
                for x in myresult:
                    profit=x[5]-x[4]*x[3]
                    print("Profits from this product is",profit,'dhs')
                    
                iloop=yorno("Do you want to check for another product's profit(y/n):")
                if iloop=="n":
                    break
             irechose=yorno("Do you want to go to the Inventory Menu again (y/n); ")

        if ioption==3:
             iloop="y"
             while iloop=="y":
                 newpid=input("enter the new product id here: ")
                 mycursor.execute("SELECT pid FROM supermarket where pid='%s';"%newpid)
                 myresult=mycursor.fetchall() 
                 if len(myresult)==0:
                     break
                 else:
                     print("id aldready exsists")
                     iloop=yorno("do you want to try again(y/n)")
                     if iloop=='n':
                         break
             if iloop=="n":
                 exit()
                 
             
             iloop="y"
             while iloop=="y":
                 newname=input("enter the new product name here")
                 mycursor.execute("SELECT pid FROM supermarket where product='%s';"%newname)
                 myresult=mycursor.fetchall() 
                 if len(myresult)==0:
                     break
                 else:
                     print("name aldready exsists")
                     iloop=yorno("do you want to try again(y/n)")
                     if iloop=='n':
                         break
             if iloop=="n":
                 exit()
            
             category=input("Enter the category here: ")
             unit_price=int(in_number("Enter the unit price here: "))
             zero=0
             inventory=int(in_number("Enter the inventory value here: "))
             print("new product is added")
             irechose=yorno("Do you want to go to the Inventory Menu again (y/n); ")
             
             mycursor.execute("insert into supermarket(pid,product,category,unit_price,Purchased_Qty,sold_qty,inventory_value,sales_value,remaining_stock) values(%s,%s,%s,%s,%s,%s,%s,%s,%s);",(newpid,newname,category,unit_price,zero,zero,inventory,zero,zero))
             mycursor.execute("commit;")
            
        if ioption==4:
             iloop="y"
             xloop="y"
             while iloop=="y":
                 while xloop=="y":
                     pid=in_number("enter product id here: ")
                     mycursor.execute("SELECT pid,unit_price,inventory_value FROM supermarket where pid='%s';"%pid)
                     myresult=mycursor.fetchall()
                     from datetime import date
                     today = date.today()
                     for x in myresult:
                         unit_price=x[1]
                         inventory_value=x[2]
                         
                         
                     if len(myresult)==1:
                         quantity=int(in_number("Enter the quantity of product bought"))
                         total_cost=quantity*inventory_value
                         sales_value=quantity*unit_price
                         mycursor.execute("update supermarket set Purchased_Qty=Purchased_Qty+%s,remaining_stock=remaining_stock+%s where pid=%s;",(quantity,quantity,pid))
                         mycursor.execute("insert into inventory_log(inv_pid,qty_bought,total_cost,value_of_product,transaction_date) values(%s,%s,%s,%s,%s);",(pid,quantity,total_cost,sales_value,today))
                         mycursor.execute("commit;")
                         print("The product has been purchased")
                         break
                     else:
                         print("id doesnt exsist")
                         iloop=yorno("do you want to try again(y/n): ")
                         if iloop=='n':
                             break
                 xloop=yorno("Do you want to buy another product(y/n); ")
                 if xloop=='n':
                             break
                 
             if iloop=="n":
                 exit()
        #irechose=yorno("Do you want to go to the Inventory Menu again (y/n); ")
        if ioption==5:
            exit()
                             
        
#Takes input product codes and quantites , calculates the amount and prints invoice
def bill():
    import mysql.connector
    import pandas as pd
     
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='tk47@tk47')
    
    mycursor=mydb.cursor()

    connection=mysql.connector.connect(host=' localhost',database='supermarket',user=' root',passwd='tk47@tk47')
    print("Billing")
    import pandas as pd
    sql='select * from supermarket'
    df=pd.read_sql(sql,connection)
    mycursor.execute('commit')
    #print(df)

    mycursor.execute('use supermarket;')
    #mycursor.execute('select * from billing;')

    mbill=[]
    while True:
        print(" _______________________")
        print("|       options         |")
        print("| 1.Enter the product ID|")
        print("| 2.Scan the Barcode    |")
        print("|_______________________|")
        ask=in_number("Chose the option: ")
        
        
        if ask==1:
            pcode=in_number("Enter the product code:  ")
        elif ask==2:
            print("Scan the barcode")
            pcode=barcode()
            print(pcode)
        
        mycursor.execute("SELECT remaining_stock FROM supermarket where pid='%s';" %pcode)
        myresult = mycursor.fetchall()
        #aqty=0;
        
        for x in myresult:
            y=list(x)
            aqty=y[0]
        while True:         
            pno=int(input("Enter the quantity:  "))
            if pno<=aqty:
                break
            else:
                print("The Entered quantity is greater than available quantity :",aqty)
                continue
        mycursor.execute("update supermarket set qty=%s where pid=%s;",(pno,pcode))
        mycursor.execute("SELECT product,unit_price,Purchased_Qty,pid,qty FROM supermarket where pid='%s';" %pcode)        
        myresult = mycursor.fetchall()
        mbill=mbill+myresult
        #updation of main table
        mycursor.execute("update supermarket set sold_qty=sold_qty+%s,remaining_stock=remaining_stock-%s,sales_value=sales_value+unit_price*%s where pid=%s;",(pno,pno,pno,pcode))
        #mycursor.execute("commit;") 

      
        qns=yorno("Do you want to add an item(y/n): ")
        if qns=="y":
            continue
        else:
            break
    from datetime import date
    today = date.today()
    
    import time
    t = time.strftime("%I:%M %p")

    mycursor.execute("select ifnull(max(billno),0)+1 from billmain;")
    tbillno=str(mycursor.fetchone())
    tbillno = tbillno.replace(',', '')
    tbillno = tbillno.replace(')', '')
    tbillno = tbillno.replace('(', '')
    import datetime
    y=str(today)
    a = datetime.datetime.strptime(y,"%Y-%m-%d") 
    #mycursor.execute('INSERT INTO billmain (billno,bdate,bamount,bvat,buser,btime) VALUES(%s,%s,%s,%s,%s,%s)', (int(tbillno),a.strftime('%Y-%m-%d'),total,vat,guser,t))
    mycursor.execute('INSERT INTO billmain (billno,bdate,buser,btime) VALUES(%s,%s,%s,%s)', (int(tbillno),a.strftime('%Y-%m-%d'),guser,t))
    
    
    seq=1
    print("___________________________________________________")
    print("               FreshCo Supermarket            ")
    print("                   Salam Road                 ")
    print("              Near Old Etisalat Blg,          ")
    print("                 Fujairah , UAE               ")
    print("              Telephone: 09-4747345           ")
    print("____________________________________________________")
    print("                                             ")
    print("                                             ")
    print("                   INVOICE                   ")
    print("Date:",today,"             Time:",t)
    print()
    

    print("------------------------------------------------------")
    print("No Product          Qty      Price      Amount")
    print("------------------------------------------------------")
    vat=0
    global total
    total=0
    for x in mbill:
        print('{:2d} {:15s}  {:3d} {:10.2f} {:10.2f}'.format(seq,x[0],x[4],x[1],int(x[1])*(x[4])))
        #print(seq ,'\t',x[0],'\t',float(pno),'\t',float(x[1]),'\t',' ',float(int(x[1])*pno))
        total+=int((x[1])*(x[4]))    
        seq+=1
        mycursor.execute('INSERT INTO billsub (sbillno,spcode,sqty,sprice) VALUES(%s,%s,%s,%s)', (int(tbillno),x[3],x[4],x[1]))
        mycursor.execute("commit;")
    print("-------------------------------------------------------")
    vat=total*0.05
    vat=round(vat,2)
    
    #print("VAT",'{:44.2f}'.format(vat))
    print("                                       Total:",total)
    print("                                        VAT:",vat)
    print("                                Grand Total:,",total+vat)
    print("---------------------------------------------------------")
    mycursor.execute('UPDATE billmain set bamount = %s, bvat=%s where billno=%s;',(total,vat,int(tbillno)))
    mycursor.execute("commit;")

def createuser():
    import mysql.connector
    import pandas as pd
     
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='tk47@tk47')
    
    mycursor=mydb.cursor()

    connection=mysql.connector.connect(host=' localhost',database='supermarket',user=' root',passwd='tk47@tk47')
    mycursor.execute("use supermarket;")
    recreate="y"
    while recreate=="y":
        nuser_name=input("Enter the new user name: ")
        #mycursor.execute("SELECT user_name FROM user_login where user_name='%s';" %nuser_name)
        mycursor.execute("SELECT user_name FROM user_login;")
        myresult = mycursor.fetchall()
        x=tuple([nuser_name])
        if x in myresult:
            print("User aldready exsists")
            recreate=yorno("Do you want to re-enter the username(y/n): ")
            if recreate=="y":
                continue
            if recreate=="n":
                break
            
            
        nusertype=input("Enter the user type(admin/user): ")
        repass="y"
        while repass=="y":
            nuser_pass1=input("Enter the new password: ")
            nuser_pass2=input("Renter the password: ")
            if  nuser_pass1 != nuser_pass2:
                print("Password does not match")
                repass=yorno("Do you want to re-enter the password(y/n): ")
            else:
                mycursor.execute("insert into user_login values( %s,%s ,%s);",(nuser_name,nuser_pass2,nusertype))
                mycursor.execute("commit;")
                break
        recreate=yorno("Do you want to create another user(y/n) :")    
       
#helps to create new usernames and passwords for using this program  
def createuser_dup():
    import mysql.connector
    import pandas as pd
     
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='tk47@tk47')
    
    mycursor=mydb.cursor()

    connection=mysql.connector.connect(host=' localhost',database='supermarket',user=' root',passwd='tk47@tk47')
    mycursor.execute("use supermarket;")
    recreate="y"
    while recreate=="y":
        nuser_name=input("Enter the new user name: ")
        #mycursor.execute("SELECT user_name FROM user_login where user_name='%s';" %nuser_name)
        mycursor.execute("SELECT user_name FROM user_login;")
        myresult = mycursor.fetchall()
        x=tuple([nuser_name])
        if x in myresult:
            print("User aldready exsists")
            recreate=yorno("Do you want to re-enter the username(y/n): ")
            if recreate=="y":
                continue
            if recreate=="n":
                break
            
            
        nusertype=input("Enter the user type(admin/user): ")
        repass="y"
        while repass=="y":
            nuser_pass1=input("Enter the new password: ")
            nuser_pass2=input("Renter the password: ")
            if  nuser_pass1 != nuser_pass2:
                print("Password does not match")
                repass=yorno("Do you want to re-enter the password(y/n): ")
            else:
                mycursor.execute("insert into user_login values( %s,%s ,%s);",(nuser_name,nuser_pass2,nusertype))
                mycursor.execute("commit;")
                break
        recreate=yorno("Do you want to create another user(y/n) :")    

#data analysis module
def analysis():
    import mysql.connector
    import pandas as pd
            
                 
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='tk47@tk47')
                
    mycursor=mydb.cursor()

    connection=mysql.connector.connect(host=' localhost',database='supermarket',user=' root',passwd='tk47@tk47')
    aloop='y'
    while aloop=='y':
        print("---------------------------------------------------------------------")
        print("  ------------------------ANALYSIS MENU ------------------------- ")
        print("---------------------------------------------------------------------")
        print("    1.Top 5 most and least sold items in the shop                   ")
        print("    2.Total sales in a day                                          ")
        print("    3.No of products in shop                                        ")
        print("    4.To check the total history of a product in a inventory        ")
        print("    5.To arrange the products in alphabetical order                 ")
        print("    6.Employee details                                              ")
        print("    7.To sort and extract the products by category                  ")
        print("    8.Highest Priced and lowest priced products in the shop         ")
        print("    9.Extracting specific columns and records                       ")
        print("    10.Exit                                                         ")
        print(" --------------------------------------------------------------------")
        print(" --------------------------------------------------------------------")        
        achoose=in_number('Choose an option: ')
        print("------------------------------")
        print("   DATA ANALYSIS")
        print("------------------------------")
        if achoose==1:
            #1 Top 5 most and least sold items in the shop
            mycursor.execute('use supermarket;')
            mycursor.execute("SELECT pid,product,unit_price,sold_Qty,sales_value FROM supermarket;")
            myresult=mycursor.fetchall()
            df1= pd.DataFrame(myresult,columns=['PID','Product Name','Unit Price','Sold_Quantity','Sales value'])
            ddf1=df1.sort_values(by='Sold_Quantity',ascending=0)
            print('This are the top 5 most sold items in the shop')
            print(ddf1.head(5))
            print("..............................................")
            ddf1=df1.sort_values(by='Sold_Quantity',ascending=1)
            print('This are the top 5 least sold items in the shop')
            print(ddf1.head(5))
            print("..............................................")
        elif achoose==2:
            #2 total sales in a day
            mycursor.execute('use supermarket;')
            mycursor.execute("SELECT bdate FROM billmain group by bdate order by bdate desc;")
            myresult=mycursor.fetchall()
            df2=pd.DataFrame(myresult, columns=['Bill_Date'])
            loop='y'
            while loop=='y':
                qns=str(input("Enter the required date(yyyy-mm-dd): "))
                if qns in str(df2['Bill_Date']):
                    mycursor.execute("SELECT sum(bamount) FROM billmain where bdate='%s';"%(qns))
                    am=str(mycursor.fetchall())
                    am=am.replace(',', '')
                    am= am.replace(')', '')
                    am= am.replace('(', '')
                    am=am.replace(']','')
                    am=am.replace('[','')
                    print('The total amount of sales on',qns,'is',am,'dhs')
                    print("..............................................")
                    loop='n'
                    break
                else:
                    print('Incorrect date/Date not there in database')
                    lqns=yorno('Do you want to try again(y/n): ')
                    if lqns=='y':
                        loop='y'
                    else:
                        break
        elif achoose==3:
            mycursor.execute('use supermarket;')
            mycursor.execute("SELECT pid FROM supermarket;")
            myresult=mycursor.fetchall()
            df3=pd.DataFrame(myresult, columns=['Product_numbers'])
            print('The numbers of produtcs in the supermarket is',int(df3.count()))
            print("................................................................")
        elif achoose==4:     
            loop='y'
            while loop=='y':
                mycursor.execute('use supermarket;')
                qns=in_number('Enter a product id to check product history')
                mycursor.execute("SELECT Inv_pid FROM inventory_log where Inv_pid='%s';"%(qns))
                myresult=mycursor.fetchall()
                if len(myresult)==0:
                    print('Incorrect id/Id not there in database')
                    lqns=yorno('Do you want to try again(y/n): ')
                    if lqns=='y':
                        loop='y'
                    else:
                        break
                
                else:
                    df4=pd.DataFrame(myresult,columns=['Inv_pid'])
                    x1=df4.groupby('Inv_pid')
                    y1=pd.DataFrame(x1.size().reset_index(name ="Group_Count"))
                    mycursor.execute("select Inv_pid,sum( Qty_bought),sum(total_cost),sum(value_of_product) from inventory_log where Inv_pid='%s';"%(qns))
                    myresult=mycursor.fetchall()
                    df5=pd.DataFrame(myresult)
                    print('The product id is :',qns)
                    print('The number of times the transaction has took place:',int(y1['Group_Count']))
                    print('The number of units of product bought: ',int(df5[1]))
                    print('The total value of product bought: ',int(df5[2]),'dhs')
                    print('The total sales value: ',int(df5[3]),'dhs')
                    print("...................................................................")
                    break
        elif achoose==5:
            #5 To arrange the products in alphabetical order 
            mycursor.execute('use supermarket;')
            mycursor.execute("SELECT pid,product,unit_price,sold_Qty,sales_value FROM supermarket;")
            myresult=mycursor.fetchall()
            df1= pd.DataFrame(myresult,columns=['PID','Product_Name','Unit_Price','Sold_Quantity','Sales_value'])
            qns=input('Ascending(a) or Descending(d)?: ')
            loop='y'
            while loop=='y':
                if qns in ('a','d','ascending','descending'):
                    if qns == 'ascending' or qns=='a':
                        print(df1.sort_values('Product_Name',ascending=1))
                        print("..............................................")
                        break
                    else:
                         print(df1.sort_values('Product_Name',ascending=0))
                         print("..............................................")
                         break
                else:
                    print('Incorrect option')
                    lqns=yorno('Do you want to try again(y/n): ')
                    if lqns=='y':
                        loop='y'
                    else:
                        break

            
        elif achoose==6:
            #6 Employee details (interration and set_index)
            mycursor.execute('use supermarket;')
            mycursor.execute("SELECT * from employee;")
            myresult=mycursor.fetchall()
            df6=pd.DataFrame(myresult, columns=['ENo','Name','Nationality','Age','Salary','ContactNo'])
            df6.set_index('Name',inplace=True)
            for (row,rowseries) in df6.iterrows():
                print('Name:', row)
                print('Details')
                print(rowseries)
                print("..............................................")
        elif achoose==7:
            #7 To get the products from cateogory 
            mycursor.execute('use supermarket;')
            mycursor.execute("select product,category, unit_price from supermarket;")
            myresult=mycursor.fetchall()
            df7= pd.DataFrame(myresult,columns=['Product_Name','Category','Unit_Price'])
            qns=input('Enter the required category: ')
            x=df7['Product_Name'].where(df7['Category']==qns)
            print('The products in the category',qns)
            for y in x :
                if len(str(y))==3:
                    continue
                else:
                    print(y)
        elif achoose==8:
            #8 Costliest and least costly products in shop
            mycursor.execute('use supermarket;')
            mycursor.execute("SELECT product,unit_price FROM supermarket;")
            myresult=mycursor.fetchall()
            df8= pd.DataFrame(myresult)
            loop='y'
            while loop=='y':
                qns=input('Maximum priced(max) or minimum priced prduct(min)')
                if qns =='max':
                    x=df8.max()
                    print('The maximum priced product is',x[0],'its price is',x[1],'dhs')
                    print("..............................................................")
                    break
                elif qns=='min':
                    y=df8.min()
                    print('The minimum priced product is',y[0],'its price is',y[1],'dhs')
                    print("..............................................................")
                    break
                else:
                    print('Incorrect Option')
                    lqns=yorno('Do you want to try again(y/n): ')
                    if lqns=='y':
                        loop='y'
                    else:
                        break
        elif achoose==9:
            #9 Extracting some specific rows and records from the dataframe

                mycursor.execute('use supermarket;')
                mycursor.execute("SELECT pid,product,unit_price,sold_Qty,sales_value FROM supermarket;")
                myresult=mycursor.fetchall()
                df9= pd.DataFrame(myresult,columns=['PID','Product_Name','Unit_Price','Sold_Quantity','Sales_value'],index=[x for x in range(1,26)])
                print(df9)
                loop='y'
                while loop=='y':
                    qns=input('Name based(n) or postion based(p) extracting:')
                    if qns=='p' or qns=='P':
                        startrp=int(in_number('Enter the starting row position'))
                        endrp=int(in_number('Enter the ending row position'))
                        startcp=int(in_number('Enter the starting column position'))
                        endcp=int(in_number('Enter the ending column position'))
                        print(df9.iloc[startrp:endrp+1,startcp:endcp+1])
                        print("..............................................................")
                    elif qns=='n' or qns=='N':
                        startrn=int(input('Enter the starting row name'))
                        endrn=int(input('Enter the ending row name'))
                        startcn=str(input('Enter the starting column name'))
                        endcn=str(input('Enter the ending column name'))
                        print(df9.loc[startrn:endrn,startcn:endcn])
                        print("..............................................................")
                    loop=yorno('Do you want to extract again(y/n): ')
        elif achoose==10:
            print('Thank you')
            break
        else:
            print('Incorrect option')
            lqns=yorno('Do you want to try again(y/n): ')
            if lqns=='y':
                aloop='y'
            else:
                break
        aqns=yorno('Do you want to go to analysis menu(y/n): ')
        if aqns=='y':
            aloop=='y'
        else:
            break
        
#csv convertion    
def convert():
    print("------------------------------")
    print("  CSV CREATION")
    print("------------------------------")
    import mysql.connector
    import pandas as pd
     
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='tk47@tk47')

    mycursor=mydb.cursor()
    loop='y'
    while loop=='y':
         mycursor.execute("use supermarket;")
         mycursor.execute("show tables;")
         tables = mycursor.fetchall()
         df1=pd.DataFrame(tables,columns=['Names'],index=[1,2,3,4,5,6,7])
         print(df1.drop([7],axis=0))
         
         tno=in_number('Choose the table you want to convert')
         if tno==1:
             mycursor.execute('SELECT * FROM billmain;')
             table_rows = mycursor.fetchall()
             billmaindf = pd.DataFrame(table_rows,columns=['billno' ,'bdate','bamount','bvat','buser','btime'])
             print(billmaindf)
             qns=str(input('Enter the name of csv: '))
             qns=qns+'.csv'
             print(qns)
             billmaindf.to_csv(r"C:\Users\TashinTanim\Desktop\csv\%s"%qns,index=True )
             
         elif tno==2:
             mycursor.execute('SELECT * FROM billsub;')
             table_rows = mycursor.fetchall()
             billsubdf = pd.DataFrame(table_rows,columns=['sbillno','spcode','sqty','sprice'])
             print(billsubdf)
             qns=str(input('Enter the name of csv: '))
             qns=qns+'.csv'
             print(qns)
             billsubdf.to_csv(r"C:\Users\TashinTanim\Desktop\csv\%s"%qns,index=True )
        
         elif tno==3:
             mycursor.execute('SELECT * FROM employee;')
             table_rows = mycursor.fetchall()
             employdf = pd.DataFrame(table_rows,columns=['E_empno','Name','Nationality','Age','Salary','ContactNo'])
             print(employdf)
             qns=str(input('Enter the name of csv: '))
             qns=qns+'.csv'
             print(qns)
             employdf.to_csv(r"C:\Users\TashinTanim\Desktop\csv\%s"%qns,index=True )
    
         elif tno==4:
             mycursor.execute('SELECT * FROM inventory_log;')
             table_rows = mycursor.fetchall()
             inventdf = pd.DataFrame(table_rows,columns=['Inv_pid','Qty_bought','total_cost','value_of_product','Transaction_date'])
             qns=str(input('Enter the name of csv: '))
             qns=qns+'.csv'
             print(qns)
             inventdf.to_csv(r"C:\Users\TashinTanim\Desktop\csv\%s"%qns,index=True )
             
         elif tno==5:
             mycursor.execute('SELECT * FROM salary;')
             table_rows = mycursor.fetchall()
             saldf = pd.DataFrame(table_rows,columns=['empno','month','year','salary_amount','amount_paid','amount_left','status','paid_date','month_num'])
             print(saldf)
             qns=str(input('Enter the name of csv: '))
             qns=qns+'.csv'
             print(qns)
             saldf.to_csv(r"C:\Users\TashinTanim\Desktop\csv\%s"%qns,index=True )
             
         elif tno==6:
             mycursor.execute("SELECT * FROM supermarket;")
             myresult=mycursor.fetchall()
             supdf= pd.DataFrame(myresult,columns=['PID','Product Name','Category','Unit Price','Purchased_qty','Sold_Quantity','Inventory_Value','Sales value','Remaining_stock'])
             print(supdf )
             qns=str(input('Enter the name of csv: '))
             qns=qns+'.csv'
             print(qns)
             supdf.to_csv(r"C:\Users\TashinTanim\Desktop\csv\%s"%qns,index=True )
         else:
             print('Incorrect Table/Table not there in database')
             lqns=yorno('Do you want to try again(y/n): ')
             if lqns=='y':
                 loop='y'
             else:
                 break
         print('Please check the folder in the desktop to find the csv you created')
         loop=yorno('Do you want to convert another table(y/n): ')
         
#data visualization
def graphs():
    import mysql.connector
    import pandas as pd
    import matplotlib.pyplot as plt
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='tk47@tk47')
    mycursor=mydb.cursor()
    
    connection=mysql.connector.connect(host=' localhost',database='supermarket',user=' root',passwd='tk47@tk47')
    loop='y'
    while loop=='y':
        print("-------------------------------------------------------")
        print(" ---------------VISUALIZATION MENU ------------------ ")
        print("-------------------------------------------------------")
        print("    1. Sales graph for month of December (line graph)")
        print("    2.Dec 2021 vs Jan 2021 sales graph (double-line) ")
        print("    3.Top selling Products in the supermarket (bar)  ")
        print("    4.Most in demand meat products (horizontal bar)  ")
        print("    5.Inventory Price vs Sales Price(histogram)      ")
        print("    6.Sales price of all the products(histogram)     ")
        print("    7.Exit                                           ")
        print(" ------------------------------------------------------")
        print(" ------------------------------------------------------")
        
        voption=in_number("Choose an option : ")
        if voption==1:
            #Sales graph for month of December (line graph)
            amount=[]
            date=[]
            mycursor.execute("use supermarket;")
            mycursor.execute("select bdate,sum(bamount) from billmain where bdate between '2021-12-01' and '2021-12-31'group by bdate;")
            table_rows = mycursor.fetchall()
            df = pd.DataFrame(table_rows,columns=['Date','Amount'])

            for x in df['Date']:
                date.append(x)
            for x in df['Amount']:
                amount.append(x)
                
            plt.plot(date,amount,label='sales')
            plt.title("Sales Graph of Shop for the Month of December")
            plt.xlabel('Dates')
            plt.ylabel('Sales amount')
            plt.legend()
            plt.show()
        elif voption==2:
            #Dec 2021 vs Jan 2021 sales graph (double-line)
            amount=[]
            date=[]
            mycursor.execute("use supermarket;")
            mycursor.execute("select bdate,sum(bamount) from billmain where bdate between '2021-12-01' and '2021-12-12'group by bdate;")
            table_rows = mycursor.fetchall()
            df = pd.DataFrame(table_rows,columns=['Date','Amount'])

            for x in df['Date']:
                date.append(x)
            for x in df['Amount']:
                amount.append(x)
                
            amount2=[]
            date2=[]
            mycursor.execute("select bdate,sum(bamount) from billmain where bdate between '2022-01-01' and '2022-01-12'group by bdate;")
            table_rows = mycursor.fetchall()
            df= pd.DataFrame(table_rows,columns=['Date','Amount'])
            for x in df['Amount']:
                amount2.append(x)
            for y in range(1,13):
                date2.append(y)
            plt.plot(date2,amount,linestyle='-',linewidth=2,color='crimson',label='december')
            plt.plot(date2,amount2,linestyle=':',linewidth=2,color='blue',label='january')
            plt.title("December 2021 Sales vs January 2022 Sales (first 12 days) ")
            plt.xlabel('Dates')
            plt.ylabel('Sales amount(in dhs)')
            plt.legend()
            plt.show()

            
            
        elif voption==3:
            #3 Top selling Products in the supermarket
            mycursor.execute("use supermarket;")
            mycursor.execute('select category,max(sales_value) from supermarket group by category;')
            table_rows = mycursor.fetchall()
            df = pd.DataFrame(table_rows,columns=['category','sales_value'])
            name=[]
            for x in df['category']:
                name.append(x)
            price=[]
            for y in df['sales_value']:
                price.append(y)  
            c1=['darkkhaki','coral','sienna','peru','tomato','brown','darksalmon']
            plt.bar(name,price,color=c1)
            plt.title("Sales Revenue generated by each category")
            plt.xlabel('Categories')
            plt.ylabel('Amount(in dhs)')
            plt.show()

            
            
        elif voption==4:
            #4 Most in demand meat products
            mycursor.execute("use supermarket;")
            mycursor.execute("select product,sold_Qty from supermarket where category='meat';")
            table_rows = mycursor.fetchall()
            df = pd.DataFrame(table_rows,columns=['product','sold_Qty'])
            name=[]
            for x in df['product']:
                name.append(x)
                print(name)

            price=[]
            for y in df['sold_Qty']:
                price.append(y)
                print(price)
            c=['blue','yellow','green','red']
            plt.barh(name,price,color=c)
            plt.title("Most in-demand Meat products ")
            plt.xlabel('No of units sold')
            plt.ylabel('Meats')
            plt.show()

            
        elif voption==5:
            #5 Inventory Price vs Sales Price by categories
            mycursor.execute("use supermarket;")
            mycursor.execute("select category,sum(unit_price),sum(inventory_value) from supermarket group by category;")
            table_rows = mycursor.fetchall()
            df =pd.DataFrame(table_rows,columns=['cat','Unit','inv'])

            inv=[]
            for y in df['inv']:
                inv.append(int(y))

            unit=[]
            for y1 in df['Unit']:
                unit.append(int(y1))

            cat=[]
            for x in df['cat']:
                cat.append(x)
            print(cat)
            data={'Category':cat,'Inventory_Value':inv,'Sales_price':unit}
            df1=pd.DataFrame(data)
            df1.plot(kind='bar')
            plt.xlabel('Categories- 0.Cleaning  1.Food  2.Canned  3.Packed  4.Dairy  5.Meat   6.Drinks')
            plt.ylabel('Price(in dhs)')
            plt.xticks()
            plt.yticks()
            plt.legend()
            plt.title('Inventory_Value vs Sales_Price')
            plt.show()

            
        
        elif voption==6:
            #6 Sales price of all the products in the Shop
            mycursor.execute("use supermarket;")
            mycursor.execute("select unit_price from supermarket ;")
            table_rows = mycursor.fetchall()
            df = pd.DataFrame(table_rows,columns=['Amount'])
            a=[]
            for x in df['Amount']:
                a.append(int(x))
            print(a)
            plt.hist(a,bins=[0,5,10,15,20,25,30,35,40,45],facecolor='powderblue',edgecolor='orchid')
            plt.title('Price range the products in the Shop')
            plt.xlabel('Price range(in dhs)')
            plt.ylabel('no of prodcuts') 
            plt.show()

            
            
        elif voption==7:
            print('Thank you')
        else:
             print('Incorrect Table/Table not there in database')
             lqns=yorno('Do you want to try again(y/n): ')
             if lqns=='y':
                 loop='y'
             else:
                 break

        loop=yorno('Do you want to go into the visualization menu again: ')  

#Main login menu
def login():
    opening()
    import mysql.connector
    import pandas as pd
         
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='tk47@tk47')
        
    mycursor=mydb.cursor()

    connection=mysql.connector.connect(host=' localhost',database='supermarket',user=' root',passwd='tk47@tk47')


    mycursor.execute("use supermarket;")
    #mycursor.execute("SELECT user_pass FROM user_login where user_name='%s';" %tuser)
    mycursor.execute("SELECT user_name,user_pass,usertype FROM user_login;")
    myresult = mycursor.fetchall()


    reuser="y"
    while reuser=="y":
        tuser=input("Enter username: ")
        global guser
        guser = tuser
        for x in myresult:
            if x[0]==tuser:
                upass=x[1]
                utype=x[2]
                print("User name is correct")
                reuser="n"
                break
            
        else:
            print("User name is not correct")
            reuser=yorno("Do you want to try again(y/n): ")
     
    repass="y"  
    while repass=="y":
        tpass=input("Enter password: ")
        if tpass==upass:
            print("Autheciated")
            repass="n"
            reuser="n"
            break
        else:
            print("incorrect password")
            repass=yorno("Do you want to try again(y/n): ")

    if utype=='admin':
        ownersmenu()
        reoption="y"
        while reoption=="y":
            cqns=in_number("Choose an option: ")
            if cqns==1:
                print("Owners End")
                rechose="y"
                while rechose=="y":
                    owner()
                    option=int(in_number("Enter the required option: "))
                    if option==1:
                        owners_details()
                       
                    elif option==2:
                        license1()
                        
                    elif option==3:
                        createuser()
                        
                    elif option==4:
                        employee()
                        
                    elif option==5:
                        print("Thank you")
                        break

                    
                    rechose=yorno("Do you want to go to the Owner's End Menu again (y/n); ")
                break
            elif cqns==2:
                print("Inventory")
                inventory()
                break
            elif cqns==3:
                bill()

                break
            elif cqns==4:
                analysis()
            elif cqns==5:
                convert()
            elif cqns==6:
                graphs()
            elif cqns==7:
                print("Thank you")
                break
            else:
                print("Invalid syntax")
                reoption=yorno("Do you want to try again(y/n): ")
                continue 
            
    else:
        othersmenu()
        reoption="y"
        while reoption=="y":
            cqns=int(in_number("Choose an option: "))
            if cqns==1:
                print("Inventory")
                inventory()
                break
            elif cqns==2:
                bill()
                break
            elif cqns==3:
                analysis()
            elif cqns==4:
                analysis()
            elif cqns==5:
                graphs()
            elif cqns==6:
                print("Thank you")
                break
            else:
                print("Invalid syntax")
                reoption=yorno("Do you want to try again(y/n): ")
                continue 

login()         
        
