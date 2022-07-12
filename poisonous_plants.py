#you have been given an array contaning pesitcides, find the maximum no. of days after which no plants dies
#ex INPUT-[6,5,8,4,7,10,9] OUTPUT-2
def poisonous_plant(p):
    stack=[]
    maxday=0
    for plant in p:
        day=0
        while stack and stack[-1][0]>=plant:
            day=max(day,stack.pop()[1])
        if(stack):
            day+=1
        else:
            day=0
        maxday=max(maxday,day)

        stack.append([plant,day])

    return maxday

plants=[6,5,8,4,7,10,9]
print(poisonous_plant(plants))