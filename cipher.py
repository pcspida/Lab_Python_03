phrase=raw_input("Enter sentence to encrypt: ")
shift=input('Enter shift value: ')
encoded_phrase = ''
for ch in phrase:
    if (ord(ch)>64 and ord(ch)<91):
        asci=ord(ch)
        alph_asci=asci-65
        shift_asci=(alph_asci+shift)%26
        encoded_asci=shift_asci+65
        encoded_phrase = encoded_phrase + chr(encoded_asci)
    elif (ord(ch)>96 and ord(ch)<123):
        asci=ord(ch)
        alph_asci=asci-97
        shift_asci=(alph_asci+shift)%26
        encoded_asci=shift_asci+97
        encoded_phrase = encoded_phrase + chr(encoded_asci)
    else:
        encoded_phrase = encoded_phrase+ch
    
print encoded_phrase
