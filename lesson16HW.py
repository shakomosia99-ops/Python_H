class BankAccount:
    bank_name = "Georgian National Bank"
    __total_accounts = 0

    def __init__(self, owner, balance):
        self._owner = owner

        if not BankAccount.validate_amount(balance):
            raise ValueError("Balance must be positive")
        self.__balance = balance

        BankAccount.__total_accounts += 1
        self.__account_number = f"AN{BankAccount.__total_accounts:04d}"

    def deposit(self, amount):
        if not BankAccount.validate_amount(amount):
            print("Invalid deposit amount")
            return
        self.__balance += amount

    def withdraw(self, amount):
        if not BankAccount.validate_amount(amount):
            print("Invalid withdrawal amount")
            return
        if amount > self.__balance:
            print("Insufficient funds")
            return
        self.__balance -= amount

    def check_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

    def change_owner(self, new_owner):
        self._owner = new_owner

    @classmethod
    def get_total_accounts(cls):
        return cls.__total_accounts

    @staticmethod
    def validate_amount(amount):
        return amount > 0

    def __str__(self):
        return f"Account: {self.__account_number} | Owner: {self._owner}"


if __name__ == "__main__":
    acc1 = BankAccount("Nino Beridze", 500)
    acc2 = BankAccount("Giorgi Kapanadze", 1000)

    print(acc1)
    print(acc2)

    acc1.deposit(200)
    print(acc1.check_balance())

    acc1.withdraw(1000)
    acc1.withdraw(300)
    print(acc1.check_balance())

    acc1.change_owner("Nino B.")
    print(acc1)

    print(BankAccount.get_total_accounts())
