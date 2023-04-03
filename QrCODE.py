import PySimpleGUI as sg
import qrcode
import io
from PIL import Image

layout = [
    [sg.Text('Enter data to encode:')],
    [sg.Input(key='-DATA-')],
    [sg.Button('Generate QR code'), sg.Button('Exit')],
    [sg.Image(key='-IMAGE-')],
    [sg.Text('', key='-STATUS-')],
]

window = sg.Window('QR Code Generator', layout)

# Event loop to process "Generate QR code" button and "Exit" button clicks
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'):  # If user closes window or clicks "Exit" button
        break
    if event == 'Generate QR code':
        data = values['-DATA-']
        if not data:  # Check if input is blank
            window['-STATUS-'].update('Error: Please enter data to encode')  # Display error message
        else:
            qr = qrcode.QRCode(
                version=1,
                box_size=10,
                border=5
            )
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill_color='black', back_color='white')

            # Convert the PIL image to a bytes object
            img_bytes = io.BytesIO()
            img.save(img_bytes, format='PNG')
            img_bytes.seek(0)

            # Update the image element and status text element in the PySimpleGUI window
            window['-IMAGE-'].update(data=img_bytes.read())
            window['-STATUS-'].update('QR code generated!')  # Attribution: Modified from original code by qrcode library

# Close the PySimpleGUI window
window.close()