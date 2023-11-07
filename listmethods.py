#Using list methods in a list
n = int(input())
List = []
for i in range(n):
    action, *line = input().split()
    number_actions = list(map(int, line))
    
    if(action == "append"):
        number_actions[0]       
        List.append(number_actions[0])
        
    elif(action == "insert"):
        List.insert(number_actions[0],number_actions[1])
        
    elif(action == "remove"):
        List.remove(number_actions[0])
        
    elif(action == "pop"):
        List.pop()
        
    elif(action == "sort"):
        List.sort()
    
    elif(action == "reverse"):
        List.reverse()
    
    elif(action == "print"):
        print(List)
