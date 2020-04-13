def get_y(m, b, x):
    #y = m*x + b
    return (m*x) + b

def calculate_error(m,b,point):
    x_point = point[0]
    y_point = point[1]
    y2 = get_y(m,b,x_point)
    return abs(y2 - y_point)

def calculate_all_error(m,b,points):
    error=0
    for point in points:
        error += calculate_error(m,b,point)
    return error

possible_ms = [ i*0.1 for i in range(-100,101)]
possible_bs = [i*0.1 for i in range(-200,201)]
#datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
smallest_error = float("inf")
best_m = 0
best_b = 0


for m in possible_ms:
    for b in possible_bs:
        error = calculate_all_error(m,b,datapoints)
        if error < smallest_error:
            best_m = m
            best_b = b
            smallest_error = error
print("Best m: {}, Best b: {}, Smallest error: {}".format(best_m,best_b,smallest_error))

# Test area
m = 0.3
b = 1.7
x = 6
print(get_y(m,b,x))
#print(calculate_error(1, 0, (3, 3)))
#datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
#print(calculate_all_error(1, 1, datapoints))