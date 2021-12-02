import turtle
drawing = open("external_turtle_file_windows.txt", "r", encoding = "utf16")
scr = turtle.Screen()
c = turtle.Turtle()
style = ('Courier', 30)

#First loop
for aline in drawing:

    turtlist = aline.split()
    #print (turtlist)

    if turtlist[0] == "UP":
        c.penup()
    
    else:
        if turtlist[0] == "DOWN":
            c.pendown()
        

    
        else:
            #Has to be coordinates
            c.goto(int(turtlist[0]), int(turtlist[1]))
drawing.close()

name = str(input("What is the Turtle's new name? "))
fname = str(input("What is the file's name? "))
pencol = str(input("What is the pen color? "))
backcol = str(input("What is the background color? "))
scr.clearscreen()

original = open("external_turtle_file_windows.txt", "r", encoding = "utf16")
newfile = open("{}.txt".format(fname), "w")

each_line = original.read()
newfile.write(fname + '\n')
newfile.write(backcol + '\n')
newfile.write(pencol + '\n')
for adding in each_line:
    newfile.write(adding)
newfile.write(name + '\n')
newfile.close
#Add the things to the new file

c = turtle.Turtle()
finale = open("{}.txt".format(fname), "r", encoding = "utf16")
#Open and read the new things in the file

#Program bricks past this line THIS IS HARD
# for fline in finale:
#     ftlist = fline.split()

#     if ftlist[0] == fname:
#         ct.penup()
#         ct.goto(100,100)
#         ct.write(fname, font = style)
#         ct.goto(0,0)
#         ct.pendown

#     elif ftlist[0] == pencol:
#         ct.color(pencol)
    
#     elif ftlist[0] == backcol:
#         scr.bgcolor(backcol)
    
#     else:
#         if turtlist[0] == "UP":
#             ct.penup()
        
#         elif turtlist[0] == "DOWN":
#             ct.pendown()
        
#         elif turtlist[0] == name:
#             ct.penup
#             ct.goto(100,80)
#             ct.write("Drawn by {}".format(name), font = style)
#             ct.goto(0,0)
    
#         else:
#             #Has to be coordinates
#             c.goto(int(turtlist[0]), int(turtlist[1]))
#Below this is the copout
c.color(pencol)
scr.bgcolor(backcol)
drawing = open("external_turtle_file_windows.txt", "r", encoding = "utf16")
for aline in drawing:

    turtlist = aline.split()
    #print (turtlist)

    if turtlist[0] == "UP":
        c.penup()
    
    else:
        if turtlist[0] == "DOWN":
            c.pendown()
        

    
        else:
            #Has to be coordinates
            c.goto(int(turtlist[0]), int(turtlist[1]))
drawing.close()
c.penup()
c.goto(100,100)
c.write(fname)
c.goto(100, 80)
c.write("Drawn by {}".format(name))
print("Thank you for using my program!")

scr.exitonclick()
