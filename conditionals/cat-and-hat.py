"""
You are given a string str, you need to return True if  the words "cat" and "hat" appear same number of times in str, otherwise return False.
Note: str contains only lowercase English alphabets.

Example 1:

Input:
str = catinahat
Output:
True
Explanation:
cat and hat both are present
1 number of times.
Example 2:

Input:
str = bazingaa
Output:
True
Explanation:
cat and hat both are present
0 number of times.
Constraints:
1 <= str.size() <= 105

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Your Task:
This is a function problem. You don't need to take any input. Just complete the function cat_hat() that takes a string str as input.
"""

def cat_hat(str):
    if str.count('cat') == str.count('hat'):
      return True
    else:
      return False