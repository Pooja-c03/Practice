counter = 0
str = "[()()]"

for p in str:
    if p == '(':
        counter +=1
    elif p == ')':
        counter -=1
    if counter < 0:
        print("Unbalanced parenthesis")
        break

if counter == 0:
    print("Balanced parenthesis")
else: 
    print("Unbalanced parenthesis")