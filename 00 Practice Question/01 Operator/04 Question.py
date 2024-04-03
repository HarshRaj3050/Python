''' WAP to calculate and display a length value in Kms and Mts,
   where the value is entered in meters only. '''

meters = int(input("Enter the length in meters: "))
km = meters / 1000
remain_meter = meters - (int(km) * 1000)
print(f"{meters} meters is equal to {int(km)} kilometers and {remain_meter} meters")