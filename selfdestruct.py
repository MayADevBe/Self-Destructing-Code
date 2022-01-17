import sys
import base64
from cryptography.fernet import Fernet

def selfdestruct():
    path = sys.argv[0]
    with open(path, 'w') as f:
        f.write('Self Destruction Successful!')

def binary_encoding():
    with open(path, 'r') as f:
        data = f.read()
    encoded = ' '.join(format(ord(x), 'b') for x in data)
    with open(path, 'w') as f:
        f.write(encoded)

def hex_encoding():
    with open(path, 'r') as f:
        data = f.read()
    encoded = data.encode('utf-8').hex()
    with open(path, 'w') as f:
        f.write(encoded)

def base64_encode():
    with open(path, 'r') as f:
        data = f.read()
    encoded = base64.b64encode(bytes(data, "utf-8"))
    encoded = encoded.decode("utf-8")
    with open(path, 'w') as f:
        f.write(encoded)

def to_decimal():
    with open(path, 'r') as f:
        data = f.read()
    encoded = "".join([str(ord(c)) for c in data])
    with open(path, 'w') as f:
        f.write(encoded)

def rot13():
    with open(path, 'r') as f:
        data = f.read()
    abc = "abcdefghijklmnopqrstuvwxyz"
    encoded = "".join([abc[(abc.find(c) + 13) % 26] if c in abc else c for c in data])
    with open(path, 'w') as f:
        f.write(encoded)

def symmetric():   
    key = Fernet.generate_key()
    fer = Fernet(key)
    with open(path, 'r') as f:
        data = f.read()
    data = data.encode("utf-8")
    token = fer.encrypt(data)
    with open(path, 'w') as f:
        f.write(token.decode("utf-8"))
    with open(path.split(".")[0]+"_key.txt", 'w') as f2:    
        f2.write(key.decode("utf-8"))

if __name__ == '__main__':
    path = __file__
    instruction = input("Enter Instruction: ")
    if instruction == "selfdestruct":
        selfdestruct()
    elif instruction == "base64":
        base64_encode()
    elif instruction == "binary":
        binary_encoding()
    elif instruction == "hex":
        hex_encoding()
    elif instruction == "rot13":
        rot13()
    elif instruction == "decimal":
        to_decimal()
    elif instruction == "symmetric":
        symmetric()
