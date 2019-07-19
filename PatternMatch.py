class Regex(object):
    def PatternMatch(self, S1, S2):
        # create the matrix
        matrix = [[False] * (len(S1) + 1) for _ in range(len(S2) + 1)]

        # initializing the first element as true
        matrix[0][0] = True

        # case when S1 is empty but S2 has some pattern
        for i in range(2, len(S2) + 1):
            matrix[i][0] = matrix[i - 2][0] and S2[i - 1] == '*'

        for i in range(1, len(S1) + 1):
            for j in range(1, len(S2) + 1):
                if S2[j - 1] != "*":
                    matrix[j][i] = matrix[j - 1][i - 1] and (S2[j - 1] == S1[i - 1] or S2[j - 1] == '.')
                else:
                    # '*' either eliminates the previous or count the previous element
                    matrix[j][i] = matrix[j - 2][i] or matrix[j - 1][i]
                    # If S2's previous characted is equal to the current S1 character
                    if S2[j - 2] == S1[i - 1] or S2[j - 2] == '.':
                        matrix[j][i] |= matrix[j][i - 1]

        if matrix[-1][-1] == True:
            print ("TRUE, the string: " + S1 + " does match the pattern: " + S2)
        else: 
            print ("FALSE, the string: " + S1 + " does not match the pattern: " + S2)


if __name__ == "__main__":
    match = Regex
    string = input("Enter a string of your choice : ")
    pattern = input("Enter the pattern to compare : ")
    S1 = string.upper()
    S2 = pattern.upper()
match().PatternMatch(S1, S2)