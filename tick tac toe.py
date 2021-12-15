import os


board = {
	"b1": "-", "b2": "-", "b3": '-',

	"b4": "-", "b5": "-", "b6": "-",

	"b7": "-", "b8": "-", "b9": "-"
}



def p1Input():	# player 1 or X's input
	draw = boardDraw()
	print(draw)
	player1 = input("p1:")
	if player1 in board:
		if board[player1] == "X" or board[player1] == "O":
			print(player1)
			print("sorry the requested position is occupied with X")
			p1Input()
		elif board[player1] == "-":
			board[player1] = "X"
			gameChecker("player2")
	else:
		print("entered wrong position of the board")
		p1Input()

def p2Input(): 	# player 2 or O's input
	draw = boardDraw()
	print(draw)
	player2 = input("p2:")
	if player2 in board:
		if board[player2] == "X" or board[player2] == "O":
			print("sorry the requested position is occupied with O" )
			p2Input()
		elif board[player2] == "-":
			board[player2] = "O"
			gameChecker("player1")
	else:
		print("entered wrong position of the board")
		p2Input()


def gameChecker(who):	# checking the board if theres a winner 
	os.system('cls')
	if board["b1"] == board["b2"] == board["b3"] and board["b1"] != '-':
		winner(board["b1"])
	elif board["b4"] == board["b5"] == board["b6"] and board["b4"] != '-':
		winner(board["b4"])
	elif board["b7"] == board["b8"] == board["b9"] and board["b7"] != '-':
		winner(board["b7"])
	elif board["b1"] == board["b4"] == board["b7"] and board["b1"] != '-':
		winner(board["b1"])
	elif board["b2"] == board["b5"] == board["b8"] and board["b2"] != '-':
		winner(board["b2"])
	elif board["b3"] == board["b6"] == board["b9"] and board["b3"] != '-':
		winner(board["b3"])
	elif board["b1"] == board["b5"] == board["b9"] and board["b1"] != '-':
		winner(board["b1"])
	elif board["b3"] == board["b5"] == board["b7"] and board["b3"] != '-':
		winner(board["b3"])

	elif '-' not in board.values():
		winner("draw")
	else: 
		functionControl[who]()



def winner(p):	# winner handler
	print(boardDraw())
	if p != "draw":
		print(p + "is the winner")
		
	else:
		print(p)
	print("Do you want to play again?\n 1) Hell yea!\n 2) Nope imma out")
	inp = int(input())
	if inp == 2:
		exit()
	if inp == 1:
		os.system('cls')
		board["b1"] = '-'
		board["b2"] = '-'
		board["b3"] = '-'
		board["b4"] = '-'
		board["b5"] = '-'
		board["b6"] = '-'
		board["b7"] = '-'
		board["b8"] = '-'
		board["b9"] = '-'
		p1Input()


		
functionControl = {
	"player1": p1Input,
	"player2": p2Input

}

def boardDraw():
	game = f"""
	{board["b1"]}|{board["b2"]}|{board["b3"]}
	 | | 
	{board["b4"]}|{board["b5"]}|{board["b6"]}
	 | | 
	{board["b7"]}|{board["b8"]}|{board["b9"]}
	"""
	return game



if __name__ == "__main__":
	# main()
	p1Input()