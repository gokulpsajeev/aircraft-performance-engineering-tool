from calculations import wing_loading

print("===================================")
print("Aircraft Performance Calculator")
print("===================================")

weight = float(input("Enter Aircraft Weight (kg): "))
wing_area = float(input("Enter Wing Area (m²): "))

result = wing_loading(weight, wing_area)

print("\nWing Loading:", round(result, 2), "kg/m²")
