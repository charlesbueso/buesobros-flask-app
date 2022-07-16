from pocketsphinx import AudioFile

def sr(audio_file, hmm='en-us',lm='en-us.lm.bin',dict='cmudict-en-us-modify.dict'):

    config = {
        'verbose': False,
        'audio_file': audio_file, #it needs to be a single-channel (monaural), little-endian, unheadered 16-bit signed PCM raw audio file sampled at 16000 Hz
        'buffer_size': 2048,
        'no_search': False,
        'full_utt': False,
        'hmm': hmm,
        'lm': lm,
        'dict': dict
    }

    audio = AudioFile(**config)
    for phrase in audio:
        return print(phrase.segments(detailed=True))

sr(audio_file='audio_files\hello_everyone.wav')
