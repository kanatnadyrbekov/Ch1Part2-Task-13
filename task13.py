# For a given integer N, print all the squares of integer numbers 
# where the square is less than or equal to N, in ascending order.

n = int(input("integer: "))
for i in range(n + 1):
    if i != 0:
        if i**2 < n:
            print(i**2, end=' ')

    