"""
"""
from functools import reduce

class Problems(object):
    """
    """
    def __init__(self):
        pass

    def day_one(self, arr, value):
        """
        [10, 2, 3, 4, 5, 7] and value = 17
        return true if sum of any two value equals value
        """
        for index, item in enumerate(arr):
            for nextindex, nextitem in enumerate(arr):
                if index != nextindex and item + nextitem == value:
                    return True
        return False

    def day_two(self, arr):
        """
        [1,2,3,4,5], result = [120, 60, 40, 30, 24]
        """
        # new_arr = []
        # for index, item in enumerate(arr):
        #     prod = 1
        #     for nextindex, nextitem in enumerate(arr):
        #         if index != nextindex:
        #             prod *= nextitem
        #     new_arr.append(prod)
        # return new_arr
        prod = reduce(lambda x, y: x * y, arr)
        return list(map(lambda x: prod//x, arr))
