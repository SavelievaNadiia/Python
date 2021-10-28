import random
nums = list(range(0, 11))
random.shuffle(nums)
z = (nums[:11])
print(z)
print('число 4 находится в списке под номером', z.index(4))
