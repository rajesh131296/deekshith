a = ['lord krishna','lord rama','lord vinayaka','lord lakshmi']

for i in a:
    if i == 'lord rama':
        print("my favorite god is {}".format(i))
    elif i == 'lord lakshmi':
        print("my favorite goddess is {0}".format(i))
    elif i == 'lord vinayaka':
        print(f"{i} festival coming soon")
    else:
        print("your favourite god name is not available")
