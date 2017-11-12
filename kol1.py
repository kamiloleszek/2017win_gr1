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





class Bank:

	def __init__(self, clients, name):

		self.list_of_clients = clients

		self.bank_name = name



	def client_information(self, client):

		return self.list_of_clients[self.list_of_clients.index(client)].first_name + ' ' + self.list_of_clients[self.list_of_clients.index(client)].last_name + ', account balance: ' + str(self.list_of_clients[self.list_of_clients.index(client)].account)





	def add_client(self, client):

		self.list_of_clients.append(client)

	def remove_client(self, client):
		if client in self.list_of_clients:

			self.list_of_clients.remove(client)
		else:
			return 'There is no such a client in this bank'



	def dump(self, filename):

		with open(filename, 'w') as file:

			for client in self.list_of_clients:

				file.write(self.client_information(client) + '\n')



#---------------------------------------------------

class Client:

	def __init__(self, first_name, last_name, account):

		self.first_name = first_name

		self.last_name = last_name

		self.account = account



#---------------------------------------------------	

class Transaction:

#	If we pass two clients it's essential that we want to make cash transfer operation. Convention: client1 is a source of cash transfer and belongs to bank1, client2 is a target of transaction and belongs to bank2. Otherwise I would have to specify source and target and then check which one belongs to bank1 and bank2.

	def __init__(self, bank1, client1, bank2 = None, client2 = None):

		self.client1 = client1

		self.client2 = client2

		self.bank1 = bank1

		self.bank2 = bank2

	

	def cash_input(self, amount_of_money):

		client_id = self.bank1.list_of_clients.index(self.client1)

		account_balance_before_transaction = self.bank1.list_of_clients[client_id].account

		self.bank1.list_of_clients[client_id].account += amount_of_money

		if self.bank1.list_of_clients[client_id].account == account_balance_before_transaction + amount_of_money:

			return 'OK. Operation commited.'

		else:

			self.bank1.list_of_clients[client_id].account = account_balance_before_transaction

			return 'FAIL. Operation rolled back.'



	def cash_withdrawal(self, amount_of_money):

		client_id = self.bank1.list_of_clients.index(self.client1)

		account_balance_before_transaction = self.bank1.list_of_clients[client_id].account

		if account_balance_before_transaction < amount_of_money:
			return 'You dont have such amount of money to withdraw'
		else:

			self.bank1.list_of_clients[client_id].account -= amount_of_money

			if self.bank1.list_of_clients[client_id].account == account_balance_before_transaction - amount_of_money:

				return 'OK. Operation commited.'

			else:

				self.bank1.list_of_clients[client_id].account = account_balance_before_transaction

				return 'FAIL. Operation rolled back.'



	def cash_transfer(self, amount_of_money):

		if self.client2 is None:

			raise Exception('Too few arguments! If you want to make a cash transfer operation you have to specify two clients')

		else:

			if self.bank2 is None:

				client1_id = self.bank1.list_of_clients.index(self.client1)

				client2_id = self.bank1.list_of_clients.index(self.client2)



				account_balance_client1_before_transaction = self.bank1.list_of_clients[client1_id].account

				account_balance_client2_before_transaction = self.bank1.list_of_clients[client2_id].account


				if account_balance_client1_before_transaction < amount_of_money:
					return 'Your account balance is less than the amount of money to transfer'
				else:

					self.bank1.list_of_clients[client1_id].account -= amount_of_money

					self.bank1.list_of_clients[client2_id].account += amount_of_money



					if self.bank1.list_of_clients[client1_id].account == account_balance_client1_before_transaction - amount_of_money and self.bank1.list_of_clients[client2_id].account == account_balance_client2_before_transaction + amount_of_money:

						return 'OK. Operation commited.'

					else:

						self.bank1.list_of_clients[client1_id].account = account_balance_client1_before_transaction

						self.bank1.list_of_clients[client2_id].account = account_balance_client2_before_transaction

						return 'FAIL. Operation rolled back.'

			else:

				client1_id = self.bank1.list_of_clients.index(self.client1)

				client2_id = self.bank2.list_of_clients.index(self.client2)

				commission = 5.0



				account_balance_client1_before_transaction = self.bank1.list_of_clients[client1_id].account

				account_balance_client2_before_transaction = self.bank2.list_of_clients[client2_id].account


				if account_balance_client1_before_transaction < amount_of_money:
					return 'Your account balance is less than the amount of money to transfer'
				else:

					self.bank1.list_of_clients[client1_id].account -= (amount_of_money + commission)

					self.bank2.list_of_clients[client2_id].account += amount_of_money



					if self.bank1.list_of_clients[client1_id].account == account_balance_client1_before_transaction - amount_of_money - commission and self.bank2.list_of_clients[client2_id].account == account_balance_client2_before_transaction + amount_of_money:

						return 'OK. Operation commited.'

					else:

						self.bank1.list_of_clients[client1_id].account = account_balance_client1_before_transaction

						self.bank2.list_of_clients[client2_id].account = account_balance_client2_before_transaction

						return 'FAIL. Operation rolled back.'





if __name__ == "__main__":	

	alex_wheeler = Client("Alex", "Wheeler", 0.0)

	bob_ryan = Client("Bob", "Ryan", 100.0)

	michael_geig = Client("Michael", "Geig", 34.0)

	thomas_castley = Client("Thomas", "Castley", 10.0)

	magnus_brown = Client("Magnus", "Brown", 1020.5)

	rob_windsor = Client("Rob", "Windsor", 446.23)
	patrick_klein = Client("Patrick", "Klein", 0.0)



	mbank_list_of_clients = [alex_wheeler, bob_ryan, michael_geig, thomas_castley]

	mbank = Bank(mbank_list_of_clients, 'mbank')

	aliorbank_list_of_clients = [magnus_brown]

	aliorbank = Bank(aliorbank_list_of_clients, 'aliorbank')

	aliorbank.add_client(rob_windsor)
	mbank.add_client(patrick_klein)
	mbank.remove_client(patrick_klein)

	print



	#Information about all mbank clients
	for client in mbank.list_of_clients:
		print(mbank.client_information(client))

	print



	#Cash input for alex_wheeler

	alex_wheeler_transaction = Transaction(mbank, alex_wheeler)

	print('Begin Alex Wheeler transaction: cash input')
	money = input('Alex, how much money do you want to input?\n')

	result_alex_wheeler_transaction = alex_wheeler_transaction.cash_input(money)

	print(result_alex_wheeler_transaction)

	print(mbank.client_information(alex_wheeler))

	print



	#Cash withdrawal for bob_ryan

	bob_ryan_transaction = Transaction(mbank, bob_ryan)

	print('Begin Bob Ryan transaction: cash withdrawal')
	money = input('Bob, how much money do you want to withdraw?\n')

	result_bob_ryan_transaction = bob_ryan_transaction.cash_withdrawal(money)

	print(result_bob_ryan_transaction)

	print(mbank.client_information(bob_ryan))

	print



	#Cash transfer within the same bank

	michael_geig_thomas_castley_transaction = Transaction(mbank, michael_geig, None, thomas_castley)

	print('Begin Michael Geig - Thomas Castley transaction: cash transfer')
	money = input('Michael, how much money do you want to send to Thomas account?\n')

	result_michael_geig_thomas_castley_transaction = michael_geig_thomas_castley_transaction.cash_transfer(money)

	print(result_michael_geig_thomas_castley_transaction)

	print(mbank.client_information(michael_geig))

	print(mbank.client_information(thomas_castley))

	print



	#Cash transfer from one bank to another one

	magnus_brown_thomas_castley_transaction = Transaction(aliorbank, magnus_brown, mbank, thomas_castley)

	print('Begin Magnus Brown - Thomas Castley transaction: cash transfer')
	money = input('Magnus, how much money do you want to send to Thomas account?\n')

	result_magnus_brown_thomas_castley_transaction = magnus_brown_thomas_castley_transaction.cash_transfer(money)

	print(result_magnus_brown_thomas_castley_transaction)

	print(aliorbank.client_information(magnus_brown))

	print(mbank.client_information(thomas_castley))

	print



	#Dump of mbank and aliorbank

	mbank.dump('mbank.txt')
	aliorbank.dump('aliorbank.txt')







