#IMPORTING
from sklearn import linear_model
import math

#DEFINING
regr = linear_model.LinearRegression()

#DATA SET FOR THE SIDES
X=[
	[0,0.693147180559945,1.09861228866811],
	[1.38629436111989,1.6094379124341,1.79175946922805],
	[1.09861228866811,1.38629436111989,1.6094378124341],
	[1.6094379124341,1.79175946922805,1.94591014905531]
  ]
  
#DATA SET FOR THE VOLUMES
Y=[
	1.791759469,
	4.787491743,
	4.094344562,
	5.347107531
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
