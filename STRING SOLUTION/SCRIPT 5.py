#WAS to create 2 udf input() to take input string and call strSymmetric() by passing inputted string.
#strSymmetric() check string is symmetric or not. A string is said to be symmetrical if both the halves of the string are the same.

def strsymmetric(s):
    a=len(s)//2
    p1=s[0:a]
    p2=s[a:]
    if p1==p2:
        print(f"\"{s}\"  Is Symmetircal  String")
    else:
        print(f"\"{s}\"  Is Not Symmetircal String")
def inputs():
       s=input("Enter String:")        
       strsymmetric(s)
inputs()
