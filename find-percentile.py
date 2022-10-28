numbers = [30, 56, 76, 12, 26, 96, 28, 77, 81, 21, 32, 93, 23, 19, 32, 43, 67, 48]

last_n = 10
last_10 = numbers[-last_n:]
last_10.sort()

percentile_n = 0.9
percentile_90 = len(last_10) * percentile_n
result = last_10[int(percentile_90)-1]
print(result)
