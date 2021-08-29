#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.4),
    on Sun Aug 29 11:38:14 2021
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.4'
expName = 'RSpan'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001', 'age': '', 'sex': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/sabrinado/Desktop/PsychoPy/RSpan/RSpan_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "TitleScreen"
TitleScreenClock = core.Clock()
introScreen = visual.TextStim(win=win, name='introScreen',
    text='Reading Span',
    font='Times New Roman',
    pos=(0, 0), height=0.10, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
responseIndicator1 = visual.TextStim(win=win, name='responseIndicator1',
    text='Click the mouse to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
mouse_1 = event.Mouse(win=win)
x, y = [None, None]
mouse_1.mouseClock = core.Clock()

# Initialize components for Routine "PracticeLetterInstruct1"
PracticeLetterInstruct1Clock = core.Clock()
instr_1 = visual.TextStim(win=win, name='instr_1',
    text='In this experiment you will try to memorize letters you see on the screen while you also read sentences.\n\nIn the next minutes, you will have some practice to get you familiar with how the experiment works.\n\nWe will begin by practicing the letter part of the experiment.\n\n',
    font='Times New Roman',
    pos=(0, 0), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
continue_2 = visual.TextStim(win=win, name='continue_2',
    text='Click the mouse to continue.\n',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()

# Initialize components for Routine "PracticeLetterInstruct2"
PracticeLetterInstruct2Clock = core.Clock()
instr_2 = visual.TextStim(win=win, name='instr_2',
    text='For this practice set, letters will appear on the screen one at a time.\n\nTry to remember each letter in the order presented.\n\nAfter 2 letters have been shown, you will see a screen listing 12 possible letters with a check box beside each one.\n\nYour job is to select each letter in the order presented. To do this, use the mouse to select the box beside each letter. The letters you select will appear at the bottom of the screen.',
    font='Times New Roman',
    pos=(0, 0), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
continue_3 = visual.TextStim(win=win, name='continue_3',
    text='Click the mouse to continue.\n\n',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()

# Initialize components for Routine "PracticeLetterInstruct3"
PracticeLetterInstruct3Clock = core.Clock()
instr_3 = visual.TextStim(win=win, name='instr_3',
    text='When you have selected all the letters, and they are in the correct order, hit the EXIT box at the bottom right of the screen.\n\nIf you make a mistake, hit the CLEAR box to start over.\n\nIf you forget one of the letters, click the BLANK box to mark the spot for the missing letter. \n\nRemember, it is very important to get the letters in the same order as you see them. If you forget one, use the BLANK box to mark the position.\n\nDo you have any questions so far?',
    font='Times New Roman',
    pos=(0, 0), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
continue_4 = visual.TextStim(win=win, name='continue_4',
    text='When you’re ready, click the mouse button to start the letter practice.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
mouse_4 = event.Mouse(win=win)
x, y = [None, None]
mouse_4.mouseClock = core.Clock()

# Initialize components for Routine "practiceList"
practiceListClock = core.Clock()
letterAppear = visual.TextStim(win=win, name='letterAppear',
    text=None,
    font='Times New Roman',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
from numpy.random import choice
letterAppear_2 = visual.TextStim(win=win, name='letterAppear_2',
    text=None,
    font='Times New Roman',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "practiceRecall"
practiceRecallClock = core.Clock()
mouseClear = event.Mouse(win=win)
x, y = [None, None]
mouseClear.mouseClock = core.Clock()
correctLettersPractice=0
correctLettersTrial = 0
mouseExit = event.Mouse(win=win)
x, y = [None, None]
mouseExit.mouseClock = core.Clock()
mouse1 = event.Mouse(win=win)
x, y = [None, None]
mouse1.mouseClock = core.Clock()
blankButton = visual.Rect(
    win=win, name='blankButton',
    width=(0.15, 0.08)[0], height=(0.15, 0.08)[1],
    ori=0, pos=(0.4, -0.4),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
gatherResponseText = visual.TextStim(win=win, name='gatherResponseText',
    text='Select the letters in the order presented. Use the blank button to fill in forgotten letters. ',
    font='Times New Roman',
    pos=(0, 0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
Fbutton = visual.Rect(
    win=win, name='Fbutton',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(-.3, 0.3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
F_text = visual.TextStim(win=win, name='F_text',
    text='F',
    font='Times New Roman',
    pos=(-.23, 0.3), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
Pbutton = visual.Rect(
    win=win, name='Pbutton',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(-0.3, 0.20),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
Qbutton = visual.Rect(
    win=win, name='Qbutton',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(-0.3, 0.10),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)
Jbutton = visual.Rect(
    win=win, name='Jbutton',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(-0.3, 0.0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-10.0, interpolate=True)
Hbutton = visual.Rect(
    win=win, name='Hbutton',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(-0.3, -0.10),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-11.0, interpolate=True)
Kbutton = visual.Rect(
    win=win, name='Kbutton',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(-0.3, -.20),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-12.0, interpolate=True)
Tbutton = visual.Rect(
    win=win, name='Tbutton',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(0.2, 0.3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-13.0, interpolate=True)
Sbutton = visual.Rect(
    win=win, name='Sbutton',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(0.2, 0.20),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-14.0, interpolate=True)
Nbutton = visual.Rect(
    win=win, name='Nbutton',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(0.2, 0.10),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-15.0, interpolate=True)
Rbutton = visual.Rect(
    win=win, name='Rbutton',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(0.2, 0.00),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-16.0, interpolate=True)
Ybutton = visual.Rect(
    win=win, name='Ybutton',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(0.2, -0.10),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-17.0, interpolate=True)
Lbutton = visual.Rect(
    win=win, name='Lbutton',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(0.2, -0.20),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-18.0, interpolate=True)
clearButton = visual.Rect(
    win=win, name='clearButton',
    width=(0.15, 0.08)[0], height=(0.15, 0.08)[1],
    ori=0, pos=(0, -0.4),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-19.0, interpolate=True)
exitButton = visual.Rect(
    win=win, name='exitButton',
    width=(0.15, 0.08)[0], height=(0.15, 0.08)[1],
    ori=0, pos=(-0.4, -0.4),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-20.0, interpolate=True)
exitText = visual.TextStim(win=win, name='exitText',
    text='EXIT',
    font='Times New Roman',
    pos=(-0.4, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-21.0);
clearText = visual.TextStim(win=win, name='clearText',
    text='CLEAR',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-22.0);
P_text = visual.TextStim(win=win, name='P_text',
    text='P',
    font='Times New Roman',
    pos=(-.23, 0.2), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-23.0);
Q_text = visual.TextStim(win=win, name='Q_text',
    text='Q',
    font='Times New Roman',
    pos=(-.23, 0.10), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-24.0);
J_text = visual.TextStim(win=win, name='J_text',
    text='J',
    font='Times New Roman',
    pos=(-.23, 0.0), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-25.0);
H_text = visual.TextStim(win=win, name='H_text',
    text='H',
    font='Times New Roman',
    pos=(-.23, -0.1), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-26.0);
K_text = visual.TextStim(win=win, name='K_text',
    text='K',
    font='Times New Roman',
    pos=(-.23, -0.2), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-27.0);
T_text = visual.TextStim(win=win, name='T_text',
    text='T',
    font='Times New Roman',
    pos=(.27, 0.3), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-28.0);
S_text = visual.TextStim(win=win, name='S_text',
    text='S',
    font='Times New Roman',
    pos=(.27, 0.2), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-29.0);
N_text = visual.TextStim(win=win, name='N_text',
    text='N',
    font='Times New Roman',
    pos=(.27, 0.1), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-30.0);
R_text = visual.TextStim(win=win, name='R_text',
    text='R',
    font='Times New Roman',
    pos=(.27, 0.0), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-31.0);
Y_text = visual.TextStim(win=win, name='Y_text',
    text='Y',
    font='Times New Roman',
    pos=(.27, -0.1), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-32.0);
L_text = visual.TextStim(win=win, name='L_text',
    text='L',
    font='Times New Roman',
    pos=(.27, -0.2), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-33.0);
blankText = visual.TextStim(win=win, name='blankText',
    text='BLANK',
    font='Times New Roman',
    pos=(0.4, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-34.0);
answer1 = visual.TextStim(win=win, name='answer1',
    text=None,
    font='Times New Roman',
    pos=(-0.05, -0.20), height=0.040, wrapWidth=None, ori=0, 
    color='grey', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-35.0);
answer2 = visual.TextStim(win=win, name='answer2',
    text=None,
    font='Times New Roman',
    pos=(0.05, -0.2), height=0.040, wrapWidth=None, ori=0, 
    color='grey', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-36.0);
mouseBlank = event.Mouse(win=win)
x, y = [None, None]
mouseBlank.mouseClock = core.Clock()

# Initialize components for Routine "PractSentInst1"
PractSentInst1Clock = core.Clock()
instr_4 = visual.TextStim(win=win, name='instr_4',
    text='Now you will practice doing the sentence reading part of the experiment.\n\nA sentence will appear on the screen, like this:\n“I like to run in the park”\n\nAs soon as you see the sentence, you should read it and determine if it makes sense or not.\n\nThe above sentence makes sense.\n\nWhen you have read the sentence and determined whether it makes sense or not, you will click the mouse buttton.',
    font='Times New Roman',
    pos=(0, 0), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
continue_5 = visual.TextStim(win=win, name='continue_5',
    text='Click the mouse to continue.\n',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
mouse_5 = event.Mouse(win=win)
x, y = [None, None]
mouse_5.mouseClock = core.Clock()

# Initialize components for Routine "PractSenInst2"
PractSenInst2Clock = core.Clock()
instr_5 = visual.TextStim(win=win, name='instr_5',
    text='You will then see “This sentence makes sense.” displayed on the next screen along with a box marked TRUE and a box marked FALSE.\n\nIf the sentence on the previous screen made sense, click on the TRUE box with the box.\n\nIf the sentence did not make sense, click on the FALSE box.\n\nAfter you click on one of the boxes, the computer will tell you if you made the right choice.',
    font='Times New Roman',
    pos=(0, 0), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
continue_6 = visual.TextStim(win=win, name='continue_6',
    text='Click the mouse to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
mouse_6 = event.Mouse(win=win)
x, y = [None, None]
mouse_6.mouseClock = core.Clock()

# Initialize components for Routine "PracSenInst3"
PracSenInst3Clock = core.Clock()
instr_6 = visual.TextStim(win=win, name='instr_6',
    text='It is VERY important that you answer the sentence problems correctly. It is also important that you try and read the sentences as quickly as you can.\n\nDo you have any questions?',
    font='Times New Roman',
    pos=(0, 0), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
continue_7 = visual.TextStim(win=win, name='continue_7',
    text='When you’re ready, click the mouse to try some practice problems. ',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
mouse_7 = event.Mouse(win=win)
x, y = [None, None]
mouse_7.mouseClock = core.Clock()

# Initialize components for Routine "sentence"
sentenceClock = core.Clock()
sentenceText = visual.TextStim(win=win, name='sentenceText',
    text='default text',
    font='Times New Roman',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
continue_12 = visual.TextStim(win=win, name='continue_12',
    text='When you have read the sentence, click the mouse to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

avgTime = 0
totalTime = 0
text_3 = visual.TextStim(win=win, name='text_3',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "sentenceResponse"
sentenceResponseClock = core.Clock()
totalCorrectPractice = 0
senseText = visual.TextStim(win=win, name='senseText',
    text='This sentence makes sense.',
    font='Times New Roman',
    pos=(0, 0.2), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
trueButton = visual.Rect(
    win=win, name='trueButton',
    width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
    ori=0, pos=(-0.20, -0.2),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
trueText = visual.TextStim(win=win, name='trueText',
    text='TRUE',
    font='Times New Roman',
    pos=(-0.20, -0.2), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
falseButton = visual.Rect(
    win=win, name='falseButton',
    width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
    ori=0, pos=(0.20, -0.2),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
falseText = visual.TextStim(win=win, name='falseText',
    text='FALSE',
    font='Times New Roman',
    pos=(0.20, -0.2), height=0.040, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
mouse12 = event.Mouse(win=win)
x, y = [None, None]
mouse12.mouseClock = core.Clock()

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
sentenceFeedback2 = visual.TextStim(win=win, name='sentenceFeedback2',
    text='default text',
    font='Times New Roman',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "RSPANpracticeInstruct1_2"
RSPANpracticeInstruct1_2Clock = core.Clock()
instr_7 = visual.TextStim(win=win, name='instr_7',
    text='Now you will practice doing both parts of the experiment at the same time. \n\nIn the next practice set, you will be given one sentence to read. Once you make your decision about the sentence, a letter will appear on the screen. Try and remember the letter.\n\nIn the previous section where you only read the sentences, the computer computed your average time to read the sentences. If you take longer than your average time, the computer will automatically move you onto the next part, thus skipping the True or False part and will count that problem as a sentence error. Thefore it is a VERY important to read the sentences as quickly and as accurately as possible. ',
    font='Times New Roman',
    pos=(0, 0), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
continue_8 = visual.TextStim(win=win, name='continue_8',
    text='Click the mouse to continue.\n\n',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
mouse_8 = event.Mouse(win=win)
x, y = [None, None]
mouse_8.mouseClock = core.Clock()

# Initialize components for Routine "RSPANpracticeInstruct2"
RSPANpracticeInstruct2Clock = core.Clock()
instr_8 = visual.TextStim(win=win, name='instr_8',
    text='After the letter goes away, another sentence will appear, and then another letter.\n\nAt the end of each set of letters and sentences, a recall screen will appear. Use the mouse to select the letter you just saw. Try your best to get the letters in the correct order.\n\nIt is important to work QUICKLY and ACCURATELY on the sentences. Make sure you know whether the sentences make sense or not before clicking to the next screen.\n\nYou will not be told if you answer regarding the sentence is correct.\n',
    font='Times New Roman',
    pos=(0, 0), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
continue_9 = visual.TextStim(win=win, name='continue_9',
    text='Click the mouse button to continue.\n',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
mouse_9 = event.Mouse(win=win)
x, y = [None, None]
mouse_9.mouseClock = core.Clock()

# Initialize components for Routine "feedbackinstruct"
feedbackinstructClock = core.Clock()
instr_9 = visual.TextStim(win=win, name='instr_9',
    text='After the recall screen, you will be given feedback about your performance regarding both the number of letters recalled and the percent correct on the sentence problems.',
    font='Times New Roman',
    pos=(0, 0), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
continue_10 = visual.TextStim(win=win, name='continue_10',
    text='Do you have any questions?\nClick the mouse to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
mouse_10 = event.Mouse(win=win)
x, y = [None, None]
mouse_10.mouseClock = core.Clock()

# Initialize components for Routine "feedbackinstruct2"
feedbackinstruct2Clock = core.Clock()
instr_10 = visual.TextStim(win=win, name='instr_10',
    text='During the feedback, you will see a number in red in the top right of the screen. \nThis indicates your percent correct for the sentence problems for the entire experiment.\n\nIt is VERY important for you to keep this at least an 85%.\n\nFor our purposes, we can only use data where the participant was at least 85% accurate on the sentences.\n\nTherefore, try to perform at least an 85% on the sentence problems WHILE doing your best to recall as many letters as possible.',
    font='Times New Roman',
    pos=(0, 0), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
continue_11 = visual.TextStim(win=win, name='continue_11',
    text='Do you have any questions?\nClick the mouse to try some practice problems. ',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
mouse_11 = event.Mouse(win=win)
x, y = [None, None]
mouse_11.mouseClock = core.Clock()

# Initialize components for Routine "sentence2"
sentence2Clock = core.Clock()
sentenceText2 = visual.TextStim(win=win, name='sentenceText2',
    text='default text',
    font='Times New Roman',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
mouse_12 = event.Mouse(win=win)
x, y = [None, None]
mouse_12.mouseClock = core.Clock()
continue_13 = visual.TextStim(win=win, name='continue_13',
    text='When you have read the sentence, click the mouse to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

timerReading = core.Clock()

avgTime = 0
totalTime = 0
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0.4, -0.4), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "sentenceResponseTrial"
sentenceResponseTrialClock = core.Clock()
totalCorrectSentenceTrial= 0
senseText_2 = visual.TextStim(win=win, name='senseText_2',
    text='This sentence makes sense.',
    font='Times New Roman',
    pos=(0, 0.2), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
trueButton_2 = visual.Rect(
    win=win, name='trueButton_2',
    width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
    ori=0, pos=(-0.20, -0.2),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
trueText_2 = visual.TextStim(win=win, name='trueText_2',
    text='TRUE',
    font='Times New Roman',
    pos=(-0.20, -0.2), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
falseButton_2 = visual.Rect(
    win=win, name='falseButton_2',
    width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
    ori=0, pos=(0.20, -0.2),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
falseText_2 = visual.TextStim(win=win, name='falseText_2',
    text='FALSE',
    font='Times New Roman',
    pos=(0.20, -0.2), height=0.040, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
mouse12_2 = event.Mouse(win=win)
x, y = [None, None]
mouse12_2.mouseClock = core.Clock()

# Initialize components for Routine "practiceList"
practiceListClock = core.Clock()
letterAppear = visual.TextStim(win=win, name='letterAppear',
    text=None,
    font='Times New Roman',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
from numpy.random import choice
letterAppear_2 = visual.TextStim(win=win, name='letterAppear_2',
    text=None,
    font='Times New Roman',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "practiceRecall"
practiceRecallClock = core.Clock()
mouseClear = event.Mouse(win=win)
x, y = [None, None]
mouseClear.mouseClock = core.Clock()
correctLettersPractice=0
correctLettersTrial = 0
mouseExit = event.Mouse(win=win)
x, y = [None, None]
mouseExit.mouseClock = core.Clock()
mouse1 = event.Mouse(win=win)
x, y = [None, None]
mouse1.mouseClock = core.Clock()
blankButton = visual.Rect(
    win=win, name='blankButton',
    width=(0.15, 0.08)[0], height=(0.15, 0.08)[1],
    ori=0, pos=(0.4, -0.4),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
gatherResponseText = visual.TextStim(win=win, name='gatherResponseText',
    text='Select the letters in the order presented. Use the blank button to fill in forgotten letters. ',
    font='Times New Roman',
    pos=(0, 0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
Fbutton = visual.Rect(
    win=win, name='Fbutton',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(-.3, 0.3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
F_text = visual.TextStim(win=win, name='F_text',
    text='F',
    font='Times New Roman',
    pos=(-.23, 0.3), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
Pbutton = visual.Rect(
    win=win, name='Pbutton',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(-0.3, 0.20),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
Qbutton = visual.Rect(
    win=win, name='Qbutton',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(-0.3, 0.10),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)
Jbutton = visual.Rect(
    win=win, name='Jbutton',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(-0.3, 0.0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-10.0, interpolate=True)
Hbutton = visual.Rect(
    win=win, name='Hbutton',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(-0.3, -0.10),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-11.0, interpolate=True)
Kbutton = visual.Rect(
    win=win, name='Kbutton',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(-0.3, -.20),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-12.0, interpolate=True)
Tbutton = visual.Rect(
    win=win, name='Tbutton',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(0.2, 0.3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-13.0, interpolate=True)
Sbutton = visual.Rect(
    win=win, name='Sbutton',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(0.2, 0.20),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-14.0, interpolate=True)
Nbutton = visual.Rect(
    win=win, name='Nbutton',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(0.2, 0.10),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-15.0, interpolate=True)
Rbutton = visual.Rect(
    win=win, name='Rbutton',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(0.2, 0.00),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-16.0, interpolate=True)
Ybutton = visual.Rect(
    win=win, name='Ybutton',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(0.2, -0.10),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-17.0, interpolate=True)
Lbutton = visual.Rect(
    win=win, name='Lbutton',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0, pos=(0.2, -0.20),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-18.0, interpolate=True)
clearButton = visual.Rect(
    win=win, name='clearButton',
    width=(0.15, 0.08)[0], height=(0.15, 0.08)[1],
    ori=0, pos=(0, -0.4),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-19.0, interpolate=True)
exitButton = visual.Rect(
    win=win, name='exitButton',
    width=(0.15, 0.08)[0], height=(0.15, 0.08)[1],
    ori=0, pos=(-0.4, -0.4),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-20.0, interpolate=True)
exitText = visual.TextStim(win=win, name='exitText',
    text='EXIT',
    font='Times New Roman',
    pos=(-0.4, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-21.0);
clearText = visual.TextStim(win=win, name='clearText',
    text='CLEAR',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-22.0);
P_text = visual.TextStim(win=win, name='P_text',
    text='P',
    font='Times New Roman',
    pos=(-.23, 0.2), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-23.0);
Q_text = visual.TextStim(win=win, name='Q_text',
    text='Q',
    font='Times New Roman',
    pos=(-.23, 0.10), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-24.0);
J_text = visual.TextStim(win=win, name='J_text',
    text='J',
    font='Times New Roman',
    pos=(-.23, 0.0), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-25.0);
H_text = visual.TextStim(win=win, name='H_text',
    text='H',
    font='Times New Roman',
    pos=(-.23, -0.1), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-26.0);
K_text = visual.TextStim(win=win, name='K_text',
    text='K',
    font='Times New Roman',
    pos=(-.23, -0.2), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-27.0);
T_text = visual.TextStim(win=win, name='T_text',
    text='T',
    font='Times New Roman',
    pos=(.27, 0.3), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-28.0);
S_text = visual.TextStim(win=win, name='S_text',
    text='S',
    font='Times New Roman',
    pos=(.27, 0.2), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-29.0);
N_text = visual.TextStim(win=win, name='N_text',
    text='N',
    font='Times New Roman',
    pos=(.27, 0.1), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-30.0);
R_text = visual.TextStim(win=win, name='R_text',
    text='R',
    font='Times New Roman',
    pos=(.27, 0.0), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-31.0);
Y_text = visual.TextStim(win=win, name='Y_text',
    text='Y',
    font='Times New Roman',
    pos=(.27, -0.1), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-32.0);
L_text = visual.TextStim(win=win, name='L_text',
    text='L',
    font='Times New Roman',
    pos=(.27, -0.2), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-33.0);
blankText = visual.TextStim(win=win, name='blankText',
    text='BLANK',
    font='Times New Roman',
    pos=(0.4, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-34.0);
answer1 = visual.TextStim(win=win, name='answer1',
    text=None,
    font='Times New Roman',
    pos=(-0.05, -0.20), height=0.040, wrapWidth=None, ori=0, 
    color='grey', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-35.0);
answer2 = visual.TextStim(win=win, name='answer2',
    text=None,
    font='Times New Roman',
    pos=(0.05, -0.2), height=0.040, wrapWidth=None, ori=0, 
    color='grey', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-36.0);
mouseBlank = event.Mouse(win=win)
x, y = [None, None]
mouseBlank.mouseClock = core.Clock()

# Initialize components for Routine "feedback_2"
feedback_2Clock = core.Clock()
lettersCorrect = visual.TextStim(win=win, name='lettersCorrect',
    text='default text',
    font='Times New Roman',
    pos=(0, 0.2), height=0.1, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
correctLetters = 0
text_2 = visual.TextStim(win=win, name='text_2',
    text='default text',
    font='Times New Roman',
    pos=(0, -0.2), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
Feedback = visual.TextStim(win=win, name='Feedback',
    text='Feedback',
    font='Times New Roman',
    pos=(0, 0.4), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "TitleScreen"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_1
gotValidClick = False  # until a click is received
# keep track of which components have finished
TitleScreenComponents = [introScreen, responseIndicator1, mouse_1]
for thisComponent in TitleScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
TitleScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "TitleScreen"-------
while continueRoutine:
    # get current time
    t = TitleScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=TitleScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *introScreen* updates
    if introScreen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        introScreen.frameNStart = frameN  # exact frame index
        introScreen.tStart = t  # local t and not account for scr refresh
        introScreen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introScreen, 'tStartRefresh')  # time at next scr refresh
        introScreen.setAutoDraw(True)
    
    # *responseIndicator1* updates
    if responseIndicator1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        responseIndicator1.frameNStart = frameN  # exact frame index
        responseIndicator1.tStart = t  # local t and not account for scr refresh
        responseIndicator1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(responseIndicator1, 'tStartRefresh')  # time at next scr refresh
        responseIndicator1.setAutoDraw(True)
    # *mouse_1* updates
    if mouse_1.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_1.frameNStart = frameN  # exact frame index
        mouse_1.tStart = t  # local t and not account for scr refresh
        mouse_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_1, 'tStartRefresh')  # time at next scr refresh
        mouse_1.status = STARTED
        mouse_1.mouseClock.reset()
        prevButtonState = mouse_1.getPressed()  # if button is down already this ISN'T a new click
    if mouse_1.status == STARTED:  # only update if started and not finished!
        buttons = mouse_1.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TitleScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "TitleScreen"-------
for thisComponent in TitleScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('introScreen.started', introScreen.tStartRefresh)
thisExp.addData('introScreen.stopped', introScreen.tStopRefresh)
thisExp.addData('responseIndicator1.started', responseIndicator1.tStartRefresh)
thisExp.addData('responseIndicator1.stopped', responseIndicator1.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_1.started', mouse_1.tStart)
thisExp.addData('mouse_1.stopped', mouse_1.tStop)
thisExp.nextEntry()
# the Routine "TitleScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "PracticeLetterInstruct1"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_2
gotValidClick = False  # until a click is received
# keep track of which components have finished
PracticeLetterInstruct1Components = [instr_1, continue_2, mouse_2]
for thisComponent in PracticeLetterInstruct1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PracticeLetterInstruct1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "PracticeLetterInstruct1"-------
while continueRoutine:
    # get current time
    t = PracticeLetterInstruct1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PracticeLetterInstruct1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_1* updates
    if instr_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_1.frameNStart = frameN  # exact frame index
        instr_1.tStart = t  # local t and not account for scr refresh
        instr_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_1, 'tStartRefresh')  # time at next scr refresh
        instr_1.setAutoDraw(True)
    
    # *continue_2* updates
    if continue_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        continue_2.frameNStart = frameN  # exact frame index
        continue_2.tStart = t  # local t and not account for scr refresh
        continue_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continue_2, 'tStartRefresh')  # time at next scr refresh
        continue_2.setAutoDraw(True)
    # *mouse_2* updates
    if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_2.frameNStart = frameN  # exact frame index
        mouse_2.tStart = t  # local t and not account for scr refresh
        mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
        mouse_2.status = STARTED
        mouse_2.mouseClock.reset()
        prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
    if mouse_2.status == STARTED:  # only update if started and not finished!
        buttons = mouse_2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PracticeLetterInstruct1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PracticeLetterInstruct1"-------
for thisComponent in PracticeLetterInstruct1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr_1.started', instr_1.tStartRefresh)
thisExp.addData('instr_1.stopped', instr_1.tStopRefresh)
thisExp.addData('continue_2.started', continue_2.tStartRefresh)
thisExp.addData('continue_2.stopped', continue_2.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_2.started', mouse_2.tStart)
thisExp.addData('mouse_2.stopped', mouse_2.tStop)
thisExp.nextEntry()
# the Routine "PracticeLetterInstruct1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "PracticeLetterInstruct2"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_3
gotValidClick = False  # until a click is received
# keep track of which components have finished
PracticeLetterInstruct2Components = [instr_2, continue_3, mouse_3]
for thisComponent in PracticeLetterInstruct2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PracticeLetterInstruct2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "PracticeLetterInstruct2"-------
while continueRoutine:
    # get current time
    t = PracticeLetterInstruct2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PracticeLetterInstruct2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_2* updates
    if instr_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_2.frameNStart = frameN  # exact frame index
        instr_2.tStart = t  # local t and not account for scr refresh
        instr_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_2, 'tStartRefresh')  # time at next scr refresh
        instr_2.setAutoDraw(True)
    
    # *continue_3* updates
    if continue_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        continue_3.frameNStart = frameN  # exact frame index
        continue_3.tStart = t  # local t and not account for scr refresh
        continue_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continue_3, 'tStartRefresh')  # time at next scr refresh
        continue_3.setAutoDraw(True)
    # *mouse_3* updates
    if mouse_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_3.frameNStart = frameN  # exact frame index
        mouse_3.tStart = t  # local t and not account for scr refresh
        mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_3, 'tStartRefresh')  # time at next scr refresh
        mouse_3.status = STARTED
        mouse_3.mouseClock.reset()
        prevButtonState = mouse_3.getPressed()  # if button is down already this ISN'T a new click
    if mouse_3.status == STARTED:  # only update if started and not finished!
        buttons = mouse_3.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PracticeLetterInstruct2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PracticeLetterInstruct2"-------
for thisComponent in PracticeLetterInstruct2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr_2.started', instr_2.tStartRefresh)
thisExp.addData('instr_2.stopped', instr_2.tStopRefresh)
thisExp.addData('continue_3.started', continue_3.tStartRefresh)
thisExp.addData('continue_3.stopped', continue_3.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_3.started', mouse_3.tStart)
thisExp.addData('mouse_3.stopped', mouse_3.tStop)
thisExp.nextEntry()
# the Routine "PracticeLetterInstruct2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "PracticeLetterInstruct3"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_4
gotValidClick = False  # until a click is received
# keep track of which components have finished
PracticeLetterInstruct3Components = [instr_3, continue_4, mouse_4]
for thisComponent in PracticeLetterInstruct3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PracticeLetterInstruct3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "PracticeLetterInstruct3"-------
while continueRoutine:
    # get current time
    t = PracticeLetterInstruct3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PracticeLetterInstruct3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_3* updates
    if instr_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_3.frameNStart = frameN  # exact frame index
        instr_3.tStart = t  # local t and not account for scr refresh
        instr_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_3, 'tStartRefresh')  # time at next scr refresh
        instr_3.setAutoDraw(True)
    
    # *continue_4* updates
    if continue_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        continue_4.frameNStart = frameN  # exact frame index
        continue_4.tStart = t  # local t and not account for scr refresh
        continue_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continue_4, 'tStartRefresh')  # time at next scr refresh
        continue_4.setAutoDraw(True)
    # *mouse_4* updates
    if mouse_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_4.frameNStart = frameN  # exact frame index
        mouse_4.tStart = t  # local t and not account for scr refresh
        mouse_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_4, 'tStartRefresh')  # time at next scr refresh
        mouse_4.status = STARTED
        mouse_4.mouseClock.reset()
        prevButtonState = mouse_4.getPressed()  # if button is down already this ISN'T a new click
    if mouse_4.status == STARTED:  # only update if started and not finished!
        buttons = mouse_4.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PracticeLetterInstruct3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PracticeLetterInstruct3"-------
for thisComponent in PracticeLetterInstruct3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr_3.started', instr_3.tStartRefresh)
thisExp.addData('instr_3.stopped', instr_3.tStopRefresh)
thisExp.addData('continue_4.started', continue_4.tStartRefresh)
thisExp.addData('continue_4.stopped', continue_4.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_4.started', mouse_4.tStart)
thisExp.addData('mouse_4.stopped', mouse_4.tStop)
thisExp.nextEntry()
# the Routine "PracticeLetterInstruct3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practiceLoop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('practiceLetter.xlsx'),
    seed=None, name='practiceLoop')
thisExp.addLoop(practiceLoop)  # add the loop to the experiment
thisPracticeLoop = practiceLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracticeLoop.rgb)
if thisPracticeLoop != None:
    for paramName in thisPracticeLoop:
        exec('{} = thisPracticeLoop[paramName]'.format(paramName))

for thisPracticeLoop in practiceLoop:
    currentLoop = practiceLoop
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeLoop.rgb)
    if thisPracticeLoop != None:
        for paramName in thisPracticeLoop:
            exec('{} = thisPracticeLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "practiceList"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    letterAppear.setText('')
    letters = ["F", "P", "Q", "J", "H", "K", "T", "S", "N", "R", "Y", "L"]
    firstLetter = choice(letters)
    letters.remove(firstLetter)
    secondLetter = choice(letters)
    letters.append(firstLetter)
    
    letterAppear.setText(firstLetter)
    letterAppear_2.setText(secondLetter)
    # keep track of which components have finished
    practiceListComponents = [letterAppear, letterAppear_2]
    for thisComponent in practiceListComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practiceListClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practiceList"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = practiceListClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practiceListClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *letterAppear* updates
        if letterAppear.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            letterAppear.frameNStart = frameN  # exact frame index
            letterAppear.tStart = t  # local t and not account for scr refresh
            letterAppear.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letterAppear, 'tStartRefresh')  # time at next scr refresh
            letterAppear.setAutoDraw(True)
        if letterAppear.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > letterAppear.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                letterAppear.tStop = t  # not accounting for scr refresh
                letterAppear.frameNStop = frameN  # exact frame index
                win.timeOnFlip(letterAppear, 'tStopRefresh')  # time at next scr refresh
                letterAppear.setAutoDraw(False)
        
        # *letterAppear_2* updates
        if letterAppear_2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            letterAppear_2.frameNStart = frameN  # exact frame index
            letterAppear_2.tStart = t  # local t and not account for scr refresh
            letterAppear_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letterAppear_2, 'tStartRefresh')  # time at next scr refresh
            letterAppear_2.setAutoDraw(True)
        if letterAppear_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > letterAppear_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                letterAppear_2.tStop = t  # not accounting for scr refresh
                letterAppear_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(letterAppear_2, 'tStopRefresh')  # time at next scr refresh
                letterAppear_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceListComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practiceList"-------
    for thisComponent in practiceListComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practiceLoop.addData('letterAppear.started', letterAppear.tStartRefresh)
    practiceLoop.addData('letterAppear.stopped', letterAppear.tStopRefresh)
    practiceLoop.addData('letterAppear_2.started', letterAppear_2.tStartRefresh)
    practiceLoop.addData('letterAppear_2.stopped', letterAppear_2.tStopRefresh)
    
    # ------Prepare to start Routine "practiceRecall"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouseClear
    mouseClear.clicked_name = []
    gotValidClick = False  # until a click is received
    checkboxes = [Fbutton, Pbutton, Qbutton, Jbutton, Hbutton, Kbutton, Tbutton, Sbutton, Nbutton, Rbutton, Ybutton, Lbutton]
    clicked = []
    clickedTrack = []
    
    timer = core.Clock()
    timer.reset()
    
    # setup some python lists for storing info about the mouseExit
    mouseExit.x = []
    mouseExit.y = []
    mouseExit.leftButton = []
    mouseExit.midButton = []
    mouseExit.rightButton = []
    mouseExit.time = []
    mouseExit.clicked_name = []
    gotValidClick = False  # until a click is received
    # setup some python lists for storing info about the mouse1
    mouse1.x = []
    mouse1.y = []
    mouse1.leftButton = []
    mouse1.midButton = []
    mouse1.rightButton = []
    mouse1.time = []
    mouse1.clicked_name = []
    gotValidClick = False  # until a click is received
    Fbutton.setFillColor('green')
    Pbutton.setFillColor('green')
    Qbutton.setFillColor('green')
    Jbutton.setFillColor('green')
    Hbutton.setFillColor('green')
    Kbutton.setFillColor('green')
    Tbutton.setFillColor('green')
    Sbutton.setFillColor('green')
    Nbutton.setFillColor('green')
    Rbutton.setFillColor('green')
    Ybutton.setFillColor('green')
    Lbutton.setFillColor('green')
    answer1.setText('')
    answer2.setText('')
    # setup some python lists for storing info about the mouseBlank
    mouseBlank.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    practiceRecallComponents = [mouseClear, mouseExit, mouse1, blankButton, gatherResponseText, Fbutton, F_text, Pbutton, Qbutton, Jbutton, Hbutton, Kbutton, Tbutton, Sbutton, Nbutton, Rbutton, Ybutton, Lbutton, clearButton, exitButton, exitText, clearText, P_text, Q_text, J_text, H_text, K_text, T_text, S_text, N_text, R_text, Y_text, L_text, blankText, answer1, answer2, mouseBlank]
    for thisComponent in practiceRecallComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practiceRecallClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practiceRecall"-------
    while continueRoutine:
        # get current time
        t = practiceRecallClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practiceRecallClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if mouseExit.isPressedIn(exitButton):
            continueRoutine = False
        
        if mouseBlank.isPressedIn(blankButton):
            clicked.append(blankButton)
            clickedTrack.append(box)
            answer1.color = "white"
            answer2.color = "white"
            if len(clicked)==1:
                answer1.setText("Blank")
            elif len(clicked) ==2:
               answer2.setText("Blank")
        
        for box in checkboxes:
            if mouse1.isPressedIn(box) and box.name not in clicked and len(clicked)==0:
                box.fillColor = "black"
                clicked.append(box.name)
                clickedTrack.append(box)
                answer1.color = "white"
                if box.name is "Fbutton":
                    answer1.setText("F")
                elif box.name is "Pbutton":
                    answer1.setText("P")
                elif box.name is "Qbutton":
                    answer1.setText("Q")
                elif box.name is "Jbutton":
                    answer1.setText("J")
                elif box.name is "Hbutton":
                    answer1.setText("H")
                elif box.name is "Kbutton":
                    answer1.setText("K")
                elif box.name is "Tbutton":
                    answer1.setText("T")
                elif box.name is"Sbutton":
                    answer1.setText("S")
                elif box.name is "Nbutton":
                    answer1.setText("N")
                elif box.name is "Rbutton":
                    answer1.setText("R")
                elif box.name is "Ybutton":
                    answer1.setText("Y")
                elif box.name is "Lbutton":
                    answer1.setText("L")
        
        for box in checkboxes:
            if mouse1.isPressedIn(box) and box.name not in clicked and len(clicked) ==1:
                box.fillColor = "black"
                clicked.append(box.name)
                answer2.color = "white"
                clickedTrack.append(box)
                if box.name is "Fbutton":
                    answer2.setText("F")
                elif box.name is "Pbutton":
                    answer2.setText("P")
                elif box.name is "Qbutton":
                    answer2.setText("Q")
                elif box.name is "Jbutton":
                    answer2.setText("J")
                elif box.name is "Hbutton":
                    answer2.setText("H")
                elif box.name is "Kbutton":
                    answer2.setText("K")
                elif box.name is "Tbutton":
                    answer2.setText("T")
                elif box.name is"Sbutton":
                    answer2.setText("S")
                elif box.name is "Nbutton":
                    answer2.setText("N")
                elif box.name is "Rbutton":
                    answer2.setText("R")
                elif box.name is "Ybutton":
                    answer2.setText("Y")
                elif box.name is "Lbutton":
                       answer2.setText("L")
                elif box.name is "blankButton":
                    answer2.setText("Blank")
        
        if mouseClear.isPressedIn(clearButton):
            if len(clicked) ==1:
                if clickedTrack[0] is not blankButton:
                    clickedTrack[0].fillColor = "green"
            answer1.setText("")
            answer2.setText("")
            if len(clicked)  ==2:
                if clickedTrack[0] is not blankButton:
                    clickedTrack[0].fillColor = "green"
                if clickedTrack[1] is not blankButton:
                    clickedTrack[1].fillColor  = "green"
            clicked = []
            clickedTrack = []
        
        
        
        # *mouseExit* updates
        if mouseExit.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouseExit.frameNStart = frameN  # exact frame index
            mouseExit.tStart = t  # local t and not account for scr refresh
            mouseExit.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouseExit, 'tStartRefresh')  # time at next scr refresh
            mouseExit.status = STARTED
            mouseExit.mouseClock.reset()
            prevButtonState = mouseExit.getPressed()  # if button is down already this ISN'T a new click
        if mouseExit.status == STARTED:  # only update if started and not finished!
            buttons = mouseExit.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [exitButton]:
                        if obj.contains(mouseExit):
                            gotValidClick = True
                            mouseExit.clicked_name.append(obj.name)
                    x, y = mouseExit.getPos()
                    mouseExit.x.append(x)
                    mouseExit.y.append(y)
                    buttons = mouseExit.getPressed()
                    mouseExit.leftButton.append(buttons[0])
                    mouseExit.midButton.append(buttons[1])
                    mouseExit.rightButton.append(buttons[2])
                    mouseExit.time.append(mouseExit.mouseClock.getTime())
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        # *mouse1* updates
        if mouse1.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse1.frameNStart = frameN  # exact frame index
            mouse1.tStart = t  # local t and not account for scr refresh
            mouse1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse1, 'tStartRefresh')  # time at next scr refresh
            mouse1.status = STARTED
            mouse1.mouseClock.reset()
            prevButtonState = mouse1.getPressed()  # if button is down already this ISN'T a new click
        if mouse1.status == STARTED:  # only update if started and not finished!
            buttons = mouse1.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [Fbutton, Pbutton, Qbutton, Jbutton, Hbutton, Kbutton, Tbutton, Sbutton, Nbutton, Rbutton, Ybutton, Lbutton]:
                        if obj.contains(mouse1):
                            gotValidClick = True
                            mouse1.clicked_name.append(obj.name)
                    x, y = mouse1.getPos()
                    mouse1.x.append(x)
                    mouse1.y.append(y)
                    buttons = mouse1.getPressed()
                    mouse1.leftButton.append(buttons[0])
                    mouse1.midButton.append(buttons[1])
                    mouse1.rightButton.append(buttons[2])
                    mouse1.time.append(mouse1.mouseClock.getTime())
        
        # *blankButton* updates
        if blankButton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blankButton.frameNStart = frameN  # exact frame index
            blankButton.tStart = t  # local t and not account for scr refresh
            blankButton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blankButton, 'tStartRefresh')  # time at next scr refresh
            blankButton.setAutoDraw(True)
        
        # *gatherResponseText* updates
        if gatherResponseText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            gatherResponseText.frameNStart = frameN  # exact frame index
            gatherResponseText.tStart = t  # local t and not account for scr refresh
            gatherResponseText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(gatherResponseText, 'tStartRefresh')  # time at next scr refresh
            gatherResponseText.setAutoDraw(True)
        
        # *Fbutton* updates
        if Fbutton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fbutton.frameNStart = frameN  # exact frame index
            Fbutton.tStart = t  # local t and not account for scr refresh
            Fbutton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fbutton, 'tStartRefresh')  # time at next scr refresh
            Fbutton.setAutoDraw(True)
        
        # *F_text* updates
        if F_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            F_text.frameNStart = frameN  # exact frame index
            F_text.tStart = t  # local t and not account for scr refresh
            F_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(F_text, 'tStartRefresh')  # time at next scr refresh
            F_text.setAutoDraw(True)
        
        # *Pbutton* updates
        if Pbutton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pbutton.frameNStart = frameN  # exact frame index
            Pbutton.tStart = t  # local t and not account for scr refresh
            Pbutton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pbutton, 'tStartRefresh')  # time at next scr refresh
            Pbutton.setAutoDraw(True)
        
        # *Qbutton* updates
        if Qbutton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Qbutton.frameNStart = frameN  # exact frame index
            Qbutton.tStart = t  # local t and not account for scr refresh
            Qbutton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Qbutton, 'tStartRefresh')  # time at next scr refresh
            Qbutton.setAutoDraw(True)
        
        # *Jbutton* updates
        if Jbutton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Jbutton.frameNStart = frameN  # exact frame index
            Jbutton.tStart = t  # local t and not account for scr refresh
            Jbutton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Jbutton, 'tStartRefresh')  # time at next scr refresh
            Jbutton.setAutoDraw(True)
        
        # *Hbutton* updates
        if Hbutton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Hbutton.frameNStart = frameN  # exact frame index
            Hbutton.tStart = t  # local t and not account for scr refresh
            Hbutton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Hbutton, 'tStartRefresh')  # time at next scr refresh
            Hbutton.setAutoDraw(True)
        
        # *Kbutton* updates
        if Kbutton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Kbutton.frameNStart = frameN  # exact frame index
            Kbutton.tStart = t  # local t and not account for scr refresh
            Kbutton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Kbutton, 'tStartRefresh')  # time at next scr refresh
            Kbutton.setAutoDraw(True)
        
        # *Tbutton* updates
        if Tbutton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Tbutton.frameNStart = frameN  # exact frame index
            Tbutton.tStart = t  # local t and not account for scr refresh
            Tbutton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Tbutton, 'tStartRefresh')  # time at next scr refresh
            Tbutton.setAutoDraw(True)
        
        # *Sbutton* updates
        if Sbutton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Sbutton.frameNStart = frameN  # exact frame index
            Sbutton.tStart = t  # local t and not account for scr refresh
            Sbutton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Sbutton, 'tStartRefresh')  # time at next scr refresh
            Sbutton.setAutoDraw(True)
        
        # *Nbutton* updates
        if Nbutton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Nbutton.frameNStart = frameN  # exact frame index
            Nbutton.tStart = t  # local t and not account for scr refresh
            Nbutton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Nbutton, 'tStartRefresh')  # time at next scr refresh
            Nbutton.setAutoDraw(True)
        
        # *Rbutton* updates
        if Rbutton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Rbutton.frameNStart = frameN  # exact frame index
            Rbutton.tStart = t  # local t and not account for scr refresh
            Rbutton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Rbutton, 'tStartRefresh')  # time at next scr refresh
            Rbutton.setAutoDraw(True)
        
        # *Ybutton* updates
        if Ybutton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Ybutton.frameNStart = frameN  # exact frame index
            Ybutton.tStart = t  # local t and not account for scr refresh
            Ybutton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Ybutton, 'tStartRefresh')  # time at next scr refresh
            Ybutton.setAutoDraw(True)
        
        # *Lbutton* updates
        if Lbutton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Lbutton.frameNStart = frameN  # exact frame index
            Lbutton.tStart = t  # local t and not account for scr refresh
            Lbutton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Lbutton, 'tStartRefresh')  # time at next scr refresh
            Lbutton.setAutoDraw(True)
        
        # *clearButton* updates
        if clearButton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            clearButton.frameNStart = frameN  # exact frame index
            clearButton.tStart = t  # local t and not account for scr refresh
            clearButton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clearButton, 'tStartRefresh')  # time at next scr refresh
            clearButton.setAutoDraw(True)
        
        # *exitButton* updates
        if exitButton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            exitButton.frameNStart = frameN  # exact frame index
            exitButton.tStart = t  # local t and not account for scr refresh
            exitButton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(exitButton, 'tStartRefresh')  # time at next scr refresh
            exitButton.setAutoDraw(True)
        
        # *exitText* updates
        if exitText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            exitText.frameNStart = frameN  # exact frame index
            exitText.tStart = t  # local t and not account for scr refresh
            exitText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(exitText, 'tStartRefresh')  # time at next scr refresh
            exitText.setAutoDraw(True)
        
        # *clearText* updates
        if clearText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            clearText.frameNStart = frameN  # exact frame index
            clearText.tStart = t  # local t and not account for scr refresh
            clearText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clearText, 'tStartRefresh')  # time at next scr refresh
            clearText.setAutoDraw(True)
        
        # *P_text* updates
        if P_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P_text.frameNStart = frameN  # exact frame index
            P_text.tStart = t  # local t and not account for scr refresh
            P_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P_text, 'tStartRefresh')  # time at next scr refresh
            P_text.setAutoDraw(True)
        
        # *Q_text* updates
        if Q_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q_text.frameNStart = frameN  # exact frame index
            Q_text.tStart = t  # local t and not account for scr refresh
            Q_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q_text, 'tStartRefresh')  # time at next scr refresh
            Q_text.setAutoDraw(True)
        
        # *J_text* updates
        if J_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            J_text.frameNStart = frameN  # exact frame index
            J_text.tStart = t  # local t and not account for scr refresh
            J_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(J_text, 'tStartRefresh')  # time at next scr refresh
            J_text.setAutoDraw(True)
        
        # *H_text* updates
        if H_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            H_text.frameNStart = frameN  # exact frame index
            H_text.tStart = t  # local t and not account for scr refresh
            H_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(H_text, 'tStartRefresh')  # time at next scr refresh
            H_text.setAutoDraw(True)
        
        # *K_text* updates
        if K_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            K_text.frameNStart = frameN  # exact frame index
            K_text.tStart = t  # local t and not account for scr refresh
            K_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(K_text, 'tStartRefresh')  # time at next scr refresh
            K_text.setAutoDraw(True)
        
        # *T_text* updates
        if T_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T_text.frameNStart = frameN  # exact frame index
            T_text.tStart = t  # local t and not account for scr refresh
            T_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T_text, 'tStartRefresh')  # time at next scr refresh
            T_text.setAutoDraw(True)
        
        # *S_text* updates
        if S_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            S_text.frameNStart = frameN  # exact frame index
            S_text.tStart = t  # local t and not account for scr refresh
            S_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(S_text, 'tStartRefresh')  # time at next scr refresh
            S_text.setAutoDraw(True)
        
        # *N_text* updates
        if N_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            N_text.frameNStart = frameN  # exact frame index
            N_text.tStart = t  # local t and not account for scr refresh
            N_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(N_text, 'tStartRefresh')  # time at next scr refresh
            N_text.setAutoDraw(True)
        
        # *R_text* updates
        if R_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            R_text.frameNStart = frameN  # exact frame index
            R_text.tStart = t  # local t and not account for scr refresh
            R_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(R_text, 'tStartRefresh')  # time at next scr refresh
            R_text.setAutoDraw(True)
        
        # *Y_text* updates
        if Y_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Y_text.frameNStart = frameN  # exact frame index
            Y_text.tStart = t  # local t and not account for scr refresh
            Y_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Y_text, 'tStartRefresh')  # time at next scr refresh
            Y_text.setAutoDraw(True)
        
        # *L_text* updates
        if L_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            L_text.frameNStart = frameN  # exact frame index
            L_text.tStart = t  # local t and not account for scr refresh
            L_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(L_text, 'tStartRefresh')  # time at next scr refresh
            L_text.setAutoDraw(True)
        
        # *blankText* updates
        if blankText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blankText.frameNStart = frameN  # exact frame index
            blankText.tStart = t  # local t and not account for scr refresh
            blankText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blankText, 'tStartRefresh')  # time at next scr refresh
            blankText.setAutoDraw(True)
        
        # *answer1* updates
        if answer1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            answer1.frameNStart = frameN  # exact frame index
            answer1.tStart = t  # local t and not account for scr refresh
            answer1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(answer1, 'tStartRefresh')  # time at next scr refresh
            answer1.setAutoDraw(True)
        
        # *answer2* updates
        if answer2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            answer2.frameNStart = frameN  # exact frame index
            answer2.tStart = t  # local t and not account for scr refresh
            answer2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(answer2, 'tStartRefresh')  # time at next scr refresh
            answer2.setAutoDraw(True)
        # *mouseBlank* updates
        if mouseBlank.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouseBlank.frameNStart = frameN  # exact frame index
            mouseBlank.tStart = t  # local t and not account for scr refresh
            mouseBlank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouseBlank, 'tStartRefresh')  # time at next scr refresh
            mouseBlank.status = STARTED
            mouseBlank.mouseClock.reset()
            prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
        if mouseBlank.status == STARTED:  # only update if started and not finished!
            buttons = mouseBlank.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [blankButton]:
                        if obj.contains(mouseBlank):
                            gotValidClick = True
                            mouseBlank.clicked_name.append(obj.name)
                    # abort routine on response
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceRecallComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practiceRecall"-------
    for thisComponent in practiceRecallComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for practiceLoop (TrialHandler)
    x, y = mouseClear.getPos()
    buttons = mouseClear.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        for obj in [clearButton]:
            if obj.contains(mouseClear):
                gotValidClick = True
                mouseClear.clicked_name.append(obj.name)
    practiceLoop.addData('mouseClear.x', x)
    practiceLoop.addData('mouseClear.y', y)
    practiceLoop.addData('mouseClear.leftButton', buttons[0])
    practiceLoop.addData('mouseClear.midButton', buttons[1])
    practiceLoop.addData('mouseClear.rightButton', buttons[2])
    if len(mouseClear.clicked_name):
        practiceLoop.addData('mouseClear.clicked_name', mouseClear.clicked_name[0])
    practiceLoop.addData('mouseClear.started', mouseClear.tStart)
    practiceLoop.addData('mouseClear.stopped', mouseClear.tStop)
    #Correct Point System
    correctLettersTrial = 0
    if practiceLoop.finished == True:
        for answer in clicked:
            if clicked[0] is firstLetter and clicked[1] is secondLetter:
                correctLettersTrial +=1
                trial.addData('correctLettersTrial', correctLettersTrial)
                trial.addData('routineTime', timer.getTime())
    else:
            for answer in clicked:
                if clicked[0] is firstLetter and clicked[1] is secondLetter:
                    correctLettersPractice +=1
                trial.addData('correctLettersPractice', correctLettersPractice)
                trial.addData('routineTime', timer.getTime())
    # store data for practiceLoop (TrialHandler)
    if len(mouseExit.x): practiceLoop.addData('mouseExit.x', mouseExit.x[0])
    if len(mouseExit.y): practiceLoop.addData('mouseExit.y', mouseExit.y[0])
    if len(mouseExit.leftButton): practiceLoop.addData('mouseExit.leftButton', mouseExit.leftButton[0])
    if len(mouseExit.midButton): practiceLoop.addData('mouseExit.midButton', mouseExit.midButton[0])
    if len(mouseExit.rightButton): practiceLoop.addData('mouseExit.rightButton', mouseExit.rightButton[0])
    if len(mouseExit.time): practiceLoop.addData('mouseExit.time', mouseExit.time[0])
    if len(mouseExit.clicked_name): practiceLoop.addData('mouseExit.clicked_name', mouseExit.clicked_name[0])
    practiceLoop.addData('mouseExit.started', mouseExit.tStart)
    practiceLoop.addData('mouseExit.stopped', mouseExit.tStop)
    # store data for practiceLoop (TrialHandler)
    practiceLoop.addData('mouse1.x', mouse1.x)
    practiceLoop.addData('mouse1.y', mouse1.y)
    practiceLoop.addData('mouse1.leftButton', mouse1.leftButton)
    practiceLoop.addData('mouse1.midButton', mouse1.midButton)
    practiceLoop.addData('mouse1.rightButton', mouse1.rightButton)
    practiceLoop.addData('mouse1.time', mouse1.time)
    practiceLoop.addData('mouse1.clicked_name', mouse1.clicked_name)
    practiceLoop.addData('mouse1.started', mouse1.tStart)
    practiceLoop.addData('mouse1.stopped', mouse1.tStop)
    practiceLoop.addData('blankButton.started', blankButton.tStartRefresh)
    practiceLoop.addData('blankButton.stopped', blankButton.tStopRefresh)
    practiceLoop.addData('gatherResponseText.started', gatherResponseText.tStartRefresh)
    practiceLoop.addData('gatherResponseText.stopped', gatherResponseText.tStopRefresh)
    practiceLoop.addData('Fbutton.started', Fbutton.tStartRefresh)
    practiceLoop.addData('Fbutton.stopped', Fbutton.tStopRefresh)
    practiceLoop.addData('F_text.started', F_text.tStartRefresh)
    practiceLoop.addData('F_text.stopped', F_text.tStopRefresh)
    practiceLoop.addData('Pbutton.started', Pbutton.tStartRefresh)
    practiceLoop.addData('Pbutton.stopped', Pbutton.tStopRefresh)
    practiceLoop.addData('Qbutton.started', Qbutton.tStartRefresh)
    practiceLoop.addData('Qbutton.stopped', Qbutton.tStopRefresh)
    practiceLoop.addData('Jbutton.started', Jbutton.tStartRefresh)
    practiceLoop.addData('Jbutton.stopped', Jbutton.tStopRefresh)
    practiceLoop.addData('Hbutton.started', Hbutton.tStartRefresh)
    practiceLoop.addData('Hbutton.stopped', Hbutton.tStopRefresh)
    practiceLoop.addData('Kbutton.started', Kbutton.tStartRefresh)
    practiceLoop.addData('Kbutton.stopped', Kbutton.tStopRefresh)
    practiceLoop.addData('Tbutton.started', Tbutton.tStartRefresh)
    practiceLoop.addData('Tbutton.stopped', Tbutton.tStopRefresh)
    practiceLoop.addData('Sbutton.started', Sbutton.tStartRefresh)
    practiceLoop.addData('Sbutton.stopped', Sbutton.tStopRefresh)
    practiceLoop.addData('Nbutton.started', Nbutton.tStartRefresh)
    practiceLoop.addData('Nbutton.stopped', Nbutton.tStopRefresh)
    practiceLoop.addData('Rbutton.started', Rbutton.tStartRefresh)
    practiceLoop.addData('Rbutton.stopped', Rbutton.tStopRefresh)
    practiceLoop.addData('Ybutton.started', Ybutton.tStartRefresh)
    practiceLoop.addData('Ybutton.stopped', Ybutton.tStopRefresh)
    practiceLoop.addData('Lbutton.started', Lbutton.tStartRefresh)
    practiceLoop.addData('Lbutton.stopped', Lbutton.tStopRefresh)
    practiceLoop.addData('clearButton.started', clearButton.tStartRefresh)
    practiceLoop.addData('clearButton.stopped', clearButton.tStopRefresh)
    practiceLoop.addData('exitButton.started', exitButton.tStartRefresh)
    practiceLoop.addData('exitButton.stopped', exitButton.tStopRefresh)
    practiceLoop.addData('exitText.started', exitText.tStartRefresh)
    practiceLoop.addData('exitText.stopped', exitText.tStopRefresh)
    practiceLoop.addData('clearText.started', clearText.tStartRefresh)
    practiceLoop.addData('clearText.stopped', clearText.tStopRefresh)
    practiceLoop.addData('P_text.started', P_text.tStartRefresh)
    practiceLoop.addData('P_text.stopped', P_text.tStopRefresh)
    practiceLoop.addData('Q_text.started', Q_text.tStartRefresh)
    practiceLoop.addData('Q_text.stopped', Q_text.tStopRefresh)
    practiceLoop.addData('J_text.started', J_text.tStartRefresh)
    practiceLoop.addData('J_text.stopped', J_text.tStopRefresh)
    practiceLoop.addData('H_text.started', H_text.tStartRefresh)
    practiceLoop.addData('H_text.stopped', H_text.tStopRefresh)
    practiceLoop.addData('K_text.started', K_text.tStartRefresh)
    practiceLoop.addData('K_text.stopped', K_text.tStopRefresh)
    practiceLoop.addData('T_text.started', T_text.tStartRefresh)
    practiceLoop.addData('T_text.stopped', T_text.tStopRefresh)
    practiceLoop.addData('S_text.started', S_text.tStartRefresh)
    practiceLoop.addData('S_text.stopped', S_text.tStopRefresh)
    practiceLoop.addData('N_text.started', N_text.tStartRefresh)
    practiceLoop.addData('N_text.stopped', N_text.tStopRefresh)
    practiceLoop.addData('R_text.started', R_text.tStartRefresh)
    practiceLoop.addData('R_text.stopped', R_text.tStopRefresh)
    practiceLoop.addData('Y_text.started', Y_text.tStartRefresh)
    practiceLoop.addData('Y_text.stopped', Y_text.tStopRefresh)
    practiceLoop.addData('L_text.started', L_text.tStartRefresh)
    practiceLoop.addData('L_text.stopped', L_text.tStopRefresh)
    practiceLoop.addData('blankText.started', blankText.tStartRefresh)
    practiceLoop.addData('blankText.stopped', blankText.tStopRefresh)
    practiceLoop.addData('answer1.started', answer1.tStartRefresh)
    practiceLoop.addData('answer1.stopped', answer1.tStopRefresh)
    practiceLoop.addData('answer2.started', answer2.tStartRefresh)
    practiceLoop.addData('answer2.stopped', answer2.tStopRefresh)
    # store data for practiceLoop (TrialHandler)
    x, y = mouseBlank.getPos()
    buttons = mouseBlank.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        for obj in [blankButton]:
            if obj.contains(mouseBlank):
                gotValidClick = True
                mouseBlank.clicked_name.append(obj.name)
    practiceLoop.addData('mouseBlank.x', x)
    practiceLoop.addData('mouseBlank.y', y)
    practiceLoop.addData('mouseBlank.leftButton', buttons[0])
    practiceLoop.addData('mouseBlank.midButton', buttons[1])
    practiceLoop.addData('mouseBlank.rightButton', buttons[2])
    if len(mouseBlank.clicked_name):
        practiceLoop.addData('mouseBlank.clicked_name', mouseBlank.clicked_name[0])
    practiceLoop.addData('mouseBlank.started', mouseBlank.tStart)
    practiceLoop.addData('mouseBlank.stopped', mouseBlank.tStop)
    # the Routine "practiceRecall" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'practiceLoop'


# ------Prepare to start Routine "PractSentInst1"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_5
gotValidClick = False  # until a click is received
# keep track of which components have finished
PractSentInst1Components = [instr_4, continue_5, mouse_5]
for thisComponent in PractSentInst1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PractSentInst1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "PractSentInst1"-------
while continueRoutine:
    # get current time
    t = PractSentInst1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PractSentInst1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_4* updates
    if instr_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_4.frameNStart = frameN  # exact frame index
        instr_4.tStart = t  # local t and not account for scr refresh
        instr_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_4, 'tStartRefresh')  # time at next scr refresh
        instr_4.setAutoDraw(True)
    
    # *continue_5* updates
    if continue_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        continue_5.frameNStart = frameN  # exact frame index
        continue_5.tStart = t  # local t and not account for scr refresh
        continue_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continue_5, 'tStartRefresh')  # time at next scr refresh
        continue_5.setAutoDraw(True)
    # *mouse_5* updates
    if mouse_5.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_5.frameNStart = frameN  # exact frame index
        mouse_5.tStart = t  # local t and not account for scr refresh
        mouse_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_5, 'tStartRefresh')  # time at next scr refresh
        mouse_5.status = STARTED
        mouse_5.mouseClock.reset()
        prevButtonState = mouse_5.getPressed()  # if button is down already this ISN'T a new click
    if mouse_5.status == STARTED:  # only update if started and not finished!
        buttons = mouse_5.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PractSentInst1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PractSentInst1"-------
for thisComponent in PractSentInst1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr_4.started', instr_4.tStartRefresh)
thisExp.addData('instr_4.stopped', instr_4.tStopRefresh)
thisExp.addData('continue_5.started', continue_5.tStartRefresh)
thisExp.addData('continue_5.stopped', continue_5.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_5.started', mouse_5.tStart)
thisExp.addData('mouse_5.stopped', mouse_5.tStop)
thisExp.nextEntry()
# the Routine "PractSentInst1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "PractSenInst2"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_6
gotValidClick = False  # until a click is received
# keep track of which components have finished
PractSenInst2Components = [instr_5, continue_6, mouse_6]
for thisComponent in PractSenInst2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PractSenInst2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "PractSenInst2"-------
while continueRoutine:
    # get current time
    t = PractSenInst2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PractSenInst2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_5* updates
    if instr_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_5.frameNStart = frameN  # exact frame index
        instr_5.tStart = t  # local t and not account for scr refresh
        instr_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_5, 'tStartRefresh')  # time at next scr refresh
        instr_5.setAutoDraw(True)
    
    # *continue_6* updates
    if continue_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        continue_6.frameNStart = frameN  # exact frame index
        continue_6.tStart = t  # local t and not account for scr refresh
        continue_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continue_6, 'tStartRefresh')  # time at next scr refresh
        continue_6.setAutoDraw(True)
    # *mouse_6* updates
    if mouse_6.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_6.frameNStart = frameN  # exact frame index
        mouse_6.tStart = t  # local t and not account for scr refresh
        mouse_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_6, 'tStartRefresh')  # time at next scr refresh
        mouse_6.status = STARTED
        mouse_6.mouseClock.reset()
        prevButtonState = mouse_6.getPressed()  # if button is down already this ISN'T a new click
    if mouse_6.status == STARTED:  # only update if started and not finished!
        buttons = mouse_6.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PractSenInst2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PractSenInst2"-------
for thisComponent in PractSenInst2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr_5.started', instr_5.tStartRefresh)
thisExp.addData('instr_5.stopped', instr_5.tStopRefresh)
thisExp.addData('continue_6.started', continue_6.tStartRefresh)
thisExp.addData('continue_6.stopped', continue_6.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_6.started', mouse_6.tStart)
thisExp.addData('mouse_6.stopped', mouse_6.tStop)
thisExp.nextEntry()
# the Routine "PractSenInst2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "PracSenInst3"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_7
gotValidClick = False  # until a click is received
mouse_7.mouseClock.reset()
# keep track of which components have finished
PracSenInst3Components = [instr_6, continue_7, mouse_7]
for thisComponent in PracSenInst3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PracSenInst3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "PracSenInst3"-------
while continueRoutine:
    # get current time
    t = PracSenInst3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PracSenInst3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_6* updates
    if instr_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_6.frameNStart = frameN  # exact frame index
        instr_6.tStart = t  # local t and not account for scr refresh
        instr_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_6, 'tStartRefresh')  # time at next scr refresh
        instr_6.setAutoDraw(True)
    
    # *continue_7* updates
    if continue_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        continue_7.frameNStart = frameN  # exact frame index
        continue_7.tStart = t  # local t and not account for scr refresh
        continue_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continue_7, 'tStartRefresh')  # time at next scr refresh
        continue_7.setAutoDraw(True)
    # *mouse_7* updates
    if mouse_7.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_7.frameNStart = frameN  # exact frame index
        mouse_7.tStart = t  # local t and not account for scr refresh
        mouse_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_7, 'tStartRefresh')  # time at next scr refresh
        mouse_7.status = STARTED
        prevButtonState = mouse_7.getPressed()  # if button is down already this ISN'T a new click
    if mouse_7.status == STARTED:  # only update if started and not finished!
        buttons = mouse_7.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PracSenInst3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PracSenInst3"-------
for thisComponent in PracSenInst3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr_6.started', instr_6.tStartRefresh)
thisExp.addData('instr_6.stopped', instr_6.tStopRefresh)
thisExp.addData('continue_7.started', continue_7.tStartRefresh)
thisExp.addData('continue_7.stopped', continue_7.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_7.started', mouse_7.tStart)
thisExp.addData('mouse_7.stopped', mouse_7.tStop)
thisExp.nextEntry()
# the Routine "PracSenInst3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practiceSentence = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('sentenceProblems.xlsx'),
    seed=None, name='practiceSentence')
thisExp.addLoop(practiceSentence)  # add the loop to the experiment
thisPracticeSentence = practiceSentence.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracticeSentence.rgb)
if thisPracticeSentence != None:
    for paramName in thisPracticeSentence:
        exec('{} = thisPracticeSentence[paramName]'.format(paramName))

for thisPracticeSentence in practiceSentence:
    currentLoop = practiceSentence
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeSentence.rgb)
    if thisPracticeSentence != None:
        for paramName in thisPracticeSentence:
            exec('{} = thisPracticeSentence[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "sentence"-------
    continueRoutine = True
    # update component parameters for each repeat
    sentenceText.setText(sentence)
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    gotValidClick = False  # until a click is received
    mouse.mouseClock.reset()
    countingClock = core.Clock()
    # keep track of which components have finished
    sentenceComponents = [sentenceText, continue_12, mouse, text_3]
    for thisComponent in sentenceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    sentenceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "sentence"-------
    while continueRoutine:
        # get current time
        t = sentenceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=sentenceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *sentenceText* updates
        if sentenceText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sentenceText.frameNStart = frameN  # exact frame index
            sentenceText.tStart = t  # local t and not account for scr refresh
            sentenceText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sentenceText, 'tStartRefresh')  # time at next scr refresh
            sentenceText.setAutoDraw(True)
        
        # *continue_12* updates
        if continue_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            continue_12.frameNStart = frameN  # exact frame index
            continue_12.tStart = t  # local t and not account for scr refresh
            continue_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(continue_12, 'tStartRefresh')  # time at next scr refresh
            continue_12.setAutoDraw(True)
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            mouse.status = STARTED
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    x, y = mouse.getPos()
                    mouse.x.append(x)
                    mouse.y.append(y)
                    buttons = mouse.getPressed()
                    mouse.leftButton.append(buttons[0])
                    mouse.midButton.append(buttons[1])
                    mouse.rightButton.append(buttons[2])
                    mouse.time.append(mouse.mouseClock.getTime())
                    # abort routine on response
                    continueRoutine = False
        #Establishing and Displaying Timer
        timeRemaining = countingClock.getTime()
        
        minutes = int (timeRemaining/60.0)
        tenSeconds= int((timeRemaining - (minutes*60))/10.0)
        oneSeconds = int (timeRemaining - (minutes*60 + tenSeconds*10))
        timeText = str(minutes) + ':'  + str(tenSeconds) + str(oneSeconds)
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:  # only update if drawing
            text_3.setText('', log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sentenceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "sentence"-------
    for thisComponent in sentenceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practiceSentence.addData('sentenceText.started', sentenceText.tStartRefresh)
    practiceSentence.addData('sentenceText.stopped', sentenceText.tStopRefresh)
    practiceSentence.addData('continue_12.started', continue_12.tStartRefresh)
    practiceSentence.addData('continue_12.stopped', continue_12.tStopRefresh)
    # store data for practiceSentence (TrialHandler)
    if len(mouse.x): practiceSentence.addData('mouse.x', mouse.x[0])
    if len(mouse.y): practiceSentence.addData('mouse.y', mouse.y[0])
    if len(mouse.leftButton): practiceSentence.addData('mouse.leftButton', mouse.leftButton[0])
    if len(mouse.midButton): practiceSentence.addData('mouse.midButton', mouse.midButton[0])
    if len(mouse.rightButton): practiceSentence.addData('mouse.rightButton', mouse.rightButton[0])
    if len(mouse.time): practiceSentence.addData('mouse.time', mouse.time[0])
    practiceSentence.addData('mouse.started', mouse.tStart)
    practiceSentence.addData('mouse.stopped', mouse.tStop)
    
    totalTime+=countingClock.getTime()
    avgTime = totalTime/15 #number repetitions
    practiceSentence.addData('text_3.started', text_3.tStartRefresh)
    practiceSentence.addData('text_3.stopped', text_3.tStopRefresh)
    # the Routine "sentence" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "sentenceResponse"-------
    continueRoutine = True
    # update component parameters for each repeat
    clicked =0
    
    correctText = ""
    trueButton.fillColor = "white"
    falseButton.fillColor = "white"
    
    timerC = core.Clock()
    timerC.reset()
    
    trueButton.setFillColor('white')
    falseButton.setFillColor('white')
    # setup some python lists for storing info about the mouse12
    mouse12.x = []
    mouse12.y = []
    mouse12.leftButton = []
    mouse12.midButton = []
    mouse12.rightButton = []
    mouse12.time = []
    mouse12.clicked_name = []
    gotValidClick = False  # until a click is received
    mouse12.mouseClock.reset()
    # keep track of which components have finished
    sentenceResponseComponents = [senseText, trueButton, trueText, falseButton, falseText, mouse12]
    for thisComponent in sentenceResponseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    sentenceResponseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "sentenceResponse"-------
    while continueRoutine:
        # get current time
        t = sentenceResponseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=sentenceResponseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        if mouse12.isPressedIn(trueButton) and CorrectResp == 'correct' and clicked == 0:
            trueButton.fillColor = "green"
            correct=1
            totalCorrectPractice +=1
            clicked=1
        elif mouse12.isPressedIn(falseButton) and CorrectResp == 'incorrect' and clicked ==0:
            trueButton.fillColor = "green"
            correct=1
            totalCorrectPractice +=1
            clicked  = 1
            countdownStarted = True
        elif mouse12.isPressedIn(trueButton) and CorrectResp ==  'incorrect' and clicked==0:
            trueButton.fillColor = "green"
            clicked = 1
            totalCorrectPractice +=0
            correct = 0
        elif mouse12.isPressedIn(falseButton) and CorrectResp ==  'correct' and clicked ==0:
            trueButton.fillColor = "green"
            clicked = 1
            totalCorrectPractice +=0
            correct = 0
        else:
            correctText = ""
            trueButton.fillColor = "white"
            falseButton.fillColor = "white"
            clicked = 0
            correct = 0
        
        # *senseText* updates
        if senseText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            senseText.frameNStart = frameN  # exact frame index
            senseText.tStart = t  # local t and not account for scr refresh
            senseText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(senseText, 'tStartRefresh')  # time at next scr refresh
            senseText.setAutoDraw(True)
        
        # *trueButton* updates
        if trueButton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trueButton.frameNStart = frameN  # exact frame index
            trueButton.tStart = t  # local t and not account for scr refresh
            trueButton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trueButton, 'tStartRefresh')  # time at next scr refresh
            trueButton.setAutoDraw(True)
        
        # *trueText* updates
        if trueText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trueText.frameNStart = frameN  # exact frame index
            trueText.tStart = t  # local t and not account for scr refresh
            trueText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trueText, 'tStartRefresh')  # time at next scr refresh
            trueText.setAutoDraw(True)
        
        # *falseButton* updates
        if falseButton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            falseButton.frameNStart = frameN  # exact frame index
            falseButton.tStart = t  # local t and not account for scr refresh
            falseButton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(falseButton, 'tStartRefresh')  # time at next scr refresh
            falseButton.setAutoDraw(True)
        
        # *falseText* updates
        if falseText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            falseText.frameNStart = frameN  # exact frame index
            falseText.tStart = t  # local t and not account for scr refresh
            falseText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(falseText, 'tStartRefresh')  # time at next scr refresh
            falseText.setAutoDraw(True)
        # *mouse12* updates
        if mouse12.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse12.frameNStart = frameN  # exact frame index
            mouse12.tStart = t  # local t and not account for scr refresh
            mouse12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse12, 'tStartRefresh')  # time at next scr refresh
            mouse12.status = STARTED
            prevButtonState = mouse12.getPressed()  # if button is down already this ISN'T a new click
        if mouse12.status == STARTED:  # only update if started and not finished!
            buttons = mouse12.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [trueButton, falseButton]:
                        if obj.contains(mouse12):
                            gotValidClick = True
                            mouse12.clicked_name.append(obj.name)
                    x, y = mouse12.getPos()
                    mouse12.x.append(x)
                    mouse12.y.append(y)
                    buttons = mouse12.getPressed()
                    mouse12.leftButton.append(buttons[0])
                    mouse12.midButton.append(buttons[1])
                    mouse12.rightButton.append(buttons[2])
                    mouse12.time.append(mouse12.mouseClock.getTime())
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sentenceResponseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "sentenceResponse"-------
    for thisComponent in sentenceResponseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practiceLoop.addData('routineTime', timerC.getTime())
    
    if (correct ==1):
        correctText= "Correct!"
    elif  (correct == 0):
        correctText  = "Incorrect"
    practiceSentence.addData('senseText.started', senseText.tStartRefresh)
    practiceSentence.addData('senseText.stopped', senseText.tStopRefresh)
    practiceSentence.addData('trueButton.started', trueButton.tStartRefresh)
    practiceSentence.addData('trueButton.stopped', trueButton.tStopRefresh)
    practiceSentence.addData('trueText.started', trueText.tStartRefresh)
    practiceSentence.addData('trueText.stopped', trueText.tStopRefresh)
    practiceSentence.addData('falseButton.started', falseButton.tStartRefresh)
    practiceSentence.addData('falseButton.stopped', falseButton.tStopRefresh)
    practiceSentence.addData('falseText.started', falseText.tStartRefresh)
    practiceSentence.addData('falseText.stopped', falseText.tStopRefresh)
    # store data for practiceSentence (TrialHandler)
    if len(mouse12.x): practiceSentence.addData('mouse12.x', mouse12.x[0])
    if len(mouse12.y): practiceSentence.addData('mouse12.y', mouse12.y[0])
    if len(mouse12.leftButton): practiceSentence.addData('mouse12.leftButton', mouse12.leftButton[0])
    if len(mouse12.midButton): practiceSentence.addData('mouse12.midButton', mouse12.midButton[0])
    if len(mouse12.rightButton): practiceSentence.addData('mouse12.rightButton', mouse12.rightButton[0])
    if len(mouse12.time): practiceSentence.addData('mouse12.time', mouse12.time[0])
    if len(mouse12.clicked_name): practiceSentence.addData('mouse12.clicked_name', mouse12.clicked_name[0])
    practiceSentence.addData('mouse12.started', mouse12.tStart)
    practiceSentence.addData('mouse12.stopped', mouse12.tStop)
    # the Routine "sentenceResponse" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    sentenceFeedback2.setText(correctText)
    # keep track of which components have finished
    feedbackComponents = [sentenceFeedback2]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *sentenceFeedback2* updates
        if sentenceFeedback2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sentenceFeedback2.frameNStart = frameN  # exact frame index
            sentenceFeedback2.tStart = t  # local t and not account for scr refresh
            sentenceFeedback2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sentenceFeedback2, 'tStartRefresh')  # time at next scr refresh
            sentenceFeedback2.setAutoDraw(True)
        if sentenceFeedback2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sentenceFeedback2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sentenceFeedback2.tStop = t  # not accounting for scr refresh
                sentenceFeedback2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sentenceFeedback2, 'tStopRefresh')  # time at next scr refresh
                sentenceFeedback2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practiceSentence.addData('sentenceFeedback2.started', sentenceFeedback2.tStartRefresh)
    practiceSentence.addData('sentenceFeedback2.stopped', sentenceFeedback2.tStopRefresh)
    if (correct ==1):
        sentenceFeedback2.setText("Correct!")
    elif  (correct == 0):
        sentenceFeedback2.setText("Incorrect")
    
    practiceSentence.addData('correctSentence', correct)
    practiceSentence.addData('totalCorrectSentence', totalCorrectPractice)
    thisExp.nextEntry()
    
# completed 1 repeats of 'practiceSentence'


# ------Prepare to start Routine "RSPANpracticeInstruct1_2"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_8
gotValidClick = False  # until a click is received
# keep track of which components have finished
RSPANpracticeInstruct1_2Components = [instr_7, continue_8, mouse_8]
for thisComponent in RSPANpracticeInstruct1_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
RSPANpracticeInstruct1_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "RSPANpracticeInstruct1_2"-------
while continueRoutine:
    # get current time
    t = RSPANpracticeInstruct1_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=RSPANpracticeInstruct1_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_7* updates
    if instr_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_7.frameNStart = frameN  # exact frame index
        instr_7.tStart = t  # local t and not account for scr refresh
        instr_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_7, 'tStartRefresh')  # time at next scr refresh
        instr_7.setAutoDraw(True)
    
    # *continue_8* updates
    if continue_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        continue_8.frameNStart = frameN  # exact frame index
        continue_8.tStart = t  # local t and not account for scr refresh
        continue_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continue_8, 'tStartRefresh')  # time at next scr refresh
        continue_8.setAutoDraw(True)
    # *mouse_8* updates
    if mouse_8.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_8.frameNStart = frameN  # exact frame index
        mouse_8.tStart = t  # local t and not account for scr refresh
        mouse_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_8, 'tStartRefresh')  # time at next scr refresh
        mouse_8.status = STARTED
        mouse_8.mouseClock.reset()
        prevButtonState = mouse_8.getPressed()  # if button is down already this ISN'T a new click
    if mouse_8.status == STARTED:  # only update if started and not finished!
        buttons = mouse_8.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RSPANpracticeInstruct1_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "RSPANpracticeInstruct1_2"-------
for thisComponent in RSPANpracticeInstruct1_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr_7.started', instr_7.tStartRefresh)
thisExp.addData('instr_7.stopped', instr_7.tStopRefresh)
thisExp.addData('continue_8.started', continue_8.tStartRefresh)
thisExp.addData('continue_8.stopped', continue_8.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_8.started', mouse_8.tStart)
thisExp.addData('mouse_8.stopped', mouse_8.tStop)
thisExp.nextEntry()
# the Routine "RSPANpracticeInstruct1_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "RSPANpracticeInstruct2"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_9
gotValidClick = False  # until a click is received
# keep track of which components have finished
RSPANpracticeInstruct2Components = [instr_8, continue_9, mouse_9]
for thisComponent in RSPANpracticeInstruct2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
RSPANpracticeInstruct2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "RSPANpracticeInstruct2"-------
while continueRoutine:
    # get current time
    t = RSPANpracticeInstruct2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=RSPANpracticeInstruct2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_8* updates
    if instr_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_8.frameNStart = frameN  # exact frame index
        instr_8.tStart = t  # local t and not account for scr refresh
        instr_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_8, 'tStartRefresh')  # time at next scr refresh
        instr_8.setAutoDraw(True)
    
    # *continue_9* updates
    if continue_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        continue_9.frameNStart = frameN  # exact frame index
        continue_9.tStart = t  # local t and not account for scr refresh
        continue_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continue_9, 'tStartRefresh')  # time at next scr refresh
        continue_9.setAutoDraw(True)
    # *mouse_9* updates
    if mouse_9.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_9.frameNStart = frameN  # exact frame index
        mouse_9.tStart = t  # local t and not account for scr refresh
        mouse_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_9, 'tStartRefresh')  # time at next scr refresh
        mouse_9.status = STARTED
        mouse_9.mouseClock.reset()
        prevButtonState = mouse_9.getPressed()  # if button is down already this ISN'T a new click
    if mouse_9.status == STARTED:  # only update if started and not finished!
        buttons = mouse_9.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RSPANpracticeInstruct2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "RSPANpracticeInstruct2"-------
for thisComponent in RSPANpracticeInstruct2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr_8.started', instr_8.tStartRefresh)
thisExp.addData('instr_8.stopped', instr_8.tStopRefresh)
thisExp.addData('continue_9.started', continue_9.tStartRefresh)
thisExp.addData('continue_9.stopped', continue_9.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_9.started', mouse_9.tStart)
thisExp.addData('mouse_9.stopped', mouse_9.tStop)
thisExp.nextEntry()
# the Routine "RSPANpracticeInstruct2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "feedbackinstruct"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_10
gotValidClick = False  # until a click is received
# keep track of which components have finished
feedbackinstructComponents = [instr_9, continue_10, mouse_10]
for thisComponent in feedbackinstructComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
feedbackinstructClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "feedbackinstruct"-------
while continueRoutine:
    # get current time
    t = feedbackinstructClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=feedbackinstructClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_9* updates
    if instr_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_9.frameNStart = frameN  # exact frame index
        instr_9.tStart = t  # local t and not account for scr refresh
        instr_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_9, 'tStartRefresh')  # time at next scr refresh
        instr_9.setAutoDraw(True)
    
    # *continue_10* updates
    if continue_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        continue_10.frameNStart = frameN  # exact frame index
        continue_10.tStart = t  # local t and not account for scr refresh
        continue_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continue_10, 'tStartRefresh')  # time at next scr refresh
        continue_10.setAutoDraw(True)
    # *mouse_10* updates
    if mouse_10.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_10.frameNStart = frameN  # exact frame index
        mouse_10.tStart = t  # local t and not account for scr refresh
        mouse_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_10, 'tStartRefresh')  # time at next scr refresh
        mouse_10.status = STARTED
        mouse_10.mouseClock.reset()
        prevButtonState = mouse_10.getPressed()  # if button is down already this ISN'T a new click
    if mouse_10.status == STARTED:  # only update if started and not finished!
        buttons = mouse_10.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in feedbackinstructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "feedbackinstruct"-------
for thisComponent in feedbackinstructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr_9.started', instr_9.tStartRefresh)
thisExp.addData('instr_9.stopped', instr_9.tStopRefresh)
thisExp.addData('continue_10.started', continue_10.tStartRefresh)
thisExp.addData('continue_10.stopped', continue_10.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_10.started', mouse_10.tStart)
thisExp.addData('mouse_10.stopped', mouse_10.tStop)
thisExp.nextEntry()
# the Routine "feedbackinstruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "feedbackinstruct2"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_11
gotValidClick = False  # until a click is received
# keep track of which components have finished
feedbackinstruct2Components = [instr_10, continue_11, mouse_11]
for thisComponent in feedbackinstruct2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
feedbackinstruct2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "feedbackinstruct2"-------
while continueRoutine:
    # get current time
    t = feedbackinstruct2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=feedbackinstruct2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_10* updates
    if instr_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_10.frameNStart = frameN  # exact frame index
        instr_10.tStart = t  # local t and not account for scr refresh
        instr_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_10, 'tStartRefresh')  # time at next scr refresh
        instr_10.setAutoDraw(True)
    
    # *continue_11* updates
    if continue_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        continue_11.frameNStart = frameN  # exact frame index
        continue_11.tStart = t  # local t and not account for scr refresh
        continue_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continue_11, 'tStartRefresh')  # time at next scr refresh
        continue_11.setAutoDraw(True)
    # *mouse_11* updates
    if mouse_11.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_11.frameNStart = frameN  # exact frame index
        mouse_11.tStart = t  # local t and not account for scr refresh
        mouse_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_11, 'tStartRefresh')  # time at next scr refresh
        mouse_11.status = STARTED
        mouse_11.mouseClock.reset()
        prevButtonState = mouse_11.getPressed()  # if button is down already this ISN'T a new click
    if mouse_11.status == STARTED:  # only update if started and not finished!
        buttons = mouse_11.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in feedbackinstruct2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "feedbackinstruct2"-------
for thisComponent in feedbackinstruct2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr_10.started', instr_10.tStartRefresh)
thisExp.addData('instr_10.stopped', instr_10.tStopRefresh)
thisExp.addData('continue_11.started', continue_11.tStartRefresh)
thisExp.addData('continue_11.stopped', continue_11.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse_11.started', mouse_11.tStart)
thisExp.addData('mouse_11.stopped', mouse_11.tStop)
thisExp.nextEntry()
# the Routine "feedbackinstruct2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trial = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('SentenceProblems2.xlsx'),
    seed=None, name='trial')
thisExp.addLoop(trial)  # add the loop to the experiment
thisTrial = trial.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trial:
    currentLoop = trial
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    sentenceTrial = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='sentenceTrial')
    thisExp.addLoop(sentenceTrial)  # add the loop to the experiment
    thisSentenceTrial = sentenceTrial.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSentenceTrial.rgb)
    if thisSentenceTrial != None:
        for paramName in thisSentenceTrial:
            exec('{} = thisSentenceTrial[paramName]'.format(paramName))
    
    for thisSentenceTrial in sentenceTrial:
        currentLoop = sentenceTrial
        # abbreviate parameter names if possible (e.g. rgb = thisSentenceTrial.rgb)
        if thisSentenceTrial != None:
            for paramName in thisSentenceTrial:
                exec('{} = thisSentenceTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "sentence2"-------
        continueRoutine = True
        # update component parameters for each repeat
        sentenceText2.setText(sentence)
        # setup some python lists for storing info about the mouse_12
        gotValidClick = False  # until a click is received
        countdownClock = core.CountdownTimer(avgTime)
        # keep track of which components have finished
        sentence2Components = [sentenceText2, mouse_12, continue_13, text]
        for thisComponent in sentence2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        sentence2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "sentence2"-------
        while continueRoutine:
            # get current time
            t = sentence2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=sentence2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *sentenceText2* updates
            if sentenceText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sentenceText2.frameNStart = frameN  # exact frame index
                sentenceText2.tStart = t  # local t and not account for scr refresh
                sentenceText2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sentenceText2, 'tStartRefresh')  # time at next scr refresh
                sentenceText2.setAutoDraw(True)
            # *mouse_12* updates
            if mouse_12.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_12.frameNStart = frameN  # exact frame index
                mouse_12.tStart = t  # local t and not account for scr refresh
                mouse_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_12, 'tStartRefresh')  # time at next scr refresh
                mouse_12.status = STARTED
                mouse_12.mouseClock.reset()
                prevButtonState = mouse_12.getPressed()  # if button is down already this ISN'T a new click
            if mouse_12.status == STARTED:  # only update if started and not finished!
                buttons = mouse_12.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # abort routine on response
                        continueRoutine = False
            
            # *continue_13* updates
            if continue_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                continue_13.frameNStart = frameN  # exact frame index
                continue_13.tStart = t  # local t and not account for scr refresh
                continue_13.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(continue_13, 'tStartRefresh')  # time at next scr refresh
                continue_13.setAutoDraw(True)
            
            #Establishing and Displaying Timer
            timeRemaining = countdownClock.getTime()
            if timeRemaining <=0.0:
                continueRoutine = False
                sentenceTrial.finished = True
                continueExperiment = True
            else:
                minutes = int (timeRemaining/60.0)
                tenSeconds= int((timeRemaining - (minutes*60))/10.0)
                oneSeconds = int (timeRemaining - (minutes*60 + tenSeconds*10))
                timeText = str(minutes) + ':'  + str(tenSeconds) + str(oneSeconds)
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            if text.status == STARTED:  # only update if drawing
                text.setText(timeText, log=False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in sentence2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "sentence2"-------
        for thisComponent in sentence2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        sentenceTrial.addData('sentenceText2.started', sentenceText2.tStartRefresh)
        sentenceTrial.addData('sentenceText2.stopped', sentenceText2.tStopRefresh)
        # store data for sentenceTrial (TrialHandler)
        x, y = mouse_12.getPos()
        buttons = mouse_12.getPressed()
        sentenceTrial.addData('mouse_12.x', x)
        sentenceTrial.addData('mouse_12.y', y)
        sentenceTrial.addData('mouse_12.leftButton', buttons[0])
        sentenceTrial.addData('mouse_12.midButton', buttons[1])
        sentenceTrial.addData('mouse_12.rightButton', buttons[2])
        sentenceTrial.addData('mouse_12.started', mouse_12.tStart)
        sentenceTrial.addData('mouse_12.stopped', mouse_12.tStop)
        sentenceTrial.addData('continue_13.started', continue_13.tStartRefresh)
        sentenceTrial.addData('continue_13.stopped', continue_13.tStopRefresh)
        sentenceTrial.addData('text.started', text.tStartRefresh)
        sentenceTrial.addData('text.stopped', text.tStopRefresh)
        # the Routine "sentence2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "sentenceResponseTrial"-------
        continueRoutine = True
        # update component parameters for each repeat
        clicked =0
        
        correctText = ""
        trueButton.fillColor = "white"
        falseButton.fillColor = "white"
        
        timerC = core.Clock()
        timerC.reset()
        
        trueButton_2.setFillColor('white')
        falseButton_2.setFillColor('white')
        # setup some python lists for storing info about the mouse12_2
        mouse12_2.x = []
        mouse12_2.y = []
        mouse12_2.leftButton = []
        mouse12_2.midButton = []
        mouse12_2.rightButton = []
        mouse12_2.time = []
        mouse12_2.clicked_name = []
        gotValidClick = False  # until a click is received
        mouse12_2.mouseClock.reset()
        # keep track of which components have finished
        sentenceResponseTrialComponents = [senseText_2, trueButton_2, trueText_2, falseButton_2, falseText_2, mouse12_2]
        for thisComponent in sentenceResponseTrialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        sentenceResponseTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "sentenceResponseTrial"-------
        while continueRoutine:
            # get current time
            t = sentenceResponseTrialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=sentenceResponseTrialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            if mouse12.isPressedIn(trueButton) and CorrectResp == 'correct' and clicked == 0:
                trueButton.fillColor = "green"
                correct=1
                totalCorrectSentenceTrial +=1
                clicked=1
            elif mouse12.isPressedIn(falseButton) and CorrectResp == 'incorrect' and clicked ==0:
                trueButton.fillColor = "green"
                correct=1
                totalCorrectSentenceTrial +=1
                clicked  = 1
                countdownStarted = True
            elif mouse12.isPressedIn(trueButton) and CorrectResp ==  'incorrect' and clicked==0:
                trueButton.fillColor = "green"
                clicked = 1
                totalCorrectSentenceTrial +=0
                correct = 0
            elif mouse12.isPressedIn(falseButton) and CorrectResp ==  'correct' and clicked ==0:
                trueButton.fillColor = "green"
                clicked = 1
                totalCorrectSentenceTrial +=0
                correct = 0
            else:
                correctText = ""
                trueButton.fillColor = "white"
                falseButton.fillColor = "white"
                clicked = 0
                correct = 0
            
            # *senseText_2* updates
            if senseText_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                senseText_2.frameNStart = frameN  # exact frame index
                senseText_2.tStart = t  # local t and not account for scr refresh
                senseText_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(senseText_2, 'tStartRefresh')  # time at next scr refresh
                senseText_2.setAutoDraw(True)
            
            # *trueButton_2* updates
            if trueButton_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trueButton_2.frameNStart = frameN  # exact frame index
                trueButton_2.tStart = t  # local t and not account for scr refresh
                trueButton_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trueButton_2, 'tStartRefresh')  # time at next scr refresh
                trueButton_2.setAutoDraw(True)
            
            # *trueText_2* updates
            if trueText_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trueText_2.frameNStart = frameN  # exact frame index
                trueText_2.tStart = t  # local t and not account for scr refresh
                trueText_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trueText_2, 'tStartRefresh')  # time at next scr refresh
                trueText_2.setAutoDraw(True)
            
            # *falseButton_2* updates
            if falseButton_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                falseButton_2.frameNStart = frameN  # exact frame index
                falseButton_2.tStart = t  # local t and not account for scr refresh
                falseButton_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(falseButton_2, 'tStartRefresh')  # time at next scr refresh
                falseButton_2.setAutoDraw(True)
            
            # *falseText_2* updates
            if falseText_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                falseText_2.frameNStart = frameN  # exact frame index
                falseText_2.tStart = t  # local t and not account for scr refresh
                falseText_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(falseText_2, 'tStartRefresh')  # time at next scr refresh
                falseText_2.setAutoDraw(True)
            # *mouse12_2* updates
            if mouse12_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse12_2.frameNStart = frameN  # exact frame index
                mouse12_2.tStart = t  # local t and not account for scr refresh
                mouse12_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse12_2, 'tStartRefresh')  # time at next scr refresh
                mouse12_2.status = STARTED
                prevButtonState = mouse12_2.getPressed()  # if button is down already this ISN'T a new click
            if mouse12_2.status == STARTED:  # only update if started and not finished!
                buttons = mouse12_2.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [trueButton, falseButton]:
                            if obj.contains(mouse12_2):
                                gotValidClick = True
                                mouse12_2.clicked_name.append(obj.name)
                        x, y = mouse12_2.getPos()
                        mouse12_2.x.append(x)
                        mouse12_2.y.append(y)
                        buttons = mouse12_2.getPressed()
                        mouse12_2.leftButton.append(buttons[0])
                        mouse12_2.midButton.append(buttons[1])
                        mouse12_2.rightButton.append(buttons[2])
                        mouse12_2.time.append(mouse12_2.mouseClock.getTime())
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in sentenceResponseTrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "sentenceResponseTrial"-------
        for thisComponent in sentenceResponseTrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        sentenceTrial.addData('totalCorrectSentenceTrial', totalCorrectSentenceTrial )
        practiceSentence.addData('correctSentenceTrial', correct)
        sentenceTrial.addData('senseText_2.started', senseText_2.tStartRefresh)
        sentenceTrial.addData('senseText_2.stopped', senseText_2.tStopRefresh)
        sentenceTrial.addData('trueButton_2.started', trueButton_2.tStartRefresh)
        sentenceTrial.addData('trueButton_2.stopped', trueButton_2.tStopRefresh)
        sentenceTrial.addData('trueText_2.started', trueText_2.tStartRefresh)
        sentenceTrial.addData('trueText_2.stopped', trueText_2.tStopRefresh)
        sentenceTrial.addData('falseButton_2.started', falseButton_2.tStartRefresh)
        sentenceTrial.addData('falseButton_2.stopped', falseButton_2.tStopRefresh)
        sentenceTrial.addData('falseText_2.started', falseText_2.tStartRefresh)
        sentenceTrial.addData('falseText_2.stopped', falseText_2.tStopRefresh)
        # store data for sentenceTrial (TrialHandler)
        if len(mouse12_2.x): sentenceTrial.addData('mouse12_2.x', mouse12_2.x[0])
        if len(mouse12_2.y): sentenceTrial.addData('mouse12_2.y', mouse12_2.y[0])
        if len(mouse12_2.leftButton): sentenceTrial.addData('mouse12_2.leftButton', mouse12_2.leftButton[0])
        if len(mouse12_2.midButton): sentenceTrial.addData('mouse12_2.midButton', mouse12_2.midButton[0])
        if len(mouse12_2.rightButton): sentenceTrial.addData('mouse12_2.rightButton', mouse12_2.rightButton[0])
        if len(mouse12_2.time): sentenceTrial.addData('mouse12_2.time', mouse12_2.time[0])
        if len(mouse12_2.clicked_name): sentenceTrial.addData('mouse12_2.clicked_name', mouse12_2.clicked_name[0])
        sentenceTrial.addData('mouse12_2.started', mouse12_2.tStart)
        sentenceTrial.addData('mouse12_2.stopped', mouse12_2.tStop)
        # the Routine "sentenceResponseTrial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'sentenceTrial'
    
    
    # ------Prepare to start Routine "practiceList"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    letterAppear.setText('')
    letters = ["F", "P", "Q", "J", "H", "K", "T", "S", "N", "R", "Y", "L"]
    firstLetter = choice(letters)
    letters.remove(firstLetter)
    secondLetter = choice(letters)
    letters.append(firstLetter)
    
    letterAppear.setText(firstLetter)
    letterAppear_2.setText(secondLetter)
    # keep track of which components have finished
    practiceListComponents = [letterAppear, letterAppear_2]
    for thisComponent in practiceListComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practiceListClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practiceList"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = practiceListClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practiceListClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *letterAppear* updates
        if letterAppear.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            letterAppear.frameNStart = frameN  # exact frame index
            letterAppear.tStart = t  # local t and not account for scr refresh
            letterAppear.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letterAppear, 'tStartRefresh')  # time at next scr refresh
            letterAppear.setAutoDraw(True)
        if letterAppear.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > letterAppear.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                letterAppear.tStop = t  # not accounting for scr refresh
                letterAppear.frameNStop = frameN  # exact frame index
                win.timeOnFlip(letterAppear, 'tStopRefresh')  # time at next scr refresh
                letterAppear.setAutoDraw(False)
        
        # *letterAppear_2* updates
        if letterAppear_2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            letterAppear_2.frameNStart = frameN  # exact frame index
            letterAppear_2.tStart = t  # local t and not account for scr refresh
            letterAppear_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letterAppear_2, 'tStartRefresh')  # time at next scr refresh
            letterAppear_2.setAutoDraw(True)
        if letterAppear_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > letterAppear_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                letterAppear_2.tStop = t  # not accounting for scr refresh
                letterAppear_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(letterAppear_2, 'tStopRefresh')  # time at next scr refresh
                letterAppear_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceListComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practiceList"-------
    for thisComponent in practiceListComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trial.addData('letterAppear.started', letterAppear.tStartRefresh)
    trial.addData('letterAppear.stopped', letterAppear.tStopRefresh)
    trial.addData('letterAppear_2.started', letterAppear_2.tStartRefresh)
    trial.addData('letterAppear_2.stopped', letterAppear_2.tStopRefresh)
    
    # ------Prepare to start Routine "practiceRecall"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouseClear
    mouseClear.clicked_name = []
    gotValidClick = False  # until a click is received
    checkboxes = [Fbutton, Pbutton, Qbutton, Jbutton, Hbutton, Kbutton, Tbutton, Sbutton, Nbutton, Rbutton, Ybutton, Lbutton]
    clicked = []
    clickedTrack = []
    
    timer = core.Clock()
    timer.reset()
    
    # setup some python lists for storing info about the mouseExit
    mouseExit.x = []
    mouseExit.y = []
    mouseExit.leftButton = []
    mouseExit.midButton = []
    mouseExit.rightButton = []
    mouseExit.time = []
    mouseExit.clicked_name = []
    gotValidClick = False  # until a click is received
    # setup some python lists for storing info about the mouse1
    mouse1.x = []
    mouse1.y = []
    mouse1.leftButton = []
    mouse1.midButton = []
    mouse1.rightButton = []
    mouse1.time = []
    mouse1.clicked_name = []
    gotValidClick = False  # until a click is received
    Fbutton.setFillColor('green')
    Pbutton.setFillColor('green')
    Qbutton.setFillColor('green')
    Jbutton.setFillColor('green')
    Hbutton.setFillColor('green')
    Kbutton.setFillColor('green')
    Tbutton.setFillColor('green')
    Sbutton.setFillColor('green')
    Nbutton.setFillColor('green')
    Rbutton.setFillColor('green')
    Ybutton.setFillColor('green')
    Lbutton.setFillColor('green')
    answer1.setText('')
    answer2.setText('')
    # setup some python lists for storing info about the mouseBlank
    mouseBlank.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    practiceRecallComponents = [mouseClear, mouseExit, mouse1, blankButton, gatherResponseText, Fbutton, F_text, Pbutton, Qbutton, Jbutton, Hbutton, Kbutton, Tbutton, Sbutton, Nbutton, Rbutton, Ybutton, Lbutton, clearButton, exitButton, exitText, clearText, P_text, Q_text, J_text, H_text, K_text, T_text, S_text, N_text, R_text, Y_text, L_text, blankText, answer1, answer2, mouseBlank]
    for thisComponent in practiceRecallComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practiceRecallClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practiceRecall"-------
    while continueRoutine:
        # get current time
        t = practiceRecallClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practiceRecallClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if mouseExit.isPressedIn(exitButton):
            continueRoutine = False
        
        if mouseBlank.isPressedIn(blankButton):
            clicked.append(blankButton)
            clickedTrack.append(box)
            answer1.color = "white"
            answer2.color = "white"
            if len(clicked)==1:
                answer1.setText("Blank")
            elif len(clicked) ==2:
               answer2.setText("Blank")
        
        for box in checkboxes:
            if mouse1.isPressedIn(box) and box.name not in clicked and len(clicked)==0:
                box.fillColor = "black"
                clicked.append(box.name)
                clickedTrack.append(box)
                answer1.color = "white"
                if box.name is "Fbutton":
                    answer1.setText("F")
                elif box.name is "Pbutton":
                    answer1.setText("P")
                elif box.name is "Qbutton":
                    answer1.setText("Q")
                elif box.name is "Jbutton":
                    answer1.setText("J")
                elif box.name is "Hbutton":
                    answer1.setText("H")
                elif box.name is "Kbutton":
                    answer1.setText("K")
                elif box.name is "Tbutton":
                    answer1.setText("T")
                elif box.name is"Sbutton":
                    answer1.setText("S")
                elif box.name is "Nbutton":
                    answer1.setText("N")
                elif box.name is "Rbutton":
                    answer1.setText("R")
                elif box.name is "Ybutton":
                    answer1.setText("Y")
                elif box.name is "Lbutton":
                    answer1.setText("L")
        
        for box in checkboxes:
            if mouse1.isPressedIn(box) and box.name not in clicked and len(clicked) ==1:
                box.fillColor = "black"
                clicked.append(box.name)
                answer2.color = "white"
                clickedTrack.append(box)
                if box.name is "Fbutton":
                    answer2.setText("F")
                elif box.name is "Pbutton":
                    answer2.setText("P")
                elif box.name is "Qbutton":
                    answer2.setText("Q")
                elif box.name is "Jbutton":
                    answer2.setText("J")
                elif box.name is "Hbutton":
                    answer2.setText("H")
                elif box.name is "Kbutton":
                    answer2.setText("K")
                elif box.name is "Tbutton":
                    answer2.setText("T")
                elif box.name is"Sbutton":
                    answer2.setText("S")
                elif box.name is "Nbutton":
                    answer2.setText("N")
                elif box.name is "Rbutton":
                    answer2.setText("R")
                elif box.name is "Ybutton":
                    answer2.setText("Y")
                elif box.name is "Lbutton":
                       answer2.setText("L")
                elif box.name is "blankButton":
                    answer2.setText("Blank")
        
        if mouseClear.isPressedIn(clearButton):
            if len(clicked) ==1:
                if clickedTrack[0] is not blankButton:
                    clickedTrack[0].fillColor = "green"
            answer1.setText("")
            answer2.setText("")
            if len(clicked)  ==2:
                if clickedTrack[0] is not blankButton:
                    clickedTrack[0].fillColor = "green"
                if clickedTrack[1] is not blankButton:
                    clickedTrack[1].fillColor  = "green"
            clicked = []
            clickedTrack = []
        
        
        
        # *mouseExit* updates
        if mouseExit.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouseExit.frameNStart = frameN  # exact frame index
            mouseExit.tStart = t  # local t and not account for scr refresh
            mouseExit.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouseExit, 'tStartRefresh')  # time at next scr refresh
            mouseExit.status = STARTED
            mouseExit.mouseClock.reset()
            prevButtonState = mouseExit.getPressed()  # if button is down already this ISN'T a new click
        if mouseExit.status == STARTED:  # only update if started and not finished!
            buttons = mouseExit.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [exitButton]:
                        if obj.contains(mouseExit):
                            gotValidClick = True
                            mouseExit.clicked_name.append(obj.name)
                    x, y = mouseExit.getPos()
                    mouseExit.x.append(x)
                    mouseExit.y.append(y)
                    buttons = mouseExit.getPressed()
                    mouseExit.leftButton.append(buttons[0])
                    mouseExit.midButton.append(buttons[1])
                    mouseExit.rightButton.append(buttons[2])
                    mouseExit.time.append(mouseExit.mouseClock.getTime())
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        # *mouse1* updates
        if mouse1.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse1.frameNStart = frameN  # exact frame index
            mouse1.tStart = t  # local t and not account for scr refresh
            mouse1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse1, 'tStartRefresh')  # time at next scr refresh
            mouse1.status = STARTED
            mouse1.mouseClock.reset()
            prevButtonState = mouse1.getPressed()  # if button is down already this ISN'T a new click
        if mouse1.status == STARTED:  # only update if started and not finished!
            buttons = mouse1.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [Fbutton, Pbutton, Qbutton, Jbutton, Hbutton, Kbutton, Tbutton, Sbutton, Nbutton, Rbutton, Ybutton, Lbutton]:
                        if obj.contains(mouse1):
                            gotValidClick = True
                            mouse1.clicked_name.append(obj.name)
                    x, y = mouse1.getPos()
                    mouse1.x.append(x)
                    mouse1.y.append(y)
                    buttons = mouse1.getPressed()
                    mouse1.leftButton.append(buttons[0])
                    mouse1.midButton.append(buttons[1])
                    mouse1.rightButton.append(buttons[2])
                    mouse1.time.append(mouse1.mouseClock.getTime())
        
        # *blankButton* updates
        if blankButton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blankButton.frameNStart = frameN  # exact frame index
            blankButton.tStart = t  # local t and not account for scr refresh
            blankButton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blankButton, 'tStartRefresh')  # time at next scr refresh
            blankButton.setAutoDraw(True)
        
        # *gatherResponseText* updates
        if gatherResponseText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            gatherResponseText.frameNStart = frameN  # exact frame index
            gatherResponseText.tStart = t  # local t and not account for scr refresh
            gatherResponseText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(gatherResponseText, 'tStartRefresh')  # time at next scr refresh
            gatherResponseText.setAutoDraw(True)
        
        # *Fbutton* updates
        if Fbutton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fbutton.frameNStart = frameN  # exact frame index
            Fbutton.tStart = t  # local t and not account for scr refresh
            Fbutton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fbutton, 'tStartRefresh')  # time at next scr refresh
            Fbutton.setAutoDraw(True)
        
        # *F_text* updates
        if F_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            F_text.frameNStart = frameN  # exact frame index
            F_text.tStart = t  # local t and not account for scr refresh
            F_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(F_text, 'tStartRefresh')  # time at next scr refresh
            F_text.setAutoDraw(True)
        
        # *Pbutton* updates
        if Pbutton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Pbutton.frameNStart = frameN  # exact frame index
            Pbutton.tStart = t  # local t and not account for scr refresh
            Pbutton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Pbutton, 'tStartRefresh')  # time at next scr refresh
            Pbutton.setAutoDraw(True)
        
        # *Qbutton* updates
        if Qbutton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Qbutton.frameNStart = frameN  # exact frame index
            Qbutton.tStart = t  # local t and not account for scr refresh
            Qbutton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Qbutton, 'tStartRefresh')  # time at next scr refresh
            Qbutton.setAutoDraw(True)
        
        # *Jbutton* updates
        if Jbutton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Jbutton.frameNStart = frameN  # exact frame index
            Jbutton.tStart = t  # local t and not account for scr refresh
            Jbutton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Jbutton, 'tStartRefresh')  # time at next scr refresh
            Jbutton.setAutoDraw(True)
        
        # *Hbutton* updates
        if Hbutton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Hbutton.frameNStart = frameN  # exact frame index
            Hbutton.tStart = t  # local t and not account for scr refresh
            Hbutton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Hbutton, 'tStartRefresh')  # time at next scr refresh
            Hbutton.setAutoDraw(True)
        
        # *Kbutton* updates
        if Kbutton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Kbutton.frameNStart = frameN  # exact frame index
            Kbutton.tStart = t  # local t and not account for scr refresh
            Kbutton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Kbutton, 'tStartRefresh')  # time at next scr refresh
            Kbutton.setAutoDraw(True)
        
        # *Tbutton* updates
        if Tbutton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Tbutton.frameNStart = frameN  # exact frame index
            Tbutton.tStart = t  # local t and not account for scr refresh
            Tbutton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Tbutton, 'tStartRefresh')  # time at next scr refresh
            Tbutton.setAutoDraw(True)
        
        # *Sbutton* updates
        if Sbutton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Sbutton.frameNStart = frameN  # exact frame index
            Sbutton.tStart = t  # local t and not account for scr refresh
            Sbutton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Sbutton, 'tStartRefresh')  # time at next scr refresh
            Sbutton.setAutoDraw(True)
        
        # *Nbutton* updates
        if Nbutton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Nbutton.frameNStart = frameN  # exact frame index
            Nbutton.tStart = t  # local t and not account for scr refresh
            Nbutton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Nbutton, 'tStartRefresh')  # time at next scr refresh
            Nbutton.setAutoDraw(True)
        
        # *Rbutton* updates
        if Rbutton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Rbutton.frameNStart = frameN  # exact frame index
            Rbutton.tStart = t  # local t and not account for scr refresh
            Rbutton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Rbutton, 'tStartRefresh')  # time at next scr refresh
            Rbutton.setAutoDraw(True)
        
        # *Ybutton* updates
        if Ybutton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Ybutton.frameNStart = frameN  # exact frame index
            Ybutton.tStart = t  # local t and not account for scr refresh
            Ybutton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Ybutton, 'tStartRefresh')  # time at next scr refresh
            Ybutton.setAutoDraw(True)
        
        # *Lbutton* updates
        if Lbutton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Lbutton.frameNStart = frameN  # exact frame index
            Lbutton.tStart = t  # local t and not account for scr refresh
            Lbutton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Lbutton, 'tStartRefresh')  # time at next scr refresh
            Lbutton.setAutoDraw(True)
        
        # *clearButton* updates
        if clearButton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            clearButton.frameNStart = frameN  # exact frame index
            clearButton.tStart = t  # local t and not account for scr refresh
            clearButton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clearButton, 'tStartRefresh')  # time at next scr refresh
            clearButton.setAutoDraw(True)
        
        # *exitButton* updates
        if exitButton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            exitButton.frameNStart = frameN  # exact frame index
            exitButton.tStart = t  # local t and not account for scr refresh
            exitButton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(exitButton, 'tStartRefresh')  # time at next scr refresh
            exitButton.setAutoDraw(True)
        
        # *exitText* updates
        if exitText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            exitText.frameNStart = frameN  # exact frame index
            exitText.tStart = t  # local t and not account for scr refresh
            exitText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(exitText, 'tStartRefresh')  # time at next scr refresh
            exitText.setAutoDraw(True)
        
        # *clearText* updates
        if clearText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            clearText.frameNStart = frameN  # exact frame index
            clearText.tStart = t  # local t and not account for scr refresh
            clearText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clearText, 'tStartRefresh')  # time at next scr refresh
            clearText.setAutoDraw(True)
        
        # *P_text* updates
        if P_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            P_text.frameNStart = frameN  # exact frame index
            P_text.tStart = t  # local t and not account for scr refresh
            P_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(P_text, 'tStartRefresh')  # time at next scr refresh
            P_text.setAutoDraw(True)
        
        # *Q_text* updates
        if Q_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q_text.frameNStart = frameN  # exact frame index
            Q_text.tStart = t  # local t and not account for scr refresh
            Q_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q_text, 'tStartRefresh')  # time at next scr refresh
            Q_text.setAutoDraw(True)
        
        # *J_text* updates
        if J_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            J_text.frameNStart = frameN  # exact frame index
            J_text.tStart = t  # local t and not account for scr refresh
            J_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(J_text, 'tStartRefresh')  # time at next scr refresh
            J_text.setAutoDraw(True)
        
        # *H_text* updates
        if H_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            H_text.frameNStart = frameN  # exact frame index
            H_text.tStart = t  # local t and not account for scr refresh
            H_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(H_text, 'tStartRefresh')  # time at next scr refresh
            H_text.setAutoDraw(True)
        
        # *K_text* updates
        if K_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            K_text.frameNStart = frameN  # exact frame index
            K_text.tStart = t  # local t and not account for scr refresh
            K_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(K_text, 'tStartRefresh')  # time at next scr refresh
            K_text.setAutoDraw(True)
        
        # *T_text* updates
        if T_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T_text.frameNStart = frameN  # exact frame index
            T_text.tStart = t  # local t and not account for scr refresh
            T_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T_text, 'tStartRefresh')  # time at next scr refresh
            T_text.setAutoDraw(True)
        
        # *S_text* updates
        if S_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            S_text.frameNStart = frameN  # exact frame index
            S_text.tStart = t  # local t and not account for scr refresh
            S_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(S_text, 'tStartRefresh')  # time at next scr refresh
            S_text.setAutoDraw(True)
        
        # *N_text* updates
        if N_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            N_text.frameNStart = frameN  # exact frame index
            N_text.tStart = t  # local t and not account for scr refresh
            N_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(N_text, 'tStartRefresh')  # time at next scr refresh
            N_text.setAutoDraw(True)
        
        # *R_text* updates
        if R_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            R_text.frameNStart = frameN  # exact frame index
            R_text.tStart = t  # local t and not account for scr refresh
            R_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(R_text, 'tStartRefresh')  # time at next scr refresh
            R_text.setAutoDraw(True)
        
        # *Y_text* updates
        if Y_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Y_text.frameNStart = frameN  # exact frame index
            Y_text.tStart = t  # local t and not account for scr refresh
            Y_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Y_text, 'tStartRefresh')  # time at next scr refresh
            Y_text.setAutoDraw(True)
        
        # *L_text* updates
        if L_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            L_text.frameNStart = frameN  # exact frame index
            L_text.tStart = t  # local t and not account for scr refresh
            L_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(L_text, 'tStartRefresh')  # time at next scr refresh
            L_text.setAutoDraw(True)
        
        # *blankText* updates
        if blankText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blankText.frameNStart = frameN  # exact frame index
            blankText.tStart = t  # local t and not account for scr refresh
            blankText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blankText, 'tStartRefresh')  # time at next scr refresh
            blankText.setAutoDraw(True)
        
        # *answer1* updates
        if answer1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            answer1.frameNStart = frameN  # exact frame index
            answer1.tStart = t  # local t and not account for scr refresh
            answer1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(answer1, 'tStartRefresh')  # time at next scr refresh
            answer1.setAutoDraw(True)
        
        # *answer2* updates
        if answer2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            answer2.frameNStart = frameN  # exact frame index
            answer2.tStart = t  # local t and not account for scr refresh
            answer2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(answer2, 'tStartRefresh')  # time at next scr refresh
            answer2.setAutoDraw(True)
        # *mouseBlank* updates
        if mouseBlank.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouseBlank.frameNStart = frameN  # exact frame index
            mouseBlank.tStart = t  # local t and not account for scr refresh
            mouseBlank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouseBlank, 'tStartRefresh')  # time at next scr refresh
            mouseBlank.status = STARTED
            mouseBlank.mouseClock.reset()
            prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
        if mouseBlank.status == STARTED:  # only update if started and not finished!
            buttons = mouseBlank.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [blankButton]:
                        if obj.contains(mouseBlank):
                            gotValidClick = True
                            mouseBlank.clicked_name.append(obj.name)
                    # abort routine on response
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceRecallComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practiceRecall"-------
    for thisComponent in practiceRecallComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trial (TrialHandler)
    x, y = mouseClear.getPos()
    buttons = mouseClear.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        for obj in [clearButton]:
            if obj.contains(mouseClear):
                gotValidClick = True
                mouseClear.clicked_name.append(obj.name)
    trial.addData('mouseClear.x', x)
    trial.addData('mouseClear.y', y)
    trial.addData('mouseClear.leftButton', buttons[0])
    trial.addData('mouseClear.midButton', buttons[1])
    trial.addData('mouseClear.rightButton', buttons[2])
    if len(mouseClear.clicked_name):
        trial.addData('mouseClear.clicked_name', mouseClear.clicked_name[0])
    trial.addData('mouseClear.started', mouseClear.tStart)
    trial.addData('mouseClear.stopped', mouseClear.tStop)
    #Correct Point System
    correctLettersTrial = 0
    if practiceLoop.finished == True:
        for answer in clicked:
            if clicked[0] is firstLetter and clicked[1] is secondLetter:
                correctLettersTrial +=1
                trial.addData('correctLettersTrial', correctLettersTrial)
                trial.addData('routineTime', timer.getTime())
    else:
            for answer in clicked:
                if clicked[0] is firstLetter and clicked[1] is secondLetter:
                    correctLettersPractice +=1
                trial.addData('correctLettersPractice', correctLettersPractice)
                trial.addData('routineTime', timer.getTime())
    # store data for trial (TrialHandler)
    if len(mouseExit.x): trial.addData('mouseExit.x', mouseExit.x[0])
    if len(mouseExit.y): trial.addData('mouseExit.y', mouseExit.y[0])
    if len(mouseExit.leftButton): trial.addData('mouseExit.leftButton', mouseExit.leftButton[0])
    if len(mouseExit.midButton): trial.addData('mouseExit.midButton', mouseExit.midButton[0])
    if len(mouseExit.rightButton): trial.addData('mouseExit.rightButton', mouseExit.rightButton[0])
    if len(mouseExit.time): trial.addData('mouseExit.time', mouseExit.time[0])
    if len(mouseExit.clicked_name): trial.addData('mouseExit.clicked_name', mouseExit.clicked_name[0])
    trial.addData('mouseExit.started', mouseExit.tStart)
    trial.addData('mouseExit.stopped', mouseExit.tStop)
    # store data for trial (TrialHandler)
    trial.addData('mouse1.x', mouse1.x)
    trial.addData('mouse1.y', mouse1.y)
    trial.addData('mouse1.leftButton', mouse1.leftButton)
    trial.addData('mouse1.midButton', mouse1.midButton)
    trial.addData('mouse1.rightButton', mouse1.rightButton)
    trial.addData('mouse1.time', mouse1.time)
    trial.addData('mouse1.clicked_name', mouse1.clicked_name)
    trial.addData('mouse1.started', mouse1.tStart)
    trial.addData('mouse1.stopped', mouse1.tStop)
    trial.addData('blankButton.started', blankButton.tStartRefresh)
    trial.addData('blankButton.stopped', blankButton.tStopRefresh)
    trial.addData('gatherResponseText.started', gatherResponseText.tStartRefresh)
    trial.addData('gatherResponseText.stopped', gatherResponseText.tStopRefresh)
    trial.addData('Fbutton.started', Fbutton.tStartRefresh)
    trial.addData('Fbutton.stopped', Fbutton.tStopRefresh)
    trial.addData('F_text.started', F_text.tStartRefresh)
    trial.addData('F_text.stopped', F_text.tStopRefresh)
    trial.addData('Pbutton.started', Pbutton.tStartRefresh)
    trial.addData('Pbutton.stopped', Pbutton.tStopRefresh)
    trial.addData('Qbutton.started', Qbutton.tStartRefresh)
    trial.addData('Qbutton.stopped', Qbutton.tStopRefresh)
    trial.addData('Jbutton.started', Jbutton.tStartRefresh)
    trial.addData('Jbutton.stopped', Jbutton.tStopRefresh)
    trial.addData('Hbutton.started', Hbutton.tStartRefresh)
    trial.addData('Hbutton.stopped', Hbutton.tStopRefresh)
    trial.addData('Kbutton.started', Kbutton.tStartRefresh)
    trial.addData('Kbutton.stopped', Kbutton.tStopRefresh)
    trial.addData('Tbutton.started', Tbutton.tStartRefresh)
    trial.addData('Tbutton.stopped', Tbutton.tStopRefresh)
    trial.addData('Sbutton.started', Sbutton.tStartRefresh)
    trial.addData('Sbutton.stopped', Sbutton.tStopRefresh)
    trial.addData('Nbutton.started', Nbutton.tStartRefresh)
    trial.addData('Nbutton.stopped', Nbutton.tStopRefresh)
    trial.addData('Rbutton.started', Rbutton.tStartRefresh)
    trial.addData('Rbutton.stopped', Rbutton.tStopRefresh)
    trial.addData('Ybutton.started', Ybutton.tStartRefresh)
    trial.addData('Ybutton.stopped', Ybutton.tStopRefresh)
    trial.addData('Lbutton.started', Lbutton.tStartRefresh)
    trial.addData('Lbutton.stopped', Lbutton.tStopRefresh)
    trial.addData('clearButton.started', clearButton.tStartRefresh)
    trial.addData('clearButton.stopped', clearButton.tStopRefresh)
    trial.addData('exitButton.started', exitButton.tStartRefresh)
    trial.addData('exitButton.stopped', exitButton.tStopRefresh)
    trial.addData('exitText.started', exitText.tStartRefresh)
    trial.addData('exitText.stopped', exitText.tStopRefresh)
    trial.addData('clearText.started', clearText.tStartRefresh)
    trial.addData('clearText.stopped', clearText.tStopRefresh)
    trial.addData('P_text.started', P_text.tStartRefresh)
    trial.addData('P_text.stopped', P_text.tStopRefresh)
    trial.addData('Q_text.started', Q_text.tStartRefresh)
    trial.addData('Q_text.stopped', Q_text.tStopRefresh)
    trial.addData('J_text.started', J_text.tStartRefresh)
    trial.addData('J_text.stopped', J_text.tStopRefresh)
    trial.addData('H_text.started', H_text.tStartRefresh)
    trial.addData('H_text.stopped', H_text.tStopRefresh)
    trial.addData('K_text.started', K_text.tStartRefresh)
    trial.addData('K_text.stopped', K_text.tStopRefresh)
    trial.addData('T_text.started', T_text.tStartRefresh)
    trial.addData('T_text.stopped', T_text.tStopRefresh)
    trial.addData('S_text.started', S_text.tStartRefresh)
    trial.addData('S_text.stopped', S_text.tStopRefresh)
    trial.addData('N_text.started', N_text.tStartRefresh)
    trial.addData('N_text.stopped', N_text.tStopRefresh)
    trial.addData('R_text.started', R_text.tStartRefresh)
    trial.addData('R_text.stopped', R_text.tStopRefresh)
    trial.addData('Y_text.started', Y_text.tStartRefresh)
    trial.addData('Y_text.stopped', Y_text.tStopRefresh)
    trial.addData('L_text.started', L_text.tStartRefresh)
    trial.addData('L_text.stopped', L_text.tStopRefresh)
    trial.addData('blankText.started', blankText.tStartRefresh)
    trial.addData('blankText.stopped', blankText.tStopRefresh)
    trial.addData('answer1.started', answer1.tStartRefresh)
    trial.addData('answer1.stopped', answer1.tStopRefresh)
    trial.addData('answer2.started', answer2.tStartRefresh)
    trial.addData('answer2.stopped', answer2.tStopRefresh)
    # store data for trial (TrialHandler)
    x, y = mouseBlank.getPos()
    buttons = mouseBlank.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        for obj in [blankButton]:
            if obj.contains(mouseBlank):
                gotValidClick = True
                mouseBlank.clicked_name.append(obj.name)
    trial.addData('mouseBlank.x', x)
    trial.addData('mouseBlank.y', y)
    trial.addData('mouseBlank.leftButton', buttons[0])
    trial.addData('mouseBlank.midButton', buttons[1])
    trial.addData('mouseBlank.rightButton', buttons[2])
    if len(mouseBlank.clicked_name):
        trial.addData('mouseBlank.clicked_name', mouseBlank.clicked_name[0])
    trial.addData('mouseBlank.started', mouseBlank.tStart)
    trial.addData('mouseBlank.stopped', mouseBlank.tStop)
    # the Routine "practiceRecall" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trial'


# ------Prepare to start Routine "feedback_2"-------
continueRoutine = True
# update component parameters for each repeat
lettersCorrect.setText(percentCorrect)
lettersRecalled = 'You recalled '  + str(correctLetters) + ' letters correctly out of ' + str(7) + 'letters.'


percentCorrect = 'Percentage correct: ' + str(totalCorrectPractice/12) + '%'

#12 represents the number of sentences (can change)
text_2.setText(lettersRecalled)
# keep track of which components have finished
feedback_2Components = [lettersCorrect, text_2, Feedback]
for thisComponent in feedback_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
feedback_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "feedback_2"-------
while continueRoutine:
    # get current time
    t = feedback_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=feedback_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *lettersCorrect* updates
    if lettersCorrect.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        lettersCorrect.frameNStart = frameN  # exact frame index
        lettersCorrect.tStart = t  # local t and not account for scr refresh
        lettersCorrect.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(lettersCorrect, 'tStartRefresh')  # time at next scr refresh
        lettersCorrect.setAutoDraw(True)
    lettersRecalled = 'You recalled ' +  str(correctLetters) + ' letters correctly out of ' + str(7) + 'letters.'
    
    
    percentCorrect = 'Percentage correct: ' + str(totalCorrectPractice/12 ) + '%'
    
    #12 represents the number of sentences (can change)
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *Feedback* updates
    if Feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Feedback.frameNStart = frameN  # exact frame index
        Feedback.tStart = t  # local t and not account for scr refresh
        Feedback.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Feedback, 'tStartRefresh')  # time at next scr refresh
        Feedback.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in feedback_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "feedback_2"-------
for thisComponent in feedback_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('lettersCorrect.started', lettersCorrect.tStartRefresh)
thisExp.addData('lettersCorrect.stopped', lettersCorrect.tStopRefresh)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
thisExp.addData('Feedback.started', Feedback.tStartRefresh)
thisExp.addData('Feedback.stopped', Feedback.tStopRefresh)
# the Routine "feedback_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
trials.addData('totalCorrectPractice', totalCorrectPractice)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
