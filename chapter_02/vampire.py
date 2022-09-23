name = 'Carol'
age = 3
msg = f"Your age is {str(age)} and "
if name == 'Alice':
    print(msg, 'Hi, Alice.')
elif age < 12:
    print(msg, 'You are not Alice, kiddo.')
elif age > 2000:
    print(msg, 'Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print(msg, 'You are not Alice, grannie.')