# Question : Given a range of numbers.
# Iterate from o^th number to the end number and print the sum of the current number and previous number
def sum_Num(num):
    previous_Num = 0
    for i in range(num):
        sum = previous_Num + i
        print(sum)
        previous_Num = i

print("Printing current and previous number sum in a given range")
sum_Num(10)