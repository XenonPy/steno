from steno import EncodeInImage, DecodeFromImage

path = input("Enter the path of the image file: ")
message = input("Enter the message to encode: ")
password = input("Enter the password (optional): ")
print("Encoding message...")
if password:
    EncodeInImage(path, message, password)
else:
    EncodeInImage(path, message)
print("Message encoded successfully!")
password2 = input("Enter the password to decode the message (optional): ")
print("\n")
input("Press Enter to decode the message...")
decoded_message = DecodeFromImage(f"{path.split(".")[0] + "_encoded" + "." + path.split(".")[1]}", password2)
print(decoded_message)