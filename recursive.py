#recursive sum method
def sdigit(y):
    
    r = 0
    for i  in y:
        r = r+int(i)
    if len(str(r))==1:
        return r
    else:
        return sdigit(str(r))
           
    

x,k = input().split()
m = sdigit(x)*int(k)
print(sdigit(str(m)))
