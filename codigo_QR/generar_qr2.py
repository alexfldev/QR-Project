import qrcode
from PIL import Image

def generate_qr_code(Text, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=20,
        border=4,
    )
    qr.add_data(Text)
    qr.make(fit=True)
    
    # Generar la imagen del código QR
    img = qr.make_image(fill_color="#800080", back_color="#FFFFFF")
    
    # Guardar la imagen en el archivo proporcionado
    img.save(file_name)
    print(f"QR code guardado como {file_name}")

if __name__ == "__main__":
    Text = input("Introduce un texto o una URL para generar el código QR: ")
    file_name = input("Introduce el nombre del código QR que debe incluir siempre la extensión .png: ")
    generate_qr_code(Text, file_name)
