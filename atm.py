import datetime
print("Welcome to fbl")
user_pin=1234
balance=10000
print("Insert your ATM card")
print("""
      
      select one of the languages below

      1.English
      2.Kannada
      3.Hindi
      """ 
      )
x=int(input())
if x==1:
    print("selected language is English")
if x==2:
     print("selected language is Kannada")
if x==3:
      print("selected language is Hindi")
pin=input("enter your PIN")
if len(pin)==4:
     if int(pin)==user_pin:
          print( """

                select a option

                1.Withdrawl
                2.Balance
                3.Mini statement
                4.PIN chanage
                5.Deposit
                
                """
               
          
          
          )
     x=int(input())  
     if x==1:
          print("Enter your amount")
          amount=int(input())
          if amount<=balance:
               balance=balance-amount
               print("Take the cash ",amount)
               print("Balance amount is: ",balance)
          else:
               print("Insufficient balance")
     elif x==2:
          print("Available balance is ",balance) 
     elif x==3:
          current_date=datetime.datetime.now().strftime("%d-%m-%y")
          current_time=datetime.datetime.now().strftime("%H:%M:%S")
          print( f"""

           STATE BANK OF INDIA

           date:{current_date}
           time:{current_time}
           Balance:{balance} 

            """
               
          )
     elif x==4:
          user_pin=int(input("set the PIN"))    
     elif x==5:
          print("Enter the amount") 
          deposit=int(input())
          if deposit%100==0:
               print("cash accepted",deposit)
               balance=balance+deposit
               print("Balance amount",balance)
          else:
               print("please give multiples of hundered")