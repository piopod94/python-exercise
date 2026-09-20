# Get room height and classifie it.
# < 2.2 m → too low (nie spełnia norm)
# 2.2–2.5 m → standard
# 2.5–3.0 m → comfortable
# 3.0 m → loft / high ceiling
# Room height 2.65 m is comfortable.

height = float(input("Room height in meters: "))

if height < 2.2:
    result = "too low"
elif height > 2.2 and height < 2.5:
    result = "standard"
elif height > 2.5 and height < 3.0:
    result = "comfortable"
else:
    result = "loft / heigh ceiling"

print(f"Room height {height} m is {result}.")