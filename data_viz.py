import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Load the audio file
AUDIO_FILE = './training_data/User2_yes_1.wav'
samples, sample_rate = librosa.load(AUDIO_FILE, sr=None)

# x-axis has been converted to time using our sample rate. 
# matplotlib plt.plot(y), would output the same figure, but with sample 
# number on the x-axis instead of seconds
plt.figure(figsize=(14, 5))
librosa.display.waveshow(samples, sr=sample_rate)

sgram = librosa.stft(samples)
librosa.display.specshow(sgram)

# use the mel-scale instead of raw frequency
sgram_mag, _ = librosa.magphase(sgram)
mel_scale_sgram = librosa.feature.melspectrogram(S=sgram_mag, sr=sample_rate)
librosa.display.specshow(mel_scale_sgram)

# use the decibel scale to get the final Mel Spectrogram
mel_sgram = librosa.amplitude_to_db(mel_scale_sgram, ref=np.min)
librosa.display.specshow(mel_sgram, sr=sample_rate, x_axis='time', y_axis='mel')
plt.colorbar(format='%+2.0f dB')
