/************** 
 * Rspan Test *
 **************/

import { PsychoJS } from './lib/core-2020.2.js';
import * as core from './lib/core-2020.2.js';
import { TrialHandler } from './lib/data-2020.2.js';
import { Scheduler } from './lib/util-2020.2.js';
import * as visual from './lib/visual-2020.2.js';
import * as sound from './lib/sound-2020.2.js';
import * as util from './lib/util-2020.2.js';
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'RSpan';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001', 'age': '', 'sex': ''};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(TitleScreenRoutineBegin());
flowScheduler.add(TitleScreenRoutineEachFrame());
flowScheduler.add(TitleScreenRoutineEnd());
flowScheduler.add(PracticeLetterInstruct1RoutineBegin());
flowScheduler.add(PracticeLetterInstruct1RoutineEachFrame());
flowScheduler.add(PracticeLetterInstruct1RoutineEnd());
flowScheduler.add(PracticeLetterInstruct2RoutineBegin());
flowScheduler.add(PracticeLetterInstruct2RoutineEachFrame());
flowScheduler.add(PracticeLetterInstruct2RoutineEnd());
flowScheduler.add(PracticeLetterInstruct3RoutineBegin());
flowScheduler.add(PracticeLetterInstruct3RoutineEachFrame());
flowScheduler.add(PracticeLetterInstruct3RoutineEnd());
const practiceLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(practiceLoopLoopBegin, practiceLoopLoopScheduler);
flowScheduler.add(practiceLoopLoopScheduler);
flowScheduler.add(practiceLoopLoopEnd);
flowScheduler.add(PractSentInst1RoutineBegin());
flowScheduler.add(PractSentInst1RoutineEachFrame());
flowScheduler.add(PractSentInst1RoutineEnd());
flowScheduler.add(PractSenInst2RoutineBegin());
flowScheduler.add(PractSenInst2RoutineEachFrame());
flowScheduler.add(PractSenInst2RoutineEnd());
flowScheduler.add(PracSenInst3RoutineBegin());
flowScheduler.add(PracSenInst3RoutineEachFrame());
flowScheduler.add(PracSenInst3RoutineEnd());
const practiceSentenceLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(practiceSentenceLoopBegin, practiceSentenceLoopScheduler);
flowScheduler.add(practiceSentenceLoopScheduler);
flowScheduler.add(practiceSentenceLoopEnd);
flowScheduler.add(RSPANpracticeInstruct1_2RoutineBegin());
flowScheduler.add(RSPANpracticeInstruct1_2RoutineEachFrame());
flowScheduler.add(RSPANpracticeInstruct1_2RoutineEnd());
flowScheduler.add(RSPANpracticeInstruct2RoutineBegin());
flowScheduler.add(RSPANpracticeInstruct2RoutineEachFrame());
flowScheduler.add(RSPANpracticeInstruct2RoutineEnd());
flowScheduler.add(feedbackinstructRoutineBegin());
flowScheduler.add(feedbackinstructRoutineEachFrame());
flowScheduler.add(feedbackinstructRoutineEnd());
flowScheduler.add(feedbackinstruct2RoutineBegin());
flowScheduler.add(feedbackinstruct2RoutineEachFrame());
flowScheduler.add(feedbackinstruct2RoutineEnd());
const trialLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialLoopBegin, trialLoopScheduler);
flowScheduler.add(trialLoopScheduler);
flowScheduler.add(trialLoopEnd);
flowScheduler.add(feedback_2RoutineBegin());
flowScheduler.add(feedback_2RoutineEachFrame());
flowScheduler.add(feedback_2RoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'sentenceProblems.xlsx', 'path': 'sentenceProblems.xlsx'},
    {'name': 'practiceLetter.xlsx', 'path': 'practiceLetter.xlsx'},
    {'name': 'SentenceProblems2.xlsx', 'path': 'SentenceProblems2.xlsx'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.DEBUG);

function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.2.4';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}

function experimentInit() {
  // Initialize components for Routine "TitleScreen"
  TitleScreenClock = new util.Clock();
  introScreen = new visual.TextStim({
    win: psychoJS.window,
    name: 'introScreen',
    text: 'Reading Span',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  responseIndicator1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'responseIndicator1',
    text: 'Click the mouse to continue.',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  mouse_1 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_1.mouseClock = new util.Clock();
  // Initialize components for Routine "PracticeLetterInstruct1"
  PracticeLetterInstruct1Clock = new util.Clock();
  instr_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_1',
    text: 'In this experiment you will try to memorize letters you see on the screen while you also read sentences.\n\nIn the next minutes, you will have some practice to get you familiar with how the experiment works.\n\nWe will begin by practicing the letter part of the experiment.\n\n',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  continue_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'continue_2',
    text: 'Click the mouse to continue.\n',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  mouse_2 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_2.mouseClock = new util.Clock();
  // Initialize components for Routine "PracticeLetterInstruct2"
  PracticeLetterInstruct2Clock = new util.Clock();
  instr_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_2',
    text: 'For this practice set, letters will appear on the screen one at a time.\n\nTry to remember each letter in the order presented.\n\nAfter 2 letters have been shown, you will see a screen listing 12 possible letters with a check box beside each one.\n\nYour job is to select each letter in the order presented. To do this, use the mouse to select the box beside each letter. The letters you select will appear at the bottom of the screen.',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  continue_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'continue_3',
    text: 'Click the mouse to continue.\n\n',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  mouse_3 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_3.mouseClock = new util.Clock();
  // Initialize components for Routine "PracticeLetterInstruct3"
  PracticeLetterInstruct3Clock = new util.Clock();
  instr_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_3',
    text: 'When you have selected all the letters, and they are in the correct order, hit the EXIT box at the bottom right of the screen.\n\nIf you make a mistake, hit the CLEAR box to start over.\n\nIf you forget one of the letters, click the BLANK box to mark the spot for the missing letter. \n\nRemember, it is very important to get the letters in the same order as you see them. If you forget one, use the BLANK box to mark the position.\n\nDo you have any questions so far?',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  continue_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'continue_4',
    text: 'When you’re ready, click the mouse button to start the letter practice.',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  mouse_4 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_4.mouseClock = new util.Clock();
  // Initialize components for Routine "practiceList"
  practiceListClock = new util.Clock();
  letterAppear = new visual.TextStim({
    win: psychoJS.window,
    name: 'letterAppear',
    text: /*  */
  ,
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  import {choice} from 'numpy/random';
  
  letterAppear_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'letterAppear_2',
    text: /*  */
  ,
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "practiceRecall"
  practiceRecallClock = new util.Clock();
  mouseClear = new core.Mouse({
    win: psychoJS.window,
  });
  mouseClear.mouseClock = new util.Clock();
  correctLettersPractice = 0;
  correctLettersTrial = 0;
  
  mouseExit = new core.Mouse({
    win: psychoJS.window,
  });
  mouseExit.mouseClock = new util.Clock();
  mouse1 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse1.mouseClock = new util.Clock();
  blankButton = new visual.Rect ({
    win: psychoJS.window, name: 'blankButton', 
    width: [0.15, 0.08][0], height: [0.15, 0.08][1],
    ori: 0, pos: [0.4, (- 0.4)],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -4, interpolate: true,
  });
  
  gatherResponseText = new visual.TextStim({
    win: psychoJS.window,
    name: 'gatherResponseText',
    text: 'Select the letters in the order presented. Use the blank button to fill in forgotten letters. ',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, 0.4], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  Fbutton = new visual.Rect ({
    win: psychoJS.window, name: 'Fbutton', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0, pos: [(- 0.3), 0.3],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -6, interpolate: true,
  });
  
  F_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'F_text',
    text: 'F',
    font: 'Times New Roman',
    units: undefined, 
    pos: [(- 0.23), 0.3], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -7.0 
  });
  
  Pbutton = new visual.Rect ({
    win: psychoJS.window, name: 'Pbutton', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0, pos: [(- 0.3), 0.2],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -8, interpolate: true,
  });
  
  Qbutton = new visual.Rect ({
    win: psychoJS.window, name: 'Qbutton', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0, pos: [(- 0.3), 0.1],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -9, interpolate: true,
  });
  
  Jbutton = new visual.Rect ({
    win: psychoJS.window, name: 'Jbutton', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0, pos: [(- 0.3), 0.0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -10, interpolate: true,
  });
  
  Hbutton = new visual.Rect ({
    win: psychoJS.window, name: 'Hbutton', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0, pos: [(- 0.3), (- 0.1)],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -11, interpolate: true,
  });
  
  Kbutton = new visual.Rect ({
    win: psychoJS.window, name: 'Kbutton', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0, pos: [(- 0.3), (- 0.2)],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -12, interpolate: true,
  });
  
  Tbutton = new visual.Rect ({
    win: psychoJS.window, name: 'Tbutton', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0, pos: [0.2, 0.3],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -13, interpolate: true,
  });
  
  Sbutton = new visual.Rect ({
    win: psychoJS.window, name: 'Sbutton', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0, pos: [0.2, 0.2],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -14, interpolate: true,
  });
  
  Nbutton = new visual.Rect ({
    win: psychoJS.window, name: 'Nbutton', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0, pos: [0.2, 0.1],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -15, interpolate: true,
  });
  
  Rbutton = new visual.Rect ({
    win: psychoJS.window, name: 'Rbutton', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0, pos: [0.2, 0.0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -16, interpolate: true,
  });
  
  Ybutton = new visual.Rect ({
    win: psychoJS.window, name: 'Ybutton', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0, pos: [0.2, (- 0.1)],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -17, interpolate: true,
  });
  
  Lbutton = new visual.Rect ({
    win: psychoJS.window, name: 'Lbutton', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0, pos: [0.2, (- 0.2)],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -18, interpolate: true,
  });
  
  clearButton = new visual.Rect ({
    win: psychoJS.window, name: 'clearButton', 
    width: [0.15, 0.08][0], height: [0.15, 0.08][1],
    ori: 0, pos: [0, (- 0.4)],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -19, interpolate: true,
  });
  
  exitButton = new visual.Rect ({
    win: psychoJS.window, name: 'exitButton', 
    width: [0.15, 0.08][0], height: [0.15, 0.08][1],
    ori: 0, pos: [(- 0.4), (- 0.4)],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -20, interpolate: true,
  });
  
  exitText = new visual.TextStim({
    win: psychoJS.window,
    name: 'exitText',
    text: 'EXIT',
    font: 'Times New Roman',
    units: undefined, 
    pos: [(- 0.4), (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -21.0 
  });
  
  clearText = new visual.TextStim({
    win: psychoJS.window,
    name: 'clearText',
    text: 'CLEAR',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -22.0 
  });
  
  P_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'P_text',
    text: 'P',
    font: 'Times New Roman',
    units: undefined, 
    pos: [(- 0.23), 0.2], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -23.0 
  });
  
  Q_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Q_text',
    text: 'Q',
    font: 'Times New Roman',
    units: undefined, 
    pos: [(- 0.23), 0.1], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -24.0 
  });
  
  J_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'J_text',
    text: 'J',
    font: 'Times New Roman',
    units: undefined, 
    pos: [(- 0.23), 0.0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -25.0 
  });
  
  H_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'H_text',
    text: 'H',
    font: 'Times New Roman',
    units: undefined, 
    pos: [(- 0.23), (- 0.1)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -26.0 
  });
  
  K_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'K_text',
    text: 'K',
    font: 'Times New Roman',
    units: undefined, 
    pos: [(- 0.23), (- 0.2)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -27.0 
  });
  
  T_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'T_text',
    text: 'T',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0.27, 0.3], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -28.0 
  });
  
  S_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'S_text',
    text: 'S',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0.27, 0.2], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -29.0 
  });
  
  N_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'N_text',
    text: 'N',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0.27, 0.1], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -30.0 
  });
  
  R_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'R_text',
    text: 'R',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0.27, 0.0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -31.0 
  });
  
  Y_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Y_text',
    text: 'Y',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0.27, (- 0.1)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -32.0 
  });
  
  L_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'L_text',
    text: 'L',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0.27, (- 0.2)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -33.0 
  });
  
  blankText = new visual.TextStim({
    win: psychoJS.window,
    name: 'blankText',
    text: 'BLANK',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -34.0 
  });
  
  answer1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'answer1',
    text: /*  */
  ,
    font: 'Times New Roman',
    units: undefined, 
    pos: [(- 0.05), (- 0.2)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('grey'),  opacity: 1,
    depth: -35.0 
  });
  
  answer2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'answer2',
    text: /*  */
  ,
    font: 'Times New Roman',
    units: undefined, 
    pos: [0.05, (- 0.2)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('grey'),  opacity: 1,
    depth: -36.0 
  });
  
  mouseBlank = new core.Mouse({
    win: psychoJS.window,
  });
  mouseBlank.mouseClock = new util.Clock();
  // Initialize components for Routine "PractSentInst1"
  PractSentInst1Clock = new util.Clock();
  instr_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_4',
    text: 'Now you will practice doing the sentence reading part of the experiment.\n\nA sentence will appear on the screen, like this:\n“I like to run in the park”\n\nAs soon as you see the sentence, you should read it and determine if it makes sense or not.\n\nThe above sentence makes sense.\n\nWhen you have read the sentence and determined whether it makes sense or not, you will click the mouse buttton.',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  continue_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'continue_5',
    text: 'Click the mouse to continue.\n',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  mouse_5 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_5.mouseClock = new util.Clock();
  // Initialize components for Routine "PractSenInst2"
  PractSenInst2Clock = new util.Clock();
  instr_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_5',
    text: 'You will then see “This sentence makes sense.” displayed on the next screen along with a box marked TRUE and a box marked FALSE.\n\nIf the sentence on the previous screen made sense, click on the TRUE box with the box.\n\nIf the sentence did not make sense, click on the FALSE box.\n\nAfter you click on one of the boxes, the computer will tell you if you made the right choice.',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  continue_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'continue_6',
    text: 'Click the mouse to continue.',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  mouse_6 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_6.mouseClock = new util.Clock();
  // Initialize components for Routine "PracSenInst3"
  PracSenInst3Clock = new util.Clock();
  instr_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_6',
    text: 'It is VERY important that you answer the sentence problems correctly. It is also important that you try and read the sentences as quickly as you can.\n\nDo you have any questions?',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  continue_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'continue_7',
    text: 'When you’re ready, click the mouse to try some practice problems. ',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  mouse_7 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_7.mouseClock = new util.Clock();
  // Initialize components for Routine "sentence"
  sentenceClock = new util.Clock();
  sentenceText = new visual.TextStim({
    win: psychoJS.window,
    name: 'sentenceText',
    text: 'default text',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  continue_12 = new visual.TextStim({
    win: psychoJS.window,
    name: 'continue_12',
    text: 'When you have read the sentence, click the mouse to continue.',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  avgTime = 0;
  totalTime = 0;
  
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: /*  */
  ,
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  // Initialize components for Routine "sentenceResponse"
  sentenceResponseClock = new util.Clock();
  totalCorrectPractice = 0;
  
  senseText = new visual.TextStim({
    win: psychoJS.window,
    name: 'senseText',
    text: 'This sentence makes sense.',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, 0.2], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  trueButton = new visual.Rect ({
    win: psychoJS.window, name: 'trueButton', 
    width: [0.15, 0.15][0], height: [0.15, 0.15][1],
    ori: 0, pos: [(- 0.2), (- 0.2)],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  trueText = new visual.TextStim({
    win: psychoJS.window,
    name: 'trueText',
    text: 'TRUE',
    font: 'Times New Roman',
    units: undefined, 
    pos: [(- 0.2), (- 0.2)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  falseButton = new visual.Rect ({
    win: psychoJS.window, name: 'falseButton', 
    width: [0.15, 0.15][0], height: [0.15, 0.15][1],
    ori: 0, pos: [0.2, (- 0.2)],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -4, interpolate: true,
  });
  
  falseText = new visual.TextStim({
    win: psychoJS.window,
    name: 'falseText',
    text: 'FALSE',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0.2, (- 0.2)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -5.0 
  });
  
  mouse12 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse12.mouseClock = new util.Clock();
  // Initialize components for Routine "feedback"
  feedbackClock = new util.Clock();
  sentenceFeedback2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'sentenceFeedback2',
    text: 'default text',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('blue'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "RSPANpracticeInstruct1_2"
  RSPANpracticeInstruct1_2Clock = new util.Clock();
  instr_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_7',
    text: 'Now you will practice doing both parts of the experiment at the same time. \n\nIn the next practice set, you will be given one sentence to read. Once you make your decision about the sentence, a letter will appear on the screen. Try and remember the letter.\n\nIn the previous section where you only read the sentences, the computer computed your average time to read the sentences. If you take longer than your average time, the computer will automatically move you onto the next part, thus skipping the True or False part and will count that problem as a sentence error. Thefore it is a VERY important to read the sentences as quickly and as accurately as possible. ',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  continue_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'continue_8',
    text: 'Click the mouse to continue.\n\n',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  mouse_8 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_8.mouseClock = new util.Clock();
  // Initialize components for Routine "RSPANpracticeInstruct2"
  RSPANpracticeInstruct2Clock = new util.Clock();
  instr_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_8',
    text: 'After the letter goes away, another sentence will appear, and then another letter.\n\nAt the end of each set of letters and sentences, a recall screen will appear. Use the mouse to select the letter you just saw. Try your best to get the letters in the correct order.\n\nIt is important to work QUICKLY and ACCURATELY on the sentences. Make sure you know whether the sentences make sense or not before clicking to the next screen.\n\nYou will not be told if you answer regarding the sentence is correct.\n',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  continue_9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'continue_9',
    text: 'Click the mouse button to continue.\n',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  mouse_9 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_9.mouseClock = new util.Clock();
  // Initialize components for Routine "feedbackinstruct"
  feedbackinstructClock = new util.Clock();
  instr_9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_9',
    text: 'After the recall screen, you will be given feedback about your performance regarding both the number of letters recalled and the percent correct on the sentence problems.',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  continue_10 = new visual.TextStim({
    win: psychoJS.window,
    name: 'continue_10',
    text: 'Do you have any questions?\nClick the mouse to continue.',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  mouse_10 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_10.mouseClock = new util.Clock();
  // Initialize components for Routine "feedbackinstruct2"
  feedbackinstruct2Clock = new util.Clock();
  instr_10 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_10',
    text: 'During the feedback, you will see a number in red in the top right of the screen. \nThis indicates your percent correct for the sentence problems for the entire experiment.\n\nIt is VERY important for you to keep this at least an 85%.\n\nFor our purposes, we can only use data where the participant was at least 85% accurate on the sentences.\n\nTherefore, try to perform at least an 85% on the sentence problems WHILE doing your best to recall as many letters as possible.',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  continue_11 = new visual.TextStim({
    win: psychoJS.window,
    name: 'continue_11',
    text: 'Do you have any questions?\nClick the mouse to try some practice problems. ',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  mouse_11 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_11.mouseClock = new util.Clock();
  // Initialize components for Routine "sentence2"
  sentence2Clock = new util.Clock();
  sentenceText2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'sentenceText2',
    text: 'default text',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  mouse_12 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_12.mouseClock = new util.Clock();
  continue_13 = new visual.TextStim({
    win: psychoJS.window,
    name: 'continue_13',
    text: 'When you have read the sentence, click the mouse to continue.',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  timerReading = new core.Clock();
  avgTime = 0;
  totalTime = 0;
  
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: /*  */
  ,
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  // Initialize components for Routine "sentenceResponseTrial"
  sentenceResponseTrialClock = new util.Clock();
  totalCorrectSentenceTrial = 0;
  
  senseText_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'senseText_2',
    text: 'This sentence makes sense.',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, 0.2], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  trueButton_2 = new visual.Rect ({
    win: psychoJS.window, name: 'trueButton_2', 
    width: [0.15, 0.15][0], height: [0.15, 0.15][1],
    ori: 0, pos: [(- 0.2), (- 0.2)],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  trueText_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'trueText_2',
    text: 'TRUE',
    font: 'Times New Roman',
    units: undefined, 
    pos: [(- 0.2), (- 0.2)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  falseButton_2 = new visual.Rect ({
    win: psychoJS.window, name: 'falseButton_2', 
    width: [0.15, 0.15][0], height: [0.15, 0.15][1],
    ori: 0, pos: [0.2, (- 0.2)],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -4, interpolate: true,
  });
  
  falseText_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'falseText_2',
    text: 'FALSE',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0.2, (- 0.2)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -5.0 
  });
  
  mouse12_2 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse12_2.mouseClock = new util.Clock();
  // Initialize components for Routine "letterTrial_2"
  letterTrial_2Clock = new util.Clock();
  letterAppear_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'letterAppear_3',
    text: /*  */
  ,
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  import {choice} from 'numpy/random';
  
  // Initialize components for Routine "practiceRecall"
  practiceRecallClock = new util.Clock();
  mouseClear = new core.Mouse({
    win: psychoJS.window,
  });
  mouseClear.mouseClock = new util.Clock();
  correctLettersPractice = 0;
  correctLettersTrial = 0;
  
  mouseExit = new core.Mouse({
    win: psychoJS.window,
  });
  mouseExit.mouseClock = new util.Clock();
  mouse1 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse1.mouseClock = new util.Clock();
  blankButton = new visual.Rect ({
    win: psychoJS.window, name: 'blankButton', 
    width: [0.15, 0.08][0], height: [0.15, 0.08][1],
    ori: 0, pos: [0.4, (- 0.4)],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -4, interpolate: true,
  });
  
  gatherResponseText = new visual.TextStim({
    win: psychoJS.window,
    name: 'gatherResponseText',
    text: 'Select the letters in the order presented. Use the blank button to fill in forgotten letters. ',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, 0.4], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  Fbutton = new visual.Rect ({
    win: psychoJS.window, name: 'Fbutton', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0, pos: [(- 0.3), 0.3],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -6, interpolate: true,
  });
  
  F_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'F_text',
    text: 'F',
    font: 'Times New Roman',
    units: undefined, 
    pos: [(- 0.23), 0.3], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -7.0 
  });
  
  Pbutton = new visual.Rect ({
    win: psychoJS.window, name: 'Pbutton', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0, pos: [(- 0.3), 0.2],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -8, interpolate: true,
  });
  
  Qbutton = new visual.Rect ({
    win: psychoJS.window, name: 'Qbutton', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0, pos: [(- 0.3), 0.1],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -9, interpolate: true,
  });
  
  Jbutton = new visual.Rect ({
    win: psychoJS.window, name: 'Jbutton', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0, pos: [(- 0.3), 0.0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -10, interpolate: true,
  });
  
  Hbutton = new visual.Rect ({
    win: psychoJS.window, name: 'Hbutton', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0, pos: [(- 0.3), (- 0.1)],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -11, interpolate: true,
  });
  
  Kbutton = new visual.Rect ({
    win: psychoJS.window, name: 'Kbutton', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0, pos: [(- 0.3), (- 0.2)],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -12, interpolate: true,
  });
  
  Tbutton = new visual.Rect ({
    win: psychoJS.window, name: 'Tbutton', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0, pos: [0.2, 0.3],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -13, interpolate: true,
  });
  
  Sbutton = new visual.Rect ({
    win: psychoJS.window, name: 'Sbutton', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0, pos: [0.2, 0.2],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -14, interpolate: true,
  });
  
  Nbutton = new visual.Rect ({
    win: psychoJS.window, name: 'Nbutton', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0, pos: [0.2, 0.1],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -15, interpolate: true,
  });
  
  Rbutton = new visual.Rect ({
    win: psychoJS.window, name: 'Rbutton', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0, pos: [0.2, 0.0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -16, interpolate: true,
  });
  
  Ybutton = new visual.Rect ({
    win: psychoJS.window, name: 'Ybutton', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0, pos: [0.2, (- 0.1)],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -17, interpolate: true,
  });
  
  Lbutton = new visual.Rect ({
    win: psychoJS.window, name: 'Lbutton', 
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0, pos: [0.2, (- 0.2)],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color(1.0),
    opacity: 1, depth: -18, interpolate: true,
  });
  
  clearButton = new visual.Rect ({
    win: psychoJS.window, name: 'clearButton', 
    width: [0.15, 0.08][0], height: [0.15, 0.08][1],
    ori: 0, pos: [0, (- 0.4)],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -19, interpolate: true,
  });
  
  exitButton = new visual.Rect ({
    win: psychoJS.window, name: 'exitButton', 
    width: [0.15, 0.08][0], height: [0.15, 0.08][1],
    ori: 0, pos: [(- 0.4), (- 0.4)],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -20, interpolate: true,
  });
  
  exitText = new visual.TextStim({
    win: psychoJS.window,
    name: 'exitText',
    text: 'EXIT',
    font: 'Times New Roman',
    units: undefined, 
    pos: [(- 0.4), (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -21.0 
  });
  
  clearText = new visual.TextStim({
    win: psychoJS.window,
    name: 'clearText',
    text: 'CLEAR',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -22.0 
  });
  
  P_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'P_text',
    text: 'P',
    font: 'Times New Roman',
    units: undefined, 
    pos: [(- 0.23), 0.2], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -23.0 
  });
  
  Q_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Q_text',
    text: 'Q',
    font: 'Times New Roman',
    units: undefined, 
    pos: [(- 0.23), 0.1], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -24.0 
  });
  
  J_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'J_text',
    text: 'J',
    font: 'Times New Roman',
    units: undefined, 
    pos: [(- 0.23), 0.0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -25.0 
  });
  
  H_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'H_text',
    text: 'H',
    font: 'Times New Roman',
    units: undefined, 
    pos: [(- 0.23), (- 0.1)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -26.0 
  });
  
  K_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'K_text',
    text: 'K',
    font: 'Times New Roman',
    units: undefined, 
    pos: [(- 0.23), (- 0.2)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -27.0 
  });
  
  T_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'T_text',
    text: 'T',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0.27, 0.3], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -28.0 
  });
  
  S_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'S_text',
    text: 'S',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0.27, 0.2], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -29.0 
  });
  
  N_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'N_text',
    text: 'N',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0.27, 0.1], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -30.0 
  });
  
  R_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'R_text',
    text: 'R',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0.27, 0.0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -31.0 
  });
  
  Y_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Y_text',
    text: 'Y',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0.27, (- 0.1)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -32.0 
  });
  
  L_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'L_text',
    text: 'L',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0.27, (- 0.2)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -33.0 
  });
  
  blankText = new visual.TextStim({
    win: psychoJS.window,
    name: 'blankText',
    text: 'BLANK',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -34.0 
  });
  
  answer1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'answer1',
    text: /*  */
  ,
    font: 'Times New Roman',
    units: undefined, 
    pos: [(- 0.05), (- 0.2)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('grey'),  opacity: 1,
    depth: -35.0 
  });
  
  answer2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'answer2',
    text: /*  */
  ,
    font: 'Times New Roman',
    units: undefined, 
    pos: [0.05, (- 0.2)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('grey'),  opacity: 1,
    depth: -36.0 
  });
  
  mouseBlank = new core.Mouse({
    win: psychoJS.window,
  });
  mouseBlank.mouseClock = new util.Clock();
  // Initialize components for Routine "feedback_2"
  feedback_2Clock = new util.Clock();
  lettersCorrect = new visual.TextStim({
    win: psychoJS.window,
    name: 'lettersCorrect',
    text: 'default text',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, 0.2], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('red'),  opacity: 1,
    depth: 0.0 
  });
  
  correctLetters = 0;
  
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'default text',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  Feedback = new visual.TextStim({
    win: psychoJS.window,
    name: 'Feedback',
    text: 'Feedback',
    font: 'Times New Roman',
    units: undefined, 
    pos: [0, 0.4], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

function TitleScreenRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'TitleScreen'-------
    t = 0;
    TitleScreenClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_1
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    TitleScreenComponents = [];
    TitleScreenComponents.push(introScreen);
    TitleScreenComponents.push(responseIndicator1);
    TitleScreenComponents.push(mouse_1);
    
    for (const thisComponent of TitleScreenComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}

function TitleScreenRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'TitleScreen'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = TitleScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *introScreen* updates
    if (t >= 0.0 && introScreen.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      introScreen.tStart = t;  // (not accounting for frame time here)
      introScreen.frameNStart = frameN;  // exact frame index
      
      introScreen.setAutoDraw(true);
    }

    
    // *responseIndicator1* updates
    if (t >= 0.0 && responseIndicator1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      responseIndicator1.tStart = t;  // (not accounting for frame time here)
      responseIndicator1.frameNStart = frameN;  // exact frame index
      
      responseIndicator1.setAutoDraw(true);
    }

    // *mouse_1* updates
    if (t >= 0.0 && mouse_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_1.tStart = t;  // (not accounting for frame time here)
      mouse_1.frameNStart = frameN;  // exact frame index
      
      mouse_1.status = PsychoJS.Status.STARTED;
      mouse_1.mouseClock.reset();
      prevButtonState = mouse_1.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_1.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_1.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // abort routine on response
          continueRoutine = false;
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of TitleScreenComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function TitleScreenRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'TitleScreen'-------
    for (const thisComponent of TitleScreenComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for thisExp (ExperimentHandler)
    // the Routine "TitleScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function PracticeLetterInstruct1RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'PracticeLetterInstruct1'-------
    t = 0;
    PracticeLetterInstruct1Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_2
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    PracticeLetterInstruct1Components = [];
    PracticeLetterInstruct1Components.push(instr_1);
    PracticeLetterInstruct1Components.push(continue_2);
    PracticeLetterInstruct1Components.push(mouse_2);
    
    for (const thisComponent of PracticeLetterInstruct1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}

function PracticeLetterInstruct1RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'PracticeLetterInstruct1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = PracticeLetterInstruct1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr_1* updates
    if (t >= 0.0 && instr_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_1.tStart = t;  // (not accounting for frame time here)
      instr_1.frameNStart = frameN;  // exact frame index
      
      instr_1.setAutoDraw(true);
    }

    
    // *continue_2* updates
    if (t >= 0.0 && continue_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      continue_2.tStart = t;  // (not accounting for frame time here)
      continue_2.frameNStart = frameN;  // exact frame index
      
      continue_2.setAutoDraw(true);
    }

    // *mouse_2* updates
    if (t >= 0.0 && mouse_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_2.tStart = t;  // (not accounting for frame time here)
      mouse_2.frameNStart = frameN;  // exact frame index
      
      mouse_2.status = PsychoJS.Status.STARTED;
      mouse_2.mouseClock.reset();
      prevButtonState = mouse_2.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_2.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_2.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // abort routine on response
          continueRoutine = false;
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of PracticeLetterInstruct1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function PracticeLetterInstruct1RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'PracticeLetterInstruct1'-------
    for (const thisComponent of PracticeLetterInstruct1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for thisExp (ExperimentHandler)
    // the Routine "PracticeLetterInstruct1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function PracticeLetterInstruct2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'PracticeLetterInstruct2'-------
    t = 0;
    PracticeLetterInstruct2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_3
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    PracticeLetterInstruct2Components = [];
    PracticeLetterInstruct2Components.push(instr_2);
    PracticeLetterInstruct2Components.push(continue_3);
    PracticeLetterInstruct2Components.push(mouse_3);
    
    for (const thisComponent of PracticeLetterInstruct2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}

function PracticeLetterInstruct2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'PracticeLetterInstruct2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = PracticeLetterInstruct2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr_2* updates
    if (t >= 0.0 && instr_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_2.tStart = t;  // (not accounting for frame time here)
      instr_2.frameNStart = frameN;  // exact frame index
      
      instr_2.setAutoDraw(true);
    }

    
    // *continue_3* updates
    if (t >= 0.0 && continue_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      continue_3.tStart = t;  // (not accounting for frame time here)
      continue_3.frameNStart = frameN;  // exact frame index
      
      continue_3.setAutoDraw(true);
    }

    // *mouse_3* updates
    if (t >= 0.0 && mouse_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_3.tStart = t;  // (not accounting for frame time here)
      mouse_3.frameNStart = frameN;  // exact frame index
      
      mouse_3.status = PsychoJS.Status.STARTED;
      mouse_3.mouseClock.reset();
      prevButtonState = mouse_3.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_3.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_3.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // abort routine on response
          continueRoutine = false;
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of PracticeLetterInstruct2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function PracticeLetterInstruct2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'PracticeLetterInstruct2'-------
    for (const thisComponent of PracticeLetterInstruct2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for thisExp (ExperimentHandler)
    // the Routine "PracticeLetterInstruct2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function PracticeLetterInstruct3RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'PracticeLetterInstruct3'-------
    t = 0;
    PracticeLetterInstruct3Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_4
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    PracticeLetterInstruct3Components = [];
    PracticeLetterInstruct3Components.push(instr_3);
    PracticeLetterInstruct3Components.push(continue_4);
    PracticeLetterInstruct3Components.push(mouse_4);
    
    for (const thisComponent of PracticeLetterInstruct3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}

function PracticeLetterInstruct3RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'PracticeLetterInstruct3'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = PracticeLetterInstruct3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr_3* updates
    if (t >= 0.0 && instr_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_3.tStart = t;  // (not accounting for frame time here)
      instr_3.frameNStart = frameN;  // exact frame index
      
      instr_3.setAutoDraw(true);
    }

    
    // *continue_4* updates
    if (t >= 0.0 && continue_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      continue_4.tStart = t;  // (not accounting for frame time here)
      continue_4.frameNStart = frameN;  // exact frame index
      
      continue_4.setAutoDraw(true);
    }

    // *mouse_4* updates
    if (t >= 0.0 && mouse_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_4.tStart = t;  // (not accounting for frame time here)
      mouse_4.frameNStart = frameN;  // exact frame index
      
      mouse_4.status = PsychoJS.Status.STARTED;
      mouse_4.mouseClock.reset();
      prevButtonState = mouse_4.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_4.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_4.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // abort routine on response
          continueRoutine = false;
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of PracticeLetterInstruct3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function PracticeLetterInstruct3RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'PracticeLetterInstruct3'-------
    for (const thisComponent of PracticeLetterInstruct3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for thisExp (ExperimentHandler)
    // the Routine "PracticeLetterInstruct3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function practiceLoopLoopBegin(practiceLoopLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  practiceLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'practiceLetter.xlsx',
    seed: undefined, name: 'practiceLoop'
  });
  psychoJS.experiment.addLoop(practiceLoop); // add the loop to the experiment
  currentLoop = practiceLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisPracticeLoop of practiceLoop) {
    const snapshot = practiceLoop.getSnapshot();
    practiceLoopLoopScheduler.add(importConditions(snapshot));
    practiceLoopLoopScheduler.add(practiceListRoutineBegin(snapshot));
    practiceLoopLoopScheduler.add(practiceListRoutineEachFrame(snapshot));
    practiceLoopLoopScheduler.add(practiceListRoutineEnd(snapshot));
    practiceLoopLoopScheduler.add(practiceRecallRoutineBegin(snapshot));
    practiceLoopLoopScheduler.add(practiceRecallRoutineEachFrame(snapshot));
    practiceLoopLoopScheduler.add(practiceRecallRoutineEnd(snapshot));
    practiceLoopLoopScheduler.add(endLoopIteration(practiceLoopLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}

function practiceLoopLoopEnd() {
  psychoJS.experiment.removeLoop(practiceLoop);

  return Scheduler.Event.NEXT;
}

function practiceSentenceLoopBegin(practiceSentenceLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  practiceSentence = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'sentenceProblems.xlsx',
    seed: undefined, name: 'practiceSentence'
  });
  psychoJS.experiment.addLoop(practiceSentence); // add the loop to the experiment
  currentLoop = practiceSentence;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisPracticeSentence of practiceSentence) {
    const snapshot = practiceSentence.getSnapshot();
    practiceSentenceLoopScheduler.add(importConditions(snapshot));
    practiceSentenceLoopScheduler.add(sentenceRoutineBegin(snapshot));
    practiceSentenceLoopScheduler.add(sentenceRoutineEachFrame(snapshot));
    practiceSentenceLoopScheduler.add(sentenceRoutineEnd(snapshot));
    practiceSentenceLoopScheduler.add(sentenceResponseRoutineBegin(snapshot));
    practiceSentenceLoopScheduler.add(sentenceResponseRoutineEachFrame(snapshot));
    practiceSentenceLoopScheduler.add(sentenceResponseRoutineEnd(snapshot));
    practiceSentenceLoopScheduler.add(feedbackRoutineBegin(snapshot));
    practiceSentenceLoopScheduler.add(feedbackRoutineEachFrame(snapshot));
    practiceSentenceLoopScheduler.add(feedbackRoutineEnd(snapshot));
    practiceSentenceLoopScheduler.add(endLoopIteration(practiceSentenceLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}

function practiceSentenceLoopEnd() {
  psychoJS.experiment.removeLoop(practiceSentence);

  return Scheduler.Event.NEXT;
}

function trialLoopBegin(trialLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trial = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'SentenceProblems2.xlsx',
    seed: undefined, name: 'trial'
  });
  psychoJS.experiment.addLoop(trial); // add the loop to the experiment
  currentLoop = trial;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrial of trial) {
    const snapshot = trial.getSnapshot();
    trialLoopScheduler.add(importConditions(snapshot));
    const sentenceTrialLoopScheduler = new Scheduler(psychoJS);
    trialLoopScheduler.add(sentenceTrialLoopBegin, sentenceTrialLoopScheduler);
    trialLoopScheduler.add(sentenceTrialLoopScheduler);
    trialLoopScheduler.add(sentenceTrialLoopEnd);
    trialLoopScheduler.add(letterTrial_2RoutineBegin(snapshot));
    trialLoopScheduler.add(letterTrial_2RoutineEachFrame(snapshot));
    trialLoopScheduler.add(letterTrial_2RoutineEnd(snapshot));
    trialLoopScheduler.add(practiceRecallRoutineBegin(snapshot));
    trialLoopScheduler.add(practiceRecallRoutineEachFrame(snapshot));
    trialLoopScheduler.add(practiceRecallRoutineEnd(snapshot));
    trialLoopScheduler.add(endLoopIteration(trialLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}

function sentenceTrialLoopBegin(sentenceTrialLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  sentenceTrial = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'sentenceTrial'
  });
  psychoJS.experiment.addLoop(sentenceTrial); // add the loop to the experiment
  currentLoop = sentenceTrial;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisSentenceTrial of sentenceTrial) {
    const snapshot = sentenceTrial.getSnapshot();
    sentenceTrialLoopScheduler.add(importConditions(snapshot));
    sentenceTrialLoopScheduler.add(sentence2RoutineBegin(snapshot));
    sentenceTrialLoopScheduler.add(sentence2RoutineEachFrame(snapshot));
    sentenceTrialLoopScheduler.add(sentence2RoutineEnd(snapshot));
    sentenceTrialLoopScheduler.add(sentenceResponseTrialRoutineBegin(snapshot));
    sentenceTrialLoopScheduler.add(sentenceResponseTrialRoutineEachFrame(snapshot));
    sentenceTrialLoopScheduler.add(sentenceResponseTrialRoutineEnd(snapshot));
    sentenceTrialLoopScheduler.add(endLoopIteration(sentenceTrialLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}

function sentenceTrialLoopEnd() {
  psychoJS.experiment.removeLoop(sentenceTrial);

  return Scheduler.Event.NEXT;
}

function trialLoopEnd() {
  psychoJS.experiment.removeLoop(trial);

  return Scheduler.Event.NEXT;
}

function practiceListRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'practiceList'-------
    t = 0;
    practiceListClock.reset(); // clock
    frameN = -1;
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    letterAppear.setText('');
    letters = ["F", "P", "Q", "J", "H", "K", "T", "S", "N", "R", "Y", "L"];
    firstLetter = choice(letters);
    letters.remove(firstLetter);
    secondLetter = choice(letters);
    letters.append(firstLetter);
    letterAppear.setText(firstLetter);
    letterAppear_2.setText(secondLetter);
    
    // keep track of which components have finished
    practiceListComponents = [];
    practiceListComponents.push(letterAppear);
    practiceListComponents.push(letterAppear_2);
    
    for (const thisComponent of practiceListComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}

function practiceListRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'practiceList'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = practiceListClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *letterAppear* updates
    if (t >= 0.0 && letterAppear.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      letterAppear.tStart = t;  // (not accounting for frame time here)
      letterAppear.frameNStart = frameN;  // exact frame index
      
      letterAppear.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (letterAppear.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      letterAppear.setAutoDraw(false);
    }
    
    // *letterAppear_2* updates
    if (t >= 1.0 && letterAppear_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      letterAppear_2.tStart = t;  // (not accounting for frame time here)
      letterAppear_2.frameNStart = frameN;  // exact frame index
      
      letterAppear_2.setAutoDraw(true);
    }

    frameRemains = 1.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (letterAppear_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      letterAppear_2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of practiceListComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function practiceListRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'practiceList'-------
    for (const thisComponent of practiceListComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}

function practiceRecallRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'practiceRecall'-------
    t = 0;
    practiceRecallClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouseClear
    mouseClear.clicked_name = [];
    gotValidClick = false; // until a click is received
    checkboxes = [Fbutton, Pbutton, Qbutton, Jbutton, Hbutton, Kbutton, Tbutton, Sbutton, Nbutton, Rbutton, Ybutton, Lbutton];
    clicked = [];
    clickedTrack = [];
    timer = new core.Clock();
    timer.reset();
    
    // setup some python lists for storing info about the mouseExit
    // current position of the mouse:
    mouseExit.x = [];
    mouseExit.y = [];
    mouseExit.leftButton = [];
    mouseExit.midButton = [];
    mouseExit.rightButton = [];
    mouseExit.time = [];
    mouseExit.clicked_name = [];
    gotValidClick = false; // until a click is received
    // setup some python lists for storing info about the mouse1
    // current position of the mouse:
    mouse1.x = [];
    mouse1.y = [];
    mouse1.leftButton = [];
    mouse1.midButton = [];
    mouse1.rightButton = [];
    mouse1.time = [];
    mouse1.clicked_name = [];
    gotValidClick = false; // until a click is received
    Fbutton.setFillColor(new util.Color('green'));
    Pbutton.setFillColor(new util.Color('green'));
    Qbutton.setFillColor(new util.Color('green'));
    Jbutton.setFillColor(new util.Color('green'));
    Hbutton.setFillColor(new util.Color('green'));
    Kbutton.setFillColor(new util.Color('green'));
    Tbutton.setFillColor(new util.Color('green'));
    Sbutton.setFillColor(new util.Color('green'));
    Nbutton.setFillColor(new util.Color('green'));
    Rbutton.setFillColor(new util.Color('green'));
    Ybutton.setFillColor(new util.Color('green'));
    Lbutton.setFillColor(new util.Color('green'));
    answer1.setText('');
    answer2.setText('');
    // setup some python lists for storing info about the mouseBlank
    mouseBlank.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    practiceRecallComponents = [];
    practiceRecallComponents.push(mouseClear);
    practiceRecallComponents.push(mouseExit);
    practiceRecallComponents.push(mouse1);
    practiceRecallComponents.push(blankButton);
    practiceRecallComponents.push(gatherResponseText);
    practiceRecallComponents.push(Fbutton);
    practiceRecallComponents.push(F_text);
    practiceRecallComponents.push(Pbutton);
    practiceRecallComponents.push(Qbutton);
    practiceRecallComponents.push(Jbutton);
    practiceRecallComponents.push(Hbutton);
    practiceRecallComponents.push(Kbutton);
    practiceRecallComponents.push(Tbutton);
    practiceRecallComponents.push(Sbutton);
    practiceRecallComponents.push(Nbutton);
    practiceRecallComponents.push(Rbutton);
    practiceRecallComponents.push(Ybutton);
    practiceRecallComponents.push(Lbutton);
    practiceRecallComponents.push(clearButton);
    practiceRecallComponents.push(exitButton);
    practiceRecallComponents.push(exitText);
    practiceRecallComponents.push(clearText);
    practiceRecallComponents.push(P_text);
    practiceRecallComponents.push(Q_text);
    practiceRecallComponents.push(J_text);
    practiceRecallComponents.push(H_text);
    practiceRecallComponents.push(K_text);
    practiceRecallComponents.push(T_text);
    practiceRecallComponents.push(S_text);
    practiceRecallComponents.push(N_text);
    practiceRecallComponents.push(R_text);
    practiceRecallComponents.push(Y_text);
    practiceRecallComponents.push(L_text);
    practiceRecallComponents.push(blankText);
    practiceRecallComponents.push(answer1);
    practiceRecallComponents.push(answer2);
    practiceRecallComponents.push(mouseBlank);
    
    for (const thisComponent of practiceRecallComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}

function practiceRecallRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'practiceRecall'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = practiceRecallClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    if (mouseExit.isPressedIn(exitButton)) {
        continueRoutine = false;
    }
    if ((practiceLoop.finished === false)) {
        if (mouseBlank.isPressedIn(blankButton)) {
            clicked.append(blankButton);
            clickedTrack.append(box);
            answer1.color = "white";
            answer2.color = "white";
            if ((clicked.length === 1)) {
                answer1.setText("Blank");
            } else {
                if ((clicked.length === 2)) {
                    answer2.setText("Blank");
                }
            }
        }
    } else {
        if (mouseBlank.isPressedIn(blankButton)) {
            clicked.append(blankButton);
            clickedTrack.append(box);
            answer1.color = "white";
            if ((clicked.length === 1)) {
                answer1.setText("Blank");
            }
        }
    }
    for (var box, _pj_c = 0, _pj_a = checkboxes, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        box = _pj_a[_pj_c];
        if (((mouse1.isPressedIn(box) && (! _pj.in_es6(box.name, clicked))) && (clicked.length === 0))) {
            box.fillColor = "black";
            clicked.append(box.name);
            clickedTrack.append(box);
            answer1.color = "white";
            if ((box.name === "Fbutton")) {
                answer1.setText("F");
            } else {
                if ((box.name === "Pbutton")) {
                    answer1.setText("P");
                } else {
                    if ((box.name === "Qbutton")) {
                        answer1.setText("Q");
                    } else {
                        if ((box.name === "Jbutton")) {
                            answer1.setText("J");
                        } else {
                            if ((box.name === "Hbutton")) {
                                answer1.setText("H");
                            } else {
                                if ((box.name === "Kbutton")) {
                                    answer1.setText("K");
                                } else {
                                    if ((box.name === "Tbutton")) {
                                        answer1.setText("T");
                                    } else {
                                        if ((box.name === "Sbutton")) {
                                            answer1.setText("S");
                                        } else {
                                            if ((box.name === "Nbutton")) {
                                                answer1.setText("N");
                                            } else {
                                                if ((box.name === "Rbutton")) {
                                                    answer1.setText("R");
                                                } else {
                                                    if ((box.name === "Ybutton")) {
                                                        answer1.setText("Y");
                                                    } else {
                                                        if ((box.name === "Lbutton")) {
                                                            answer1.setText("L");
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    if ((practiceLoop.finished === false)) {
        for (var box, _pj_c = 0, _pj_a = checkboxes, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
            box = _pj_a[_pj_c];
            if (((mouse1.isPressedIn(box) && (! _pj.in_es6(box.name, clicked))) && (clicked.length === 1))) {
                box.fillColor = "black";
                clicked.append(box.name);
                answer2.color = "white";
                clickedTrack.append(box);
                if ((box.name === "Fbutton")) {
                    answer2.setText("F");
                } else {
                    if ((box.name === "Pbutton")) {
                        answer2.setText("P");
                    } else {
                        if ((box.name === "Qbutton")) {
                            answer2.setText("Q");
                        } else {
                            if ((box.name === "Jbutton")) {
                                answer2.setText("J");
                            } else {
                                if ((box.name === "Hbutton")) {
                                    answer2.setText("H");
                                } else {
                                    if ((box.name === "Kbutton")) {
                                        answer2.setText("K");
                                    } else {
                                        if ((box.name === "Tbutton")) {
                                            answer2.setText("T");
                                        } else {
                                            if ((box.name === "Sbutton")) {
                                                answer2.setText("S");
                                            } else {
                                                if ((box.name === "Nbutton")) {
                                                    answer2.setText("N");
                                                } else {
                                                    if ((box.name === "Rbutton")) {
                                                        answer2.setText("R");
                                                    } else {
                                                        if ((box.name === "Ybutton")) {
                                                            answer2.setText("Y");
                                                        } else {
                                                            if ((box.name === "Lbutton")) {
                                                                answer2.setText("L");
                                                            } else {
                                                                if ((box.name === "blankButton")) {
                                                                    answer2.setText("Blank");
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    if (mouseClear.isPressedIn(clearButton)) {
        if ((clicked.length === 1)) {
            if ((clickedTrack[0] !== blankButton)) {
                clickedTrack[0].fillColor = "green";
            }
        }
        answer1.setText("");
        answer2.setText("");
        if ((clicked.length === 2)) {
            if ((clickedTrack[0] !== blankButton)) {
                clickedTrack[0].fillColor = "green";
            }
            if ((clickedTrack[1] !== blankButton)) {
                clickedTrack[1].fillColor = "green";
            }
        }
        clicked = [];
        clickedTrack = [];
    }
    
    // *mouseExit* updates
    if (t >= 0.0 && mouseExit.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouseExit.tStart = t;  // (not accounting for frame time here)
      mouseExit.frameNStart = frameN;  // exact frame index
      
      mouseExit.status = PsychoJS.Status.STARTED;
      mouseExit.mouseClock.reset();
      prevButtonState = mouseExit.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouseExit.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouseExit.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          _mouseXYs = mouseExit.getPos();
          mouseExit.x.push(_mouseXYs[0]);
          mouseExit.y.push(_mouseXYs[1]);
          mouseExit.leftButton.push(_mouseButtons[0]);
          mouseExit.midButton.push(_mouseButtons[1]);
          mouseExit.rightButton.push(_mouseButtons[2]);
          mouseExit.time.push(mouseExit.mouseClock.getTime());
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [exitButton]) {
            if (obj.contains(mouseExit)) {
              gotValidClick = true;
              mouseExit.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // *mouse1* updates
    if (t >= 0.0 && mouse1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse1.tStart = t;  // (not accounting for frame time here)
      mouse1.frameNStart = frameN;  // exact frame index
      
      mouse1.status = PsychoJS.Status.STARTED;
      mouse1.mouseClock.reset();
      prevButtonState = mouse1.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse1.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse1.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          _mouseXYs = mouse1.getPos();
          mouse1.x.push(_mouseXYs[0]);
          mouse1.y.push(_mouseXYs[1]);
          mouse1.leftButton.push(_mouseButtons[0]);
          mouse1.midButton.push(_mouseButtons[1]);
          mouse1.rightButton.push(_mouseButtons[2]);
          mouse1.time.push(mouse1.mouseClock.getTime());
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [Fbutton, Pbutton, Qbutton, Jbutton, Hbutton, Kbutton, Tbutton, Sbutton, Nbutton, Rbutton, Ybutton, Lbutton]) {
            if (obj.contains(mouse1)) {
              gotValidClick = true;
              mouse1.clicked_name.push(obj.name)
            }
          }
        }
      }
    }
    
    // *blankButton* updates
    if (t >= 0.0 && blankButton.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blankButton.tStart = t;  // (not accounting for frame time here)
      blankButton.frameNStart = frameN;  // exact frame index
      
      blankButton.setAutoDraw(true);
    }

    
    // *gatherResponseText* updates
    if (t >= 0.0 && gatherResponseText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      gatherResponseText.tStart = t;  // (not accounting for frame time here)
      gatherResponseText.frameNStart = frameN;  // exact frame index
      
      gatherResponseText.setAutoDraw(true);
    }

    
    // *Fbutton* updates
    if (t >= 0.0 && Fbutton.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Fbutton.tStart = t;  // (not accounting for frame time here)
      Fbutton.frameNStart = frameN;  // exact frame index
      
      Fbutton.setAutoDraw(true);
    }

    
    // *F_text* updates
    if (t >= 0.0 && F_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      F_text.tStart = t;  // (not accounting for frame time here)
      F_text.frameNStart = frameN;  // exact frame index
      
      F_text.setAutoDraw(true);
    }

    
    // *Pbutton* updates
    if (t >= 0.0 && Pbutton.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pbutton.tStart = t;  // (not accounting for frame time here)
      Pbutton.frameNStart = frameN;  // exact frame index
      
      Pbutton.setAutoDraw(true);
    }

    
    // *Qbutton* updates
    if (t >= 0.0 && Qbutton.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Qbutton.tStart = t;  // (not accounting for frame time here)
      Qbutton.frameNStart = frameN;  // exact frame index
      
      Qbutton.setAutoDraw(true);
    }

    
    // *Jbutton* updates
    if (t >= 0.0 && Jbutton.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Jbutton.tStart = t;  // (not accounting for frame time here)
      Jbutton.frameNStart = frameN;  // exact frame index
      
      Jbutton.setAutoDraw(true);
    }

    
    // *Hbutton* updates
    if (t >= 0.0 && Hbutton.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Hbutton.tStart = t;  // (not accounting for frame time here)
      Hbutton.frameNStart = frameN;  // exact frame index
      
      Hbutton.setAutoDraw(true);
    }

    
    // *Kbutton* updates
    if (t >= 0.0 && Kbutton.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Kbutton.tStart = t;  // (not accounting for frame time here)
      Kbutton.frameNStart = frameN;  // exact frame index
      
      Kbutton.setAutoDraw(true);
    }

    
    // *Tbutton* updates
    if (t >= 0.0 && Tbutton.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Tbutton.tStart = t;  // (not accounting for frame time here)
      Tbutton.frameNStart = frameN;  // exact frame index
      
      Tbutton.setAutoDraw(true);
    }

    
    // *Sbutton* updates
    if (t >= 0.0 && Sbutton.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Sbutton.tStart = t;  // (not accounting for frame time here)
      Sbutton.frameNStart = frameN;  // exact frame index
      
      Sbutton.setAutoDraw(true);
    }

    
    // *Nbutton* updates
    if (t >= 0.0 && Nbutton.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Nbutton.tStart = t;  // (not accounting for frame time here)
      Nbutton.frameNStart = frameN;  // exact frame index
      
      Nbutton.setAutoDraw(true);
    }

    
    // *Rbutton* updates
    if (t >= 0.0 && Rbutton.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Rbutton.tStart = t;  // (not accounting for frame time here)
      Rbutton.frameNStart = frameN;  // exact frame index
      
      Rbutton.setAutoDraw(true);
    }

    
    // *Ybutton* updates
    if (t >= 0.0 && Ybutton.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Ybutton.tStart = t;  // (not accounting for frame time here)
      Ybutton.frameNStart = frameN;  // exact frame index
      
      Ybutton.setAutoDraw(true);
    }

    
    // *Lbutton* updates
    if (t >= 0.0 && Lbutton.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Lbutton.tStart = t;  // (not accounting for frame time here)
      Lbutton.frameNStart = frameN;  // exact frame index
      
      Lbutton.setAutoDraw(true);
    }

    
    // *clearButton* updates
    if (t >= 0.0 && clearButton.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      clearButton.tStart = t;  // (not accounting for frame time here)
      clearButton.frameNStart = frameN;  // exact frame index
      
      clearButton.setAutoDraw(true);
    }

    
    // *exitButton* updates
    if (t >= 0.0 && exitButton.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      exitButton.tStart = t;  // (not accounting for frame time here)
      exitButton.frameNStart = frameN;  // exact frame index
      
      exitButton.setAutoDraw(true);
    }

    
    // *exitText* updates
    if (t >= 0.0 && exitText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      exitText.tStart = t;  // (not accounting for frame time here)
      exitText.frameNStart = frameN;  // exact frame index
      
      exitText.setAutoDraw(true);
    }

    
    // *clearText* updates
    if (t >= 0.0 && clearText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      clearText.tStart = t;  // (not accounting for frame time here)
      clearText.frameNStart = frameN;  // exact frame index
      
      clearText.setAutoDraw(true);
    }

    
    // *P_text* updates
    if (t >= 0.0 && P_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      P_text.tStart = t;  // (not accounting for frame time here)
      P_text.frameNStart = frameN;  // exact frame index
      
      P_text.setAutoDraw(true);
    }

    
    // *Q_text* updates
    if (t >= 0.0 && Q_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Q_text.tStart = t;  // (not accounting for frame time here)
      Q_text.frameNStart = frameN;  // exact frame index
      
      Q_text.setAutoDraw(true);
    }

    
    // *J_text* updates
    if (t >= 0.0 && J_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      J_text.tStart = t;  // (not accounting for frame time here)
      J_text.frameNStart = frameN;  // exact frame index
      
      J_text.setAutoDraw(true);
    }

    
    // *H_text* updates
    if (t >= 0.0 && H_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      H_text.tStart = t;  // (not accounting for frame time here)
      H_text.frameNStart = frameN;  // exact frame index
      
      H_text.setAutoDraw(true);
    }

    
    // *K_text* updates
    if (t >= 0.0 && K_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      K_text.tStart = t;  // (not accounting for frame time here)
      K_text.frameNStart = frameN;  // exact frame index
      
      K_text.setAutoDraw(true);
    }

    
    // *T_text* updates
    if (t >= 0.0 && T_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      T_text.tStart = t;  // (not accounting for frame time here)
      T_text.frameNStart = frameN;  // exact frame index
      
      T_text.setAutoDraw(true);
    }

    
    // *S_text* updates
    if (t >= 0.0 && S_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      S_text.tStart = t;  // (not accounting for frame time here)
      S_text.frameNStart = frameN;  // exact frame index
      
      S_text.setAutoDraw(true);
    }

    
    // *N_text* updates
    if (t >= 0.0 && N_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      N_text.tStart = t;  // (not accounting for frame time here)
      N_text.frameNStart = frameN;  // exact frame index
      
      N_text.setAutoDraw(true);
    }

    
    // *R_text* updates
    if (t >= 0.0 && R_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      R_text.tStart = t;  // (not accounting for frame time here)
      R_text.frameNStart = frameN;  // exact frame index
      
      R_text.setAutoDraw(true);
    }

    
    // *Y_text* updates
    if (t >= 0.0 && Y_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Y_text.tStart = t;  // (not accounting for frame time here)
      Y_text.frameNStart = frameN;  // exact frame index
      
      Y_text.setAutoDraw(true);
    }

    
    // *L_text* updates
    if (t >= 0.0 && L_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      L_text.tStart = t;  // (not accounting for frame time here)
      L_text.frameNStart = frameN;  // exact frame index
      
      L_text.setAutoDraw(true);
    }

    
    // *blankText* updates
    if (t >= 0.0 && blankText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blankText.tStart = t;  // (not accounting for frame time here)
      blankText.frameNStart = frameN;  // exact frame index
      
      blankText.setAutoDraw(true);
    }

    
    // *answer1* updates
    if (t >= 0.0 && answer1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      answer1.tStart = t;  // (not accounting for frame time here)
      answer1.frameNStart = frameN;  // exact frame index
      
      answer1.setAutoDraw(true);
    }

    
    // *answer2* updates
    if (t >= 0.0 && answer2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      answer2.tStart = t;  // (not accounting for frame time here)
      answer2.frameNStart = frameN;  // exact frame index
      
      answer2.setAutoDraw(true);
    }

    // *mouseBlank* updates
    if (t >= 0.0 && mouseBlank.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouseBlank.tStart = t;  // (not accounting for frame time here)
      mouseBlank.frameNStart = frameN;  // exact frame index
      
      mouseBlank.status = PsychoJS.Status.STARTED;
      mouseBlank.mouseClock.reset();
      prevButtonState = [0, 0, 0];  // if now button is down we will treat as 'new' click
      }
    if (mouseBlank.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouseBlank.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [blankButton]) {
            if (obj.contains(mouseBlank)) {
              gotValidClick = true;
              mouseBlank.clicked_name.push(obj.name)
            }
          }
          // abort routine on response
          continueRoutine = false;
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of practiceRecallComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function practiceRecallRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'practiceRecall'-------
    for (const thisComponent of practiceRecallComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for thisExp (ExperimentHandler)
    _mouseXYs = mouseClear.getPos();
    _mouseButtons = mouseClear.getPressed();
    psychoJS.experiment.addData('mouseClear.x', _mouseXYs[0]);
    psychoJS.experiment.addData('mouseClear.y', _mouseXYs[1]);
    psychoJS.experiment.addData('mouseClear.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('mouseClear.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('mouseClear.rightButton', _mouseButtons[2]);
    if (mouseClear.clicked_name.length > 0) {
      psychoJS.experiment.addData('mouseClear.clicked_name', mouseClear.clicked_name[0]);}
    /* Syntax Error: Fix Python code */
    // store data for thisExp (ExperimentHandler)
    if (mouseExit.x) {  psychoJS.experiment.addData('mouseExit.x', mouseExit.x[0])};
    if (mouseExit.y) {  psychoJS.experiment.addData('mouseExit.y', mouseExit.y[0])};
    if (mouseExit.leftButton) {  psychoJS.experiment.addData('mouseExit.leftButton', mouseExit.leftButton[0])};
    if (mouseExit.midButton) {  psychoJS.experiment.addData('mouseExit.midButton', mouseExit.midButton[0])};
    if (mouseExit.rightButton) {  psychoJS.experiment.addData('mouseExit.rightButton', mouseExit.rightButton[0])};
    if (mouseExit.time) {  psychoJS.experiment.addData('mouseExit.time', mouseExit.time[0])};
    if (mouseExit.clicked_name) {  psychoJS.experiment.addData('mouseExit.clicked_name', mouseExit.clicked_name[0])};
    
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('mouse1.x', mouse1.x);
    psychoJS.experiment.addData('mouse1.y', mouse1.y);
    psychoJS.experiment.addData('mouse1.leftButton', mouse1.leftButton);
    psychoJS.experiment.addData('mouse1.midButton', mouse1.midButton);
    psychoJS.experiment.addData('mouse1.rightButton', mouse1.rightButton);
    psychoJS.experiment.addData('mouse1.time', mouse1.time);
    psychoJS.experiment.addData('mouse1.clicked_name', mouse1.clicked_name);
    
    // store data for thisExp (ExperimentHandler)
    _mouseXYs = mouseBlank.getPos();
    _mouseButtons = mouseBlank.getPressed();
    psychoJS.experiment.addData('mouseBlank.x', _mouseXYs[0]);
    psychoJS.experiment.addData('mouseBlank.y', _mouseXYs[1]);
    psychoJS.experiment.addData('mouseBlank.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('mouseBlank.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('mouseBlank.rightButton', _mouseButtons[2]);
    if (mouseBlank.clicked_name.length > 0) {
      psychoJS.experiment.addData('mouseBlank.clicked_name', mouseBlank.clicked_name[0]);}
    // the Routine "practiceRecall" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function PractSentInst1RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'PractSentInst1'-------
    t = 0;
    PractSentInst1Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_5
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    PractSentInst1Components = [];
    PractSentInst1Components.push(instr_4);
    PractSentInst1Components.push(continue_5);
    PractSentInst1Components.push(mouse_5);
    
    for (const thisComponent of PractSentInst1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}

function PractSentInst1RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'PractSentInst1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = PractSentInst1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr_4* updates
    if (t >= 0.0 && instr_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_4.tStart = t;  // (not accounting for frame time here)
      instr_4.frameNStart = frameN;  // exact frame index
      
      instr_4.setAutoDraw(true);
    }

    
    // *continue_5* updates
    if (t >= 0.0 && continue_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      continue_5.tStart = t;  // (not accounting for frame time here)
      continue_5.frameNStart = frameN;  // exact frame index
      
      continue_5.setAutoDraw(true);
    }

    // *mouse_5* updates
    if (t >= 0.0 && mouse_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_5.tStart = t;  // (not accounting for frame time here)
      mouse_5.frameNStart = frameN;  // exact frame index
      
      mouse_5.status = PsychoJS.Status.STARTED;
      mouse_5.mouseClock.reset();
      prevButtonState = mouse_5.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_5.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_5.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // abort routine on response
          continueRoutine = false;
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of PractSentInst1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function PractSentInst1RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'PractSentInst1'-------
    for (const thisComponent of PractSentInst1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for thisExp (ExperimentHandler)
    // the Routine "PractSentInst1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function PractSenInst2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'PractSenInst2'-------
    t = 0;
    PractSenInst2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_6
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    PractSenInst2Components = [];
    PractSenInst2Components.push(instr_5);
    PractSenInst2Components.push(continue_6);
    PractSenInst2Components.push(mouse_6);
    
    for (const thisComponent of PractSenInst2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}

function PractSenInst2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'PractSenInst2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = PractSenInst2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr_5* updates
    if (t >= 0.0 && instr_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_5.tStart = t;  // (not accounting for frame time here)
      instr_5.frameNStart = frameN;  // exact frame index
      
      instr_5.setAutoDraw(true);
    }

    
    // *continue_6* updates
    if (t >= 0.0 && continue_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      continue_6.tStart = t;  // (not accounting for frame time here)
      continue_6.frameNStart = frameN;  // exact frame index
      
      continue_6.setAutoDraw(true);
    }

    // *mouse_6* updates
    if (t >= 0.0 && mouse_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_6.tStart = t;  // (not accounting for frame time here)
      mouse_6.frameNStart = frameN;  // exact frame index
      
      mouse_6.status = PsychoJS.Status.STARTED;
      mouse_6.mouseClock.reset();
      prevButtonState = mouse_6.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_6.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_6.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // abort routine on response
          continueRoutine = false;
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of PractSenInst2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function PractSenInst2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'PractSenInst2'-------
    for (const thisComponent of PractSenInst2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for thisExp (ExperimentHandler)
    // the Routine "PractSenInst2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function PracSenInst3RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'PracSenInst3'-------
    t = 0;
    PracSenInst3Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_7
    gotValidClick = false; // until a click is received
    mouse_7.mouseClock.reset();
    // keep track of which components have finished
    PracSenInst3Components = [];
    PracSenInst3Components.push(instr_6);
    PracSenInst3Components.push(continue_7);
    PracSenInst3Components.push(mouse_7);
    
    for (const thisComponent of PracSenInst3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}

function PracSenInst3RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'PracSenInst3'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = PracSenInst3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr_6* updates
    if (t >= 0.0 && instr_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_6.tStart = t;  // (not accounting for frame time here)
      instr_6.frameNStart = frameN;  // exact frame index
      
      instr_6.setAutoDraw(true);
    }

    
    // *continue_7* updates
    if (t >= 0.0 && continue_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      continue_7.tStart = t;  // (not accounting for frame time here)
      continue_7.frameNStart = frameN;  // exact frame index
      
      continue_7.setAutoDraw(true);
    }

    // *mouse_7* updates
    if (t >= 0.0 && mouse_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_7.tStart = t;  // (not accounting for frame time here)
      mouse_7.frameNStart = frameN;  // exact frame index
      
      mouse_7.status = PsychoJS.Status.STARTED;
      prevButtonState = mouse_7.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_7.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_7.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // abort routine on response
          continueRoutine = false;
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of PracSenInst3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function PracSenInst3RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'PracSenInst3'-------
    for (const thisComponent of PracSenInst3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for thisExp (ExperimentHandler)
    // the Routine "PracSenInst3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function sentenceRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'sentence'-------
    t = 0;
    sentenceClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    sentenceText.setText(sentence);
    // setup some python lists for storing info about the mouse
    // current position of the mouse:
    mouse.x = [];
    mouse.y = [];
    mouse.leftButton = [];
    mouse.midButton = [];
    mouse.rightButton = [];
    mouse.time = [];
    gotValidClick = false; // until a click is received
    mouse.mouseClock.reset();
    countingClock = new core.Clock();
    
    // keep track of which components have finished
    sentenceComponents = [];
    sentenceComponents.push(sentenceText);
    sentenceComponents.push(continue_12);
    sentenceComponents.push(mouse);
    sentenceComponents.push(text_3);
    
    for (const thisComponent of sentenceComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}

function sentenceRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'sentence'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = sentenceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *sentenceText* updates
    if (t >= 0.0 && sentenceText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sentenceText.tStart = t;  // (not accounting for frame time here)
      sentenceText.frameNStart = frameN;  // exact frame index
      
      sentenceText.setAutoDraw(true);
    }

    
    // *continue_12* updates
    if (t >= 0.0 && continue_12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      continue_12.tStart = t;  // (not accounting for frame time here)
      continue_12.frameNStart = frameN;  // exact frame index
      
      continue_12.setAutoDraw(true);
    }

    // *mouse* updates
    if (t >= 0.0 && mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse.tStart = t;  // (not accounting for frame time here)
      mouse.frameNStart = frameN;  // exact frame index
      
      mouse.status = PsychoJS.Status.STARTED;
      prevButtonState = mouse.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          _mouseXYs = mouse.getPos();
          mouse.x.push(_mouseXYs[0]);
          mouse.y.push(_mouseXYs[1]);
          mouse.leftButton.push(_mouseButtons[0]);
          mouse.midButton.push(_mouseButtons[1]);
          mouse.rightButton.push(_mouseButtons[2]);
          mouse.time.push(mouse.mouseClock.getTime());
          // abort routine on response
          continueRoutine = false;
        }
      }
    }
    timeRemaining = countingClock.getTime();
    minutes = Number.parseInt((timeRemaining / 60.0));
    tenSeconds = Number.parseInt(((timeRemaining - (minutes * 60)) / 10.0));
    oneSeconds = Number.parseInt((timeRemaining - ((minutes * 60) + (tenSeconds * 10))));
    timeText = (((minutes.toString() + ":") + tenSeconds.toString()) + oneSeconds.toString());
    
    
    // *text_3* updates
    if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }

    
    if (text_3.status === PsychoJS.Status.STARTED){ // only update if being drawn
      text_3.setText('');
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of sentenceComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function sentenceRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'sentence'-------
    for (const thisComponent of sentenceComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for thisExp (ExperimentHandler)
    if (mouse.x) {  psychoJS.experiment.addData('mouse.x', mouse.x[0])};
    if (mouse.y) {  psychoJS.experiment.addData('mouse.y', mouse.y[0])};
    if (mouse.leftButton) {  psychoJS.experiment.addData('mouse.leftButton', mouse.leftButton[0])};
    if (mouse.midButton) {  psychoJS.experiment.addData('mouse.midButton', mouse.midButton[0])};
    if (mouse.rightButton) {  psychoJS.experiment.addData('mouse.rightButton', mouse.rightButton[0])};
    if (mouse.time) {  psychoJS.experiment.addData('mouse.time', mouse.time[0])};
    
    totalTime += countingClock.getTime();
    avgTime = (totalTime / 15);
    
    // the Routine "sentence" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function sentenceResponseRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'sentenceResponse'-------
    t = 0;
    sentenceResponseClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    clicked = 0;
    correct = 0;
    correctText = "";
    trueButton.fillColor = "white";
    falseButton.fillColor = "white";
    timerC = new core.Clock();
    timerC.reset();
    
    trueButton.setFillColor(new util.Color('white'));
    falseButton.setFillColor(new util.Color('white'));
    // setup some python lists for storing info about the mouse12
    // current position of the mouse:
    mouse12.x = [];
    mouse12.y = [];
    mouse12.leftButton = [];
    mouse12.midButton = [];
    mouse12.rightButton = [];
    mouse12.time = [];
    mouse12.clicked_name = [];
    gotValidClick = false; // until a click is received
    mouse12.mouseClock.reset();
    // keep track of which components have finished
    sentenceResponseComponents = [];
    sentenceResponseComponents.push(senseText);
    sentenceResponseComponents.push(trueButton);
    sentenceResponseComponents.push(trueText);
    sentenceResponseComponents.push(falseButton);
    sentenceResponseComponents.push(falseText);
    sentenceResponseComponents.push(mouse12);
    
    for (const thisComponent of sentenceResponseComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}

function sentenceResponseRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'sentenceResponse'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = sentenceResponseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    if (((mouse12.isPressedIn(trueButton) && (CorrectResp === "correct")) && (clicked === 0))) {
        trueButton.fillColor = "green";
        correct = 1;
        totalCorrectPractice += 1;
        clicked = 1;
    } else {
        if (((mouse12.isPressedIn(falseButton) && (CorrectResp === "incorrect")) && (clicked === 0))) {
            trueButton.fillColor = "green";
            correct = 1;
            totalCorrectPractice += 1;
            clicked = 1;
            countdownStarted = true;
        } else {
            if (((mouse12.isPressedIn(trueButton) && (CorrectResp === "incorrect")) && (clicked === 0))) {
                trueButton.fillColor = "green";
                clicked = 1;
                totalCorrectPractice += 0;
                correct = 0;
            } else {
                if (((mouse12.isPressedIn(falseButton) && (CorrectResp === "correct")) && (clicked === 0))) {
                    trueButton.fillColor = "green";
                    clicked = 1;
                    totalCorrectPractice += 0;
                    correct = 0;
                } else {
                    correctText = "";
                    trueButton.fillColor = "white";
                    falseButton.fillColor = "white";
                    clicked = 0;
                    correct = 0;
                }
            }
        }
    }
    
    
    // *senseText* updates
    if (t >= 0.0 && senseText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      senseText.tStart = t;  // (not accounting for frame time here)
      senseText.frameNStart = frameN;  // exact frame index
      
      senseText.setAutoDraw(true);
    }

    
    // *trueButton* updates
    if (t >= 0.0 && trueButton.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trueButton.tStart = t;  // (not accounting for frame time here)
      trueButton.frameNStart = frameN;  // exact frame index
      
      trueButton.setAutoDraw(true);
    }

    
    // *trueText* updates
    if (t >= 0.0 && trueText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trueText.tStart = t;  // (not accounting for frame time here)
      trueText.frameNStart = frameN;  // exact frame index
      
      trueText.setAutoDraw(true);
    }

    
    // *falseButton* updates
    if (t >= 0.0 && falseButton.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      falseButton.tStart = t;  // (not accounting for frame time here)
      falseButton.frameNStart = frameN;  // exact frame index
      
      falseButton.setAutoDraw(true);
    }

    
    // *falseText* updates
    if (t >= 0.0 && falseText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      falseText.tStart = t;  // (not accounting for frame time here)
      falseText.frameNStart = frameN;  // exact frame index
      
      falseText.setAutoDraw(true);
    }

    // *mouse12* updates
    if (t >= 0.0 && mouse12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse12.tStart = t;  // (not accounting for frame time here)
      mouse12.frameNStart = frameN;  // exact frame index
      
      mouse12.status = PsychoJS.Status.STARTED;
      prevButtonState = mouse12.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse12.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse12.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          _mouseXYs = mouse12.getPos();
          mouse12.x.push(_mouseXYs[0]);
          mouse12.y.push(_mouseXYs[1]);
          mouse12.leftButton.push(_mouseButtons[0]);
          mouse12.midButton.push(_mouseButtons[1]);
          mouse12.rightButton.push(_mouseButtons[2]);
          mouse12.time.push(mouse12.mouseClock.getTime());
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [trueButton, falseButton]) {
            if (obj.contains(mouse12)) {
              gotValidClick = true;
              mouse12.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of sentenceResponseComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function sentenceResponseRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'sentenceResponse'-------
    for (const thisComponent of sentenceResponseComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    practiceLoop.addData("routineTime", timerC.getTime());
    if ((correct === 1)) {
        correctText = "Correct!";
    } else {
        if ((correct === 0)) {
            correctText = "Incorrect";
        }
    }
    practiceLoop.addData("correct", correctText);
    
    // store data for thisExp (ExperimentHandler)
    if (mouse12.x) {  psychoJS.experiment.addData('mouse12.x', mouse12.x[0])};
    if (mouse12.y) {  psychoJS.experiment.addData('mouse12.y', mouse12.y[0])};
    if (mouse12.leftButton) {  psychoJS.experiment.addData('mouse12.leftButton', mouse12.leftButton[0])};
    if (mouse12.midButton) {  psychoJS.experiment.addData('mouse12.midButton', mouse12.midButton[0])};
    if (mouse12.rightButton) {  psychoJS.experiment.addData('mouse12.rightButton', mouse12.rightButton[0])};
    if (mouse12.time) {  psychoJS.experiment.addData('mouse12.time', mouse12.time[0])};
    if (mouse12.clicked_name) {  psychoJS.experiment.addData('mouse12.clicked_name', mouse12.clicked_name[0])};
    
    // the Routine "sentenceResponse" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function feedbackRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'feedback'-------
    t = 0;
    feedbackClock.reset(); // clock
    frameN = -1;
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    sentenceFeedback2.setText(correctText);
    // keep track of which components have finished
    feedbackComponents = [];
    feedbackComponents.push(sentenceFeedback2);
    
    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}

function feedbackRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'feedback'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *sentenceFeedback2* updates
    if (t >= 0.0 && sentenceFeedback2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sentenceFeedback2.tStart = t;  // (not accounting for frame time here)
      sentenceFeedback2.frameNStart = frameN;  // exact frame index
      
      sentenceFeedback2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (sentenceFeedback2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      sentenceFeedback2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function feedbackRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'feedback'-------
    for (const thisComponent of feedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    if ((correct === 1)) {
        sentenceFeedback2.setText("Correct!");
    } else {
        if ((correct === 0)) {
            sentenceFeedback2.setText("Incorrect");
        }
    }
    practiceSentence.addData("correctSentence", correct);
    practiceSentence.addData("totalCorrectSentence", totalCorrectPractice);
    
    return Scheduler.Event.NEXT;
  };
}

function RSPANpracticeInstruct1_2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'RSPANpracticeInstruct1_2'-------
    t = 0;
    RSPANpracticeInstruct1_2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_8
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    RSPANpracticeInstruct1_2Components = [];
    RSPANpracticeInstruct1_2Components.push(instr_7);
    RSPANpracticeInstruct1_2Components.push(continue_8);
    RSPANpracticeInstruct1_2Components.push(mouse_8);
    
    for (const thisComponent of RSPANpracticeInstruct1_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}

function RSPANpracticeInstruct1_2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'RSPANpracticeInstruct1_2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = RSPANpracticeInstruct1_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr_7* updates
    if (t >= 0.0 && instr_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_7.tStart = t;  // (not accounting for frame time here)
      instr_7.frameNStart = frameN;  // exact frame index
      
      instr_7.setAutoDraw(true);
    }

    
    // *continue_8* updates
    if (t >= 0.0 && continue_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      continue_8.tStart = t;  // (not accounting for frame time here)
      continue_8.frameNStart = frameN;  // exact frame index
      
      continue_8.setAutoDraw(true);
    }

    // *mouse_8* updates
    if (t >= 0.0 && mouse_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_8.tStart = t;  // (not accounting for frame time here)
      mouse_8.frameNStart = frameN;  // exact frame index
      
      mouse_8.status = PsychoJS.Status.STARTED;
      mouse_8.mouseClock.reset();
      prevButtonState = mouse_8.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_8.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_8.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // abort routine on response
          continueRoutine = false;
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of RSPANpracticeInstruct1_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function RSPANpracticeInstruct1_2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'RSPANpracticeInstruct1_2'-------
    for (const thisComponent of RSPANpracticeInstruct1_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for thisExp (ExperimentHandler)
    // the Routine "RSPANpracticeInstruct1_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function RSPANpracticeInstruct2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'RSPANpracticeInstruct2'-------
    t = 0;
    RSPANpracticeInstruct2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_9
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    RSPANpracticeInstruct2Components = [];
    RSPANpracticeInstruct2Components.push(instr_8);
    RSPANpracticeInstruct2Components.push(continue_9);
    RSPANpracticeInstruct2Components.push(mouse_9);
    
    for (const thisComponent of RSPANpracticeInstruct2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}

function RSPANpracticeInstruct2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'RSPANpracticeInstruct2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = RSPANpracticeInstruct2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr_8* updates
    if (t >= 0.0 && instr_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_8.tStart = t;  // (not accounting for frame time here)
      instr_8.frameNStart = frameN;  // exact frame index
      
      instr_8.setAutoDraw(true);
    }

    
    // *continue_9* updates
    if (t >= 0.0 && continue_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      continue_9.tStart = t;  // (not accounting for frame time here)
      continue_9.frameNStart = frameN;  // exact frame index
      
      continue_9.setAutoDraw(true);
    }

    // *mouse_9* updates
    if (t >= 0.0 && mouse_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_9.tStart = t;  // (not accounting for frame time here)
      mouse_9.frameNStart = frameN;  // exact frame index
      
      mouse_9.status = PsychoJS.Status.STARTED;
      mouse_9.mouseClock.reset();
      prevButtonState = mouse_9.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_9.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_9.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // abort routine on response
          continueRoutine = false;
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of RSPANpracticeInstruct2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function RSPANpracticeInstruct2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'RSPANpracticeInstruct2'-------
    for (const thisComponent of RSPANpracticeInstruct2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for thisExp (ExperimentHandler)
    // the Routine "RSPANpracticeInstruct2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function feedbackinstructRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'feedbackinstruct'-------
    t = 0;
    feedbackinstructClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_10
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    feedbackinstructComponents = [];
    feedbackinstructComponents.push(instr_9);
    feedbackinstructComponents.push(continue_10);
    feedbackinstructComponents.push(mouse_10);
    
    for (const thisComponent of feedbackinstructComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}

function feedbackinstructRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'feedbackinstruct'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = feedbackinstructClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr_9* updates
    if (t >= 0.0 && instr_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_9.tStart = t;  // (not accounting for frame time here)
      instr_9.frameNStart = frameN;  // exact frame index
      
      instr_9.setAutoDraw(true);
    }

    
    // *continue_10* updates
    if (t >= 0.0 && continue_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      continue_10.tStart = t;  // (not accounting for frame time here)
      continue_10.frameNStart = frameN;  // exact frame index
      
      continue_10.setAutoDraw(true);
    }

    // *mouse_10* updates
    if (t >= 0.0 && mouse_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_10.tStart = t;  // (not accounting for frame time here)
      mouse_10.frameNStart = frameN;  // exact frame index
      
      mouse_10.status = PsychoJS.Status.STARTED;
      mouse_10.mouseClock.reset();
      prevButtonState = mouse_10.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_10.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_10.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // abort routine on response
          continueRoutine = false;
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedbackinstructComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function feedbackinstructRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'feedbackinstruct'-------
    for (const thisComponent of feedbackinstructComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for thisExp (ExperimentHandler)
    // the Routine "feedbackinstruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function feedbackinstruct2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'feedbackinstruct2'-------
    t = 0;
    feedbackinstruct2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_11
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    feedbackinstruct2Components = [];
    feedbackinstruct2Components.push(instr_10);
    feedbackinstruct2Components.push(continue_11);
    feedbackinstruct2Components.push(mouse_11);
    
    for (const thisComponent of feedbackinstruct2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}

function feedbackinstruct2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'feedbackinstruct2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = feedbackinstruct2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr_10* updates
    if (t >= 0.0 && instr_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_10.tStart = t;  // (not accounting for frame time here)
      instr_10.frameNStart = frameN;  // exact frame index
      
      instr_10.setAutoDraw(true);
    }

    
    // *continue_11* updates
    if (t >= 0.0 && continue_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      continue_11.tStart = t;  // (not accounting for frame time here)
      continue_11.frameNStart = frameN;  // exact frame index
      
      continue_11.setAutoDraw(true);
    }

    // *mouse_11* updates
    if (t >= 0.0 && mouse_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_11.tStart = t;  // (not accounting for frame time here)
      mouse_11.frameNStart = frameN;  // exact frame index
      
      mouse_11.status = PsychoJS.Status.STARTED;
      mouse_11.mouseClock.reset();
      prevButtonState = mouse_11.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_11.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_11.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // abort routine on response
          continueRoutine = false;
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedbackinstruct2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function feedbackinstruct2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'feedbackinstruct2'-------
    for (const thisComponent of feedbackinstruct2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for thisExp (ExperimentHandler)
    // the Routine "feedbackinstruct2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function sentence2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'sentence2'-------
    t = 0;
    sentence2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    sentenceText2.setText(sentence);
    // setup some python lists for storing info about the mouse_12
    gotValidClick = false; // until a click is received
    countdownClock = new core.CountdownTimer(avgTime);
    
    // keep track of which components have finished
    sentence2Components = [];
    sentence2Components.push(sentenceText2);
    sentence2Components.push(mouse_12);
    sentence2Components.push(continue_13);
    sentence2Components.push(text);
    
    for (const thisComponent of sentence2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}

function sentence2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'sentence2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = sentence2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *sentenceText2* updates
    if (t >= 0.0 && sentenceText2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sentenceText2.tStart = t;  // (not accounting for frame time here)
      sentenceText2.frameNStart = frameN;  // exact frame index
      
      sentenceText2.setAutoDraw(true);
    }

    // *mouse_12* updates
    if (t >= 0.0 && mouse_12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_12.tStart = t;  // (not accounting for frame time here)
      mouse_12.frameNStart = frameN;  // exact frame index
      
      mouse_12.status = PsychoJS.Status.STARTED;
      mouse_12.mouseClock.reset();
      prevButtonState = mouse_12.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_12.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_12.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // abort routine on response
          continueRoutine = false;
        }
      }
    }
    
    // *continue_13* updates
    if (t >= 0.0 && continue_13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      continue_13.tStart = t;  // (not accounting for frame time here)
      continue_13.frameNStart = frameN;  // exact frame index
      
      continue_13.setAutoDraw(true);
    }

    timeRemaining = countdownClock.getTime();
    if ((timeRemaining <= 0.0)) {
        continueRoutine = false;
        sentenceTrial.finished = true;
        continueExperiment = true;
    } else {
        minutes = Number.parseInt((timeRemaining / 60.0));
        tenSeconds = Number.parseInt(((timeRemaining - (minutes * 60)) / 10.0));
        oneSeconds = Number.parseInt((timeRemaining - ((minutes * 60) + (tenSeconds * 10))));
        timeText = (((minutes.toString() + ":") + tenSeconds.toString()) + oneSeconds.toString());
    }
    
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    
    if (text.status === PsychoJS.Status.STARTED){ // only update if being drawn
      text.setText('');
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of sentence2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function sentence2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'sentence2'-------
    for (const thisComponent of sentence2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for thisExp (ExperimentHandler)
    _mouseXYs = mouse_12.getPos();
    _mouseButtons = mouse_12.getPressed();
    psychoJS.experiment.addData('mouse_12.x', _mouseXYs[0]);
    psychoJS.experiment.addData('mouse_12.y', _mouseXYs[1]);
    psychoJS.experiment.addData('mouse_12.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('mouse_12.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('mouse_12.rightButton', _mouseButtons[2]);
    // the Routine "sentence2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function sentenceResponseTrialRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'sentenceResponseTrial'-------
    t = 0;
    sentenceResponseTrialClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    clicked = 0;
    correctText = "";
    trueButton.fillColor = "white";
    falseButton.fillColor = "white";
    timerC = new core.Clock();
    timerC.reset();
    
    trueButton_2.setFillColor(new util.Color('white'));
    falseButton_2.setFillColor(new util.Color('white'));
    // setup some python lists for storing info about the mouse12_2
    // current position of the mouse:
    mouse12_2.x = [];
    mouse12_2.y = [];
    mouse12_2.leftButton = [];
    mouse12_2.midButton = [];
    mouse12_2.rightButton = [];
    mouse12_2.time = [];
    mouse12_2.clicked_name = [];
    gotValidClick = false; // until a click is received
    mouse12_2.mouseClock.reset();
    // keep track of which components have finished
    sentenceResponseTrialComponents = [];
    sentenceResponseTrialComponents.push(senseText_2);
    sentenceResponseTrialComponents.push(trueButton_2);
    sentenceResponseTrialComponents.push(trueText_2);
    sentenceResponseTrialComponents.push(falseButton_2);
    sentenceResponseTrialComponents.push(falseText_2);
    sentenceResponseTrialComponents.push(mouse12_2);
    
    for (const thisComponent of sentenceResponseTrialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}

function sentenceResponseTrialRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'sentenceResponseTrial'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = sentenceResponseTrialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    if (((mouse12.isPressedIn(trueButton) && (CorrectResp === "correct")) && (clicked === 0))) {
        trueButton.fillColor = "green";
        correct = 1;
        totalCorrectSentenceTrial += 1;
        clicked = 1;
    } else {
        if (((mouse12.isPressedIn(falseButton) && (CorrectResp === "incorrect")) && (clicked === 0))) {
            trueButton.fillColor = "green";
            correct = 1;
            totalCorrectSentenceTrial += 1;
            clicked = 1;
            countdownStarted = true;
        } else {
            if (((mouse12.isPressedIn(trueButton) && (CorrectResp === "incorrect")) && (clicked === 0))) {
                trueButton.fillColor = "green";
                clicked = 1;
                totalCorrectSentenceTrial += 0;
                correct = 0;
            } else {
                if (((mouse12.isPressedIn(falseButton) && (CorrectResp === "correct")) && (clicked === 0))) {
                    trueButton.fillColor = "green";
                    clicked = 1;
                    totalCorrectSentenceTrial += 0;
                    correct = 0;
                } else {
                    correctText = "";
                    trueButton.fillColor = "white";
                    falseButton.fillColor = "white";
                    clicked = 0;
                    correct = 0;
                }
            }
        }
    }
    
    
    // *senseText_2* updates
    if (t >= 0.0 && senseText_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      senseText_2.tStart = t;  // (not accounting for frame time here)
      senseText_2.frameNStart = frameN;  // exact frame index
      
      senseText_2.setAutoDraw(true);
    }

    
    // *trueButton_2* updates
    if (t >= 0.0 && trueButton_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trueButton_2.tStart = t;  // (not accounting for frame time here)
      trueButton_2.frameNStart = frameN;  // exact frame index
      
      trueButton_2.setAutoDraw(true);
    }

    
    // *trueText_2* updates
    if (t >= 0.0 && trueText_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trueText_2.tStart = t;  // (not accounting for frame time here)
      trueText_2.frameNStart = frameN;  // exact frame index
      
      trueText_2.setAutoDraw(true);
    }

    
    // *falseButton_2* updates
    if (t >= 0.0 && falseButton_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      falseButton_2.tStart = t;  // (not accounting for frame time here)
      falseButton_2.frameNStart = frameN;  // exact frame index
      
      falseButton_2.setAutoDraw(true);
    }

    
    // *falseText_2* updates
    if (t >= 0.0 && falseText_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      falseText_2.tStart = t;  // (not accounting for frame time here)
      falseText_2.frameNStart = frameN;  // exact frame index
      
      falseText_2.setAutoDraw(true);
    }

    // *mouse12_2* updates
    if (t >= 0.0 && mouse12_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse12_2.tStart = t;  // (not accounting for frame time here)
      mouse12_2.frameNStart = frameN;  // exact frame index
      
      mouse12_2.status = PsychoJS.Status.STARTED;
      prevButtonState = mouse12_2.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse12_2.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse12_2.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          _mouseXYs = mouse12_2.getPos();
          mouse12_2.x.push(_mouseXYs[0]);
          mouse12_2.y.push(_mouseXYs[1]);
          mouse12_2.leftButton.push(_mouseButtons[0]);
          mouse12_2.midButton.push(_mouseButtons[1]);
          mouse12_2.rightButton.push(_mouseButtons[2]);
          mouse12_2.time.push(mouse12_2.mouseClock.getTime());
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [trueButton, falseButton]) {
            if (obj.contains(mouse12_2)) {
              gotValidClick = true;
              mouse12_2.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of sentenceResponseTrialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function sentenceResponseTrialRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'sentenceResponseTrial'-------
    for (const thisComponent of sentenceResponseTrialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    sentenceTrial.addData("totalCorrectSentenceTrial", totalCorrectSentenceTrial);
    practiceSentence.addData("correctSentenceTrial", correct);
    if ((correct === 1)) {
        correctText = "Correct!";
    } else {
        if ((correct === 0)) {
            correctText = "Incorrect";
        }
    }
    sentenceTrial.addData("correct", correctText);
    
    // store data for thisExp (ExperimentHandler)
    if (mouse12_2.x) {  psychoJS.experiment.addData('mouse12_2.x', mouse12_2.x[0])};
    if (mouse12_2.y) {  psychoJS.experiment.addData('mouse12_2.y', mouse12_2.y[0])};
    if (mouse12_2.leftButton) {  psychoJS.experiment.addData('mouse12_2.leftButton', mouse12_2.leftButton[0])};
    if (mouse12_2.midButton) {  psychoJS.experiment.addData('mouse12_2.midButton', mouse12_2.midButton[0])};
    if (mouse12_2.rightButton) {  psychoJS.experiment.addData('mouse12_2.rightButton', mouse12_2.rightButton[0])};
    if (mouse12_2.time) {  psychoJS.experiment.addData('mouse12_2.time', mouse12_2.time[0])};
    if (mouse12_2.clicked_name) {  psychoJS.experiment.addData('mouse12_2.clicked_name', mouse12_2.clicked_name[0])};
    
    // the Routine "sentenceResponseTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function letterTrial_2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'letterTrial_2'-------
    t = 0;
    letterTrial_2Clock.reset(); // clock
    frameN = -1;
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    letterAppear_3.setText('');
    letters = ["F", "P", "Q", "J", "H", "K", "T", "S", "N", "R", "Y", "L"];
    firstLetter = choice(letters);
    letterAppear_3.setText(firstLetter);
    
    // keep track of which components have finished
    letterTrial_2Components = [];
    letterTrial_2Components.push(letterAppear_3);
    
    for (const thisComponent of letterTrial_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}

function letterTrial_2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'letterTrial_2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = letterTrial_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *letterAppear_3* updates
    if (t >= 0.0 && letterAppear_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      letterAppear_3.tStart = t;  // (not accounting for frame time here)
      letterAppear_3.frameNStart = frameN;  // exact frame index
      
      letterAppear_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (letterAppear_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      letterAppear_3.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of letterTrial_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function letterTrial_2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'letterTrial_2'-------
    for (const thisComponent of letterTrial_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}

function feedback_2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'feedback_2'-------
    t = 0;
    feedback_2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    lettersCorrect.setText(percentCorrect);
    lettersRecalled = (((("You recalled " + correctLetters.toString()) + " letters correctly out of ") + 7.toString()) + "letters.");
    percentCorrect = (("Percentage correct: " + (totalCorrectPractice / 12).toString()) + "%");
    
    text_2.setText(lettersRecalled);
    // keep track of which components have finished
    feedback_2Components = [];
    feedback_2Components.push(lettersCorrect);
    feedback_2Components.push(text_2);
    feedback_2Components.push(Feedback);
    
    for (const thisComponent of feedback_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}

function feedback_2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'feedback_2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = feedback_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *lettersCorrect* updates
    if (t >= 0.0 && lettersCorrect.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      lettersCorrect.tStart = t;  // (not accounting for frame time here)
      lettersCorrect.frameNStart = frameN;  // exact frame index
      
      lettersCorrect.setAutoDraw(true);
    }

    lettersRecalled = (((("You recalled " + correctLetters.toString()) + " letters correctly out of ") + 7.toString()) + "letters.");
    percentCorrect = (("Percentage correct: " + (totalCorrectPractice / 12).toString()) + "%");
    
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }

    
    // *Feedback* updates
    if (t >= 0.0 && Feedback.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Feedback.tStart = t;  // (not accounting for frame time here)
      Feedback.frameNStart = frameN;  // exact frame index
      
      Feedback.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedback_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function feedback_2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'feedback_2'-------
    for (const thisComponent of feedback_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "feedback_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}

function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  trials.addData("totalCorrectPractice", totalCorrectPractice);
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
