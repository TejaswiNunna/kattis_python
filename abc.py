x,y,z = [int(x) for x in input().split()]
order = input()
order_map = {"C":max(x,y,z), "A":min(x,y,z)}

if order_map["C"] != x and order_map["A"] != x:
    order_map.update({"B": x})
elif order_map["C"] != y and order_map["A"] != y:
    order_map.update({"B": y})
else:
    order_map.update({"B": z})
print(order_map[order[0]],order_map[order[1]], order_map[order[2]])