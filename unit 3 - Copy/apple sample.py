#   a123_apple_1.py
import random as rand
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("tree.png")

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

applelist = []
appleletters = []

for i in range(5):
  applelist.append(trtl.Turtle())
  appleletters.append(rand.choice(letters))


#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(index):
  applelist[index].pu()
  applelist[index].shape(apple_image)
  wn.tracer(False)
  applelist[index].sety(rand.randint(-25,240))
  applelist[index].setx(rand.randint(-250,250))
  applelist[index].sety(applelist[index].ycor()-40)
  applelist[index].color("white")
  applelist[index].write(appleletters[index], align="center" ,font=("Arial", 55, "bold")) 
  applelist[index].sety(applelist[index].ycor()+40)
  applelist[index].showturtle()
  wn.tracer(True)
  wn.update()

def apple_falls(index):
  applelist[index].pu()
  applelist[index].clear()
  applelist[index].sety(-150)
  applelist[index].hideturtle()
  appleletters[index] = rand.choice(letters)
  draw_apple(index)
  
  
def typeda():
  if i in range(5) and appleletters[i] == "a":
    apple_falls(i)

def typedb():
  if i in range(5) and appleletters[i] == "b":
    apple_falls(i)

def typedc():
  if i in range(5) and appleletters[i] == "c":
    apple_falls(i)

def typedd():
  if i in range(5) and appleletters[i] == "d":
    apple_falls(i)

def typede():
  if i in range(5) and appleletters[i] == "e":
    apple_falls(i)

def typedf():
  if i in range(5) and appleletters[i] == "f":
    apple_falls(i)

def typedg():
  if i in range(5) and appleletters[i] == "g":
    apple_falls(i)

def typedh():
  if i in range(5) and appleletters[i] == "h":
    apple_falls(i)

def typedi():
  if i in range(5) and appleletters[i] == "i":
    apple_falls(i)

def typedj():
  if i in range(5) and appleletters[i] == "j":
    apple_falls(i)

def typedk():
  if i in range(5) and appleletters[i] == "k":
    apple_falls(i)

def typedl():
  if i in range(5) and appleletters[i] == "l":
    apple_falls(i)

def typedm():
  if i in range(5) and appleletters[i] == "m":
    apple_falls(i)

def typedn():
  if i in range(5) and appleletters[i] == "n":
    apple_falls(i)

def typedo():
  if i in range(5) and appleletters[i] == "o":
    apple_falls(i)

def typedp():
  if i in range(5) and appleletters[i] == "p":
    apple_falls(i)

def typedq():
  if i in range(5) and appleletters[i] == "q":
    apple_falls(i)

def typedr():
  if i in range(5) and appleletters[i] == "r":
    apple_falls(i)

def typeds():
  if i in range(5) and appleletters[i] == "s":
    apple_falls(i)

def typedt():
  if i in range(5) and appleletters[i] == "t":
    apple_falls(i)

def typedu():
  if i in range(5) and appleletters[i] == "u":
    apple_falls(i)

def typedv():
  if i in range(5) and appleletters[i] == "v":
    apple_falls(i)

def typedw():
  if i in range(5) and appleletters[i] == "w":
    apple_falls(i)

def typedx():
  if i in range(5) and appleletters[i] == "x":
    apple_falls(i)

def typedy():
  if i in range(5) and appleletters[i] == "y":
    apple_falls(i)

def typedz():
  if i in range(5) and appleletters[i] == "z":
    apple_falls(i)


#-----function calls-----
for i in range(5):
  draw_apple(i)

wn.onkeypress(typeda, "a")
wn.onkeypress(typedb, "b")
wn.onkeypress(typedc, "c")
wn.onkeypress(typedd, "d")
wn.onkeypress(typede, "e")
wn.onkeypress(typedf, "f")
wn.onkeypress(typedg, "g")
wn.onkeypress(typedh, "h")
wn.onkeypress(typedi, "i")
wn.onkeypress(typedj, "j")
wn.onkeypress(typedk, "k")
wn.onkeypress(typedl, "l")
wn.onkeypress(typedm, "m")
wn.onkeypress(typedn, "n")
wn.onkeypress(typedo, "o")
wn.onkeypress(typedp, "p")
wn.onkeypress(typedq, "q")
wn.onkeypress(typedr, "r")
wn.onkeypress(typeds, "s")
wn.onkeypress(typedt, "t")
wn.onkeypress(typedu, "u")
wn.onkeypress(typedv, "v")
wn.onkeypress(typedw, "w")
wn.onkeypress(typedx, "x")
wn.onkeypress(typedy, "y")
wn.onkeypress(typedz, "z")

wn.listen()
wn.mainloop()
