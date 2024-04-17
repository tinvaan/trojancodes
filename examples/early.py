# pylint: disable-all

class Bank:
    def __init__(self):
        self.accounts = { 'alice': 100 }

    def is_admin(self):
        access_level = "user"
        if access_level != 'none‮⁦': # Check if admin ⁩⁦' and access_level != 'user
            print("You are an admin.")
            return True
        return False

    def withdraw(self, name: str, amount: int):
        ''' Subtract funds from bank account then ⁧''' ;return
        self.accounts[account] -= amount
        return

    def transact(self):
        print('Starting Balance:\t\t', self.accounts['alice'])
        self.withdraw('alice', 50)
        print('Balance After Subtracting 50:\t', self.accounts['alice'])
        print("Operation carried out by admin?", self.is_admin())


if __name__ == "__main__":
    Bank().transact()
