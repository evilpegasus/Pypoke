[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/gluten-free.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/you-didnt-ask-for-this.svg)](https://forthebadge.com)
# Pypoke
A Selenium Python bot to automate poking your Facebook friends
## Usage
Clone the files and run [pypoke.py](pypoke.py)
### Login
By default, the terminal will prompt for a username and password.

You can store your login credentials by writting your credentials into [secrets.py](secrets.py) and using the following call at the bottom of [pypoke.py](pypoke.py)
```
pypoke(username(), password())
```
instead of the default prompt
```
pypoke(input("Username: "), getpass("Password (input is hidden): "))
```