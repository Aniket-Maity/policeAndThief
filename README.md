Problem Statement
You are given an array of size n that has the following specifications:

           1. Each element in the array contains either a police man or a thief.

           2. Each policeman catch only one thief.

           3. A policeman cannot catch a thief who is more than k units away from the policeman.

You need to find the maximum number of thieves that can be caught.

Extra Info


Input Format
First line having two space separated integers represent the value of n and k. 

Second line having n space separated characters (T and P) represents the array. ( T-> Thief and P->Policeman)

Output Format
Single line containing the value of maximum number of thieves that could be caught

Constraints
length of the array would be less than 1000 and K < 100

Time Limit
2s.
Each test case should pass in 2s.
Sample Input
5 1 
P T T P T 
Sample Output
2