

ft_list		= ["Hello", "tata!"]
ft_tuple	= ("Hello", "toto!")
ft_set		= {"Hello", "tutu!"}
ft_dict		= {"Hello" : "titi!"}

ft_list[1] = "World!"

#tuples are immutable, concat to new tuple
ft_tuple = ft_tuple[:1] + ("Czechia!", ) + ft_tuple[2:] 

#sets are unordered and unchangable, have to remove and add new value
ft_set.remove("tutu!")
ft_set.add("Prague!")

#replace key Hello with correct value
ft_dict.update({"Hello": "42Prague!"})


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)