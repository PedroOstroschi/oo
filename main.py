from conta import Conta


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    conta  = Conta(123, "Pedro", 10000000, 30000000000)
    conta.extrato()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
