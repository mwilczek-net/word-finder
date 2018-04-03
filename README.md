# word-finder
Find words that contains only available characters.

Grep-like behaviour. Script check every line from stdin if contains only available characters and
available occurence of characters. Supports 'any' characters. Outputs only matched words.

Helpfull sollutions for searching word list for games like Scrable, where player has limited
number of letters for building words.

For English language lists like enable1.txt ( https://code.google.com/archive/p/dotnetperls-controls/downloads )
can be used.

## Example:

### Only available chars
command:
```bash
cat enable1.txt | ./word-finder.py word
```

result:
```
do
dor
dow
od
or
ow
rod
row
wo
word
```

### Repeated chars
command:
```bash
cat enable1.txt | ./word-finder.py wood
```

result:
```
do
dow
od
ow
wo
woo
wood
```

### Available chars and one 'any' char present
command:
```bash
cat enable1.txt | ./word-finder.py word --any 1
```

result:
```
ad
ado
ar
aw
bo
bod
bow
bro
brow
cod
cor
cord
cow
crow
crowd
daw
de
dew
dhow
do
doc
doe
doer
dog
dol
dom
don
door
dor
dore
dork
dorm
dorp
dorr
dors
dory
dos
dot
dour
dow
dower
down
dowry
dows
draw
drew
drop
drown
dry
duo
duro
ed
er
for
ford
fro
frow
go
god
gor
gowd
grow
ho
hod
how
id
jo
jow
kor
lo
lord
low
mo
mod
mor
mow
no
nod
nor
now
oar
od
odd
ode
odor
ods
oe
of
oh
old
om
on
op
or
ora
orad
orb
orc
ordo
ore
ors
ort
os
oud
our
ow
owe
owed
owl
own
ox
oy
pod
pow
pro
prod
prow
rad
raw
re
red
redo
rho
rid
road
rob
roc
rod
rode
rods
roe
rom
rood
rot
row
rowdy
rowed
rows
so
sod
sord
sow
sword
to
tod
tor
tow
trod
trow
two
udo
urd
vow
vrow
wad
war
ward
we
wed
who
wo
woad
woe
wog
wok
wold
won
woo
wood
wop
word
words
wordy
wore
work
world
worm
worn
wort
wos
wot
wow
wry
wud
yo
yod
yow
```
