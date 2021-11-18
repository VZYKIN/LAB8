
import random
def kbig(nums, k)
nums = [random.randint(1, 3) for i in range(5)]

print('Сгенерированы такие числа: ')
print(nums)

sorted_nums = sorted(nums, reverse=True)
print('В порядке убывания: ')
print(sorted_nums)
sorted_nums = sorted(set(sorted_nums), reverse=True)

for i, num in enumerate(sorted_nums, 1):
    print('{i} максимум: {maxim}'.format(i=i, maxim=num))
