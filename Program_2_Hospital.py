n = int(input("Enter number of hours: "))
patients = list(map(int, input("Enter patient counts: ").split()))

maximum = max(patients)
minimum = min(patients)
peak_hour = patients.index(maximum) + 1
average = sum(patients) / n

above_average = 0

for p in patients:
    if p > average:
        above_average += 1

print("Maximum patients:", maximum)
print("Hour of maximum patients:", peak_hour)
print("Minimum patients:", minimum)
print("Peak hour:", peak_hour)
print("Hours above average:", above_average)