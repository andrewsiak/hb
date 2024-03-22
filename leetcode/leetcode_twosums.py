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



