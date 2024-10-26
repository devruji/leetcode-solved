from quizzes._1 import Solution as _1
from quizzes._2 import Solution as _2, ListNode
from quizzes._3 import Solution as _3
from quizzes._169 import Solution as _169
from quizzes._976 import Solution as _976
from quizzes.pandas._175 import Solution as _175
from quizzes.pandas._181 import Solution as _181
from quizzes.pandas._182 import Solution as _182
from quizzes.pandas._183 import Solution as _183

# if __name__ == "__main__":
#     input = [2, 2, 1, 1, 1, 2, 2]
#     print(f'quiz#169 (Majority Element): {input}, answer: {_169().majorityElement(input)}')


# if __name__ == "__main__":
#     input = [-3, 0, 1, 3, 4]
#     target = 0
#     print(f'quiz#1 (TwoSum): input={input}, target ={target}, answer: {_1().twoSum(input, target)}')


# if __name__ == "__main__":
#     #l1 = [2,4,3]
#     #l2 = [5,6,4]
#     l1=ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3, next=None)))
#     l2=ListNode(val=5, next=ListNode(val= 6, next=ListNode(val= 4, next= None)))
#     print(f'quiz#2 (addTwoNumbers): l1={l1}, l2 ={l2}, answer: {_2().addTwoNumbers(l1, l2)}')


# if __name__ == "__main__":
#     #input = "  "
#     # print(f'quiz#3 (lengthOfLongestSubstring): input="{input}", answer: {_3().lengthOfLongestSubstring(input)}')
#     # # input = "pwwkew"
#     # print(f'quiz#3 (lengthOfLongestSubstring): input="{input}", answer: {_3().lengthOfLongestSubstring(input)}')
#     input = "dvdf"
#     print(f'quiz#3 (lengthOfLongestSubstring): input="{input}", answer: {_3().lengthOfLongestSubstring(input)}')


# if __name__ == "__main__":
#     #input = [2,1,2]
#     #input = [2,1,1]
#     #input = [3,2,3,4]
#     input = [3,6,2,3]
#     #input  = [77,53,76,84,63,77,39,38,97,26841,29,93,87,85,31,88,43447,100,44,6,21,22,6,30,13,27,8,1,48,92,74,89,70,54,61,69,72,98,24,76,85,67,83,4,3,72,100,59,10,75,19,100,70,82,81,7,73,5,78,50,1,72,11,85,44,77,80,10,1,10,41,82,71,11,38,40,66,2,62,49,33,58,93,36,58,42,30,70,34,12,46,51,99,32,69,49,50,64,66,100,14,7,30,62,21,12,52,52,81,27,72,27,10,93,75,91,98,36,23,12,34,53,86,25,73,68,16,6325,1,54,39,47,39,85,94,33,100,27,3,85,82,29,1,6,15,1,53,34,78,3906,80,52,62,59,7,48,83,41,47,100,98,7,4,66,7,31,42,34,4,46,18,68,9,95,12,32,31,16,57,76,85,86,53,29,9,31,3,15,80,75,36,8,20,85,13,3,42,8,28,10,8,21,80,95,74,60,79,79,45,562,20,45,42,46,1,49,2,62,45,36,41,35,66,71,56,25,20,32,59,86,15,5,44,55,76,89,40,8,20,24,54,75,2,72,36,17,78,48,8,71,63,94,51,69,72,94,32,73,29,48,8,84,13,85,30,6,77,14,77,17,54,58,81,61,74,63,3,33,32,56,29,20,49,3,100,78,94,24,24,63,46,94,26,30,76,62,35,33,96,58,58,18,77,72,26,35,96,83,57,69,99,59,85,57,6,37,2,27,50,24,54,61,13,36,74,80,14,16,36,72,27,30,46,28,28,47,91,91,73,34,39,68,17,73,9,8,34,61,82,12,66,75,61,45,56,38,13,86,65,2,56,8,2,70,64,76,10,17,10,53,7,71,41,46,59,88,23,67,91,31,12,72,74,6,89,18,75,41,50,8,10,79,82,67,47,48,1,55,70,23,24,22,94,31,34,46,43,481886,85,82,33,99,9,9,5,64,65,57,67,13,38,12,66,11,63,35,30,34,29,21,6,5,73,26,42,83,100,78,47,12,48,44,95,79,99,43,90,3,56,64,32,28,9,43,64,95,92,65,5,72,44,29,20,33,20,73,82,37,24,33,54,48,37,8,95,94,32,99,28,49,19,48,67,88,29,67,55,67,31,75,53,28,86,32,41,16586,16,76,81,40,90,86,59,36,29,41,93,40,39,95,18,63,13,9,79,97,28,24,14,54,19,5,88,73,53,93,6,90,15,85,1,78,48,83,30,3,27,84,45,47,71,93,69,34,62,71,15,52,74,97,62,41,62,66,36,26,49,83,31,80,60,2401,72,19,23,21,86,41,13,68,15,54,85,29,46,55,31,94,71,3,36,31,95,26,50,40,70292,11,98,7,32,2,83,7,22,78,66,47,76,100,9,60,34,30,89,28,73,32,6,39,70,73,20,63,52,78,67,81,32,76,91,27,28,52,30,297820,7,33,27,3,10,17,70,91,100,94,53,100,44,83,98,61,31,96,22,84,2,2,97,58,17,57,7,19,10,63,60,64,74,2,36,95,53,97,1,42,50,96,66,14,26,39,50,22,31,48,42,68,24,30,30,59,14,96,56,84,77,73,98,59,85,1488,57,41,93,20,28,68,49,41,7,184049,14,73,89,56,7,84,43,22,28,91,74,58,100,65,65,57,51,44,94,73,13,4,13,64,32,73,3,7,66,97,29,48,33,46,80,63,91,8,84,12,24,4,58,44,77,125,67,64,100,64,12,11,87,57,96,56,27,49,71,113756,77,19,26,91,63,92,19,78,80,74,29,908,98,28,85,56,11,22,37,5,42,56,96,21,3,85,54,24,34,1,73,62,41,39,86,81,29,13,205,65,35,85,77,88,70,72,20,4,82,33,83,77,83,41,21,80,29,83,38,48,28,26,87,47,59,95,2,24,93,57,16,12,100,76,31,66,75,50,84,34,93,23,71,51,71,13,5,66,57,26,17,27,91,22,57,39,88,33,16,56,23,43,97,51,60,95,4,95,59,97,96,84,44,79,18,30,80,58,95,56,9,16,78,89,779723,49,51,44,26,18,61,56,97,98,64,77,19,91,4,100,33,345,26,27,57,79,60,40,38,25,77,60,21,2,11,35,21,68,8,89,62,86,76,71,71,60,58,2,6,13,21,51,69,24,2,2,72,44,55,10245,64,44,5,76,76,80,91,67,60,29,67,87,82,25,90,25,63,35,88,48,87,8,39,47,46,36,12,73,18,62,56,69,43,26,50,19,71,63,50,12,81,76,4,41,91,53,2,94,89,37,68,70,94,51,62,16,32,32]
#     print(f'quiz#976 (Largest Perimeter Triangle): input={input}, answer: {_976().largestPerimeter(input)}')

# 175
# if __name__ == "__main__":
#     import pandas as pd

#     # Example data
#     person_data = {
#         "personId": [1, 2],
#         "lastName": ["Wang", "Alice"],
#         "firstName": ["Allen", "Bob"],
#     }

#     address_data = {
#         "addressId": [1, 2],
#         "personId": [2, 3],
#         "city": ["New York City", "Leetcode"],
#         "state": ["New York", "California"],
#     }

#     # Convert to DataFrames
#     person_df = pd.DataFrame(person_data)
#     address_df = pd.DataFrame(address_data)

#     # Call the function
#     result_df = _175.combine_two_tables(person_df, address_df)
#     print(result_df)

# 181
# if __name__ == "__main__":
#     import pandas as pd

#     employee_data = {
#         "id": [1, 2, 3, 4],
#         "name": ["Joe", "Henry", "Sam", "Max"],
#         "salary": [70000, 80000, 60000, 90000],
#         "managerId": [3, 4, None, None],
#     }

#     # Convert to DataFrame
#     employee_df = pd.DataFrame(employee_data)

#     # Call the function
#     result_df = _181.find_employees(employee_df)

# 182
# if __name__ == "__main__":
#     import pandas as pd

#     person_data = {"id": [1, 2, 3], "email": ["a@b.com", "c@d.com", "a@b.com"]}

#     # Convert to DataFrame
#     person_df = pd.DataFrame(person_data)

#     # Call the function
#     result_df = _182.duplicate_emails(person_df)
#     print(result_df)

# 183
# if __name__ == "__main__":
#     import pandas as pd

#     # Input data
#     customers_data = {"id": [1, 2, 3, 4], "name": ["Joe", "Henry", "Sam", "Max"]}

#     orders_data = {"id": [1, 2], "customerId": [3, 1]}

#     # Convert to DataFrames
#     customers_df = pd.DataFrame(customers_data)
#     orders_df = pd.DataFrame(orders_data)

#     # Call the function
#     result_df = _183.find_customers(customers_df, orders_df)
#     print(result_df)
