import operator

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

sorted_asc =dict(sorted(d.items(),key=operator.itemgetter(1)))
print("Ascending:", sorted_asc)

sorted_desc = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
print("Descending:", sorted_desc)

