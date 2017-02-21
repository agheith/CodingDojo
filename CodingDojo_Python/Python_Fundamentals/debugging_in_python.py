  # def multiply(arr,num):
  # a = [2,4,10,16]
  # b = multiply(a,5)
  # print b



def multiply(arr,num):
    # print arr, num #first step
    for i in arr:
        i *= num
    return arr
a = [2,4,10,16]
b = multiply(a,5)
print b
