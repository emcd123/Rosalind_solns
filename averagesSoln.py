s= [17903,18484,19871,18921,18160,18331]

p_list = [1, 1, 1, 0.75, 0.5, 0]
EV_list =[]

# A simple application of expected value.
for index, num_parents in enumerate(s):
        EV_list.append(2*int(num_parents)*p_list[index])

        print sum(EV_list)
