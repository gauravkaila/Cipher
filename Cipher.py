import string

# Create dictionary for Vignere Cipher
def vignereCipher():
    cipherdict = {}
    shift = 0
    for i in range(len(string.ascii_lowercase)):
        cipherdict[string.ascii_lowercase[i]] = []
        for j in range(len(string.ascii_lowercase)):
            ind = string.ascii_lowercase.index(string.ascii_lowercase[j])
            new_ind = ind+shift
            if new_ind > 25:
                new_ind -= 26
            cipherdict[string.ascii_lowercase[i]].append(string.ascii_lowercase[new_ind])
        shift +=1
    return cipherdict
        
    
# Vignere Cipher class
class Cipher(object):
    
    def __init__(self):
        self.key = None
        self.cipher = vignereCipher()
        
    # encrypt method using VC    
    def encrypt(self,originalText):
        encryptedTextList = []
        self.cipher = vignereCipher()
        originalTextcopy = originalText.replace(" ", "")
        finalKey = (self.key * len(originalTextcopy))[:len(originalTextcopy)]                        # bringing to length the key
        for i in range(len(originalTextcopy)):                                    
            if originalTextcopy[i] in string.ascii_lowercase:                                    # assumption that the message is in lowercase
                row = finalKey[i]                                                             # row is letter in keyword
                col = originalTextcopy[i]                                                         # column is the letter in original text
                encryptedTextList.append(self.cipher[row][string.ascii_lowercase.index(col)])
            else:
                encryptedTextList.append(originalTextcopy[i])
        
        # restoring the original sequence of the input text
        space = [] 
        for i in range(len(originalText)):
            if originalText[i] == ' ':
                space.append(i)
        for i in space:
            encryptedTextList.insert(i,' ')
        encryptedText = ''.join(encryptedTextList)
        return encryptedText
    
    # decrypt method using VC    
    def decrypt(self,encryptedText):
        decryptedTextList = []
        self.cipher = vignereCipher()
        encryptedTextcopy = encryptedText.replace(' ','')
        finalKey = (self.key * len(encryptedTextcopy))[:len(encryptedTextcopy)]
        for i in range(len(finalKey)):
            if encryptedTextcopy[i] in string.ascii_lowercase:
                row = finalKey[i]
                col = encryptedTextcopy[i]
                ind = (self.cipher[row]).index(col)
                decryptedTextList.append(string.ascii_lowercase[ind])
            else:
                decryptedTextList.append(encryptedTextcopy[i])
    
        space = []
        for i in range(len(encryptedText)):
            if encryptedText[i] == ' ':
                space.append(i)
        for i in space:
            decryptedTextList.insert(i,' ')
        decryptedText = ''.join(decryptedTextList)
        return decryptedText
        
    # method to set key
    def setKey(self,key):
        self.key = key
    
    def __str__(self):
        return 'Vignere Cipher'

message = Cipher()
key = input('Enter key for the vignere cipher: ')
message.setKey(key)
message2encrypt = input('Enter message to encrypt: ')
print message.encrypt(message2encrypt)
message2decrypt = input('Enter message to decrypt: ')
print message.decrypt(message2decrypt)
k = raw_input('press any key: ')
