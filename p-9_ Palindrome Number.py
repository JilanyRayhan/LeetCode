class Solution:
  def isPalindrome(self, x : int) -> bool:
    if x < 0:
      return False
    temp = x
    reverse = 0
    while temp != 0:
      digit = temp % 10
      reverse = reverse * 10 + digit
      temp //= 10
    return x == reverse
num = int(input("enter a number to check palindrome: "))
sol = Solution()
result = sol.isPalindrome(num)
print(result)