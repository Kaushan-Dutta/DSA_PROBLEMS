#finding out the longest common subsequence
#INPUT-shinchan,noharaaa OUTPUT-3

def lcs_recursion(s1,s2,i,j):

    if(i==len(s1) or j==len(s2)):
        return 0

    if(s1[i]==s2[j]):
        return 1+lcs_recursion(s1,s2,i+1,j+1)

    return max(lcs_recursion(s1,s2,i+1,j),lcs_recursion(s1,s2,i,j+1))

s1,s2=map(str,input().split(' '))
print(lcs_recursion(s1,s2,0,0))

#complexity(O(2^n)), but a runtime error will be there....going to upload it later
