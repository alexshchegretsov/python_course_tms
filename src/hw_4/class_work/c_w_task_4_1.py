"""
Дан произвольный список, содержащий только числа.
Выведите результат сложения всех чисел больше 10.

"""
nums = [2, 17, 9, 4, 56, 11]
length = len(nums)
i = 0
sum = 0
while i < length:
    if nums[i] > 10:
        sum += nums[i]
    i += 1
print(sum)
