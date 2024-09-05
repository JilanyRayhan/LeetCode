from typing import List
class Solution:
  def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
      result = []
      if len(original) != m*n:
          return result
      else:
          for i in range(m):
              result.append(original[i*n:(i+1)*n])
          return result



org = [1,2,3,4,5,6,7,8,9,10]
m1 = 5
n1 = 2
sol = Solution()
vec = sol.construct2DArray(org,m1,n1)
print(vec)