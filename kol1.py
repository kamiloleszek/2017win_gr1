#Banking simulator. Write a code in python that simulates the banking system. 
#The program should:
# - be able to create new banks
# - store client information in banks
# - allow for cash input and withdrawal
# - allow for money transfer from client to client
#If you can thing of any other features, you can add them.
#This code shoud be runnable with 'python kol1.py'.
#You don't need to use user input, just show me in the script that the structure of your code works.
#If you have spare time you can implement: Command Line Interface, some kind of data storage, or even multiprocessing.
#Do your best, show off with good, clean, well structured code - this is more important than number of features.
#After you finish, be sure to UPLOAD this (add, commit, push) to the remote repository.
#Good Luck

#!/usr/bin/env python2.7

class Bank:
	def __init__(self, clients):
		self.listOfClients = clients

	def cashInput(self, ident, moneyAmount):
		self.listOfClients[ident].account = self.listOfClients[ident].account + moneyAmount

	def cashWithdrawal(self, ident, moneyAmount):
		self.listOfClients[ident].account = self.listOfClients[ident].account - moneyAmount

	def cashTransfer(self, identFrom, identTo, moneyAmount):
		self.listOfClients[identFrom].account = self.listOfClients[identFrom].account - moneyAmount
		self.listOfClients[identTo].account = self.listOfClients[identTo].account + moneyAmount
		

	def clientInformation(self, ident):
		print('First name: ' + self.listOfClients[ident].fname)
		print('Last name: ' + self.listOfClients[ident].lname)
		print('ClientId number: ' + self.listOfClients[ident].ident)
		print('Amount of money: ' + self.listOfClients[ident].account)

class Client:
	def __init__(self, fname, lname, ident, account):
		self.fname = fname
		self.lname = lname
		self.ident = ident
		self.account = account

client1 = Client("John", "Kowalsky", 0, 0.0)
client2 = Client("Bob", "Ryan", 1, 100.0)
client3 = Client("John", "Kowalsky", 2, 34.0)
client4 = Client("Bob", "Ryan", 3, 10.0)

listOfClients = [client1, client2, client3, client4]
mbank = Bank(listOfClients)

mbank.clientInformation(0)
mbank.clientInformation(1)
mbank.clientInformation(2)
mbank.clientInformation(3)

mbank.cashInput(0, 53.0)
mbank.clientInformation(0)

mbank.cashWithdrawal(1, 22.5)
mbank.clientInformation(1)

mbank.cashTransfer(3, 4, 10.0)
mbank.clientInformation(3)
mbank.clientInformation(4)




