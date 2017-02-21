# str = "If monkeys like bananas, then I must be a monkey!"
# print str.find("monkey")
# print str.replace("monkey", "alligator")
#
#
# x = [2,54,-2,7,12,98]
# print max(x)
# print min(x)
#
# x = ["hello",2,54,-2,7,12,98,"world"]
# new_list = [x[0],x[-1]]
# print [x[0],x[-1]]
# print new_list



x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
y = []
def removeNeg()
for i in range(len(x)):
    if x[i] < 0:
        y.append(x[i])
    return removeNeg()
print x.insert(0,y),x



# x.sort()
# slice = x[0:2]
# x.insert(0,slice)
# x.pop(1)
# x.pop(1)
# print x
