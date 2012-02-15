#euler project problem 18

#quickest route through triangle

#triangle in list form

triangle = [
 [75],
 [95, 64],
 [17, 47, 82],
 [18, 35, 87, 10],
 [20, 04, 82, 47, 65],
 [19, 01, 23, 75, 03, 34],
 [88, 02, 77, 73, 07, 63, 67],
 [99, 65, 04, 28, 06, 16, 70, 92],
 [41, 41, 26, 56, 83, 40, 80, 70, 33],
 [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
 [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
 [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
 [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
 [63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
 [04, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 04, 23]]

#flip the triangle
triangle.reverse()


#side = len(triangle)
side = 15
#x is row, y is element inside row

for x in xrange(0,15):
    for y in xrange(0, side - x):
	max = 0
	if y+1 == side - x:
	    break
	max = triangle[x][y]+triangle[x+1][y]
	    
	if triangle[x][y+1] + triangle[x+1][y] > max:
	    max = triangle[x][y+1] + triangle[x+1][y]
	triangle[x+1][y] = max
	#print max
    print triangle[x]
#print triangle[x]    
