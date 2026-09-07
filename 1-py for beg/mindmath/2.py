import matplotlib.pyplot as plt

# Get values from the user
m = float(input("Enter m (slope): "))
c = float(input("Enter c (y-intercept): "))

#---------------------------------------------------
#get the value range from user







#---------------------------------------------------

# Create x values
x = range(-10, 11)

# Calculate y values
y = []

for value in x:
    y.append(m * value + c)

# Draw graph
plt.plot(x, y)

# Draw X and Y axis
plt.axhline(0)
plt.axvline(0)

# Labels
plt.xlabel("X")
plt.ylabel("Y")
plt.title(f"y = {m}x + {c}")

# Show grid
plt.grid()

# Show graph
plt.show()