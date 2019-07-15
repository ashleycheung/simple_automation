'''
This code is written by Ashley Cheung
15/10/2018

This is a very simple code that holds down one of the following WASD keys
and moves in a random direction. It also holds down the space key to jump

This code was written for the roblox "legends of speed" game as an automated
bot that could easily run around in random directions to obtain points. The directkeys
module is essential for this code which can be found here:

https://gist.github.com/Aniruddha-Tapas/1627257344780e5429b10bc92eb2f52a

The following should be added into the directkeys module so that the wasd keys can
be used:

W = 0x11
A = 0x1E
S = 0x1F
D = 0x20
Spc = 0x39

General instructions on how to use this bot:
1) Open the roblox game and have it run on one side of your computer screen
2) Run this code and place it on the other side of your computer screen
3) Use your mouse and click your roblox game window to ensure the keys are
sent to that game window
4)The bot should now run in random directions infinitely

'''


import time, random
from directkeys import ReleaseKey, PressKey, W, A, S, D, Spc

'''
This is a countdown before the keys are sent. The roblox game should be loaded
before the countdown reaches 0
'''

for i in range(4):
    print(4-i);
    time.sleep(1);
    
#prints an output of the remaining steps before the direction is changed

def running(t):
    for i in range(t):
        print(str(t-i)+" steps remaining");
        time.sleep(1);


while(True):
    x=random.randint(1, 4);
    PressKey(Spc);
    if x==1:
        print('Running Forward');
        PressKey(W);
        running(5);
        ReleaseKey(W);
    elif x==2:
        print('Running Right')
        PressKey(D);
        running(5);
        ReleaseKey(D);
    elif x==3:
        print('Running Back')
        PressKey(S);
        running(5);
        ReleaseKey(S);
    elif x==4:
        print('Running Left')
        PressKey(A);
        running(5);
        ReleaseKey(A);
