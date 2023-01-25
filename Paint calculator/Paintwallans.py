#Creating a class for Wall
class Wall: 
    def __init__(self, height:float, length:float):
        self.height = height
        self.length = length
        self.area = height*length
#Creating the program to calculate how much paint would be needed with only a measuring tape.

#function to check that user is inputting a number
def userValidated(question):
    questionUnanswered = True
    while questionUnanswered == True:
        print(question)
        answer = input()
        try:
            answer = float(answer)
            questionUnanswered = False
        except ValueError:
            print("Please input a valid number")
    return answer   

def userValidatedInt(question):
    isInt = True
    while isInt == True:
        print(question)
        answer = input()
        try:
            answer = int(answer)
            isInt = False
        except ValueError:
            print("Please input a valid number")
    return answer 

def main():
    totalSurfaceArea = 0 #To calculate the total surface area of all walls
#How many rooms would you like to be painted
    wallno = userValidatedInt('Please input how many walls you would like to paint?')
    walls = [] #holds the wall
    for i in range(wallno): 
        wall_height = userValidated('Please input wall height in metres:>') #Figure out how high the wall is 
        wall_length = userValidated('Please input wall length in metres:>') #Figure out how long the wall is 
        
        wall = Wall(wall_height, wall_length) #calculate the surface are of the wall

        walls.append(wall) #add a wall to list


    coats = userValidatedInt('Enter number of coats needed: ') #How many coats of paint the user would like 


    obstructions = input('Are there any obstructions? Please enter yes or no. ') #check if there any obstructions
    if obstructions == 'yes': 
        objectSurfaceAreas = [] #List to store all the obstruction surface areas 
        completed = False
        while completed == False: #If user says yes, will enter a loop asking for height and width until user says no
            object_width = userValidated('Please input object width:>')
            object_height = userValidated('Please input object height:>')
            object_area = object_height*object_width
            objectSurfaceAreas.append(object_area)
        
            obstructions = input('Are there any obstructions? Please enter yes or no. ')
            if obstructions == 'no': #once user says no more obstruction, then it will exit loop
                completed = True             


    for wall in walls:
        totalSurfaceArea += wall.area #add the surface area of all the walls
    
    totalSurfaceArea -= sum(objectSurfaceAreas) #minus the obstruction surface area from the total surface area

    paint_gallons = round(coats*totalSurfaceArea/12)
    print(" # of litres of paint needed = " + str(paint_gallons)) #prints the number of litres needed for the total surface area the user has inputted.

    #add options for paint - cheaper paint - so user 
    x = input('Which brand of paint would you like to choose? Please enter 1, 2 or 3. (Dulux(£2.50 per Litre) = 1, Johnstones(£2 per litre) = 2, Crown(£1.50 per litre) = 3)')
    match x:
        case "1": #Dulux
            print(2.5)
            costPaint = 2.5
        case "2": #Johnstones
            print(2)
            costPaint = 2
        case "3": #Crown
            print(1.5)
            costPaint = 1.5
    
    print("It will cost £ " + str(paint_gallons*costPaint)) #prints the total cost against one paint comapany currently - dulux

main()
    
#how many cans you need and how much would that cost.
#user validation/error handling