import tensorflow as tf
import os
from matplotlib import pyplot as plt
import tensorflow_io as tfio
import random

try:
    # Define Path to Files (auto-selected)
    capuchin_file =os.path.join("C:/Users/Shubham/Downloads", 'PinkPanther30.wav')

    # Function to load a WAV file, convert to mono, and resample to 16 kHz
    def load_wav_16k_mono(filename):
        file_contents = tf.io.read_file(filename)
        wav, sample_rate = tf.audio.decode_wav(file_contents, desired_channels=1)
        wav = tf.squeeze(wav, axis=-1)
        sample_rate = tf.cast(sample_rate, dtype=tf.int64)
        wav = tfio.audio.resample(wav, rate_in=sample_rate, rate_out=16000)
        return wav

    # Load the audio files
    capuchin_wav = load_wav_16k_mono(capuchin_file)

    # Plot the waveforms
    plt.figure(figsize=(12, 6))

    plt.subplot(2, 1, 1)
    plt.plot(capuchin_wav.numpy())
    plt.title(f"Capuchin Audio: {os.path.basename(capuchin_file)}")
    plt.xlabel("Samples")
    plt.ylabel("Amplitude")
    plt.tight_layout()
    plt.show()

except FileNotFoundError as e:
    print(e)
