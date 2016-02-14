import sys
import random

MAPXLEN = 100
MAPYLEN = 60


mymap = [(['0'] * MAPYLEN) for i in range(MAPXLEN)]

direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def drawRoom(x, y):
	print 'room'

def drawChest(x, y):
	print 'chest'

choiceOperator = {0:drawRoom, 1: drawChest}

def isPointValid(x, y):
	if x < 0 or x >= MAPXLEN:
		return False
	if y < 0 or y >= MAPYLEN:
		return False
	return True

def getEdges(x1, x2, y1, y2):
	edges = []
	# for x in range(x1, x2+1):
	for x in range(x1, x2):
		if isPointValid(x, y2) and mymap[x][y2] == '0':
			edges.append([x, y2])
		if isPointValid(x, y1-1) and mymap[x][y1-1] == '0':
			edges.append([x, y1-1])
	for y in range(y1, y2):
		if isPointValid(x2, y) and mymap[x2][y] == '0':
			edges.append([x2, y])
		if isPointValid(x1-1, y) and mymap[x1-1][y] == '0':
			edges.append([x1-1, y])
	return edges

def printMap():
	for row in mymap:
		for ele in row:
			print ele,
		print ''

def smoothRange(corridorRange):
	if corridorRange[0] > corridorRange[1]:
		tmp = corridorRange[0]
		corridorRange[0] = corridorRange[1]
		corridorRange[1] = tmp
	if corridorRange[2] > corridorRange[3]:
		tmp = corridorRange[2]
		corridorRange[2] = corridorRange[3]
		corridorRange[3] = tmp
	corridorRange[0] = corridorRange[0] if corridorRange[0] >= 0 else 0
	corridorRange[1] = corridorRange[1] if corridorRange[1] < MAPXLEN else MAPXLEN - 1
	corridorRange[2] = corridorRange[2] if corridorRange[2] >= 0 else 0
	corridorRange[3] = corridorRange[3] if corridorRange[3] < MAPYLEN else MAPYLEN - 1
	return corridorRange

def drawCorridor(corridorRange):
	for x in range(corridorRange[0], corridorRange[1]+1):
		for y in range(corridorRange[2], corridorRange[3]+1):
			if mymap[x][y] == '0':
				mymap[x][y] = '.'


def isEdge(point):
	if point[0] <= 0 or point[0] >= MAPXLEN:
		return True
	if point[1] <= 0 or point[1] >= MAPYLEN:
		return True
	return False

def drawMap(edges):
	if len(edges) == 0:
		return
	for edge in edges:
		mymap[edge[0]][edge[1]] = 'W'
	doorPoints = []
	# Generate 2~4 doors
	doorNum = random.randint(2, 5)
	for n in range(doorNum):
		doorPoint = edges[random.randint(0, len(edges)-1)]
		print 'doorpoint', doorPoint
		if isEdge(doorPoint):
			continue
		mymap[doorPoint[0]][doorPoint[1]] = 'D'
		doorPoints.append(doorPoint)

	for point in doorPoints:
		for i in range(4):
			xx = point[0] + direction[i][0]
			yy = point[1] + direction[i][1]
			if not isPointValid(xx, yy):
				continue
			if mymap[xx][yy] == '0':
				print 'x and y: forward point', xx, yy
				# Draw corridor
				tmpLen = random.randint(5, 10)
				corridorLen = [direction[i][0]*tmpLen, direction[i][1]*tmpLen]
				# Check whether corridor is validate or not
				corridorRange = [0]*4
				if corridorLen[0] == 0:
					corridorRange = [xx-1, xx+1, yy, yy+corridorLen[1]]
				elif corridorLen[1] == 0:
					corridorRange = [xx, xx+corridorLen[0], yy-1, yy+1]
				corridorRange = smoothRange(corridorRange)
				drawCorridor(corridorRange)
				print 'range', corridorRange
				edges = getEdges(corridorRange[0], corridorRange[1]+1, corridorRange[2], corridorRange[3]+1)
				print 'edges', edges
				# printMap()
				print ''
				drawMap(edges)
				# drawMap(xx, yy)

def main():
	# choice = random.randint(0, 1)
	# choiceOperator.get(choice)(x, y)
	width = 20
	height = 20
	for i in range(width):
		for j in range(height):
			mymap[i][j] = '.'
	edges = getEdges(0, width, 0, height)
	drawMap(edges)
	printMap()

if __name__ == '__main__':
	main()