print("Hello world")
print("Please input measures in Metres")
wall_height = int(input('Please input wall height:>'))
wall_length = int(input('Please input wall length:>'))
surface_area = (wall_height*wall_length)
paint_gallons = round(2*surface_area/12)
print(" # of gallons of paint needed = " + str(paint_gallons))
#original calculator