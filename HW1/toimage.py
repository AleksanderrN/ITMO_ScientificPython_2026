import base64  # For decoding.
txtscreen = input('Enter the path to text fie: ')
f = open(txtscreen, 'rb')  # Open encoded file.
byte = f.read()  # Read data.
f.close()
outscreen = input('Enter the path to image: ')
decode = open(outscreen, 'wb')  # Open image file to save.
decode.write(base64.b64decode(byte))  # Decode and write data.
decode.close()