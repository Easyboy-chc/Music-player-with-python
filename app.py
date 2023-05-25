import PySimpleGUI as sg
import pygame
from pygame import mixer
from mutagen.mp3 import MP3

files = [("MP3 (*.mp3)", "*.mp3"),
         ("WAV (*.wav)", "*.wav"),
         ("All files (*.*)", "*.*")]

mixer.init()
layout = [
    [sg.Text('Choose song', background_color='#151515', text_color='white'),
     sg.In(size=(30, 1), enable_events=True, key='-MUSIC-'),
     sg.FileBrowse(file_types=files, key="-BROWSE-", change_submits=True)],
    [sg.ProgressBar(100, orientation='h', size=(20, 5), key='-PROGRESS-', bar_color=('red', 'white'))],
    [sg.Button('Play'), sg.Button('Pause'), sg.Button('Resume'), sg.Button('Stop'), sg.Button('Exit'),
     sg.Canvas(size=(20, 10), background_color='#151515'),
     sg.Slider(range=(1, 100), orientation='h', size=(10, 15), key='volume',
               default_value=15, background_color='black', enable_events=True,
               change_submits=True)],
]

window = sg.Window('Knight Music Player',
                   layout,
                   background_color='#151515', element_justification='c',
                   titlebar_background_color='#D35100',
                   button_color='#F07900')


mixer.music.set_endevent(pygame.USEREVENT)
is_playing = False
current_file = None
duration = 0

clock = pygame.time.Clock()

while True:
    event, values = window.read(timeout=0)
    if event == 'Exit' or event == sg.WINDOW_CLOSED:
        break

    if event == 'Play':
        song = values['-MUSIC-']
        mixer.music.load(song)
        mixer.music.play()
        is_playing = True
        volume = values['volume']

        # Get the duration of the audio file
        audio = MP3(song)
        duration = audio.info.length

    if event == 'Pause':
        mixer.music.pause()
        is_playing = False
    if event == 'Resume':
        mixer.music.unpause()
        is_playing = True
    if event == 'Stop':
        mixer.music.stop()
        is_playing = False

    # Check for music end event
    if event == pygame.USEREVENT:
        # Do something when the music ends
        pass

    # Update volume
    volume = values['volume']
    mixer.music.set_volume(volume / 100)

    if is_playing:
        # Get the audio time position
        audio_time = pygame.mixer.music.get_pos() / 1000  # Convert to seconds

        # Update the progress bar
        progress_percent = int((audio_time / duration) * 100)
        window['-PROGRESS-'].update(progress_percent)

    # Read audio stream and calculate the volume
    data = pygame.mixer.music.get_busy()
    rms = 0  # Placeholder value for demonstration

    clock.tick(1000)  # Limit the frame rate to 1000 FPS (1 millisecond)

pygame.mixer.quit()
window.close()
