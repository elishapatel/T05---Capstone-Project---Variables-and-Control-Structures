my_num = 0

while my_num < 100:
    my_num += 1
    if my_num > 10:
        continue
    print(my_num)


print(f"\nThe element stored in my_num is:\n{my_num}")