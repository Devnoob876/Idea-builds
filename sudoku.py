test = [
[0, 5, 0, 3, 1, 4, 0, 6, 0],

[8, 7, 0, 0, 0, 9, 4, 0, 3],

[6, 4, 3, 5, 0, 7, 1, 9, 2],

[0, 0, 7, 8, 0, 5, 2, 1, 0],

[4, 1, 0, 9, 0, 0, 0, 0, 0],

[0, 2, 5, 0, 6, 1, 9, 0, 7],

[7, 9, 0, 2, 5, 0, 8, 4, 0],

[0, 0, 4, 0, 9, 6, 0, 0, 5],

[0, 3, 0, 1, 0, 8, 6, 7, 0]
]


def possible(row, column, number):
	for i in range(9):
		if test[row][i] == number:
			return False

	for i in range(9):
		if test[i][column] == number:
			return False

	y0 = (row // 3) * 3
	x0 = (column // 3) * 3
	for i in range(0,3):
		for j in range(0,3):
			if test[y0+i][x0+j] == number:
				return False

	return True
def solve():
	for row in range(0,9):
		for column in range(0,9):
			if test[row][column] == 0:
				for number in range(1,10):
					if possible(row, column, number):
						test[row][column] = number
						solve()
						test[row][column] = 0
				return
	print(test)
solve()





