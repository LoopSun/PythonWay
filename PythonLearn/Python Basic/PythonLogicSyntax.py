#!/user/bin/python3
#^.^ coding=utf-8 ^.^#


# 1. if elif else
# 2. for ...
# 3. while ...
# 4.


#************  if elif else ************#

if 'Dog' > 'Cat':
    print('Dog Win')
elif 'Fish' > 'Cat':
    print('Fish Win')
else:
    print('Cat Win')

print("*"*20)

#************  for ... ************#

list_sample = (element for element in range(101) if not element % 2)

for each in list_sample:
    print(each)
    if each > 10:
        break
else:
    print("end for loop.")

#************  while ... ************#

while False:
    print("I am a stupid man.")