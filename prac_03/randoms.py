import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

#for line 1 the smallest number I have seen was 5 and the largest is 20
#for line 2 the smallest number I have seen was a 3 and the largest is 9. this line can't produce 4
#for line 2 the smallest number I have seen was 2.532174477402699 and the largest is  5.402580255044663
print(random.randint(1, 100))