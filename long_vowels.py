#Long-long Vowels
def long_vowels():
    print('Long-long Vowels')
    user_input = input('Please enter your long vowel word: ')
    print('Your entry is %s' % user_input)
    long_vowels = 'aeiouAEIOU'
    prev = ''
    long_long_vowel = ''
    print('Long-long Vowel: ', end='')
    for letter in user_input:
        long_long_vowel += letter
        if letter == prev and letter in long_vowels:
            long_long_vowel += letter*3
        prev = letter
    print(long_long_vowel)
    print()
    return

    # this is awesome