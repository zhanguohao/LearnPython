# -*- coding: utf-8 -*-


class Solution1(object):
    def two_sum(self, nums, target):
        """
        :param nums: List[int]
        :param target: int
        :return: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if target == (nums[i] + nums[i + j + 1]):
                    return [i, i + j + 1]
        return False


class Solution2(object):
    def two_sum(self, nums, target):
        """
        :param nums: List[int]
        :param target: int
        :return: List[int]
        """
        buff_index = dict(zip(nums, range(len(nums))))
        buff_list = sorted(nums)
        i = 0
        j = len(buff_list) - 1
        while i < j:
            if buff_list[i] + buff_list[j] > target:
                j -= 1
            elif buff_list[i] + buff_list[j] < target:
                i += 1
            elif i != j:
                return [buff_index[buff_list[i]], buff_index[buff_list[j]]]

        return False


class Solution3(object):
    def two_sum(self, nums, target):
        """
        :param nums: List[int]
        :param target: int
        :return: List[int]
        """
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if target - nums[i] in buff_dict:
                return [buff_dict[target - nums[i]], i]
            buff_dict[nums[i]] = i
        return False


class Solution4(object):
    def two_sum(self, nums, target):
        """
        :param nums: List[int]
        :param target: int
        :return: List[int]
        """
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i


class Solution5(object):
    def two_sum(self, nums, target):
        """
        :param nums: List[int]
        :param target: int
        :return: List[int]
        """
        buff_dict = {}
        for i, num in enumerate(nums):
            if target - num in buff_dict:
                return [buff_dict[target - num], i]
            else:
                buff_dict[num] = i


if __name__ == "__main__":
    test = Solution2()
    ab = test.two_sum([3, 2, 4, 5], 7)
    print ab
