# Maximum string length 
N = 100
L = [[0 for i in range(N)]  
        for j in range(N)] 
  
def findallLCS(s1, s2, m, n): 
    s = set() 
    if m == 0 or n == 0: 
        s.add("") 
        return s 
    if s1[m - 1] == s2[n - 1]: 
        tmp = findallLCS(s1, s2, m - 1, n - 1) 
        for string in tmp: 
            s.add(string + s1[m - 1]) 
    else: 
        if L[m - 1][n] >= L[m][n - 1]: 
            s = findallLCS(s1, s2, m - 1, n) 
        if L[m][n - 1] >= L[m - 1][n]: 
            tmp = findallLCS(s1, s2, m, n - 1) 
            for i in tmp: 
                s.add(i) 
    return s 
  
def LCS(s1, s2, m, n): 
    for i in range(m + 1): 
        for j in range(n + 1): 
            if i == 0 or j == 0: 
                L[i][j] = 0
            elif s1[i - 1] == s2[j - 1]: 
                L[i][j] = L[i - 1][j - 1] + 1
            else: 
                L[i][j] = max(L[i - 1][j], 
                              L[i][j - 1]) 
    return L[m][n] 
  

print("Enter string 1:")
s1 = input().strip()
print("Enter string 2:")
s2 = input().strip()
m = len(s1) 
n = len(s2) 
print("\nLCS length is", LCS(s1, s2, m, n)) 
s = findallLCS(s1, s2, m, n)
print("\nThe sequences are:")
for i in s: 
    print(i) 