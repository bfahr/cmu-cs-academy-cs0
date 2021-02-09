"""
CS0 Lesson 2 - Objects, Variables and Functions
===============================================

Resources:
  - Find out more about Class objects in Python:
    https://docs.python.org/3/tutorial/classes.html#a-first-look-at-classes
    
  - Valid variable names in Python can include:
    1. Letters A..Z and a..z
    2. Underscore "_"
    3. Numbers 0..9 but not as the first character in the name
    
    Find out more about Python variables (identifiers):
    https://docs.python.org/3/reference/lexical_analysis.html#identifiers
"""

# First lets create a function that will take a Circle object and show
# all of its attributes.  Find out more about functions here:
# https://docs.python.org/3/tutorial/controlflow.html#defining-functions
def show_circle(my_circle, title=None):
    # All statements inside this function must be indented by the same
    # amount of whitespace, here I've used the typical 4 spaces
    
    # The default is no title, but if one is supplied then print it
    # '\n' is the end-of-line character and adds a blank line
    if title is not None:
        print('\n***', title, '***\n')
    
    # Print the object using its own built-in formatter
    print('Object  :', my_circle)
    
    # Next print the required attributes individually accessing them
    # using the object.attribute_name notation 
    print('--- Required Arguments ---')
    print('Center X:', my_circle.centerX)
    print('Center Y:', my_circle.centerY)
    print('Radius  :', my_circle.radius)
    
    # Finally print the optional attributes individually accessing them
    # using the object.attribute_name notation
    print('--- Optional Arguments with Default ---')
    print('Fill        :', my_circle.fill)
    print('Border      :', my_circle.border)
    print('Border Width:', my_circle.borderWidth)
    print('Opacity     :', my_circle.opacity)
    print('Rotate Angle:', my_circle.rotateAngle)
    print('Dashes      :', my_circle.dashes)
    print('Visible     :', my_circle.visible)
    
    # The function ends when the indentation is stopped


# Create a new circle object using the Circle class
# and store the created object in the variable c1.
c1 = Circle(125, 150, 40, fill='blue')


# Lets look at the object, notice how the attributes you passed
# above are stored in the object and printed
show_circle(c1)


# Lets change the fill from 'blue' to a gradient and see how that changes
# the circle object.  Notice that the circle changes color immediately,
# and also notice the fill attribute changes.
c1.fill=gradient('yellow', 'blue', start='left')
show_circle(c1, 'Changed the fill from blue to gradient')


# Move it to the lower part of the display, position 300, 310
c1.centerX = 300
c1.centerY = 310
show_circle(c1, 'Moved the circle to 300, 310')


# You can also get the values of attributes and use them to change
# the object.  For instance to rotate the circle 10 degrees from its
# current position you can just add 10 to the current rotateAngle attribute
c1.rotateAngle = c1.rotateAngle + 10
show_circle(c1, 'Rotated the circle by 10 degrees')
