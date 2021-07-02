def encrypt(message, key):
    # 用来存储最终结果集
    result = ""
    for letter in message:
        if letter.isalpha():
            # 获取每个字节的ascII码
            num = ord(letter)
            if letter.isupper():
                base = ord('A')
            else:
                assert letter.islower()
                base = ord('a')
            num = (num - base + key) % 26 + base
            result += chr(num)

        elif letter.isdigit():
            result += letter
        else:
            result += letter
    return result


# 解密
def decrypt(message, key):
    return encrypt(message, -key)


def get_key():
    try:
        text = input('Enter a key(1-25):')
        key = int(text)
        return key
    except:
        print('Invalid key,Using key:0.')
        return 0


print('Do you wish to encrypt, decrypt, or decode a initdata?')
choice = input()

if choice == "encrypt":
    phrase = input('Message:')
    code = get_key()
    print('Encrypt initdata:', encrypt(phrase, code))
elif choice == "decrypt":
    phrase = input('Message:')
    code = get_key()
    print('Decrypt initdata:', decrypt(phrase, code))
else:
    print('Error: Unrecognized Command')
