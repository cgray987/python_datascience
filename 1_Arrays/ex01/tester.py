from array2D import slice_me


family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))

print("broken family:")
broken_family = [[1.80, 78.4],
                 [2.15, 102.7, 27],
                 [2.10, 98.5],
                 [1.88, 75.2]]

print(slice_me(broken_family, 0, 2))
print(slice_me(broken_family, 1, -2))

print("list with mutliple types:")
broken_family = [["test", "hello"],
                 [2.15, 102.7],
                 [2.10, 98.5],
                 [1.88, 75.2]]

print(f"float indicies: {slice_me(broken_family, 1.4, 4.2)}")
print(slice_me(broken_family, 1, -2))
