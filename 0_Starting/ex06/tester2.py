from ft_filter import ft_filter
original = filter.__doc__
copy  = ft_filter.__doc__

print(copy) # output: docstring
print(original)
print(original == copy) # output: True
