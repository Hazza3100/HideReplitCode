# Hide Replit Code

Hide your replit code with 2 simple steps!


## Usage

```js
    * Create a repl
    * Go to https://www.base64encode.org/ and encode your code
    * Create a secret enviroment called `SECRET_ENV`
    * Paste the example code below into main.py
    * Copy the encoded base64 string and paste it as the value for `SECRET_ENV`
    * Import required modules
    * Run main.py
    * Your code is hidden and works!
```

## Example Cide
```
import os
import base64

SECRET_ENV = os.environ['SECRET_ENV']
exec(base64.b64decode(SECRET_ENV))
```
