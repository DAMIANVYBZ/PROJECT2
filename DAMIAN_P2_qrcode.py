import PySimpleGUI as sg
import qrcode

sg.theme("LightBlue3")
font = ('DejaVu Sans Mono',20)

qr_image= [sg.Image('',key ='-QRCODE-')]

layout = [
     [sg.Text('WHAT TEXT OR LINK  WOULD YOU LIKE TO CREATE A QRCODE FOR ?')],
     [sg.Input('',key='-INPUT-')],
     [sg.Button('CREATE QRCODE', key='-CREATE-'), sg.Button('EXIT')],
     [sg.Column([qr_image], justification='center')]
           
]
 
window = sg.Window("DAMIAN'S QR CODE GENERATOR", layout,font=font)

while True:
    event, values = window.read()
    if event == "EXIT" or event == sg.WIN_CLOSED:
        break
    elif event =='-CREATE-':
        text = values['-INPUT-']
        if text:
            img = qrcode.make(text)
            img.save('qr.png')
            window['-QRCODE-'].update('qr.png')

window.close()