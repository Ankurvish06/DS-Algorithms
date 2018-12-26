Recursive Approach
def isSubSequence(string1, string2, m, n): 
    # Base Cases 
    if m == 0:    return True
    if n == 0:    return False
  
    # If last characters of two strings are matching 
    if string1[m-1] == string2[n-1]: 
        return isSubSequence(string1, string2, m-1, n-1) 
  
    # If last characters are not matching 
    return isSubSequence(string1, string2, m, n-1) 
    
Iterative:
def isSubSequence(str1,str2,m,n): 
      
    j = 0    # Index of str1 
    i = 0    # Index of str2 
      
    # Traverse both str1 and str2 
    # Compare current character of str2 with  
    # first unmatched character of str1 
    # If matched, then move ahead in str1 
      
    while j<m and i<n: 
        if str1[j] == str2[i]:     
            j = j+1    
        i = i + 1
          
    # If all characters of str1 matched, then j is equal to m 
    return j==m 
