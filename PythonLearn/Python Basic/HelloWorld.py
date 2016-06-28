#!/user/bin/python3
#^.^ coding=utf-8 ^.^#

def cute_split_line():
    print("*"*20)

class hello_world():
    def __init__(self, want_to_say = "Hello, World"):
        self.want_to_say = want_to_say

    def __str__(self):
        return self.want_to_say

    def say(self):
        print("{0}.".format(self.want_to_say))

if __name__ == "__main__":
    human = hello_world("Hi, Mama")
    human.say()