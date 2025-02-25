import time

# Epoch is the time from which time.time() measures.
obj = time.gmtime(0)
epoch = time.strftime("%B %-d, %Y", obj)
epoch += ":"

t = time.time()
t_comma = '{:,.4f}'.format(t)

t_sci = '{:.2e}'.format(t)
current_date = time.strftime("%B %d %Y")

print("Seconds since", epoch, t_comma, 
	  "or", t_sci, "in scientific notation")
print(current_date)