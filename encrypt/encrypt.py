from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import base64
# import pyperclip as clip
import getpass # for hiding text on type
import sys # for getting sys.argv

def encryptor(text, key):

    BLOCK_SIZE = 16     # 16 Bytes indicating AES-128 ECB

    byte_text = bytes(text, encoding='utf-8')
    byte_key = bytes(key,encoding='utf-8')
    cipher = AES.new(byte_key, AES.MODE_ECB)

    msg = cipher.encrypt(pad(byte_text, BLOCK_SIZE))
    bs64_msg = base64.b64encode(msg)

    return bs64_msg.decode()

    #decipher = AES.new(byte_key, AES.MODE_ECB)
    #msg_dec = decipher.decrypt(msg)
    #print(unpad(msg_dec, BLOCK_SIZE).decode())