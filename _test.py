from board import Board
from game import Game
from player import Player

import sys

class TestSession:


	def __init__(self):

		self.tests = []
		self.completedCount = 0
		

	# runs all pass fail tests and gives summary
	def allPassFail():

		print("====================================")
		print(" ... | Result | Test Description")
		print("====================================")

		for f, args in tests:
			result, details = passFail(f, args)
			print(estimateProgress().ljust(4) + " | " result.ljust(6) + " | " + str(f))
			


	# runs a single pass/fail test
	def passFail(self, f, args):

		try:
			result = f(*args)

		except:
			result = ["Error", sys.exec_info()]

		return result

	def estimateProgress(self):
		self.completedCount += 1
		return str(int(self.completedCount / len(self.tests))) + "%"

	def addTest(self, f, args):
		self.tests.append([f, args])

	

def checkMove(given, expected, whiteTurn, move)
	
	


# startup a test session
if __name__	== "__main__":

	ts = TestSession()
	ts.allPassFail()	
