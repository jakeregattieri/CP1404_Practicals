

def main():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
    'swei45''BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
    'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    username = input("enter username: ")
    while username not in usernames:
        print("access denied")
        username = input("enter username: ")
    if username in usernames:
        print("access granted")


main()