print("Hello world")
print("Please input measures in Metres")

wall_height = float(input('Please input wall height:>'))

wall_length = float(input('Please input wall length:>'))
#write a variable to include how many coats to add
surface_area = (wall_height*wall_length)

paint_gallons = round(2*surface_area/12)

print(" # of litres of paint needed = " + str(paint_gallons))

