
def caeser(message):
    print('Caesar Cipher')
    key = 13
    print('Encrypted Message: %s' % message)
    decrypted_message = ''
    for letter in message:
        if letter.isalpha():
            num = ord(letter)
            if (num + key) > 122:
                unicode_num_with_key = (num + key) - 122
                decrypted_message += chr(unicode_num_with_key + ord('a')-1)
            elif num + key <= 122:
                decrypted_message += chr(num+key)
        else:
            decrypted_message += letter
    print('Decrypted Message: %s' % decrypted_message)
    return decrypted_message 


