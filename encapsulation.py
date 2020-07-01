# private/protected variables assignment
# Encapsulation

class cust_info:
    def __init__(self):
        self._customerName = 'Justin A Perry'
        self.__customer_payment = 'Credit'
        self.__paymentNumber = 8008966790081234

    def getCustPayment(self):
        print(self.__customer_payment)
    def getPaymentNum(self):
        print(self.__paymentNumber)

    def changePayment(self, payType):
        self.__customer_payment = payType

    def newCardNumber(self, newPayment):
        self.__paymentNumber = newPayment


if __name__ == '__main__':
    cust = cust_info()
    cust._customerName = 'Jenny Fillebrown'
    print(cust._customerName)
    cust.changePayment('Visa')
    cust.newCardNumber(4004874587651001)
    cust.getCustPayment()
    cust.getPaymentNum()


    
