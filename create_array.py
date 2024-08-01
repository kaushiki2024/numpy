import numpy as numpy
arr1=numpy.array([1,2,3,4])
print(arr1)
print(arr1.dtype)
print(arr1.shape)
print(type(arr1))
arr2=numpy.array([[1,2,3,4],[5,6,7,5]])
print(arr2)
print(arr2.shape)
arr3=numpy.zeros((2,3))                   
print(arr3)                  
arr4=numpy.ones((3,4))
print(arr4)
arr5=numpy.identity(6) 
print(arr5)
arr6=numpy.arange(10,13,2)
print(arr6)
arr7=numpy.linspace(0,20,5)#difference
print(arr7)
print(arr7.shape)
arr8 = numpy.array([1,2,3,4],ndmin=10)#convert into n-dimensional array
print(arr8)
arr9=numpy.empty(4)
print(arr9)
arr10=numpy.eye(3,5)
print(arr10)

n = input("Enter a string: ")  # Takes an input string from the user
l = list(n)  # Converts the input string into a list of characters
l.reverse()  # Reverses the list of characters
reversed_string = ''.join(l)  # Joins the reversed list into a string
print(int(reversed_string))  # Prints the reversed string
x,y,z=1,2,3
print(x,y,z)
i=0
while(i<3):
   print(i)
   i=i+1
else:
  print(0)