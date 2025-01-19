numbers1=[1,2,3]
numbers2=[4,5,6]
results=map(lambda x,y: x+y,numbers1,numbers2)
print("Addition of two lists")
print(list(results))

nums=[1,2,3,4,5]
def sq (n):
    n*n
square=list(map(sq,nums))
print("Number of squares in list")
print("Square")
