#Task 3

spendings = [140, 30, 999, 145, 538, 878, 901, 613, 471, 286, 147, 90]
income = [300, 40, 0, 4000, 8911, 73, 85, 0, 9000, 941, 658, 190]
#
main_coff = 0
for i in range(12):
    try:
        coff = spendings[i] / income[i]
    except ZeroDivisionError:
        coff = 0
        continue
    # finally:
    #     main_coff += 0

print(main_coff)
print(coff)
