Q=int(int(input("enter the value of Q")))#Q and alpha Public Parameters: available numbers
alpha=int(input("enter the value of alpha"))#Q and alpha Public Parameters: available numbers
Xa=int(input("enter the value of Xa"))#private values
Xb=int(input("enter the value of Xb"))#private values
Ya=pow(alpha,Xa,Q)#public key
print("Alice computed public key is:",Ya)
Yb=pow(alpha,Xb,Q)#public key
print("Bob computed public key is:",Yb)
Ka=pow(Yb,Xa,Q)#shared secrest key
print("Alice computed secret key is:",Ka)
Kb=pow(Ya,Xb,Q)#shared secrest key
print("Bob computed secreat key is:",Kb)
