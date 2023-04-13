class Client:
    def __init__(self, id, fio, date, amount, interest):
        self.id = id
        self.fio = fio
        self.date = date
        self.amount = amount
        self.interest = interest

    def __str__(self):
        return "id " + str(self.id) + ", fio: " + self.fio + ", date: " + self.date + ", amount: " + str(
            self.amount) + ", inerest: " + str(self.interest)

    def __copy__(self):
        new_obj = Client(self.id, self.fio, self.date, self.amount, self.interest)
        return new_obj

