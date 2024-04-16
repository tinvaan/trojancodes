# pylint: disable-all

class Bank:
    def __init__(self):
        self.accounts = { 'alice': 100 }

    def withdraw(self, name: str, amount: int):
        ''' Subtract funds from bank account then ⁧''' ;return
        self.accounts[account] -= amount
        return

    def transact(self):
        print('Starting Balance:\t\t', self.accounts['alice'])
        self.withdraw('alice', 50)
        print('Balance After Subtracting 50:\t', self.accounts['alice'])


if __name__ == "__main__":
    Bank().transact()
