import random

friends = {}
lucky_feature = False
lucky = None

print('Enter the number of friends joining (including you):')
num = int(input())
print()

if num > 0:
    print('Enter the name of every friend (including you), each on a new line:')
    for _ in range(num):
        friend = input()
        friends[friend] = 0
    print()
    print('Enter the total bill value:')
    bill = int(input())
    print()
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    answer = input()
    if answer.lower() == 'yes':
        print()
        lucky = random.choice(list(friends.keys()))
        print(f'{lucky} is the lucky one!')
        lucky_feature = True
    else:
        print()
        print('No one is going to be lucky')
    if lucky_feature:
        price = round(bill / (len(friends)-1), 2)
    else:
        price = round(bill / len(friends), 2)
    print()
    for x, y in friends.items():
        if x != lucky:
            friends[x] = y+price
    print(friends)
else:
    print('No one is joining for the party')
