def longestCommonSubsequence(S1, S2, len_S1, len_S2): 
    # create the matrix
    L = [[0 for x in range(len_S2+1)] for x in range(len_S1+1)] 

    for i in range(len_S1+1): 
        for j in range(len_S2+1): 
            if i == 0 or j == 0: 
                L[i][j] = 0
            elif S1[i-1] == S2[j-1]: 
                L[i][j] = L[i-1][j-1] + 1
            else: 
                L[i][j] = max(L[i-1][j], L[i][j-1]) 
  
    # Following variable will contain the length of LCS
    cursor = L[len_S1][len_S2] 
  
    # Create an array to store the LCS string 
    lcs = [""] * (cursor+1) 
    lcs[cursor] = "" 
  
    # Starting from last element in the table store character 
    # one by one as they match 
    i = len_S1 
    j = len_S2 
    while i > 0 and j > 0: 
        if S1[i-1] == S2[j-1]: 
            lcs[cursor-1] = S1[i-1] 
            i-=1; j-=1; cursor-=1
        elif L[i-1][j] > L[i][j-1]: 
            i-=1
        else: 
            j-=1
  
    print ("LCS of " + S1 + " and " + S2 + " is " + "".join(lcs))
    print ("Length of the LCS is " + str(L[len_S1][len_S2]))
  
if __name__ == "__main__":
    string1 = input("Enter a string of your choice : ")
    string2 = input('Enter another string to compare : ")
    S1 = string1.upper()
    S2 = string2.upper()
    len_S1 = len(S1) 
    len_S2 = len(S2) 
longestCommonSubsequence(S1, S2, len_S1, len_S2) 