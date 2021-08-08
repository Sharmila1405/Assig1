

import math
radius = float(input("Input the radius of a circle: "));
area = math.pi*radius**2;
print("The area of the circle with radius {} is: {}".format(radius,area));



dict = {"py":"python","java":"Java","c":"C","hmt":"Html"} 
filename = input("Input the Filename: ");

s = filename.split(".");

print("The extension of the file is : {}".format(dict.get(s[-1])));


