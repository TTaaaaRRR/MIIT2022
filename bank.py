from client import Client

class Bank:
    def __init__(self):
        self.clients = []

    def addClient(self, id, fio, date, amount, interest):
        self.clients.append(Client(id, fio, date, amount, interest))

    def amountOver(self, n):
        res = []
        for client in self.clients:
            if client.amount > n:
                res.append(str(client))
        return res

    def interestOver(self, n):
        res = []
        for client in self.clients:
            if client.interest > n:
                res.append(str(client))
        return res

    def getByDate(self, date):
        res = []
        for client in self.clients:
            if client.date == date:
                res.append(str(client))
        return res

    def getBalance(self, id):
        for client in self.clients:
            if client.id == id:
                return client.amount
        raise ClientNotFoundException

    def setBalance(self, id, amount):
        for client in self.clients:
            if client.id == id:
                client.amount = amount
                return True
        raise ClientNotFoundException

    def getInterest (self, id):
        for client in self.clients:
            if client.id == id:
                return client.interest
        raise ClientNotFoundException


class ClientNotFoundException(Exception):
    def __init__(self):
        print("Client not found!")
