from ft_calculator import calculator


v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v1 + 5
print("~~~~~~")
v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v2 * 5
print("~~~~~~")
v3 = calculator([10.0, 15.0, 20.0])
v3 - 5
v3 / 5
v3 / 0
print("~~~~~~")
v4 = calculator([42, 69, 12.4, -24.0])
v4 + 2
v4 + 2.2
v4 - 2.2  # interesting.. doesn't go back to int, and bad float math
v4 * 10
