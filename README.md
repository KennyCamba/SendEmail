# SendEmail

Python project for send emails with image.

## Dependences
Python 3

## Usage
Enable unsafe app access for gmail server [here](https://myaccount.google.com/lesssecureapps)

```bash
usage: SendEmail [-h] [-firm FIRM] from_addr from_pass subject emails

positional arguments:
  from_addr   Email de donde se envía el correo.
  from_pass   Contraseña de donde se envía el correo.
  subject     Asusnto del correo.
  emails      Path a un archivo csv con la estructura email,img_path.

optional arguments:
  -h, --help  show this help message and exit
  -firm FIRM  Argumento opcional, especifica la firma en el correo.
```

## Example
```bash
python main.py mail@gmail.com password Subject input/file.csv -firm "User<br>Admin"
```