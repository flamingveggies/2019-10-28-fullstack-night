d_ft = int(input("Input distance in feet: "))
#d_inches = d_ft * 12
#d_yards = d_ft / 3.0
d_miles = d_ft / 5280.0
d_meters = d_ft/0.3048
d_km = d_ft/3280.84

#print("The distance in inches is %i inches." % d_inches)
#print("The distance in yards is %.2f yards." % d_yards)
print("The distance in miles is %.2f miles." % d_miles)
print("The distance in meters is %.2f meters." % d_meters)
print("The distance in kilometers is %.2f kilometers." % d_km)
