balance = 5000
pin = 1234
attempts = 3
daily_limit = 2000
transactions = []
def check_balance():
  st.write(" Current Balance:", balance)
def deposit_money():
  global balance
  amount = int(input("Enter deposit amount: "))
  if amount > 0:
    balance += amount
    transactions.append(f"Deposited: {amount}")
    st.write(" Deposit successful")
  else:
    st.write(" Invalid amount")
def withdraw_money():
    global balance
    amount = int(input("Enter withdrawal amount: "))
    if amount > daily_limit:
        st.write(" Daily limit exceeded")
    elif amount > balance:
       st.write(" Insufficient balance")
    elif amount <= 0:
        st.write(" Invalid amount")
    else:
        balance -= amount
        transactions.append(f"Withdrawn: {amount}")
        st.write(" Please collect your cash")
def mini_statement():
    if not transactions:
        st.write("No transactions yet")
    else:
        st.write(" Mini Statement:")
        for t in transactions:
            st.write("-", t)
# PIN CHECK
while attempts > 0:
    user_pin = int(input("Enter your PIN: "))
    if user_pin == pin:
        st.write(" Login successful")
        break
    else:
        attempts -= 1
        st.write(" Wrong PIN. Attempts left:", attempts)
if attempts == 0:
    st.write(" Card blocked")
else:
    while True:
        st.write("\n1. Check Balance")
        st.write("2. Deposit Money")
        st.write("3. Withdraw Money")
        st.write("4. Mini Statement")
        st.write("5. Exit")
        choice = int(input("Choose option: "))
        if choice == 1:
            check_balance()
        elif choice == 2:
            deposit_money()
        elif choice == 3:
            withdraw_money()
        elif choice == 4:
            mini_statement()
        elif choice == 5:
            print(" Thank you for using ATM")
            break
        else:
            st.write(" Invalid option")
