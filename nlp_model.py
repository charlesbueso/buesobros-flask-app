from pocketsphinx import AudioFile
import json
import os

def sr(audio_file, hmm='en-us',lm='en-us.lm.bin',dict='cmudict-en-us-modify-TEST.dict'):

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
        return phrase.segments(detailed=True)

#if audio contains selected word and other non-selected words, keep it (for unique words)
#2-second recordings minimum (silence before, and after word), or add .5seg silence before and after?

#for every list in output, for every 1st element in list (create list of all), compare elements with keys in modify dict
#if any key matches, word has been trained
#if any key does not match, remove 1st key from removedDict, run sr() again

toIgnore = {'<sil>':0,'<s>':0,'</s>':0, '[SPEECH]':0}
#finalDeleted = {}

modifyDict = {}
with open("cmudict-en-us-modify-TEST.dict") as file:
    for line in file:
        if line == '\n':
            continue
        else:
            keyAndValue = line.split(' ',1)
            modifyDict[keyAndValue[0]] = keyAndValue[1]

modifyDictTest = modifyDict

def trainVoc(newWord, newWordAudio, modifyDict, deletedWords, counter=0):
    heard = {}
    srOut = sr(audio_file=newWordAudio)
    if srOut is None:
        return print("sr() returns none")
    for i in srOut:
        if i[0] in toIgnore: continue
        else: heard[i[0]] = 0

    print(heard)

    if newWord in heard:
        with open("cmudict-en-us-modify-TEST.dict", 'w') as f:
            for key in modifyDictTest.keys():
                f.write(key + " " + modifyDictTest[key])
        return print(newWord + " -- has been trained:\n deleted: " + str(len(deletedWords)) + " words from previous DICT file")
    else:
        print(list(heard.keys())[0] + " was deleted")
        del modifyDictTest[list(heard.keys())[0]]
        deletedWords[list(heard.keys())[0]] = newWord
        #finalDeleted[list(heard.keys())[0]] = newWord    we want to save deleted files to cleaner dictionary (for later), for now removed_dict.txt
        with open("cmudict-en-us-modify-TEST.dict", 'w') as f:
            for key in modifyDictTest.keys():
                f.write(key + " " + modifyDictTest[key])
        counter += 1
        if counter < 10:
            trainVoc(newWord=newWord, newWordAudio=newWordAudio, modifyDict=modifyDictTest,deletedWords=deletedWords, counter=counter)
        else:
            return print('fail, try another audio!')

delThese = {}
trainVoc(newWord='money', newWordAudio='audio_files\money.wav', modifyDict=modifyDictTest, deletedWords=delThese)