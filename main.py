from alfabank import Alfabank

bank = Alfabank()
bank.addClient(123, "AAA", "12.12.12", 23344, 10)
bank.addClient(124, "AAA", "12.12.12", 4000, 5)
bank.addClient(125, "AAA", "13.12.12", 12000, 4)

print(bank.amountOver(3000))
bank.transfer(123, 124, 10000)
bank.capitalization(124)
print(bank.amountOver(10000))



