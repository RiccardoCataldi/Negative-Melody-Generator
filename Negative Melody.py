from music21 import *

environment.set('musescoreDirectPNGPath', 'C:/Program Files/MuseScore 3/bin/MuseScore3.exe')
environment.set("musicxmlPath", 'C:/Program Files/MuseScore 3/bin/MuseScore3.exe')

notelis = input('Insert melody.Each note needs to be separeted by space. (Ex. a4 c5 b4 a4 e5): ')
notelist = notelis.split()
d = {}
for x in range(len(notelist)):
    d["note{0}".format(x)] = notelist[x]

streamlist = list(d.values())
print(streamlist)
stream = stream.Stream()
streamtonote = []
for elem in streamlist:
    streamtonote.append(note.Note(elem))

for i in streamtonote:
    stream.append(i)

stream.show('midi')

newlist = []


for i in range(len(streamtonote)):
    Interval = interval.Interval(noteStart=stream[0], noteEnd=stream[i])
    for i in range(89):
        if Interval == interval.Interval(i):
            x1 = stream[0].transpose(-i)
            newlist.append(x1)
        elif Interval == interval.Interval(-i):
            x1 = stream[0].transpose(+i)
            newlist.append(x1)
        else:
            pass



print(newlist)

from music21 import stream
s = stream.Stream()
for i in newlist:
    s.append(i)

s.show('midi')
