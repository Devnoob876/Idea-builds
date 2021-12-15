def solution(string,markers):
    for i in markers:
        string = string.replace(i, "")
        
    return string

def test():
	test1 = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])

	print(test1)
	#test2 = main()
	#test3 = main()

test()