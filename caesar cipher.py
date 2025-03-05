def encrypt(plainText, key):
	cipherText = ""
	for letter in plainText:
		asciiValue = ord(letter)
		encryptedLetter = chr(asciiValue + key)
		cipherText += encryptedLetter
	return cipherText

def decrypt(cipherText, key):
	plainText = ""
	for letter in cipherText:
		asciiValue = ord(letter)
		encryptedLetter = chr(asciiValue - key)
		plainText += encryptedLetter
	return plainText

cipherText = encrypt("jumanji",0)
print(cipherText)
plainText = decrypt(cipherText, 0)
print(plainText)

secretMessage = "M$FIX$SRP]$HER$KIXW$XLMW"
plainText = decrypt(secretMessage, 4)
print(plainText)
# what is the message?
