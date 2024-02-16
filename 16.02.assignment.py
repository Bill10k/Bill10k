# List of current users (all lowercase for case insensitive comparison)
current_users = ['precious', 'peter', 'jesse', 'david', 'kobby']


new_users = ['kobby', 'phlip', 'asamoah', 'bill', 'elaine']


for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"The username {new_user} is already in use. Please enter a new username.")
    else:
        print(f"The username {new_user} is available.")

# Loop from 1 to 100
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
