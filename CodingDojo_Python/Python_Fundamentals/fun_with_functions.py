# def odd_even():
#     for i in range(1,2001):
#         if i%2 == 0:
#             print "Numer is {}. This is an even number.".format(i)
#         else:
#             print "Number is {}. This is an odd number.".format(i)
# odd_even() #call the function

# Create a program that counts from 1 to 2000. As it loops through each number, have your program
# generate the number and whether it's an odd number or whether it's an even number

# for i in range(1,2001):
#     if i % 2 == 0:
#         print 'Number is ' + str(i) + '. This is an odd number.'
#     else:
#         print 'Number is ' + str(i) + '. This is an even number.'



def multiply(arr,num):
    for i in range(len(arr)):
        arr[i] *= num
    return arr
a = [2,4,10,16]
b = multiply(a,5)
print b
