from VDgames.cli import welcome_user

def greeter():
	print("Welcome to the VD-games!")
	name = welcome_user()
	return name
