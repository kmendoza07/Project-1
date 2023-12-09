from PyQt6.QtWidgets import *
from bank_accountGUI import *
from bank_historyGUI import *


class Logic(QMainWindow, Ui_MainWindow):
    """
    A class that describes the functions of the bank app
    """

    def __init__(self, balance=0.00) -> None:
        """
        Method that creates the balance object with its initial value.
        Also calls to other methods upon an action being detected on an app.
        """
        super().__init__()
        self.setupUi(self)

        self.__account_balance = balance
        self.set_balance(self.__account_balance)

        self.deposit_Button.clicked.connect(lambda: self.deposit())
        self.withdraw_Button.clicked.connect(lambda: self.withdraw())
        self.history_Button.clicked.connect(lambda: self.view_history())

    def set_balance(self, balance) -> None:
        """
        Method that shows the total account balance on the main page
        :param balance: total balance
        :type balance: float
        """
        self.accountBalance_Label.setText(f'${balance:.2f}')

    def deposit(self) -> None:
        """
        Method that calculates the total balance by adding.
        Updates the text file upon completing each calculation.
        """
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

    def withdraw(self) -> None:
        """
        Method that calculates the total balance by subtracting.
        Updates the text file upon completing each calculation.
        """
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

    def view_history(self) -> None:
        """
        Method that opens a new window upon clicking the button.
        Displays the text file onto a plain text box.
        """
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_TransactionWindow()
        self.ui.setupUi(self.window)
        self.window.show()

        with open('Transaction_History.txt', 'r') as transaction:
            for i in transaction:
                self.ui.transaction_history_text.insertPlainText(i)
