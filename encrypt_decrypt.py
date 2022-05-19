from cryptography.fernet import Fernet

key=Fernet.generate_key()
#key=b'bLOrajwtkS1MCjwrO3m6axoOqDP2Nzw9gjC8UHyS0Bg='
print("KEY:",key)
f=Fernet(key)
mypass=f.encrypt(b"Funnypass@123")
print(mypass)

password=f.decrypt(mypass).decode()
print(password)