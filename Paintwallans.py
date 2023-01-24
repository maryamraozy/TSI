#Creating a class for Wall
class Wall: 
    def __init__(self, height:float, length:float):
        self.height = height
        self.length = length
        self.area = height*length
#Creating the program to calculate how much paint would be needed with only a measuring tape.

def main():
    totalSurfaceArea = 0 #To calculate the total surface area of all walls
#How many rooms would you like to be painted
    wallno = int(input('Please input how many walls you would like to paint?'))
    walls = [] #holds the wall
    for i in range(wallno): 
        wall_height = float(input('Please input wall height in metres:>')) #Figure out how high the wall is 
        wall_length = float(input('Please input wall length in metres:>')) #Figure out how long the wall is 
        
        wall = Wall(wall_height, wall_length) #calculate the surface are of the wall

        walls.append(wall) #add a wall to list

#How many coats of paint the user would like 
    coats = int(input('Enter number of coats needed: '))


#def removeObstructions():
 #   obstructions = str('Are there any obstructions? Please enter yes or no')
  #  if obstructions == yes()
    

#def door():
 #   door_width = input('Please input door width :>')
  #  door_height = input('Please input door height :>')

#def window():
 #   window1_width = input('Please input 1st window width :>')
  #  window1_height = input('Please input 1st window height :>')

#def object():
 #   object_width = input('Please input bookshelf width:>')
  #  object_height = input('Please input bookshelf height:>')

    for wall in walls:
        totalSurfaceArea += wall.area #add the surface area of all the walls
         
    paint_gallons = round(coats*totalSurfaceArea/12)
    print(" # of litres of paint needed = " + str(paint_gallons)) #prints the number of litres needed for the total surface area the user has inputted.

    costPaint = 2.5 #cost per litre
    print("It will cost £ " + str(paint_gallons*costPaint)) #prints the total cost against one paint comapany currently - dulux

main()