# -*- coding:utf-8 -*-


# # 代理模式示例：演员经纪人制作公司
# class Actor(object):
#     def __init__(self):
#         self.isBusy = False
#
#     def occupied(self):
#         self.isBusy = True
#         print(type(self).__name__, "is occupied with current movie")
#
#     def available(self):
#         self.isBusy = False
#         print(type(self).__name__, "is free for the movie")
#
#     def getStatus(self):
#         return self.isBusy
#
#
# class Agent(object):
#     def __init__(self):
#         self.principal = None
#
#     def work(self):
#         self.actor = Actor()
#         if self.actor.getStatus():
#             self.actor.occupied()
#         else:
#             self.actor.available()
#
#
# if __name__ == "__main__":
#     r = Agent()
#     r.work()


# 代理模式实例：银行借记卡
from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def do_pay(self):
        pass


class Bank(Payment):
    def __init__(self):
        self.card = None
        self.account = None

    def __getAccount(self):
        self.account = self.card    # Assume card number is account number
        return self.account

    def __hasFunds(self):
        print("Bank:: Checking if Account", self.__getAccount(), "has enough funds")
        return True

    def setCard(self, card):
        self.card = card

    def do_pay(self):
        if self.__hasFunds():
            print("Bank:: Paying the merchant")
            return True
        else:
            print("Bank:: Sorry, not enough funds! ")
            return False


class DebitCard(Payment):
    def __init__(self):
        self.bank = Bank()

    def do_pay(self):
        card = input("Proxy:: Punch in Card Number: ")
        self.bank.setCard(card)
        return self.bank.do_pay()


class You:
    def __init__(self):
        print("You:: Lets buy the Denim shirt")
        self.debitCard = DebitCard()
        self.isPuchased = None

    def make_payment(self):
        self.isPuchased = self.debitCard.do_pay()

    def __del__(self):
        if self.isPuchased:
            print("You:: Wow! Denim shirt is Mine :-)")
        else:
            print("You:: I should earn more :(")


you = You()
you.make_payment()
