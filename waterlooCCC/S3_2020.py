"""
Problem S3: Searching for Strings
Problem Description
You’re given a string N, called the needle, and a string H, called the haystack, both of which
contain only lowercase letters “a”..“z”.
Write a program to count the number of distinct permutations of N which appear as a substring of
H at least once. Note that N can have anywhere between 1 and |N|! distinct permutations in total
– for example, the string “aab” has 3 distinct permutations (“aab”, “aba”, and “baa”).
Input Specification
The first line contains N (1 ≤ |N| ≤ 200 000), the needle string.
The second line contains H (1 ≤ |H| ≤ 200 000), the haystack string.
For 3 of the 15 available marks, |N| ≤ 8 and |H| ≤ 200.
For an additional 2 of the 15 available marks, |N| ≤ 200 and |H| ≤ 200.
For an additional 2 of the 15 available marks, |N| ≤ 2000 and |H| ≤ 2000.
Output Specification
Output consists of one integer, the number of distinct permutations of N which appear as a substring of H.
Sample Input
aab
abacabaa
Output for Sample Input
2
Explanation of Output for Sample Input
The permutations “aba” and “baa” each appear as substrings of H (the former appears twice),
while the permutation “aab” does not appear.
"""

N = input()
Nsequence = [char for char in N]
M = input()
Msequence = [char for char in M]

permutations = []
Nchecker = [False for char in N]

for mletter in Msequence:
    counter = Msequence.index(mletter)
    while counter <= 2:
        for nletter in Nsequence:
            try:
                if Msequence[counter] == nletter and Nchecker[counter] == False:
                    Nchecker[counter] = True
                    break
                else:
                    continue
            except:
                continue
        counter += 1
    isPermutation = False
    for Bool in Nchecker:
        if not Bool:
            isPermutation = False
            break
        else:
            isPermutation = True
    if isPermutation == True:

        for perm in permutations:
            if perm = 




