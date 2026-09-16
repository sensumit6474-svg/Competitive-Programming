n = int(input("Enter number of students: "))
attendance = list(map(float, input("Enter attendance percentages: ").split()))
threshold = float(input("Enter attendance threshold: "))

below = 0
lowest = attendance[0]
position = 0

for i in range(n):
    if attendance[i] < threshold:
        below += 1

    if attendance[i] < lowest:
        lowest = attendance[i]
        position = i

average = sum(attendance) / n

print("Students below threshold:", below)
print("Lowest attendance:", lowest)
print("Position:", position + 1)
print("Average attendance:", average)