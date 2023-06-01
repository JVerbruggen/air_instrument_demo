import numpy as np
import pyaudio
import time

import audio_input

p = pyaudio.PyAudio()

fs = 44100

def play(stream, duration, frequency, volume):
    # generate samples, note conversion to float32 array
    samples = (np.sin(2 * np.pi * np.arange(fs * duration) * frequency / fs)).astype(np.float32)

    # per @yahweh comment explicitly convert to bytes sequence
    output_bytes = (volume * samples).tobytes()

    stream.write(output_bytes)

# for paFloat32 sample values must be in range [-1.0, 1.0]
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)

audio_input_controller: audio_input.AudioInputController = audio_input.MouseXYAudioInputController()

loops = 500
for i in range(loops):
    pitch = audio_input_controller.get_pitch()
    volume = audio_input_controller.get_volume()
    play(stream, 0.05, pitch, volume)

stream.stop_stream()
stream.close()

p.terminate()