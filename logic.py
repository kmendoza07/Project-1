from PyQt6.QtWidgets import *
from bank_accountGUI import *
from bank_historyGUI import *


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self, balance = 0.00):
        super().__init__()
        self.setupUi(self)

        self.__account_balance = balance
        self.set_balance(self.__account_balance)
        self.deposit_Button.clicked.connect(lambda: self.deposit())
        self.withdraw_Button.clicked.connect(lambda: self.withdraw())
        self.history_Button.clicked.connect(lambda: self.view_history())


    def set_balance(self, balance):
        self.accountBalance_Label.setText(f'${balance:.2f}')

    def deposit(self):
        with open('Transaction_History.txt', 'a') as transaction:
            try:
                amount = float(self.input_deposit_amount.text())
                if amount <= 0:
                    raise TypeError
                else:
                    self.__account_balance += amount
                    self.set_balance(self.__account_balance)
                    self.input_deposit_amount.setText('')
                    transaction.write(f'Deposited: ${amount}\n'
                                      f'Total Balance: ${self.__account_balance}\n')

            except ValueError:
                self.message_label.setText(f'Error: Please enter a numeric value')
            except TypeError:
                self.message_label.setText(f'Error: Please enter a positive value')

    def withdraw(self):
        with open('Transaction_History.txt', 'a') as transaction:
            try:
                amount = float(self.input_withdraw_amount.text())
                if self.__account_balance <= 0 or self.__account_balance < amount:
                    self.message_label.setText(f'Error: Can not withdraw more than current balance')
                else:
                    if amount <= 0:
                        raise TypeError
                    else:
                        self.__account_balance -= amount
                        self.set_balance(self.__account_balance)
                        self.input_withdraw_amount.setText('')
                        transaction.write(f'Withdrew: ${amount}\n'
                                          f'Total Balance: ${self.__account_balance}\n')
            except ValueError:
                self.message_label.setText(f'Error: Please enter a numeric value')
            except TypeError:
                self.message_label.setText(f'Error: Please enter a positive value')

    def view_history(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_TransactionWindow()
        self.ui.setupUi(self.window)
        self.window.show()

        with open('Transaction_History.txt', 'r') as transaction:
            for i in transaction:
                self.ui.transaction_history_text.insertPlainText(i)

