speechToText:

random sound or word(s) is reproduced by system --> 'randomSound'
user records wav file replicating randomSound
system receives wav file
check validity of file, if not repeat wav recording
transcribe to text
compare text transcription to randomSound
	**How does wav2text produce output?
		- Normalize both variables
	**Three metrics:
		- Good pronounciation
		- Needs practice
		- Wrong pronouncitation
Return metric as output

Language learning will require you to build a framework for tracking incorrect 
pronunciations. That will include the generation and scoring of incorrect 
pronunciations.

If you need speed or portability ⇢ use pocketsphinx

Another implementation challenge is that the software requires a good deal of 
memory and must be saved on a single server folder. These voice files improve 
in accuracy with use, so it is important that students work in their own saved
 file. This means that this assistive technology is not always portable. 
Schools have overcome this challenge by assigning students laptops with the 
software installed or storing files on a networked server that can be accessed
 from anywhere on campus.

In this thesis, the goal of mispronunciation detection for language learning is to
detect phone-level and syllable-level mispronunciations in words and sentences. A
baseline text-dependent word mispronunciation detection system based on Hidden
Markov Models (HMM) was constructed. Mispronunciations are detected by comparing 
the log likelihood of the potential state of the targeting pronunciation unit with
a certain pre-determined threshold, given HMM model parameter λ and observation
of the testing sample.


public <i am going to eat> = sil i [ sil ] am [ sil ] going [ sil ] to [ sil ] eat [ sil ];


bin\Release\Win32\pocketsphinx_continuous.exe -infile C:\Users\papia\Documents\BuesoBros\hello_everyone.wav -hmm model\en-us\en-us -lm model\en-us\en-us.lm.bin


bin\Release\Win32\pocketsphinx_continuous.exe -infile C:\Users\papia\Documents\BuesoBros\hello_everyone.wav -hmm model\en-us\en-us -lm model\en-us\en-us.lm.bin -jsgf C:\Users\papia\Documents\BuesoBros\hello-align.jsgf -dict model\en-us\cmudict-en-us.dict -backtrace yes -fsgusefiller no -bestpath no
bin\Release\Win32\pocketsphinx_continuous.exe -infile C:\Users\papia\Documents\BuesoBros\i_am_going_to_eat.wav -hmm model\en-us\en-us -lm model\en-us\en-us.lm.bin -jsgf C:\Users\papia\Documents\BuesoBros\i_am_going_to_eat-align.jsgf -dict model\en-us\cmudict-en-us.dict -backtrace yes -fsgusefiller no -bestpath no
bin\Release\Win32\pocketsphinx_continuous.exe -infile C:\Users\papia\Documents\BuesoBros\i_am_going_to_eat.wav -hmm model\en-us\en-us -lm model\en-us\en-us.lm.bin -jsgf C:\Users\papia\Documents\BuesoBros\i_am_going_to_eat-align.jsgf -dict C:\Users\papia\Documents\BuesoBros\customized_words.dict -backtrace yes -fsgusefiller no -bestpath no

people-apple-map: P IY P AH L - AE P AH L - M AE P
people-i-hope-not: P IY P AH L - AY - HH OW P - N AA T


Vocabulary:
People
Apple
Map

Bike
Number
Lab

Take
Stiff
Late

Water
Butter

Certain
Put
Rent

Drink
Adapt
Mad

Kind
Marker
Smak

Get
Magnet
Rag

Money
Lamp
Ram

Night
Cranberry
Run

Think
Thing

Fake
Photograph
Offer
Laugh

Vertical
Liver
Love

Think
Nothing
Math

The
Rather
Smooth

Small
Mask
Miss

Zebra
Busy
Maze

Shake
Smushed
Mash

Genre
Television
Gage

Hunt
Ahead

Chase
Teacher
Match

Jog
Magic
Age

Yes
Mayo
Million

Waste
Away

Right
Run
Mark

Lake
Belt
Mall
Model
-------Part II--------
Hello
Hi
Hey

Hello, my name is...
Hi, my name is...

Hello, pleasure to meet you.
Hi...

Hello, how are you?
Hi...?

Good morning.
Good afternoon.
Good evening.

Good morning, how are you?
Good afternoon.
Good evening.
