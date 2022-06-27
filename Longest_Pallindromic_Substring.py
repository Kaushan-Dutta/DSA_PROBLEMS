#Finding the length of the largest subarray which is pallindrome
#example--INPUT-abadab OUTPUT-aba

def long_substring(string):
    substring="" #initializtion
    for i in range(len(string)):
        odd_length=check(string,i,i)
        even_length=check(string,i,i+1)
        if(len(odd_length)>len(even_length) and len(odd_length)>len(substring)):
            substring=odd_length
        elif(len(odd_length)<len(even_length) and len(even_length)>len(substring)):
            substring=even_length
    return(substring)

def check(string,left,right):
    while(left>=0 and right<=len(string)-1 and string[left]==string[right]):#creating the largest length
        left-=1
        right+=1
    return string[left+1:right]

string=input()#accepting string
print(long_substring(string))