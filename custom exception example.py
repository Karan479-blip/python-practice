class InsufficientFundsError(Exception):
    #This custom exception is raised when a bank account has insufficient funds for a withdrawal.
  

  def __init__(self, message="Insufficient funds in account"):
    self.message = message
class BankAccount:
  def __init__(self, balance):
    self.balance = balance

  def withdraw(self, amount):
    if amount > self.balance:
      raise InsufficientFundsError("Attempted withdrawal of ₹{}".format(amount))
    else:
      self.balance -= amount
      print("Withdrawal successful. New balance: ₹{}".format(self.balance))
try:
  my_account = BankAccount(1000)
  my_account.withdraw(1500)  # This will raise InsufficientFundsError
except InsufficientFundsError as e:
  print("Error:", e.message)  # Print the custom error message
