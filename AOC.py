#to find area of circle
def circ_Area(rad):
	PI = 3.142
	return PI * (rad*rad);

rad = float(input('Enter the radius of the circle: '))
print("Area of the circle is %.6f" % circ_Area(rad));
