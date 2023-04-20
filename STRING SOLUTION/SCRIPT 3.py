#Write a script to create a list with 5 string and count total number of string with even number of length with string using UDF

def evenlenstr(l):
    c=0
    for i in range(5):
       n=input("Enter String : ")
       l.append(n)
    print(l)
    for j in l:
       if len(j)%2==0:
          c+=1
          print(j)
    print(f"Total String With Even Length : {c}")
l=[]
evenlenstr(l)
