import random


class SplitBillCalculator:
    def __init__(self):
        self.friends = {}
        self.lucky_feature = False
        self.lucky = None

    def get_number_of_friends(self):
        return int(input('Enter the number of friends joining (including you):\n'))

    def get_friend_names(self, num_friends):
        print('Enter the name of every friend (including you), each on a new line:')
        for _ in range(num_friends):
            friend = input()
            self.friends[friend] = 0

    def get_total_bill(self):
        return int(input('Enter the total bill value:\n'))

    def use_lucky_feature(self):
        answer = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
        if answer.lower() == 'yes':
            self.lucky = random.choice(list(self.friends.keys()))
            print(f'{self.lucky} is the lucky one!')
            self.lucky_feature = True
        else:
            print('No one is going to be lucky')

    def calculate_and_print_split_bill(self, bill):
        if self.lucky_feature:
            price = round(bill / (len(self.friends) - 1), 2)
        else:
            price = round(bill / len(self.friends), 2)

        for friend in self.friends:
            if friend != self.lucky:
                self.friends[friend] += price

        print(self.friends)

    def main(self):
        num_friends = self.get_number_of_friends()

        if num_friends > 0:
            self.get_friend_names(num_friends)
            total_bill = self.get_total_bill()
            self.use_lucky_feature()
            self.calculate_and_print_split_bill(total_bill)
        else:
            print('No one is joining for the party')


if __name__ == "__main__":
    split_bill_calculator = SplitBillCalculator()
    split_bill_calculator.main()

