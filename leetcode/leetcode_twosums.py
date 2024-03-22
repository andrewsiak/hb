# def twoSum(nums_list, target):
#     """Find two numbers in a list that add up to target"""

#     for index, number in enumerate(nums_list):
        
#         remainder = target - number
#         if remainder in nums_list:
#             return [index, nums_list.index(remainder)]


def two_sum_dict(nums_list, target):
    """Find indexes of integer elements that add up to target"""

    target_dict = {}
    for i in range(0,len(nums_list)):
        if target - nums_list[i] in target_dict:
            return [target_dict[target-nums_list[i]],i]
        else:
            target_dict[nums_list[i]] = i  



sum_test = 16
test_list = [1,2,3,4,5,6,7,8,9]
print("Test", two_sum_dict(test_list, sum_test))

test_case_one = [2,7,11,15]
sum_one = 9
print("Case 1", two_sum_dict(test_case_one, sum_one))

test_case_two = [3,2,4]
sum_two = 6
print("Case 2", two_sum_dict(test_case_two, sum_two))

test_case_three = [3,3]
sum_three = 6
print("Case 3", two_sum_dict(test_case_three, sum_three))
