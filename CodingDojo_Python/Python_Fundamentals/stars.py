x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
def draw_stars(list):
    for i in range(0,len(list),1):
        if type(list[i]) is int:      #set up conditional on integer type
            num = "*"*(list[i])
            print num
        elif type(list[i]) is str:     #set up conditional on string type
            string = list[i][:1]*(len(list[i]))   #print the first digit of the string mulitpied by the length of the string
            print string.lower()

print draw_stars(x)



x = [4, 6, 1, 3, 5, 7, 25]
def draw_stars():
    for i in xrange(0,len(x),1):
        i = "*"*(x[i])

        print i
print draw_stars()


# worked with Willie Shubert
