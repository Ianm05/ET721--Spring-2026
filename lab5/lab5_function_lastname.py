"""
Ian Martinez
Feb 5, 2025
Lab5, function
"""
def area_rentangle (width, length):
     return width * length

# void function doesn't return a vlue
def print_area_result(width, length, area):
    print(f'The area of a rectangle with width {width} and length {length} is {area}.')

    # example 2L calculare the distance of two points
    # distance - square_root of ( (x2-x1^2) + (y2-y1^2)     
    # function 1) collect a number between 1 and 10
    def collectnum():
        num = int(input('Enter a number between 1 and 10: '))
        while num < 1 or num > 10:
            print('Invalid input. Please try again.')
            num = int(input('Enter a number between 1 and 10: '))
        return num
    
    #distance = square_root of ( (x2-x1^2) + (y2-y1^2   )
    def calculate_distance(x1, x2, y1, y2):
        return math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2))
    
    # function to prin the result
    def print_distance_result(x1,x2,y1,y2, distance):
        print(f'The distance between the points ({x1}, {y1}) and ({x2}, {y2}) is {distance}')
