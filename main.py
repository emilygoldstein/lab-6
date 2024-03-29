def encode(password): # emily goldstein
    # takes 8 digit password inputed by user in string format that is only integers
    # stores the encoded password into a new variable new_pass
    # encoded password shifts each digit in the string up by 3 numbers
    res = ''
    for num in password:
        new_pass = str((int(num) + 3) % 10)
        res += new_pass
    return res

def decode(password):
    password_list = [int(x) for x in str(password)]
    new_password_list = []
    for i in password_list:
        x = i - 3
        new_password_list.append(x)
    password = ''.join(str(x) for x in new_password_list)
    int(password)
    return password

if __name__ == "__main__":
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit\n')
        option = int(input('Please enter an option: '))
        if option == 3: # exit program
            break
        elif option == 1:
            password = input('Please enter your password to encode: ')
            res = encode(password)
            print('Your password has been encoded and stored!\n')
        elif option == 2:
            encoded_password = encode(password)
            print(f'The encoded password is {encoded_password}, and the original password is {password}.')
        else:
            print('Invalid option.')



