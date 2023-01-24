# Online Python compiler (interpreter) to run Python online.
#need to paint a wall but dont know how much paint needed to paint a wall. measuring tape, how much something measures. 
# Write Python 3 code in this online editor and run it.

print("Hello world")



door_width = input('Please input door width :>')

door_height = input('Please input door height :>')



window1_width = input('Please input 1st window width :>')

window1_height = input('Please input 1st window height :>')

window2_width = input('Please input 2nd window width :>')

window2_height = input('Please input 2nd window height:>')

bookshelf_width = input('Please input bookshelf width:>')

bookshelf_height = input('Please input bookshelf height:>')



room_width = input('Please input room width :>')

room_height = input('Please input room height :>')

room_length = input('Please input room length:>')



door_area = float(door_width) * float(door_height)

window1_area = float(window1_width)*float(window1_height)

window2_area = float(window2_width)*float(window2_height)

bookshelf_area = float(bookshelf_width)*float(bookshelf_height)



# are we painting the floor?

wall_area1 = float(room_width)*float(room_height)

wall_area2 = float(room_width)*float(room_length)

wall_area3 = float(room_height)*float(room_length)



print("door area = " + str(door_area))

print(" area of 1st window is " + str(window1_area))

print(" area of 2nd window is " + str(window2_area))

print(" area of bookshelf is " + str(bookshelf_area))



print(" wall area #1 = " + str(wall_area1))

print(" wall area #2 = " + str(wall_area2))

print(" wall area #3 = " + str(wall_area3))



surface_area = 2*(wall_area1 + wall_area2 + wall_area3)

print(" surface area = " + str(surface_area))



paintable_area = surface_area - window1_area - window2_area -  bookshelf_area - door_area



paint_gallons = round(paintable_area/120)





print(" paintable area = " + str(paintable_area))

print(" # of gallons of paint needed = " + str(paint_gallons))



price_per_gallon = input(' please input price per gallon :> ')

total_cost = float(price_per_gallon) * float(paint_gallons)

print(" cost = " + str(total_cost))