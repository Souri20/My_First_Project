'''Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. Find the missing element.'''
'''N = 5
A[] = {1,2,3,5}
Output: 4 '''
# class Solution:
# 	def missingNumber(self ,array ,n):
#
# 		total_sum = (n *(n +1) )//2
#
# 		sum1 = sum(array)
#
# 		missing_num = total_sum - sum1
#
#
# 		return missing_num
#
# solution = Solution()
# num = 5
# A = [1,2,3,5]
#
# missing_value = solution.missingNumber(A, num)
#
# print(missing_value)

####'''Given an array arr[] of positive integers of size N. Reverse every sub-array group of size K.

# Note: If at any instance, there are no more subarrays of size greater than or equal to K, then reverse the last subarray (irrespective of its size). You shouldnt return any array, modify the given array in-place.
#
# Example 1:
#
# Input:
# N = 5, K = 3
# arr[] = {1,2,3,4,5}
# Output: 3 2 1 5 4
# Explanation: First group consists of elements
# 1, 2, 3. Second group consists of 4,5
class Solution:
	# Function to reverse every sub-array group of size k.
	def reverseInGroups(self, arr, N, K):
		for i in range(0, N, K):
			left = i
			right = min(i + K - 1, N - 1)

			while left < right:
				arr[left], arr[right] = arr[right], arr[left]

				left += 1
				right -= 1


solu = Solution()
arr=[1,2,3,8,9]
n = 5
k=3

solu.reverseInGroups(arr,n,k)
solu.reverseInGroups(arr,n,k)
print(arr)




#####


from collections import defaultdict


def findFirstKOccurrence(N, K, A):
	count = defaultdict(int)  # Dictionary to store element counts

	for i in range(N):
		count[A[i]] += 1

		# Check if the count of the current element is at least K
		if count[A[i]] == K:
			return A[i]

	return -1  # Return -1 if no element occurs at least K times


# Example usage
N = 7
K = 2
A = [1, 7, 4, 3, 4, 8, 7]

print("Array:", A)

result = findFirstKOccurrence(N, K, A)
if result != -1:
	print("First element occurring at least", K, "times:", result)
else:
	print("No element occurs at least", K, "times")
