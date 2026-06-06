# Task 1

a = int(input("Enter the lenght of the first leg A :"))
b = int(input("Enter the lenght of the second leg B :"))

hypothenuse = (a**2 + b**2) ** 0.5
area = (a*b/2)

print("hypothenuse =", hypothenuse)
print("area =", area)


# Task 2


# dev notes:
# saati = mititebuli wamebi gakofili 3600 ze
# wutebi = darchenili wamebis nashti 3600 dan gakofili 60 ze
# wamebi = mititebulidan darchenili nashti

total_seconds = int(input("Enter the number of seconds :"))

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60


print("Hour = ", hours, "Minutes = ", minutes, "Seconds = ", seconds)
