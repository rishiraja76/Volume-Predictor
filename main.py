#IMPORTING
from sklearn import linear_model
import math

#DEFINING
regr = linear_model.LinearRegression()

#DATA SET FOR THE SIDES
X=[
	[],
	[],
	[],
	[]
  ]
  
#DATA SET FOR THE VOLUMES
Y=[
	,
	,
	,
	
  ]
  
#LEARNING
regr.fit(X,Y)

#print regr.coef_#

#INPUTING
l=int(raw_input("Enter length"))
b=int(raw_input("Enter breadth"))
h=int(raw_input("Enter height"))

#CONVERTING
l=math.log10(l)
b=math.log10(b)
h=math.log10(h)

#PREDICTING
v=regr.predict([[ l, b, h]])

#CONVERTING
v=math.pow(10, v)
v=int(v)

#OUTPUTING
print " "
print "Approx volume is",v