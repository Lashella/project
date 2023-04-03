import PySimpleGUI as sg
import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Define the layout of the PySimpleGUI window
layout = [
    [sg.Text('Enter text to speak:')],
    [sg.Input(key='-TEXT-')],
    [sg.Radio('Male', 'voice', key='-MALE-'), sg.Radio('Female', 'voice', key='-FEMALE-', default=True)],
    [sg.Button('Speak'), sg.Button('Exit')],
    [sg.Text('', key='-STATUS-')],
]

# Create the PySimpleGUI window
window = sg.Window('Text-to-Speech App', layout)

# Event loop to process "Speak" button and "Exit" button clicks
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'):  # If user closes window or clicks "Exit" button
        break
    if event == 'Speak':
        text = values['-TEXT-']
        if text.strip() != '':
            engine.setProperty('voice', 'english-male' if values['-MALE-'] else 'english-female')
            engine.say(text)
            engine.runAndWait()
            window['-STATUS-'].update('Text spoken!')
        else:
            window['-STATUS-'].update('Please enter some text.', text_color='red')

# Close the PySimpleGUI window
window.close()