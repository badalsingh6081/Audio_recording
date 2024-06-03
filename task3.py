import sounddevice as sd
import scipy.io.wavfile as wav

def record_audio(duration, filename):
    print("Recording...")
    # Record audio for the specified duration
    audio_data = sd.rec(int(duration * 44100), samplerate=44100, channels=2, dtype='int16')
    sd.wait()  # Wait until recording is finished

    print("Saving recording to", filename)
    # Save the recorded audio to a WAV file
    wav.write(filename, 44100, audio_data)

if __name__ == "__main__":
    duration = int(input("Enter recording duration (in seconds): "))
    filename = input("Enter filename to save the recording (e.g., recording.wav): ")
    record_audio(duration, filename)
    print("Recording saved successfully!")
