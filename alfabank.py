from bank import Bank

class Alfabank(Bank):

    def transfer(self, sender_id, receiver_id, amount):
        sender_balance = super().getBalance(sender_id)
        receiver_balance = super().getBalance(receiver_id)

        if sender_balance >= amount:
            super().setBalance(sender_id, sender_balance - amount)
            super().setBalance(receiver_id, receiver_balance + amount)
            return True
        raise NotEnoughMoney


    def capitalization (self, id):
        interest = super().getInterest(id)
        amount = super().getBalance(id)
        super().setBalance(id, amount * (1 + (interest / 100)))
        return True


class NotEnoughMoney(Exception):
    def __init__(self):
        print("Not enough money")