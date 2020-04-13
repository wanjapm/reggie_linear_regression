def get_y(m, b, x):
    #y = m*x + b
    return (m*x) + b

def calculate_error(m,b,point):
    x_point = point[0]
    y_point = point[1]
    y2 = get_y(m,b,x_point)
    #print("y2: {} y_point: {}".format(y2,y_point))
    return abs(y2 - y_point)

def calculate_all_error(m,b,points):
    error=0
    for point in points:
        error += calculate_error(m,b,point)
    return error

#print(calculate_error(1, 0, (3, 3)))
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 1, datapoints))