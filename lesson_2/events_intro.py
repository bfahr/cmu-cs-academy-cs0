"""
CS0 Lesson 2 - Events
=====================

There are events that you can capture in your program to get input from the
user.  All of the events that are available can be found in the documentation
here:

https://academy.cs.cmu.edu/docs#eventFunctions

One of these events is "onMousePress".  This event is triggered when
the user clicks the mouse button and has 2 arguments "mouseX" and "mouseY",
the X and Y position of the mouse pointer when the button was clicked.
When you create a function in your code with this name and arguments then
the graphics system will perform its processing and then it will call your
function and pass in the two required arguments. You don't have to do anything
else to make it work other than to declare it with the same name and arguments.
"""

# Lets define a function to handle the onMousePress event.  As long as your
# application is running this function will be called every time a mouse
# button is clicked
def onMousePress(mouseX, mouseY):
    print('Mouse X:', mouseX)
    print('Mouse Y:', mouseY)


# Now lets keep track of the number of times the function is called
# We'll use a global variable "click_count" that is defined and initialized
# outside of the function.  Inside the function you can access global
# variables, but if variables are defined inside the function they go away
# (out of scope) when the function is exited.

# Comment out the onMousePress function above and uncomment the code
# below to run it instead.
#
# HINT: you can select the lines and then click
# on the icon that looks like a caption, named "toggle comment".  This will
# add comments if they are not present, and remove them if they are.

# # Create a circle shape object and save it in a variable
# c1 = Circle(100, 200, 50, fill=gradient('yellow', 'blue', start='left'))

# # Create a global variable for counting mouse clicks and initialize it to 0
# click_count = 0

# def onMousePress(mouseX, mouseY):
#     # Variables in this program that are not shape objects must be
#     # declared as global to avoid an error
#     global click_count

#     # Increment the global click_count variable by 1
#     click_count = click_count + 1
    
#     # Rotate the circle angle by 45 degrees
#     # Shape objects are global by default so no need to declare them
#     # as global
#     c1.rotateAngle += 45
    
#     # Now show the values
#     print('--------------------')
#     print('Mouse X     :', mouseX)
#     print('Mouse Y     :', mouseY)
#     print('Click Count :', click_count)
#     print('Shape Object:', c1)
