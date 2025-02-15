'''
A basic cipher encription tools. Thought it might need later.
'''


from Crypto.Cipher import AES
import base64

def ecb_encrypt(message, key):
    aes = AES.new(key, AES.MODE_ECB)
    return base64.b64encode(aes.encrypt(message)).decode()

def ecb_decrypt(encrypted, key):
    aes = AES.new(key, AES.MODE_ECB)
    return aes.decrypt(base64.b64decode(encrypted))

if __name__ == "__main__":

    Key = "0000000000000000"
    plain_text = "There's no text basically this a"

    cipher_text = ecb_encrypt(plain_text, Key)
    decrypted_pt = ecb_decrypt(cipher_text, Key).decode()

    print("Original message: {}".format(plain_text))
    print("Encrypted message: {}".format(cipher_text))
    print("Decrypted message: {}".format(decrypted_pt))


