n = int(input())
iteration_corners = {1:3}
for i in range(2,16):
    iteration_corners.update({i:iteration_corners[i-1]+(iteration_corners[i-1]-1)})
print(iteration_corners[n]**2)