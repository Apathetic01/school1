

# Create two six-sided dice.
die_1 = die_1(6)
die_2 = Die(6)

# Make some rolls and store the results in a list.
results = []
for _ in range(1000):  # Use '_' to indicate an unused loop variable
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = 6 * 2  # Assuming six-sided dice
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Print the results.
print(f"Results: {results}")
print(f"Frequencies: {frequencies}")
