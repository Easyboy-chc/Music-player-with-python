import PySimpleGUI as sg 
from pygame import mixer 


files = [("MP3 (*.mp3)", "*.mp3"), 
         ("WAV (*.wav)", "*.wav"),
              ("All files (*.*)", "*.*")]

mixer.init()
layout = [ 
          [sg.Text('Choose song',background_color='#151515', text_color='white'), sg.In(size = (30,1), enable_events=True,key='-MUSIC-'), sg.FileBrowse(file_types = files, key = "-BROWSE-",  change_submits=True)],
          [sg.Button('Play'),sg.Button('Pause'),sg.Button('Resume'),sg.Button('Stop'),sg.Button('Exit'),
           sg.Canvas(size=(20, 10), background_color='#151515'),
           sg.Slider(range=(1, 100), orientation='h', size=(10,15), key='volume',
                     default_value=100,background_color='black', enable_events=True,
                     change_submits=True)],
          ]

window = sg.Window('Knight Music Player', 
                   layout,
                   background_color='#151515',element_justification='c',
                   titlebar_background_color='#D35100',
                   button_color='#F07900')



while True:
    event, values = window.read()
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break

    if event == 'Play':
        song = f"{values['-MUSIC-']}"
        song1 = song
        mixer.music.load(song)
        mixer.music.play()
        volume = values['volume']
      
      
    if event == 'Pause':
        mixer.music.pause()
    if event == 'Resume':
        mixer.music.unpause()
    if event == 'Stop':
        mixer.music.stop()
        
window.close()
#window.close
