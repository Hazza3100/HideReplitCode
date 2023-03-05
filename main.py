#read the readme for info on usage
# you can use https://www.base64encode.org/ to encode your code

x = input('encoded code: ')
print(f'Your env: {x}\nYour public code: import base64; exec(base64.b64decode("{x}"))')
