from myFunctions import *
stars(100, 2)
moon(-250, 100, 600)
mountain(-300, -300, 400, 500)
mountain(0, -300, 200, 300)
grass(1000, -480, -400)
clouds(100, 100, 20,40)
clouds(-350, 75, 20, 40)
for _ in range(10):
    x = randint(-480, 480)
    size = randint(35, 50)
    trees(x, -300, size)
# ignore this tree, Used for fixing the tree function.
trees(10000, -300, 40)
turtle.done()