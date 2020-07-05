# abstraction assignment
from abc import ABC, abstractmethod
# define a parent class

class loan(ABC):
    l_amount = 5000
    def loan_amount(self, l_amount):
##        loan = l_amount
        print('Your owe {} on your car..'.format(l_amount))
        return l_amount

    def monthly_payment(self, pay_amount):
        print('Your monthly payment is: {}'.format(pay_amount))
        return pay_amount

    # this is the abstract method that will be defined in the child classes
    @abstractmethod
    def payment_actual(self, act_amount):
        pass


# child class
class leased_suv(loan):

    # abstract parent class defined
    def payment_actual(self, act_amount):
##        loan = 5000
        total_amount = self.l_amount - act_amount
        print('After your monthly payment of {} this month, you still owe {} on the rav4.'.format(act_amount, total_amount))

if __name__ == '__main__':
    money = leased_suv()
    money.loan_amount(5000)
    money.monthly_payment(300)
    money.payment_actual(100)
