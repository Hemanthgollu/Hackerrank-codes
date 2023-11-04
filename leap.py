# write a function
def is_leap(b):
    leap = False
    if (b%400==0 or (b%4==0 and b%100!=0)):
        leap = True
    # Write your logic here
    
    return leap

year = int(input())
print(is_leap(year))
