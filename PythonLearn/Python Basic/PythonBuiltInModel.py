#!/user/bin/python3
#^.^ coding=utf-8 ^.^#
from HelloWorld import cute_split_line

# 1. datetime
# 2. collections
# 3. base64
# 4. struct
# 5. hashlib
# 6. itertools
# 7. xml
# 8. htmlparser
# 9. urllib


#************ datetime ************#

from datetime import datetime,timedelta,timezone

print("now:", datetime.now())
print("now type:", type(datetime.now()))

print("One day:", datetime(2992, 7 , 3, 17, 42, 12))
print("One day time stamp:", datetime(2992, 7 , 3, 17, 42, 12).timestamp())
print("One day time stamp translate:", datetime.fromtimestamp(datetime(2992, 7 , 3, 17, 42, 12).timestamp()))
print("One day time stamp translate(UTC):", datetime.utcfromtimestamp(datetime(2992, 7 , 3, 17, 42, 12).timestamp()))

recv_format = "%Y-%m-%d %H:%M:%S"
show_format = "%H:%M:%S %Y-%m-%d"
print("String time to object:", datetime.strptime("2992-07-03 09:42:12", recv_format))
print("object time to String:", datetime.strptime("2992-07-03 09:42:12", recv_format).strftime(show_format))
print("add 2 hours from now:", datetime.now() + timedelta(hours=2))

cute_split_line()

#************ collections ************#

from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

namedtuple_sample = namedtuple('Point', ['x', 'y'])
p = namedtuple_sample(1,2)
print("namedtuple_sample p x:", p.x)
print("namedtuple_sample p y:", p.y)

cute_split_line()
deque_sample = deque()
for i in range(10):
    if i % 2:
        deque_sample.appendleft(i)
    else:
        deque_sample.append(i)

print("deque_sample:", deque_sample)

cute_split_line()

defaultdict_sample = defaultdict(lambda:None)
defaultdict_sample["var"] = "Earth"
print("defaultdict_sample var:", defaultdict_sample.get('var'))
print("defaultdict_sample var1:", defaultdict_sample.get('var1'))

cute_split_line()

# OrderedDict in PythonDataStruct.py

sample_text = '''
The Moon is Earth's only permanent natural satellite. It is one of the largest natural satellites in the Solar System, and the largest among planetary satellites relative to the size of the planet that it orbits (its primary). It is the second-densest satellite among those whose densities are known (after Jupiter's satellite Io).

The Moon is thought to have formed approximately 4.5 billion years ago, not long after Earth. There are several hypotheses for its origin; the most widely accepted explanation is that the Moon formed from the debris left over after a giant impact between Earth and a Mars-sized body called Theia.

The Moon is in synchronous rotation with Earth, always showing the same face with its near side marked by dark volcanic maria that fill between the bright ancient crustal highlands and the prominent impact craters. It is the second-brightest regularly visible celestial object in Earth's sky after the Sun, as measured by illuminance on Earth's surface. Its surface is actually dark (although it can appear a very bright white) with a reflectance just slightly higher than that of worn asphalt. Its prominence in the sky and its regular cycle of phases have made the Moon an important cultural influence since ancient times on language, calendars, art, and mythology.

The Moon's gravitational influence produces the ocean tides, body tides, and the slight lengthening of the day. The Moon's current orbital distance is about thirty times the diameter of Earth, with its apparent size in the sky almost the same as that of the Sun, resulting in the Moon covering the Sun nearly precisely in total solar eclipse. This matching of apparent visual size will not continue in the far future. The Moon's linear distance from Earth is currently increasing at a rate of 3.82 ± 0.07 centimetres (1.504 ± 0.028 in) per year, but this rate is not constant.

The Soviet Union's Luna programme was the first to reach the Moon with unmanned spacecraft in 1959; the United States' NASA Apollo program achieved the only manned missions to date, beginning with the first manned lunar orbiting mission by Apollo 8 in 1968, and six manned lunar landings between 1969 and 1972, with the first being Apollo 11. These missions returned over 380 kg (840 lb) of lunar rocks, which have been used to develop a geological understanding of the Moon's origin, the formation of its internal structure, and its subsequent history. After the Apollo 17 mission in 1972, the Moon has been visited only by unmanned spacecraft.
'''

c = Counter()
for char in sample_text:
    c[char] = c[char] + 1
print("counter", c)
