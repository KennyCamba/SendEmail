import argparse
import src.email_helper
import csv


def main():
    parser = argparse.ArgumentParser('SendEmail')
    parser.add_argument('from_addr', help='Email de donde se envía el correo.', type=str)
    parser.add_argument('from_pass', help='Contraseña de donde se envía el correo.', type=str)
    parser.add_argument('subject', help='Asusnto del correo.', type=str)
    parser.add_argument('emails', help='Path a un archivo csv con la estructura email,img_path.', type=str)
    parser.add_argument('-firm', help='Argumento opcional, especifica la firma en el correo.', type=str)
    args = parser.parse_args()
    with open(args.emails, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            value = src.email_helper.send(args.from_addr, args.from_pass, row[0], 'Certificado', row[1], args.firm)
            if not value:
                print("Ocurrión un error al enviar el correo a la dirección: " + row[0])
            else:
                print("Envío exitoso a: " + row[0])

if __name__ == '__main__':
    main()
