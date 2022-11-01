#Joel Wilkins
#03/08
#password



password=input('Please enter a password: ')
if len(password)<8:
  password=input('Password must be at least 8 characters long.\nPlease enter again: ')
passwordcount=0
passwordlimit=5
while passwordcount<passwordlimit:
  password2=input('Please enter password again to validate: ')
  passwordcount+=1
  if password2!=password:
    print('Passwords do not match')
  if passwordcount>=passwordlimit:
    print('You have ran out of attempts.')
  elif password2==password:
    print('This password is valid')