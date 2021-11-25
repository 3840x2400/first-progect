from random import randint

class Matrix:
    def __init__(self, nums):
        self.nums = nums

    def __str__(self):
        s = ""
        for i in range(len(self.nums)):
            for j in range(len(self.nums[i])):
                s += f'{self.nums[i][j]:02}'
            s += "\n"
        return s

    def __add__(self, other):
        nums = [
            [self.nums[i][j] + other.nums[i][j] for j in range(len(self.nums[i]))]
                for i in range(len(self.nums))]
        return Matrix(nums)

a = Matrix([[randint(0, 99) for _ in range(10)] for _ in range(10)])
b = Matrix([[randint(0, 99) for _ in range(10)] for _ in range(10)])
print(a)
print(b)
print(a + b)