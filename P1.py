
#?
n = int(input("enter number of rows needed: "))
for ro in range(n):
    for co in range(ro+1):
        print(co+1, end=" ")
