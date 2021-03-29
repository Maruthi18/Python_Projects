from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
			'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
			'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar (start_text, shift_amount, directions):
	end_text = ''
	if directions == 'decode':
		shift_amount *= -1
	for character in start_text:
		if character in alphabet:
			position = alphabet.index (character)
			new_position = position + shift_amount
			end_text += alphabet [new_position]
		else:
			end_text += character


	print (f'{directions} text is : {end_text}')


should_continue = True
while should_continue:
	direction = input ("Type 'encode' to encrypt , type 'decode' to decrypt : \n")
	text = input ("Enter Your Message : \n").lower ()
	shift = int (input ("Type The Shift Number : \n"))

	shift = shift % 26  # here when we given a large shift number it will select the remainder part EG : shift = 45 , 45 % 26 = 19
	caesar (start_text=text, shift_amount=shift, directions=direction)

	result =  input("Type Yes if you want to do it again? Otherwise type No ..\n")
	if result == 'No':
		should_continue = False
		print("GoodBye")


# ----------------- Encryption ------------------------
# def is_encrypt(plain_text , shift_amount):
#     cipher_text = ""
#     for letter in plain_text :
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text  += letter
#     print(f"encode text is : {cipher_text}")


# ----------------------- Decryption -----------------------------
# def is_decrypt(plain_text , shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         cipher_text += alphabet[new_position]
#     print(f"decode text is : {cipher_text}")
