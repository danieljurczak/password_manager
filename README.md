# Simple Password Manager

My simple implementation of the password manager.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install project.

```bash
pip install -r requirements.txt
```

## Usage
Create your database first.
```bash
python database.py
```
You can add new password with name of it as cli parameter.
Your password will be copied to the clipboard.
```bash
python add_password.py name_of_your_password
```
You can also get your password to clipboard.
```bash
python get_password.py name_of_your_password
```
To view all names of saved passwords.
```bash
python all_passwords.py
```

## Testing
The project has basic tests. You can run them as follows.
```bash
python tests.py
```

## TODO
Sample features that I could implement in the future:
- hashing password before writing to DB
- generating user-friendly passwords
