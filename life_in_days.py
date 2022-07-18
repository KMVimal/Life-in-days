print("Estimated lifespan is 90 years.")
age = int(input("What is your current age: "))
yrs_rem = 90-age
days_rem = yrs_rem*365
weeks_rem = yrs_rem*52
months_rem = yrs_rem*12
print(f"you have {days_rem} days, {weeks_rem} weeks and {months_rem} months remaining.")