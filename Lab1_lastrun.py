#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on Juli 24, 2021, at 14:39
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, microphone
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

vorlage = {'de' : "", 'en' : ""}

import sys
sys.coinit_flags = 2
import subprocess
import time
from pywinauto import Application
from pynput.keyboard import Key, Controller

welcome_messages = {'de': "Herzlich willkommen zu unserer EATMAPS-Studie.\n\nBitte drücken Sie die Leertaste, um fortzufahren.", 'en': "Welcome to our EATMAPS-study.\n\nPlease press the space bar to continue."}

sample_beeps_text = {'de' : "Drücken Sie bitte die Leertaste, um den nächsten Piepton zu hören.", 'en' : "Please press the space bar to hear the next beep sound."}
sample_beeps_instruction_text = {'de' : "Sie werden gleich vier Pieptöne hören. Bitten stellen Sie gemeinsam mit dem Experimentator die Kopfhörer auf eine angenehme Lautstärke. \nDrücken Sie die Leertaste, um den ersten Piepton zu hören.", 'en' : "You will hear 4 beep sounds. Please change the volume of your headphones to a niveau that is comfortable to you. The experimenter will help you. \nPress the space bar to hear the first beep sound."}

time_sync_text = {'de': "Um die Sensoren zu synchronisieren, schlagen Sie bitte 3 mal kraftvoll aus Schulterhöhe mit dem Zeigefinger Ihrer nicht-dominanten Hand auf die Leertaste.", 'en' : "To synchronise the sensors, please hit the space bar 3 times forcefully from shoulder height with the index finger of your non-dominant hand."}
time_sync_train_text = {'de': "Um die Sensoren zu synchronisieren, schlagen Sie bitte 3 mal kraftvoll aus Schulterhöhe mit dem Zeigefinger Ihrer nichtdominanten Hand auf die Leertaste. \nDies ist ein Übungsversuch.", 'en' : "To synchronise the sensors, please hit the space bar 3 times forcefully from shoulder height with the index finger of your non-dominant hand. This is a training trial."}

dominant_hand_info = {'de' : "Bitte versuchen Sie, Ihre nicht-dominate Hand auf dem Tisch liegen zu lassen und sie nicht zur Bedienung der Maus oder der Tastatur zu verwenden. \nDrücken Sie die Leertaste um fortzufahren.", 'en' : "Please try to keep your non dominant hand rested on the desk and don't use it to operate the mouse or keyboard. Press the space bar to continue."}

audio_sync_text = {'de' : "Um die Mikrophone zu synchronisieren, klatschen Sie bitte 3 mal laut in die Hände.", 'en' : "To synchronise the microphones, please clap your hands loudly 3 times."}
audio_test_text = {'de' : "Um zu überprüfen, ob Ihre Sprache richtig aufgenommen wird, lesen Sie bitte den folgenden Satz vor. Drücken Sie anschließend bitte die Leertaste.\n\nFranz jagt im komplett verwahrlosten Taxi quer durch Bayern.", 'en' : "To check if your voice is being recorded properly, please read out aloud the following sentence. Please press the space bar afterwards.\n\nThe quick brown fox jumps over the lazy dog."}

video_instruction_text = {'de' : "Auf der nächsten Seite wird Ihnen ein 10-minütiges Video vorgespielt. Schauen Sie sich es an und entspannen Sie sich dabei. \nDrücken Sie die Leertaste um fortzufahren.", 'en' : "On the next page you will see a 10 minute video. Please watch it and relax yourself. \nPress the space bar to start."}

instruction_play_game_text = {'de' : "Auf der nächsten Seite wird ein Spiel erscheinen, das Sie für 25 Minuten spielen können um sich dabei zu entspannen.", 'en' : "On the next screen a game will pop up. Please presss \"Play Now\" and play the game for 25 minutes and relax yourself."}
play_game_text = {'de' : "Bitte spielen Sie das Spiel und entspannen sich dabei.", 'en' : "Please play the game and relax yourself."}
neutral_speech_instruction_text = {'de' : "Als nächstes würden wir Sie bitten, einen Paragraphen auf der folgenden Seite in einem neutralen Tonfall vorzulesen. \n\nDrücken Sie die Leertaste um mit der Aufnahme zu beginnen. Der Paragraph ist über 3 Seiten aufgeteilt. Nachdem Sie eine Seite gelesen haben, drücken Sie bitte die Leertaste, um die nächste Seite anzuzeigen. Drücken Sie erneut die Leertaste, wenn sie fertig sind." ,'en' : "Next we would like you to read a paragraph on the following page in a neutral tone. \n\nPress the space bar to start the recording. The text passage will be segmented across 3 pages. After reading one page, please press the space bar to continue. Press the space bar again when you finished"}
neutral_speech_text = {'de' : ["Einst stritten sich Nordwind und Sonne, wer von ihnen beiden wohl der Stärkere wäre, als ein Wanderer, der in einen warmen Mantel gehüllt war, des Weges daherkam. \nSie wurden einig, dass derjenige für den Stärkeren gelten sollte, der den Wanderer zwingen würde, seinen Mantel abzunehmen.", "Der Nordwind blies mit aller Macht, aber je mehr er blies, desto fester hüllte sich der Wanderer in seinen Mantel ein. \nEndlich gab der Nordwind den Kampf auf.", "Nun erwärmte die Sonne die Luft mit ihren freundlichen Strahlen, und schon nach wenigen Augenblicken zog der Wanderer seinen Mantel aus. \nDa musste der Nordwind zugeben, dass die Sonne von ihnen beiden der Stärkere war."], 'en' : ["The North Wind and the Sun were disputing which was the stronger, when a traveller came along wrapped in a warm cloak. \nThey agreed that the one who first succeeded in making the traveller take his cloak off should be considered stronger than the other.", "Then the North Wind blew as hard as he could, but the more he blew the more closely did the traveller fold his cloak around him; and at last the North Wind gave up the attempt.", "Then the Sun shone out warmly, and immediately the traveller took off his cloak. And so the North Wind was obliged to confess that the Sun was the stronger of the two."]}

emotional_sentence_intro = {'de' : "Als nächstes sollen Sie versuchen, Sätze in geschauspielerten Emotionen zu sprechen. Sie werden den Satz und die Emotion, in welcher dieser geschauspielert werden soll, auf dem Bildschirm sehen. Auf dem Bildschirm können Sie den Satz in Ruhe für sich lesen und wenn Sie bereit sind, können Sie die Aufnahme durch Drücken der Leertaste starten. \nUm die Aufnahme abzuschließen, drücken Sie einfach erneut die Leertaste.", 'en' : "Next, you should try to speak sentences in acted emotions. You will see the sentence and the emotion in which you should act it and record it on one screen. There, you can read it by yourself and when you are ready, start the recording by pressing the space bar. \nTo finish the recording, just press the space bar again."}
emotional_sentence_preview_text = {'de' : "Auf dem nächsten Bildschirm lesen Sie bitte den folgenden Satz vor:", 'en' : "On the next screen, please read the following sentence:"}
act_emotion_text = {'de' : "geschauspielert in der Emotion: ", 'en' : "acted with the emotion: "}
start_recording_text = {'de' : "Drücken Sie bitte die Leertaste, um die Aufnahme zu starten.", 'en' : "Please press the space bar to start the recording."}
stop_recording_text = {'de' : "Drücken Sie bitte die Leertaste, um die Aufnahme abzuschließen.", 'en' : "Please press the space bar to finish the recording."}
emotional_sentence_read_text = {'de' : "\nLesen Sie bitte den folgenden Satz vor:", 'en' : "\nPlease read the following sentence:"}

speaking_vowels_intro = {'de' : "Als nächstes sollen Sie 5 langgezogene Laute artikulieren (z.B. \"Sagen Sie 'a' wie in Tal\"). \nSie werden ein Beispielwort, in welchem der zu sprechende Laut hervorgehoben ist, auf dem Bildschirm sehen. Auf dem Bildschirm können Sie den Laut in Ruhe für sich lesen und wenn Sie bereit sind, können Sie die Aufnahme durch Drücken der Leertaste starten. Um die Aufnahme abzuschließen, drücken Sie einfach erneut die Leertaste. \nArtikulieren Sie den Laut in einer für Sie angenehmen Lautstärke und Tonlage. \nSprechen sie nicht das Beispielwort, artikulieren sie nur den Laut (z.B. 'a').", 'en' : "Next, you should try to speak 5 sustained phonemes. You will see an example-word in which a phoneme is highlighted on one screen (e.g. \"Say 'a' as in father\"). There, you can read the phoneme by yourself and when you are ready, start the recording by pressing the space bar. To finish the recording, just press the space bar again. Utter the phoneme with a loudness and pitch that are comfortable for you. Just say the phoneme sound itself (e.g. 'a'). Don't read the whole example word."}
speaking_vowels_preview1 = {'de' : "Auf dem nächsten Bildschirm artikulieren Sie bitte den folgenden Laut:", 'en' : "On the next screen, please say the following phone:"}
speaking_vowels_preview2 = {'de' : "in einer für Sie angenehmen Lautstärke und Tonlage. Halten Sie den Ton konstant so lange wie möglich in einem Atemzug.\n\nDrücken Sie bitte die Leertaste, um die Aufnahme zu starten.", 'en' : "with a loudness and pitch that is comfortable for you. Hold the sound consistently as long as you can in one breath.\n\nPlease press the space bar to start the recording."}
speaking_vowels = {'de' : "Artikulieren Sie bitte den folgenden Laut:", 'en' : "Please say the following phoneme:"}
stop_vowels_recording = {'de' : "in einer für Sie angenehmen Lautstärke und Tonlage.\nHalten Sie den Ton konstant so lange wie möglich <b>in einem Atemzug</b>.\nDrücken Sie bitte die Leertaste, um die Aufnahme zu abzuschließen.", 'en' : "with a loudness and pitch that is comfortable for you.\nHold the sound consistently as long as you can <b>in one breath</b>.\n\nPlease press the space bar to finish the recording."} 
speaking_vowels_5_secs_preview = {'de' : "in einer für Sie angenehmen Lautstärke und Tonlage.\nHalten Sie den Ton konstant für <b>5 Sekunden</b> bis der Countdown abgelaufen ist.\nDrücken Sie bitte die Leertaste, um die Aufnahme zu starten, welche automatisch nach Ablauf des 5-Sekunden Countdown abgeschlossen wird.", 'en' : "with a loudness and pitch that is comfortable for you.\nHold the sound consistently for <b>5 seconds</b> until the countdown ends.\n\nPlease press the space bar to start the recording, which will be stopped automatically after the 5 second timer."}
speaking_vowels_5_secs = {'de' : "in einer für Sie angenehmen Lautstärke und Tonlage.\nHalten Sie den Ton konstant für <b>5 Sekunden</b> bis der Countdown abgelaufen ist.", 'en' : "with a loudness and pitch that is comfortable for you.\nHold the sound consistently for <b>5 seconds</b> until the countdown ends."}

wait_for_experimenter_text = {'de' : "Warten Sie bitte auf den Experimentator.", 'en' : "Please wait for the experimenter."}
instruction_60_sec_mood_text = {'de' : "Auf dem nächsten Bildschirm werden Sie einen Timer sehen.\nBeschreiben Sie bitte ihre aktuelle Stimmung, sobald der Timer erscheint. Bitte vermeiden Sie es, persönliche und private Details zu erzählen, sondern versuchen Sie eher Ihre aktuellen Gefühle durch ihre Stimme auszudrücken.\nSie haben bis zu 60 Sekunden Zeit. Versuchen Sie bitte für mindestens 30 Sekunden zu sprechen. Sobald Sie fertig sind, drücken Sie bitte die Leertaste um fortzufahren.\n\nSagen Sie bitte dem Experimentator Bescheid, dass er kurz den Raum verlassen soll, während Sie diese Aufnahme machen.\n\nBitte drücken Sie die Leertaste sobald Sie bereit sind.", 'en' : "On the next screen you will see a timer.\nWhen the timer appears, please describe your current mood. Please avoid telling any personal and private details, but rather try to express your current feelings through your voice.\nYou have up to 60 seconds and please try to speak at least for 30 seconds. If you are done, please press the space bar to commence.\n\nPlease tell the experimenter to briefly leave the room while you perform this recording.\n\nPlease press the space bar when you are ready."}
mood_text = {'de' : "Beschreiben Sie bitte Ihre aktuelle Stimmung, sobald der Timer erscheint. Bitte vermeiden Sie es, persönliche und private Details zu erzählen, sondern versuchen Sie eher Ihre aktuellen Gefühle durch ihre Stimme auszudrücken.\nSie haben bis zu 60 Sekunden Zeit. Versuchen Sie bitte für mindestens 30 Sekunden zu sprechen. Sobald Sie fertig sind, drücken Sie bitte die Leertaste um fortzufahren.\n\n\n\n", 'en' : "\nWhen the timer appears, please describe your current mood. Please avoid telling any personal and private details, but rather try to express your current feelings through your voice.\nYou have up to 60 seconds and please try to speak at least for 30 seconds. If you are done, please press the space bar to commence.\n\n\n\n"}
seconds = {'de' : "Sekunden", 'en' : "seconds"}

before_close_eyes_text = {'de' : "Bitte drücken Sie die Leertaste und schließen Sie Ihre Augen für eine Minute, bis Sie einen Piepton hören.", 'en' : "Please press the space bar and close your eyes for one minute until you hear a beep sound."}
close_eyes_text = {'de' : "Bitte halten Sie Ihre Augen geschlossen.", 'en' : "Please keep your eyes closed."}
after_close_eyes_text = {'de' : "Bitte öffnen Sie Ihre Augen und drücken Sie die Leertaste, um fortzufahren.", 'en' : "Please open your eyes and hit the space bar to continue with the next task."}

PANAS_text = {'de' : "Nun möchten wir gerne von Ihnen wissen, wie Sie sich fühlen. Die folgenden Wörter beschreiben unterschiedliche Gefühle und Empfindungen. Lesen Sie jedes Wort und tragen Sie dann in die Skala unter jedem Wort die Intensität ein. Sie haben die Möglichkeit, zwischen fünf Abstufungen zu wählen. Geben Sie bitte an, wie Sie sich im Moment fühlen.", 'en' : "Now we would like to know how you feel. The following words describe different kinds of feelings and perception. Read every word and mark the intensity on the scale. You have the choice between five gradations. Please indicate how you are feeling right now."}

nasa_comparison_text = {'de' : "Klicken Sie auf die Dimension, die den jeweils wichtigeren Beitrag zur Arbeitsbelastung hinsichtlich der Aufgabe darstellt.", 'en' : "Click on the factor that represents the more important contributor to workload for the task."}

affective_slider_instruction_text = {'de' : "Bitte beschreiben Sie Ihre aktuellen Emotionen mit den beiden Slidern. Denken Sie nicht zu viel darüber nach, sondern geben Sie einfach an, wie Sie sich im Moment fühlen. Drücken Sie die Leertaste um fortzufahren.", 'en' : "Please rate your current emotions using both sliders. Don't think too much about it, just rate how you feel at this moment. Press the space bar to continue."}
slider_arousal_text = {'de' : "Bitte markieren Sie, wie aktiv Sie sich fühlen.", 'en' : "Click the slider to rate your level of Arousal."}
slider_pleasure_text = {'de' : "Bitte markieren Sie, wie viel Freude Sie fühlen.", 'en' : "Click the slider to rate your level of Pleasure."}

nback_instruction_text = {'de' : "Bitte lesen Sie die folgenden Anweisungen sorgfältig durch, bevor Sie fortfahren.\n\nAls nächstes werden Sie den sogenannten n-back-Test durchführen. Alle 3 Sekunden wird Ihnen ein Buchstabe vorgesprochen. Gleichzeitig sehen Sie auf Ihrem Bildschirm ein Quadrat in einem 3x3-Raster erscheinen. Ihre Aufgabe ist es, sich sowohl den Buchstaben als auch die Position des Quadrats so gut wie möglich einzuprägen.\n\nWenn ein Buchstabe gesprochen wird und das Quadrat seine Position ändert, drücken Sie die entsprechenden Tasten, um zu reagieren:\n\nDrücken Sie die linke Pfeiltaste auf Ihrer Tastatur, wenn die aktuelle Position des Quadrats mit der Position n (z.B. 2) Positionswechsel vorher übereinstimmt.\n\n\nDrücken Sie die rechte Pfeiltaste auf Ihrer Tastatur, wenn der aktuelle Buchstabe mit dem Buchstaben vor n Positionswechsel übereinstimmt.\n\nManchmal müssen Sie beide Tasten drücken.\nDie Zahl n ändert sich nach jeder Runde abhängig von Ihrer Leistung. Sie ist in der oberen Mitte des Bildschirms zu sehen. Sie beginnen mit einem n von 1. Sie müssen sich also die Position des Quadrats und den Buchstaben des letzten Versuchs merken.\n\nWenn Sie Fragen haben, fragen Sie bitte einen Experimentator. Wenn Sie bereit sind zu beginnen, drücken Sie bitte die Leertaste.", 'en' : "Please read the following instructions carefully, before you continue.\n\nYou will be performing the so called n-back test next. Every 3 seconds, you will hear a letter spoken out. Simultaneously, you will see a square appearing on your screen within a 3x3-grid. Your task is to memorize both the letter and the position of the square as good as you can.\n\nWhen a letter is spoken and the square changes position, press the respective keys to react:\n\nPress the left arrow key on your keyboard, if the current position of the square matches the position n (e.g. 2) changes in position ago.\n\nPress the right arrow key on your keyboard if the current letter matches the letter n changes in position ago.\n\nSometimes you have to press both buttons.\nThe number of n might change after each round depending on your performance. You can be seen at the upper middle of the screen. You will start with an n of 1, so you have to remember the square's position and the letter of the last trial.\n\nIf you have any questions, please ask an experimenter. If you are ready to go, please press the space bar."}
nback_start_text = {'de' : "Nach der Übungsrunde kommt der tatsächliche n-back-Test. Drücken Sie die Leertaste um zu beginnen.\nSie werden den Test für 5 Minuten bearbeiten.", 'en' : "After the practice round, now follows the actual n-back-test for 5 minutes. Please press the space bar to begin."}
nback_practice_text = {'de' : "Sie haben nun die Möglichkeit, den n-back Test für eine Minute auszuprobieren. \n\nDrücken Sie die Leertaste um zu beginnen.", 'en' : "You now have the opportunity to try out the n-back test for one minute. \n\nPress the space bar to begin."}

stroop_instruction_text = {'de' : "Die nächste Aufgabe ist der so genannte Stroop-Test. \n\nAuf dem Bildschirm wird ein Farbname angezeigt. Bitte lesen Sie dieses geschriebene Wort laut vor und ignorieren Sie die Farbe, in der es abgebildet ist. Seien Sie dabei so schnell wie möglich. Drücken Sie die Leertaste, nachdem Sie ein Wort vorgelesen haben. \n\nEs ist wichtig, dass Sie nur das Wort lesen und nicht die Farbe, in der es gedruckt ist, während Sie versuchen so schnell wie möglich zu sein.\n\nAuf der nächsten Seite sehen Sie eine Übersicht aller Farbwörter, die vorkommen werden werden.\n\nDrücken Sie die Leertaste, um fortzufahren.", 'en' : "The next task is the so called Stroop test. \n\nA color name will appear on the screen. Please read aloud that written word and ignore the color, in which it is printed, while being as quickly as possible. Press the space bar after your read a word. \n\nIt is important that you only read the word and not say the color, in which it is printed, while being as fast as possible. \n\nOn the next page, you can see an overview all color words, which will be presented. \n\nPress the space bar to proceed."}
stroop_beep1_text = {'de' : "Drücken Sie die Leertaste, um ein Beispiel für einen tiefen Ton zu höhren.", 'en' : "Press the space bar to hear an example for a low-pitched tone."}
stroop_practice_break_text = {'de' : "Nach der Übungsrunde kommt nun der eigentliche Stroop-Test. Hierbei sollen Sie jeweils 20 Wörter hintereinander wie gehabt vorlesen. Es gibt insgesamt 3 solcher Runden. \n\nDrücken Sie die Leertaste um zu beginnen.", 'en' : "After the practice round, now follows the actual Stroop test. Here you are to read out 20 words after another as before. There are in total 3 of these rounds. \n\nPress the space bar to beginn."}
stroop_before_practice_text = {'de' : "Sie haben nun die Möglichkeit den Stroop-Test in einer Übungsrunde auszuprobieren. \n\nDrücken Sie die Leertaste um zu beginnen.", 'en' : "You now have the opportunity to try out the Stroop test in a practice round. \n\nPress the space bar to beginn."}
short_break_stroop_text = {'de' : "Atmen Sie tief durch. Drücken Sie die Leertaste, um mit der nächsten Runde fortzufahren.", 'en' : "Take a deep breath. Press the space bar to continue with the next round."}
stroop_before_practice_timepressure_text = {'de' : "Als nächstes folgt der Stroop-Test mit Zeitdruck. \n\nLesen Sie bitte wie zuvor das geschriebene Wort laut vor und ignorieren Sie die Farbe, in der es abgebildet ist. Das nächste Wort wird nach sehr kurzer Zeit automatisch erscheinen, versuchen Sie also so schnell wie möglich das aktuelle Wort zu lesen. \n\nDrücken Sie die Leertaste um eine Proberunde zu beginnen.", 'en' : "The next task is the Stroop test with time pressure. \n\nAs before, please read the written word aloud, ignoring the color in which it is shown. The next word will appear automatically after a very short time, so try to read the current word as quickly as possible. \n\nPress the space bar to start a practice round."}
instruction_stroop_timepressure_text = {'de' : "Nach der Übungsrunde kommt nun der eigentliche Stroop-Test mit Zeitdruck. Hierbei sollen Sie jeweils 20 Wörter hintereinander wie gehabt vorlesen. Es gibt insgesamt 3 solcher Runden. \n\nDrücken Sie die Leertaste um zu beginnen.", 'en' : "After the practice round, now follow the actual Stroop test with time pressure. Here you are to read out 20 words after another as before. There are in total 3 of these rounds. \n\nPress the space bar to beginn."}
instruction_stroop_dual_text = {'de' : "Nach der Übungsrunde kommt nun der eigentliche Stroop-Test mit einer Multitasking-Aufgabe. Hierbei sollen Sie jeweils 20 Wörter hintereinander wie gehabt vorlesen. Es gibt insgesamt 3 solcher Runden. \n\nDrücken Sie die Leertaste um zu beginnen.", 'en' : "After the practice round, now follow the actual Stroop test with a multitasking aspect. Here you are to read out 20 words after another as before. There are in total 3 of these rounds. \n\nPress the space bar to beginn."}
stroop_before_practice_dual_text = {'de' : "Als nächstes folgt der Stroop-Test mit einer Multitasking-Aufgabe. \n\nLesen Sie bitte wie zuvor das geschriebene Wort laut vor und ignorieren Sie die Farbe, in der es abgebildet ist. Wie zuvor wird das nächste Wort nach sehr kurzer Zeit automatisch erscheinen. \n\nZusätzlich werden Sie zwei verschiedene Arten von Tönen hören: einen hohen Ton oder einen tiefen Ton. \nZusätzlich zum lauten Aussprechen des geschriebenen Wortes sollen Sie nun auch leise für sich die Anzahl der hohen Töne zählen und diese am Ende jeder Runde angeben. \nEs ist nicht erlaubt, die Töne mit den Fingern zu zählen! \n\nDrücken Sie die Leertaste um ein Beispiel für einen hohen Ton zu hören.", 'en' : "The next task is the Stroop test with a multitasking aspect. \n\nPlease read the written word aloud and ignore the color in which it is displayed. As before, the next word will appear automatically after a very short time. \n\nIn addition, you will hear two different types of tones: a high tone or a low tone. \nAdditional to saying the written word out loud, you should now also silently count by yourself the number of high-pitched tones and enter that number at the end of each round. \nYou are not allowed to use your fingers to count the tones! \n\nPress the space bar to hear an example for a high-pitched tone."}
ask_for_num_high_pitches_text = {'de' : "Bitte geben Sie die Anzahl der hohen Töne ein, die Sie bei der letzten Runde gehört haben und bestätigen Sie Ihre Eingabe mit der Eingabetaste.", 'en' : "Please enter the number of high pitched tones that you heard during the last round and confirm by pressing the enter key."}
color_words = {'de' : ["weiß", "blau", "braun", "schwarz", "grün", "orange", "pink", "lila", "rot", "gelb", "weiß", "blau", "braun", "schwarz", "grün", "orange", "pink", "lila", "rot", "gelb"], 'en' : [ "white", "blue", "brown", "black", "green", "orange", "pink", "purple", "red", "yellow",  "white", "blue", "brown", "black", "green", "orange", "pink", "purple", "red", "yellow"]}

instruction_readingspan_practice_text = {'de' : "Wir beginnen nun mit einem Reading-Span Test. \n\nHierbei sollen Sie \"Blöcke\" abarbeiten, die jeweils aus einer unterschiedlichen Anzahl an Sätzen bestehen. Vor jedem Satz sehen Sie für bis zu 5 Sekunden lang eine Zahl, die Sie sich merken sollen. Nach jedem Block von Sätzen werden Sie aufgefordert werden, die Zahlen, die Sie sich merken sollten, in der Reihenfolge, in der Sie sie gesehen haben, einzugeben. \n\nNachdem Sie die Zahl gesehen haben, sollen Sie den darauffolgenden Satz laut vorlesen. Für jeden Satz sollen Sie entscheiden, ob dieser Sinn macht oder nicht. \nDrücken Sie die rechte Pfeiltaste auf der Tastatur, wenn der Satz für Sie Sinn ergibt, oder drücken Sie die linke Pfeiltaste auf der Tastatur, wenn der Satz für Sie keinen Sinn ergibt.\n\nDrücken Sie die Leertaste, um eine Übungsrunde zu beginnen.", 'en' : "We now begin with a reading span test. \n\nYou will be presented with \"blocks\", each of which consist of a different number of sentences. Before each sentence, for up to 5 seconds, you will see a number, which you should remember. After every block of sentences, we will ask you to type the numbers, which you were asked to memorize, in the order in which you saw them. \n\nAfter seeing the number, you should read aloud the consecutive sentence. For each sentence, you should decide if it makes sense or not. \nPress the right arrow key on the keyboard if the sentence makes sense to you, or press the left arrow key on the keyboard if the sentence does not make sense to you. \n\nPress the space bar to begin a practice round."}
instruction_readingspan_text = {'de' : "Nach der Übungsrunde kommt nun der eigentliche Reading-Span Test. Jede Runde besteht aus Blöcken von jeweils 2 - 5 Sätzen. In jedem Block sollen Sie sich die Zahl, die vor jedem Satz angezeigt wird, merken und anschließend den Satz laut vorlesen und entscheiden, ob dieser Sinn macht oder nicht. \nEs gibt insgesamt 3 solcher Runden. \n\nDrücken Sie die Leertaste um zu beginnen.", 'en' : "After the practice round, now follow the actual reading span test. Each round consists of blocks of 2 - 5 sentences each. In each block, you are supposed to remember the number that is displayed before each sentence and then read out aloud the sentence and decide whether it makes sense or not. \nThere are 3 such rounds in total. \n\nPress the space bar to beginn."}

readingspan_number_text = {'de' : "Merken Sie sich die Zahl! \nDrücken Sie die Leertaste um fortzufahren.", 'en' : "Remember the number!\nPress the space bar or the right arrow to continue!"}
readingspan_sentence_text = {'de' : "Bitte lesen Sie den Satz unten laut vor und entscheiden Sie, ob er wahr oder falsch ist.", 'en' : "Please read the sentence below aloud and decide, if it is true or false."}
readingspan_arrows_text = {'de' : "rechte Pfeiltaste: wahr \t\n linke Pfeiltaste: falsch", 'en' : "right arrow: sentence makes sense \n\t\t left arrow: sentence does not make sense"}
correct = {'de' : "Richtig!", 'en' : "Correct!"}
false = {'de' : "Falsch!", 'en' : "False!"}

readingspan_say_numbers_text = {'de' : "Schreiben Sie die letzten Zahlen in der richtigen Reihenfolge auf. Drücken Sie zwischen den Zahlen Enter.", 'en' : "Please write the last remembered numbers down in the right order! Press the return key after each number!"}
reading_span_feedback_text = {'de' : "\n Die richtige Zahl war ", 'en' : "\n The correct number was "}

eating_message_text = {'de' : "Vielen Dank für Ihre Teilnahme \n\nBitte erholen Sie sich für 20 Minuten und nehmen ein paar Snacks zu sich. Der Experimentator zeigt Ihnen alles. \n\nWenn Sie zurück sind, drücken Sie bitte die Leertaste, um den letzten Fragebogen zu beantworten.", 'en' : "Thank you for participating. \n\nPlease relax yourself for 20 minutes and eat some snacks. The experimenter will show you everything\n\nOnce you are back, please press the space bar to proceed to the last questionnaire."}

dont_move_instruction_text = {'de' : "Bitte drücken Sie die Leertaste und schließen Ihre Augen für 3 Minuten bis Sie einen Piepton hören. Legen Sie Ihre Hände entspannt auf den Tisch. Bitte versuchen Sie, sich in der Zeit nicht zu bewegen.", 'en' : "Please press the space bar and close your eyes for 3 minutes until you hear a beep sound. Put your hands on the table in a relaxed manner. Please do not move your bady too much."}
dont_move_text = {'de' : "Bitte halten Sie Ihre Augen geschlossen und bewegen sich nicht.", 'en' : "Please keep your eyes closed and do not move your body."}

finish_text = {'de' : "Vielen Dank für Ihre Teilnahme! \nSie haben die Studie beendet.", 'en' : "Thank you for participating! \nYou've finished the study!"}


emotions_path = {'de' : "res/de/conditions/emotions.xlsx", 'en' : "res/en/conditions/emotions.xlsx"}
vowels_path = {'de' : "res/de/conditions/vowel_sentences.xlsx", 'en' : "res/en/conditions/vowel_sentences.xlsx"}


emotional_sentences_path = {'de' : "res/de/conditions/emotional_sentences.xlsx", 'en' : "res/en/conditions/emotional_sentences.xlsx"}
stroop_path = {'de' : "res/de/conditions/stroop.xlsx", 'en' : "res/en/conditions/stroop.xlsx"}
POMS_path = {'de' : "res/de/conditions/emotions_questionaire.xlsx", 'en' : "res/en/conditions/emotions_questionaire.xlsx"}
PANAS_path = {'de' : "res/de/conditions/PANAS_questionaire.xlsx", 'en' : "res/en/conditions/PANAS_questionaire.xlsx"}
nasa_path = {'de' : "res/de/conditions/questions_nasa_txl.xlsx", 'en' : "res/en/conditions/questions_nasa_txl.xlsx"}
reading_span_path = {'de' : "res/de/conditions/reading_span.xlsx", 'en' : "res/en/conditions/reading_span.xlsx"}
nasa_comparison_path = {'de' : "res/de/conditions/nasa_comparison.xlsx", 'en' : "res/en/conditions/nasa_comparison.xlsx"}



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'Lab1'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
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
    originPath='C:\\Users\\Public\\Documents\\PsychoPy\\psychopy\\Lab1_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation
wavDirName = filename + '_wav'
if not os.path.isdir(wavDirName):
    os.makedirs(wavDirName)  # to hold .wav files
wavDirName = filename + '_wav'
if not os.path.isdir(wavDirName):
    os.makedirs(wavDirName)  # to hold .wav files
wavDirName = filename + '_wav'
if not os.path.isdir(wavDirName):
    os.makedirs(wavDirName)  # to hold .wav files
wavDirName = filename + '_wav'
if not os.path.isdir(wavDirName):
    os.makedirs(wavDirName)  # to hold .wav files
wavDirName = filename + '_wav'
if not os.path.isdir(wavDirName):
    os.makedirs(wavDirName)  # to hold .wav files
wavDirName = filename + '_wav'
if not os.path.isdir(wavDirName):
    os.makedirs(wavDirName)  # to hold .wav files

# Setup the Window
win = visual.Window(
    size=[1680, 1049], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')

# Enable sound input/output:
microphone.switchOn()
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instruction_texts_configuration_and_imports"
instruction_texts_configuration_and_importsClock = core.Clock()

# Initialize components for Routine "choose_language"
choose_languageClock = core.Clock()
text_15 = visual.TextStim(win=win, name='text_15',
    text='Please choose a language.\n\nPress "D" for german or "E" for englisch.\n\nBitte wählen Sie Ihre Sprache.\n\nDrücken Sie "D" für deutsch oder "E" für Englisch.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_23 = keyboard.Keyboard()

# Initialize components for Routine "welcome_screen"
welcome_screenClock = core.Clock()
welcome_message = visual.TextStim(win=win, name='welcome_message',
    text='',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
next = keyboard.Keyboard()

# Initialize components for Routine "sample_beeps_instruction"
sample_beeps_instructionClock = core.Clock()
key_resp_51 = keyboard.Keyboard()
text_36 = visual.TextStim(win=win, name='text_36',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "sample_beep"
sample_beepClock = core.Clock()
sound_3 = sound.Sound('1000', secs=0.5, stereo=True, hamming=True,
    name='sound_3')
sound_3.setVolume(1.0)

# Initialize components for Routine "sample_beeps_press_space"
sample_beeps_press_spaceClock = core.Clock()
beeps_text = visual.TextStim(win=win, name='beeps_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_50 = keyboard.Keyboard()

# Initialize components for Routine "sample_beep"
sample_beepClock = core.Clock()
sound_3 = sound.Sound('1000', secs=0.5, stereo=True, hamming=True,
    name='sound_3')
sound_3.setVolume(1.0)

# Initialize components for Routine "sample_beeps_press_space"
sample_beeps_press_spaceClock = core.Clock()
beeps_text = visual.TextStim(win=win, name='beeps_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_50 = keyboard.Keyboard()

# Initialize components for Routine "sample_beep_2"
sample_beep_2Clock = core.Clock()
sound_8 = sound.Sound('2000', secs=0.5, stereo=True, hamming=True,
    name='sound_8')
sound_8.setVolume(1.0)

# Initialize components for Routine "time_synchronisation_training"
time_synchronisation_trainingClock = core.Clock()
text_32 = visual.TextStim(win=win, name='text_32',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_37 = keyboard.Keyboard()

# Initialize components for Routine "time_synchronisation"
time_synchronisationClock = core.Clock()
text_9 = visual.TextStim(win=win, name='text_9',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_17 = keyboard.Keyboard()

# Initialize components for Routine "dominant_hand_info"
dominant_hand_infoClock = core.Clock()
text_25 = visual.TextStim(win=win, name='text_25',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_32 = keyboard.Keyboard()

# Initialize components for Routine "audio_test"
audio_testClock = core.Clock()
text_11 = visual.TextStim(win=win, name='text_11',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_20 = keyboard.Keyboard()

# Initialize components for Routine "wait_for_experimenter"
wait_for_experimenterClock = core.Clock()
text_28 = visual.TextStim(win=win, name='text_28',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_35 = keyboard.Keyboard()

# Initialize components for Routine "instruction_video"
instruction_videoClock = core.Clock()
text_35 = visual.TextStim(win=win, name='text_35',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_49 = keyboard.Keyboard()

# Initialize components for Routine "play_video"
play_videoClock = core.Clock()
movie = visual.MovieStim3(
    win=win, name='movie',
    noAudio = False,
    filename='res\\\\video\\\\Beautiful_15min.mp4',
    ori=0.0, pos=(0, 0), opacity=None,
    loop=False,
    size=[1680, 1049],
    depth=0.0,
    )

# Initialize components for Routine "introduction_60_sec_mood"
introduction_60_sec_moodClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='',
    font='Open Sans',
    pos=(0, 0.25), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_12 = keyboard.Keyboard()

# Initialize components for Routine "routine_60_Sec_mood"
routine_60_Sec_moodClock = core.Clock()
mood_voice = visual.TextStim(win=win, name='mood_voice',
    text='',
    font='Arial',
    pos=(0, 0.25), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Timer = visual.TextStim(win=win, name='Timer',
    text='',
    font='Arial',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_11 = keyboard.Keyboard()
recording_image = visual.ImageStim(
    win=win,
    name='recording_image', 
    image='res\\\\img\\\\recording.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# Initialize components for Routine "neutral_speech_instruction"
neutral_speech_instructionClock = core.Clock()
key_resp_25 = keyboard.Keyboard()
text_17 = visual.TextStim(win=win, name='text_17',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "neutral_speech_start_mic"
neutral_speech_start_micClock = core.Clock()

# Initialize components for Routine "neutral_speech_recording"
neutral_speech_recordingClock = core.Clock()
text_18 = visual.TextStim(win=win, name='text_18',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_26 = keyboard.Keyboard()

# Initialize components for Routine "neutral_speech_stop_mic"
neutral_speech_stop_micClock = core.Clock()

# Initialize components for Routine "emotional_sentences_introduction"
emotional_sentences_introductionClock = core.Clock()
emotional_sentence_textfield = visual.TextStim(win=win, name='emotional_sentence_textfield',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_38 = keyboard.Keyboard()

# Initialize components for Routine "emotional_sentence_preview"
emotional_sentence_previewClock = core.Clock()
key_resp_41 = keyboard.Keyboard()
text_37 = visual.TextStim(win=win, name='text_37',
    text='',
    font='Open Sans',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_41 = visual.TextStim(win=win, name='text_41',
    text='',
    font='Open Sans',
    pos=(0, 0.2), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
text_42 = visual.TextStim(win=win, name='text_42',
    text='',
    font='Open Sans',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_43 = visual.TextStim(win=win, name='text_43',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
text_44 = visual.TextStim(win=win, name='text_44',
    text='',
    font='Open Sans',
    pos=(0, -0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "emotional_sentence_recording"
emotional_sentence_recordingClock = core.Clock()
key_resp_42 = keyboard.Keyboard()
text_45 = visual.TextStim(win=win, name='text_45',
    text='',
    font='Open Sans',
    pos=(0, -0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
text_46 = visual.TextStim(win=win, name='text_46',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_47 = visual.TextStim(win=win, name='text_47',
    text='',
    font='Open Sans',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
text_48 = visual.TextStim(win=win, name='text_48',
    text='',
    font='Open Sans',
    pos=(0, 0.2), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
text_49 = visual.TextStim(win=win, name='text_49',
    text='',
    font='Open Sans',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "speaking_vowels_introduction"
speaking_vowels_introductionClock = core.Clock()
text_40 = visual.TextStim(win=win, name='text_40',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_43 = keyboard.Keyboard()

# Initialize components for Routine "phones_as_long_as_possible_preview"
phones_as_long_as_possible_previewClock = core.Clock()
textbox = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(0, 0),     letterHeight=0.05,
     size=None, borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='textbox',
     autoLog=True,
)
key_resp_44 = keyboard.Keyboard()

# Initialize components for Routine "phones_as_long_possible_recording"
phones_as_long_possible_recordingClock = core.Clock()
textbox_2 = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(0, 0),     letterHeight=0.05,
     size=None, borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='textbox_2',
     autoLog=True,
)
key_resp_45 = keyboard.Keyboard()

# Initialize components for Routine "phones_5_secs_preview"
phones_5_secs_previewClock = core.Clock()
textbox_3 = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(0, 0),     letterHeight=0.05,
     size=None, borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='textbox_3',
     autoLog=True,
)
key_resp_46 = keyboard.Keyboard()

# Initialize components for Routine "phones_5_secs_recording"
phones_5_secs_recordingClock = core.Clock()
textbox_4 = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(0, 0.1),     letterHeight=0.05,
     size=None, borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='textbox_4',
     autoLog=True,
)
timer_vowels = visual.TextStim(win=win, name='timer_vowels',
    text='',
    font='Open Sans',
    pos=(0, -0.4), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "before_close_eyes"
before_close_eyesClock = core.Clock()
key_resp_6 = keyboard.Keyboard()
text_12 = visual.TextStim(win=win, name='text_12',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "close_eyes"
close_eyesClock = core.Clock()
text_13 = visual.TextStim(win=win, name='text_13',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
sound_4 = sound.Sound('1000', secs=0.5, stereo=True, hamming=True,
    name='sound_4')
sound_4.setVolume(1.0)

# Initialize components for Routine "after_close_eyes"
after_close_eyesClock = core.Clock()
text_14 = visual.TextStim(win=win, name='text_14',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_22 = keyboard.Keyboard()

# Initialize components for Routine "affective_slider"
affective_sliderClock = core.Clock()
text_29 = visual.TextStim(win=win, name='text_29',
    text='',
    font='Open Sans',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
arousel_slider_3 = visual.Slider(win=win, name='arousel_slider_3',
    size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=["", ""], ticks=(1, 10), granularity=0.0,
    style='slider', styleTweaks=(), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, depth=-1, readOnly=False)
pleasure_slider_3 = visual.Slider(win=win, name='pleasure_slider_3',
    size=(1.0, 0.1), pos=(0, -0.3), units=None,
    labels=["", ""], ticks=(1, 10), granularity=0.0,
    style='slider', styleTweaks=(), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, depth=-2, readOnly=False)
key_resp_36 = keyboard.Keyboard()
arousal_low = visual.ImageStim(
    win=win,
    name='arousal_low', 
    image='res\\\\img\\\\arousal_low.png', mask=None,
    ori=0.0, pos=(-0.6, 0), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
arousal_high = visual.ImageStim(
    win=win,
    name='arousal_high', 
    image='res\\\\img\\\\arousal_high.png', mask=None,
    ori=0.0, pos=(0.6, 0), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
pleasure_low = visual.ImageStim(
    win=win,
    name='pleasure_low', 
    image='res\\\\img\\\\pleasure_low.png', mask=None,
    ori=0.0, pos=(-0.6, -0.3), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
pleasure_high = visual.ImageStim(
    win=win,
    name='pleasure_high', 
    image='res\\\\img\\\\pleasure_high.png', mask=None,
    ori=0.0, pos=(0.6, -0.3), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)

# Initialize components for Routine "questionaire"
questionaireClock = core.Clock()
instructions_questionaire = visual.TextStim(win=win, name='instructions_questionaire',
    text='',
    font='Arial',
    pos=(0, 0.30), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
question_slider = visual.Slider(win=win, name='question_slider',
    size=(1.0, 0.1), pos=(0, -0.2), units=None,
    labels=["not at all", "a little", "moderatly", "quite a bit",  "extremely"], ticks=(1, 2, 3, 4, 5), granularity=1,
    style=['rating'], styleTweaks=(), opacity=1,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='HelveticaBold', labelHeight=0.05,
    flip=False, depth=-2, readOnly=False)
question_text = visual.TextStim(win=win, name='question_text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "questionaire_german"
questionaire_germanClock = core.Clock()
instructions_questionaire_4 = visual.TextStim(win=win, name='instructions_questionaire_4',
    text='',
    font='Arial',
    pos=(0, 0.30), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
question_slider_4 = visual.Slider(win=win, name='question_slider_4',
    size=(1.0, 0.1), pos=(0, -0.2), units=None,
    labels=["gar nicht", "ein bisschen", "einigermaßen", "erheblich", "äußerst"], ticks=(1, 2, 3, 4, 5), granularity=1,
    style=['rating'], styleTweaks=(), opacity=1,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='HelveticaBold', labelHeight=0.03,
    flip=False, depth=-1, readOnly=False)
question_text_4 = visual.TextStim(win=win, name='question_text_4',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "instruction_play_game"
instruction_play_gameClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_47 = keyboard.Keyboard()

# Initialize components for Routine "play_game"
play_gameClock = core.Clock()
play_game_duration = 60*25

# Initialize components for Routine "nasa_txl_questionaire"
nasa_txl_questionaireClock = core.Clock()
instructions_questionaire_2 = visual.TextStim(win=win, name='instructions_questionaire_2',
    text='',
    font='Arial',
    pos=(0, 0.35), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
questionaire_answer = visual.RatingScale(win=win, name='questionaire_answer', stretch = 2,
low = 0,
high = 200,
tickMarks = sorted({i*10 for i in range(21)}),
labels = ['Low', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'High'],
scale = None,
singleClick = True,
showAccept = False)
question_text_2 = visual.TextStim(win=win, name='question_text_2',
    text='',
    font='Arial',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
question_slider = visual.Slider(win=win, name='question_slider',
    size=(1.0, 0.1), pos=(0, -0.2), units=None,
    labels=["not at all", "slightly", "moderately", "very",  "extremely"], ticks=(1, 2, 3, 4, 5),
    granularity=1, style=('rating',),
    color='LightGray', font='HelveticaBold',
    flip=False, labelHeight=0.03)
polygon = visual.Line(
    win=win, name='polygon',
    start=(-(0.025, 0)[0]/2.0, 0), end=(+(0.025, 0)[0]/2.0, 0),
    ori=90, pos=[0,-0.180],
    lineWidth=4,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-4.0, interpolate=True)

# Initialize components for Routine "nasa_txl_questionaire_german"
nasa_txl_questionaire_germanClock = core.Clock()
instructions_questionaire_3 = visual.TextStim(win=win, name='instructions_questionaire_3',
    text='',
    font='Arial',
    pos=(0, 0.35), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
questionaire_answer_2 = visual.RatingScale(win=win, name='questionaire_answer_2', stretch = 2,
low = 0,
high = 200,
tickMarks = sorted({i*10 for i in range(21)}),
labels = ['Gering', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Hoch'],
scale = None,
singleClick = True,
showAccept = False)
question_text_3 = visual.TextStim(win=win, name='question_text_3',
    text='',
    font='Arial',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
question_slider = visual.Slider(win=win, name='question_slider',
    size=(1.0, 0.1), pos=(0, -0.2), units=None,
    labels=["not at all", "slightly", "moderately", "very",  "extremely"], ticks=(1, 2, 3, 4, 5),
    granularity=1, style=('rating',),
    color='LightGray', font='HelveticaBold',
    flip=False, labelHeight=0.03)
polygon_2 = visual.Line(
    win=win, name='polygon_2',
    start=(-(0.025, 0)[0]/2.0, 0), end=(+(0.025, 0)[0]/2.0, 0),
    ori=90, pos=[0,-0.180],
    lineWidth=4,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-4.0, interpolate=True)

# Initialize components for Routine "nasa_txl_comparison"
nasa_txl_comparisonClock = core.Clock()
button_3 = visual.ButtonStim(win, 
   text='', font='Arvo',
   pos=(-0.5, 0.1),
   letterHeight=0.03,
   size=(0.3, 0.1), borderWidth=0.0,
   fillColor='darkgrey', borderColor=None,
   color='white', colorSpace='rgb',
   opacity=None,
   bold=False, italic=False,
   padding=None,
   anchor='center',
   name='button_3')
button_3.buttonClock = core.Clock()
button_4 = visual.ButtonStim(win, 
   text='', font='Arvo',
   pos=(-0.5, -0.2),
   letterHeight=0.03,
   size=(0.3, 0.1), borderWidth=0.0,
   fillColor='darkgrey', borderColor=None,
   color='white', colorSpace='rgb',
   opacity=None,
   bold=False, italic=False,
   padding=None,
   anchor='center',
   name='button_4')
button_4.buttonClock = core.Clock()
nasa_comparison_textf = visual.TextStim(win=win, name='nasa_comparison_textf',
    text='',
    font='Open Sans',
    pos=(0, 0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
description1_textfield = visual.TextStim(win=win, name='description1_textfield',
    text='',
    font='Open Sans',
    pos=(0.2, 0.1), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
description2_textfield = visual.TextStim(win=win, name='description2_textfield',
    text='',
    font='Open Sans',
    pos=(0.2, -0.2), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "affective_slider"
affective_sliderClock = core.Clock()
text_29 = visual.TextStim(win=win, name='text_29',
    text='',
    font='Open Sans',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
arousel_slider_3 = visual.Slider(win=win, name='arousel_slider_3',
    size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=["", ""], ticks=(1, 10), granularity=0.0,
    style='slider', styleTweaks=(), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, depth=-1, readOnly=False)
pleasure_slider_3 = visual.Slider(win=win, name='pleasure_slider_3',
    size=(1.0, 0.1), pos=(0, -0.3), units=None,
    labels=["", ""], ticks=(1, 10), granularity=0.0,
    style='slider', styleTweaks=(), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, depth=-2, readOnly=False)
key_resp_36 = keyboard.Keyboard()
arousal_low = visual.ImageStim(
    win=win,
    name='arousal_low', 
    image='res\\\\img\\\\arousal_low.png', mask=None,
    ori=0.0, pos=(-0.6, 0), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
arousal_high = visual.ImageStim(
    win=win,
    name='arousal_high', 
    image='res\\\\img\\\\arousal_high.png', mask=None,
    ori=0.0, pos=(0.6, 0), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
pleasure_low = visual.ImageStim(
    win=win,
    name='pleasure_low', 
    image='res\\\\img\\\\pleasure_low.png', mask=None,
    ori=0.0, pos=(-0.6, -0.3), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
pleasure_high = visual.ImageStim(
    win=win,
    name='pleasure_high', 
    image='res\\\\img\\\\pleasure_high.png', mask=None,
    ori=0.0, pos=(0.6, -0.3), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)

# Initialize components for Routine "questionaire"
questionaireClock = core.Clock()
instructions_questionaire = visual.TextStim(win=win, name='instructions_questionaire',
    text='',
    font='Arial',
    pos=(0, 0.30), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
question_slider = visual.Slider(win=win, name='question_slider',
    size=(1.0, 0.1), pos=(0, -0.2), units=None,
    labels=["not at all", "a little", "moderatly", "quite a bit",  "extremely"], ticks=(1, 2, 3, 4, 5), granularity=1,
    style=['rating'], styleTweaks=(), opacity=1,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='HelveticaBold', labelHeight=0.05,
    flip=False, depth=-2, readOnly=False)
question_text = visual.TextStim(win=win, name='question_text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "questionaire_german"
questionaire_germanClock = core.Clock()
instructions_questionaire_4 = visual.TextStim(win=win, name='instructions_questionaire_4',
    text='',
    font='Arial',
    pos=(0, 0.30), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
question_slider_4 = visual.Slider(win=win, name='question_slider_4',
    size=(1.0, 0.1), pos=(0, -0.2), units=None,
    labels=["gar nicht", "ein bisschen", "einigermaßen", "erheblich", "äußerst"], ticks=(1, 2, 3, 4, 5), granularity=1,
    style=['rating'], styleTweaks=(), opacity=1,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='HelveticaBold', labelHeight=0.03,
    flip=False, depth=-1, readOnly=False)
question_text_4 = visual.TextStim(win=win, name='question_text_4',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "introduction_60_sec_mood"
introduction_60_sec_moodClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='',
    font='Open Sans',
    pos=(0, 0.25), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_12 = keyboard.Keyboard()

# Initialize components for Routine "routine_60_Sec_mood"
routine_60_Sec_moodClock = core.Clock()
mood_voice = visual.TextStim(win=win, name='mood_voice',
    text='',
    font='Arial',
    pos=(0, 0.25), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Timer = visual.TextStim(win=win, name='Timer',
    text='',
    font='Arial',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_11 = keyboard.Keyboard()
recording_image = visual.ImageStim(
    win=win,
    name='recording_image', 
    image='res\\\\img\\\\recording.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# Initialize components for Routine "neutral_speech_instruction"
neutral_speech_instructionClock = core.Clock()
key_resp_25 = keyboard.Keyboard()
text_17 = visual.TextStim(win=win, name='text_17',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "neutral_speech_start_mic_2"
neutral_speech_start_mic_2Clock = core.Clock()

# Initialize components for Routine "neutral_speech_recording_2"
neutral_speech_recording_2Clock = core.Clock()
text_50 = visual.TextStim(win=win, name='text_50',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_52 = keyboard.Keyboard()

# Initialize components for Routine "neutral_speech_stop_mic_2"
neutral_speech_stop_mic_2Clock = core.Clock()

# Initialize components for Routine "eating_message"
eating_messageClock = core.Clock()
text_finish = visual.TextStim(win=win, name='text_finish',
    text='',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "instruction_dont_move"
instruction_dont_moveClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_48 = keyboard.Keyboard()

# Initialize components for Routine "dont_move_beep"
dont_move_beepClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
sound_1 = sound.Sound('1000', secs=0.5, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(1.0)

# Initialize components for Routine "after_close_eyes"
after_close_eyesClock = core.Clock()
text_14 = visual.TextStim(win=win, name='text_14',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_22 = keyboard.Keyboard()

# Initialize components for Routine "affective_slider"
affective_sliderClock = core.Clock()
text_29 = visual.TextStim(win=win, name='text_29',
    text='',
    font='Open Sans',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
arousel_slider_3 = visual.Slider(win=win, name='arousel_slider_3',
    size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=["", ""], ticks=(1, 10), granularity=0.0,
    style='slider', styleTweaks=(), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, depth=-1, readOnly=False)
pleasure_slider_3 = visual.Slider(win=win, name='pleasure_slider_3',
    size=(1.0, 0.1), pos=(0, -0.3), units=None,
    labels=["", ""], ticks=(1, 10), granularity=0.0,
    style='slider', styleTweaks=(), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, depth=-2, readOnly=False)
key_resp_36 = keyboard.Keyboard()
arousal_low = visual.ImageStim(
    win=win,
    name='arousal_low', 
    image='res\\\\img\\\\arousal_low.png', mask=None,
    ori=0.0, pos=(-0.6, 0), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
arousal_high = visual.ImageStim(
    win=win,
    name='arousal_high', 
    image='res\\\\img\\\\arousal_high.png', mask=None,
    ori=0.0, pos=(0.6, 0), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
pleasure_low = visual.ImageStim(
    win=win,
    name='pleasure_low', 
    image='res\\\\img\\\\pleasure_low.png', mask=None,
    ori=0.0, pos=(-0.6, -0.3), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
pleasure_high = visual.ImageStim(
    win=win,
    name='pleasure_high', 
    image='res\\\\img\\\\pleasure_high.png', mask=None,
    ori=0.0, pos=(0.6, -0.3), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)

# Initialize components for Routine "questionaire"
questionaireClock = core.Clock()
instructions_questionaire = visual.TextStim(win=win, name='instructions_questionaire',
    text='',
    font='Arial',
    pos=(0, 0.30), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
question_slider = visual.Slider(win=win, name='question_slider',
    size=(1.0, 0.1), pos=(0, -0.2), units=None,
    labels=["not at all", "a little", "moderatly", "quite a bit",  "extremely"], ticks=(1, 2, 3, 4, 5), granularity=1,
    style=['rating'], styleTweaks=(), opacity=1,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='HelveticaBold', labelHeight=0.05,
    flip=False, depth=-2, readOnly=False)
question_text = visual.TextStim(win=win, name='question_text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "questionaire_german"
questionaire_germanClock = core.Clock()
instructions_questionaire_4 = visual.TextStim(win=win, name='instructions_questionaire_4',
    text='',
    font='Arial',
    pos=(0, 0.30), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
question_slider_4 = visual.Slider(win=win, name='question_slider_4',
    size=(1.0, 0.1), pos=(0, -0.2), units=None,
    labels=["gar nicht", "ein bisschen", "einigermaßen", "erheblich", "äußerst"], ticks=(1, 2, 3, 4, 5), granularity=1,
    style=['rating'], styleTweaks=(), opacity=1,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='HelveticaBold', labelHeight=0.03,
    flip=False, depth=-1, readOnly=False)
question_text_4 = visual.TextStim(win=win, name='question_text_4',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "finish_message"
finish_messageClock = core.Clock()
text_finished_message = visual.TextStim(win=win, name='text_finished_message',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
end_study = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instruction_texts_configuration_and_imports"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
instruction_texts_configuration_and_importsComponents = []
for thisComponent in instruction_texts_configuration_and_importsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruction_texts_configuration_and_importsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruction_texts_configuration_and_imports"-------
while continueRoutine:
    # get current time
    t = instruction_texts_configuration_and_importsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruction_texts_configuration_and_importsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction_texts_configuration_and_importsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction_texts_configuration_and_imports"-------
for thisComponent in instruction_texts_configuration_and_importsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instruction_texts_configuration_and_imports" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "choose_language"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_23.keys = []
key_resp_23.rt = []
_key_resp_23_allKeys = []
# keep track of which components have finished
choose_languageComponents = [text_15, key_resp_23]
for thisComponent in choose_languageComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
choose_languageClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "choose_language"-------
while continueRoutine:
    # get current time
    t = choose_languageClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=choose_languageClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_15* updates
    if text_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_15.frameNStart = frameN  # exact frame index
        text_15.tStart = t  # local t and not account for scr refresh
        text_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_15, 'tStartRefresh')  # time at next scr refresh
        text_15.setAutoDraw(True)
    
    # *key_resp_23* updates
    waitOnFlip = False
    if key_resp_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_23.frameNStart = frameN  # exact frame index
        key_resp_23.tStart = t  # local t and not account for scr refresh
        key_resp_23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_23, 'tStartRefresh')  # time at next scr refresh
        key_resp_23.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_23.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_23.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_23.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_23.getKeys(keyList=['e', 'd'], waitRelease=False)
        _key_resp_23_allKeys.extend(theseKeys)
        if len(_key_resp_23_allKeys):
            key_resp_23.keys = _key_resp_23_allKeys[-1].name  # just the last key pressed
            key_resp_23.rt = _key_resp_23_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in choose_languageComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "choose_language"-------
for thisComponent in choose_languageComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_15.started', text_15.tStartRefresh)
thisExp.addData('text_15.stopped', text_15.tStopRefresh)
# check responses
if key_resp_23.keys in ['', [], None]:  # No response was made
    key_resp_23.keys = None
thisExp.addData('key_resp_23.keys',key_resp_23.keys)
if key_resp_23.keys != None:  # we had a response
    thisExp.addData('key_resp_23.rt', key_resp_23.rt)
thisExp.addData('key_resp_23.started', key_resp_23.tStartRefresh)
thisExp.addData('key_resp_23.stopped', key_resp_23.tStopRefresh)
thisExp.nextEntry()
if key_resp_23.keys == 'd':
    language = 'de'
else:
    language = 'en'

# the Routine "choose_language" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "welcome_screen"-------
continueRoutine = True
# update component parameters for each repeat
welcome_message.setText(welcome_messages[language])
next.keys = []
next.rt = []
_next_allKeys = []
# keep track of which components have finished
welcome_screenComponents = [welcome_message, next]
for thisComponent in welcome_screenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcome_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcome_screen"-------
while continueRoutine:
    # get current time
    t = welcome_screenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcome_screenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome_message* updates
    if welcome_message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_message.frameNStart = frameN  # exact frame index
        welcome_message.tStart = t  # local t and not account for scr refresh
        welcome_message.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_message, 'tStartRefresh')  # time at next scr refresh
        welcome_message.setAutoDraw(True)
    
    # *next* updates
    waitOnFlip = False
    if next.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next.frameNStart = frameN  # exact frame index
        next.tStart = t  # local t and not account for scr refresh
        next.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next, 'tStartRefresh')  # time at next scr refresh
        next.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(next.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(next.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next.status == STARTED and not waitOnFlip:
        theseKeys = next.getKeys(keyList=['space'], waitRelease=False)
        _next_allKeys.extend(theseKeys)
        if len(_next_allKeys):
            next.keys = _next_allKeys[-1].name  # just the last key pressed
            next.rt = _next_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcome_screenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome_screen"-------
for thisComponent in welcome_screenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('welcome_message.started', welcome_message.tStartRefresh)
thisExp.addData('welcome_message.stopped', welcome_message.tStopRefresh)
# check responses
if next.keys in ['', [], None]:  # No response was made
    next.keys = None
thisExp.addData('next.keys',next.keys)
if next.keys != None:  # we had a response
    thisExp.addData('next.rt', next.rt)
thisExp.addData('next.started', next.tStartRefresh)
thisExp.addData('next.stopped', next.tStopRefresh)
thisExp.nextEntry()
# the Routine "welcome_screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "sample_beeps_instruction"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_51.keys = []
key_resp_51.rt = []
_key_resp_51_allKeys = []
text_36.setText(sample_beeps_instruction_text[language])
# keep track of which components have finished
sample_beeps_instructionComponents = [key_resp_51, text_36]
for thisComponent in sample_beeps_instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
sample_beeps_instructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "sample_beeps_instruction"-------
while continueRoutine:
    # get current time
    t = sample_beeps_instructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=sample_beeps_instructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_51* updates
    waitOnFlip = False
    if key_resp_51.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_51.frameNStart = frameN  # exact frame index
        key_resp_51.tStart = t  # local t and not account for scr refresh
        key_resp_51.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_51, 'tStartRefresh')  # time at next scr refresh
        key_resp_51.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_51.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_51.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_51.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_51.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_51_allKeys.extend(theseKeys)
        if len(_key_resp_51_allKeys):
            key_resp_51.keys = _key_resp_51_allKeys[-1].name  # just the last key pressed
            key_resp_51.rt = _key_resp_51_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_36* updates
    if text_36.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_36.frameNStart = frameN  # exact frame index
        text_36.tStart = t  # local t and not account for scr refresh
        text_36.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_36, 'tStartRefresh')  # time at next scr refresh
        text_36.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in sample_beeps_instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "sample_beeps_instruction"-------
for thisComponent in sample_beeps_instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_51.keys in ['', [], None]:  # No response was made
    key_resp_51.keys = None
thisExp.addData('key_resp_51.keys',key_resp_51.keys)
if key_resp_51.keys != None:  # we had a response
    thisExp.addData('key_resp_51.rt', key_resp_51.rt)
thisExp.addData('key_resp_51.started', key_resp_51.tStartRefresh)
thisExp.addData('key_resp_51.stopped', key_resp_51.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_36.started', text_36.tStartRefresh)
thisExp.addData('text_36.stopped', text_36.tStopRefresh)
# the Routine "sample_beeps_instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "sample_beep"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
sound_3.setSound('1000', secs=0.5, hamming=True)
sound_3.setVolume(1.0, log=False)
# keep track of which components have finished
sample_beepComponents = [sound_3]
for thisComponent in sample_beepComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
sample_beepClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "sample_beep"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = sample_beepClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=sample_beepClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop sound_3
    if sound_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sound_3.frameNStart = frameN  # exact frame index
        sound_3.tStart = t  # local t and not account for scr refresh
        sound_3.tStartRefresh = tThisFlipGlobal  # on global time
        sound_3.play(when=win)  # sync with win flip
    if sound_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > sound_3.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            sound_3.tStop = t  # not accounting for scr refresh
            sound_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(sound_3, 'tStopRefresh')  # time at next scr refresh
            sound_3.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in sample_beepComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "sample_beep"-------
for thisComponent in sample_beepComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_3.stop()  # ensure sound has stopped at end of routine
thisExp.addData('sound_3.started', sound_3.tStartRefresh)
thisExp.addData('sound_3.stopped', sound_3.tStopRefresh)

# ------Prepare to start Routine "sample_beeps_press_space"-------
continueRoutine = True
# update component parameters for each repeat
beeps_text.setText(sample_beeps_text[language])
key_resp_50.keys = []
key_resp_50.rt = []
_key_resp_50_allKeys = []
# keep track of which components have finished
sample_beeps_press_spaceComponents = [beeps_text, key_resp_50]
for thisComponent in sample_beeps_press_spaceComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
sample_beeps_press_spaceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "sample_beeps_press_space"-------
while continueRoutine:
    # get current time
    t = sample_beeps_press_spaceClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=sample_beeps_press_spaceClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *beeps_text* updates
    if beeps_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        beeps_text.frameNStart = frameN  # exact frame index
        beeps_text.tStart = t  # local t and not account for scr refresh
        beeps_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(beeps_text, 'tStartRefresh')  # time at next scr refresh
        beeps_text.setAutoDraw(True)
    
    # *key_resp_50* updates
    waitOnFlip = False
    if key_resp_50.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_50.frameNStart = frameN  # exact frame index
        key_resp_50.tStart = t  # local t and not account for scr refresh
        key_resp_50.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_50, 'tStartRefresh')  # time at next scr refresh
        key_resp_50.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_50.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_50.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_50.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_50.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_50_allKeys.extend(theseKeys)
        if len(_key_resp_50_allKeys):
            key_resp_50.keys = _key_resp_50_allKeys[-1].name  # just the last key pressed
            key_resp_50.rt = _key_resp_50_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in sample_beeps_press_spaceComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "sample_beeps_press_space"-------
for thisComponent in sample_beeps_press_spaceComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('beeps_text.started', beeps_text.tStartRefresh)
thisExp.addData('beeps_text.stopped', beeps_text.tStopRefresh)
# check responses
if key_resp_50.keys in ['', [], None]:  # No response was made
    key_resp_50.keys = None
thisExp.addData('key_resp_50.keys',key_resp_50.keys)
if key_resp_50.keys != None:  # we had a response
    thisExp.addData('key_resp_50.rt', key_resp_50.rt)
thisExp.addData('key_resp_50.started', key_resp_50.tStartRefresh)
thisExp.addData('key_resp_50.stopped', key_resp_50.tStopRefresh)
thisExp.nextEntry()
# the Routine "sample_beeps_press_space" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "sample_beep"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
sound_3.setSound('1000', secs=0.5, hamming=True)
sound_3.setVolume(1.0, log=False)
# keep track of which components have finished
sample_beepComponents = [sound_3]
for thisComponent in sample_beepComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
sample_beepClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "sample_beep"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = sample_beepClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=sample_beepClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop sound_3
    if sound_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sound_3.frameNStart = frameN  # exact frame index
        sound_3.tStart = t  # local t and not account for scr refresh
        sound_3.tStartRefresh = tThisFlipGlobal  # on global time
        sound_3.play(when=win)  # sync with win flip
    if sound_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > sound_3.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            sound_3.tStop = t  # not accounting for scr refresh
            sound_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(sound_3, 'tStopRefresh')  # time at next scr refresh
            sound_3.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in sample_beepComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "sample_beep"-------
for thisComponent in sample_beepComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_3.stop()  # ensure sound has stopped at end of routine
thisExp.addData('sound_3.started', sound_3.tStartRefresh)
thisExp.addData('sound_3.stopped', sound_3.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=2.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_4')
thisExp.addLoop(trials_4)  # add the loop to the experiment
thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
if thisTrial_4 != None:
    for paramName in thisTrial_4:
        exec('{} = thisTrial_4[paramName]'.format(paramName))

for thisTrial_4 in trials_4:
    currentLoop = trials_4
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            exec('{} = thisTrial_4[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "sample_beeps_press_space"-------
    continueRoutine = True
    # update component parameters for each repeat
    beeps_text.setText(sample_beeps_text[language])
    key_resp_50.keys = []
    key_resp_50.rt = []
    _key_resp_50_allKeys = []
    # keep track of which components have finished
    sample_beeps_press_spaceComponents = [beeps_text, key_resp_50]
    for thisComponent in sample_beeps_press_spaceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    sample_beeps_press_spaceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "sample_beeps_press_space"-------
    while continueRoutine:
        # get current time
        t = sample_beeps_press_spaceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=sample_beeps_press_spaceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *beeps_text* updates
        if beeps_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            beeps_text.frameNStart = frameN  # exact frame index
            beeps_text.tStart = t  # local t and not account for scr refresh
            beeps_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(beeps_text, 'tStartRefresh')  # time at next scr refresh
            beeps_text.setAutoDraw(True)
        
        # *key_resp_50* updates
        waitOnFlip = False
        if key_resp_50.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_50.frameNStart = frameN  # exact frame index
            key_resp_50.tStart = t  # local t and not account for scr refresh
            key_resp_50.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_50, 'tStartRefresh')  # time at next scr refresh
            key_resp_50.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_50.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_50.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_50.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_50.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_50_allKeys.extend(theseKeys)
            if len(_key_resp_50_allKeys):
                key_resp_50.keys = _key_resp_50_allKeys[-1].name  # just the last key pressed
                key_resp_50.rt = _key_resp_50_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sample_beeps_press_spaceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "sample_beeps_press_space"-------
    for thisComponent in sample_beeps_press_spaceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_4.addData('beeps_text.started', beeps_text.tStartRefresh)
    trials_4.addData('beeps_text.stopped', beeps_text.tStopRefresh)
    # check responses
    if key_resp_50.keys in ['', [], None]:  # No response was made
        key_resp_50.keys = None
    trials_4.addData('key_resp_50.keys',key_resp_50.keys)
    if key_resp_50.keys != None:  # we had a response
        trials_4.addData('key_resp_50.rt', key_resp_50.rt)
    trials_4.addData('key_resp_50.started', key_resp_50.tStartRefresh)
    trials_4.addData('key_resp_50.stopped', key_resp_50.tStopRefresh)
    # the Routine "sample_beeps_press_space" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "sample_beep_2"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    sound_8.setSound('2000', secs=0.5, hamming=True)
    sound_8.setVolume(1.0, log=False)
    # keep track of which components have finished
    sample_beep_2Components = [sound_8]
    for thisComponent in sample_beep_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    sample_beep_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "sample_beep_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = sample_beep_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=sample_beep_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_8
        if sound_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_8.frameNStart = frameN  # exact frame index
            sound_8.tStart = t  # local t and not account for scr refresh
            sound_8.tStartRefresh = tThisFlipGlobal  # on global time
            sound_8.play(when=win)  # sync with win flip
        if sound_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_8.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                sound_8.tStop = t  # not accounting for scr refresh
                sound_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_8, 'tStopRefresh')  # time at next scr refresh
                sound_8.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sample_beep_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "sample_beep_2"-------
    for thisComponent in sample_beep_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_8.stop()  # ensure sound has stopped at end of routine
    trials_4.addData('sound_8.started', sound_8.tStartRefresh)
    trials_4.addData('sound_8.stopped', sound_8.tStopRefresh)
# completed 2.0 repeats of 'trials_4'


# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=3.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "time_synchronisation_training"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_32.setText(time_sync_train_text[language])
    key_resp_37.keys = []
    key_resp_37.rt = []
    _key_resp_37_allKeys = []
    # keep track of which components have finished
    time_synchronisation_trainingComponents = [text_32, key_resp_37]
    for thisComponent in time_synchronisation_trainingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    time_synchronisation_trainingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "time_synchronisation_training"-------
    while continueRoutine:
        # get current time
        t = time_synchronisation_trainingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=time_synchronisation_trainingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_32* updates
        if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_32.frameNStart = frameN  # exact frame index
            text_32.tStart = t  # local t and not account for scr refresh
            text_32.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
            text_32.setAutoDraw(True)
        
        # *key_resp_37* updates
        waitOnFlip = False
        if key_resp_37.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_37.frameNStart = frameN  # exact frame index
            key_resp_37.tStart = t  # local t and not account for scr refresh
            key_resp_37.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_37, 'tStartRefresh')  # time at next scr refresh
            key_resp_37.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_37.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_37.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_37.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_37.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_37_allKeys.extend(theseKeys)
            if len(_key_resp_37_allKeys):
                key_resp_37.keys = _key_resp_37_allKeys[-1].name  # just the last key pressed
                key_resp_37.rt = _key_resp_37_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in time_synchronisation_trainingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "time_synchronisation_training"-------
    for thisComponent in time_synchronisation_trainingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('text_32.started', text_32.tStartRefresh)
    trials_2.addData('text_32.stopped', text_32.tStopRefresh)
    # check responses
    if key_resp_37.keys in ['', [], None]:  # No response was made
        key_resp_37.keys = None
    trials_2.addData('key_resp_37.keys',key_resp_37.keys)
    if key_resp_37.keys != None:  # we had a response
        trials_2.addData('key_resp_37.rt', key_resp_37.rt)
    trials_2.addData('key_resp_37.started', key_resp_37.tStartRefresh)
    trials_2.addData('key_resp_37.stopped', key_resp_37.tStopRefresh)
    # the Routine "time_synchronisation_training" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 3.0 repeats of 'trials_2'

# get names of stimulus parameters
if trials_2.trialList in ([], [None], None):
    params = []
else:
    params = trials_2.trialList[0].keys()
# save data for this loop
trials_2.saveAsExcel(filename + '.xlsx', sheetName='trials_2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials_2.saveAsText(filename + 'trials_2.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=3.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "time_synchronisation"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_9.setText(time_sync_text[language])
    key_resp_17.keys = []
    key_resp_17.rt = []
    _key_resp_17_allKeys = []
    # keep track of which components have finished
    time_synchronisationComponents = [text_9, key_resp_17]
    for thisComponent in time_synchronisationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    time_synchronisationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "time_synchronisation"-------
    while continueRoutine:
        # get current time
        t = time_synchronisationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=time_synchronisationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_9* updates
        if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_9.frameNStart = frameN  # exact frame index
            text_9.tStart = t  # local t and not account for scr refresh
            text_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
            text_9.setAutoDraw(True)
        
        # *key_resp_17* updates
        waitOnFlip = False
        if key_resp_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_17.frameNStart = frameN  # exact frame index
            key_resp_17.tStart = t  # local t and not account for scr refresh
            key_resp_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_17, 'tStartRefresh')  # time at next scr refresh
            key_resp_17.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_17.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_17.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_17.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_17.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_17_allKeys.extend(theseKeys)
            if len(_key_resp_17_allKeys):
                key_resp_17.keys = _key_resp_17_allKeys[-1].name  # just the last key pressed
                key_resp_17.rt = _key_resp_17_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in time_synchronisationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "time_synchronisation"-------
    for thisComponent in time_synchronisationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('text_9.started', text_9.tStartRefresh)
    trials_3.addData('text_9.stopped', text_9.tStopRefresh)
    # check responses
    if key_resp_17.keys in ['', [], None]:  # No response was made
        key_resp_17.keys = None
    trials_3.addData('key_resp_17.keys',key_resp_17.keys)
    if key_resp_17.keys != None:  # we had a response
        trials_3.addData('key_resp_17.rt', key_resp_17.rt)
    trials_3.addData('key_resp_17.started', key_resp_17.tStartRefresh)
    trials_3.addData('key_resp_17.stopped', key_resp_17.tStopRefresh)
    # the Routine "time_synchronisation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 3.0 repeats of 'trials_3'

# get names of stimulus parameters
if trials_3.trialList in ([], [None], None):
    params = []
else:
    params = trials_3.trialList[0].keys()
# save data for this loop
trials_3.saveAsExcel(filename + '.xlsx', sheetName='trials_3',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials_3.saveAsText(filename + 'trials_3.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "dominant_hand_info"-------
continueRoutine = True
# update component parameters for each repeat
text_25.setText(dominant_hand_info[language])
key_resp_32.keys = []
key_resp_32.rt = []
_key_resp_32_allKeys = []
# keep track of which components have finished
dominant_hand_infoComponents = [text_25, key_resp_32]
for thisComponent in dominant_hand_infoComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
dominant_hand_infoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "dominant_hand_info"-------
while continueRoutine:
    # get current time
    t = dominant_hand_infoClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=dominant_hand_infoClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_25* updates
    if text_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_25.frameNStart = frameN  # exact frame index
        text_25.tStart = t  # local t and not account for scr refresh
        text_25.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_25, 'tStartRefresh')  # time at next scr refresh
        text_25.setAutoDraw(True)
    
    # *key_resp_32* updates
    waitOnFlip = False
    if key_resp_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_32.frameNStart = frameN  # exact frame index
        key_resp_32.tStart = t  # local t and not account for scr refresh
        key_resp_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_32, 'tStartRefresh')  # time at next scr refresh
        key_resp_32.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_32.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_32.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_32.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_32.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_32_allKeys.extend(theseKeys)
        if len(_key_resp_32_allKeys):
            key_resp_32.keys = _key_resp_32_allKeys[-1].name  # just the last key pressed
            key_resp_32.rt = _key_resp_32_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in dominant_hand_infoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "dominant_hand_info"-------
for thisComponent in dominant_hand_infoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_25.started', text_25.tStartRefresh)
thisExp.addData('text_25.stopped', text_25.tStopRefresh)
# check responses
if key_resp_32.keys in ['', [], None]:  # No response was made
    key_resp_32.keys = None
thisExp.addData('key_resp_32.keys',key_resp_32.keys)
if key_resp_32.keys != None:  # we had a response
    thisExp.addData('key_resp_32.rt', key_resp_32.rt)
thisExp.addData('key_resp_32.started', key_resp_32.tStartRefresh)
thisExp.addData('key_resp_32.stopped', key_resp_32.tStopRefresh)
thisExp.nextEntry()
# the Routine "dominant_hand_info" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "audio_test"-------
continueRoutine = True
# update component parameters for each repeat
text_11.setText(audio_test_text[language])
key_resp_20.keys = []
key_resp_20.rt = []
_key_resp_20_allKeys = []
audio_test_mic = microphone.AdvAudioCapture(name='audio_test_mic', saveDir=wavDirName, stereo=False, chnl=0)
# keep track of which components have finished
audio_testComponents = [text_11, key_resp_20, audio_test_mic]
for thisComponent in audio_testComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
audio_testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "audio_test"-------
while continueRoutine:
    # get current time
    t = audio_testClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=audio_testClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_11* updates
    if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_11.frameNStart = frameN  # exact frame index
        text_11.tStart = t  # local t and not account for scr refresh
        text_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
        text_11.setAutoDraw(True)
    
    # *key_resp_20* updates
    waitOnFlip = False
    if key_resp_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_20.frameNStart = frameN  # exact frame index
        key_resp_20.tStart = t  # local t and not account for scr refresh
        key_resp_20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_20, 'tStartRefresh')  # time at next scr refresh
        key_resp_20.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_20.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_20.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_20.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_20.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_20_allKeys.extend(theseKeys)
        if len(_key_resp_20_allKeys):
            key_resp_20.keys = _key_resp_20_allKeys[-1].name  # just the last key pressed
            key_resp_20.rt = _key_resp_20_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *audio_test_mic* updates
    if audio_test_mic.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        audio_test_mic.frameNStart = frameN  # exact frame index
        audio_test_mic.tStart = t  # local t and not account for scr refresh
        audio_test_mic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(audio_test_mic, 'tStartRefresh')  # time at next scr refresh
        audio_test_mic.status = STARTED
        audio_test_mic.record(sec=7200.0, block=False)  # start the recording thread
    
    if audio_test_mic.status == STARTED and not audio_test_mic.recorder.running:
        audio_test_mic.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in audio_testComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "audio_test"-------
for thisComponent in audio_testComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_11.started', text_11.tStartRefresh)
thisExp.addData('text_11.stopped', text_11.tStopRefresh)
# check responses
if key_resp_20.keys in ['', [], None]:  # No response was made
    key_resp_20.keys = None
thisExp.addData('key_resp_20.keys',key_resp_20.keys)
if key_resp_20.keys != None:  # we had a response
    thisExp.addData('key_resp_20.rt', key_resp_20.rt)
thisExp.addData('key_resp_20.started', key_resp_20.tStartRefresh)
thisExp.addData('key_resp_20.stopped', key_resp_20.tStopRefresh)
thisExp.nextEntry()
# audio_test_mic stop & responses
audio_test_mic.stop()  # sometimes helpful
if not audio_test_mic.savedFile:
    audio_test_mic.savedFile = None
# store data for thisExp (ExperimentHandler)
thisExp.addData('audio_test_mic.filename', audio_test_mic.savedFile)
thisExp.addData('audio_test_mic.started', audio_test_mic.tStart)
thisExp.addData('audio_test_mic.stopped', audio_test_mic.tStop)
thisExp.nextEntry()
audio_test_mic.stop()
# the Routine "audio_test" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "wait_for_experimenter"-------
continueRoutine = True
# update component parameters for each repeat
text_28.setText(wait_for_experimenter_text[language])
key_resp_35.keys = []
key_resp_35.rt = []
_key_resp_35_allKeys = []
# keep track of which components have finished
wait_for_experimenterComponents = [text_28, key_resp_35]
for thisComponent in wait_for_experimenterComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
wait_for_experimenterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "wait_for_experimenter"-------
while continueRoutine:
    # get current time
    t = wait_for_experimenterClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=wait_for_experimenterClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_28* updates
    if text_28.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_28.frameNStart = frameN  # exact frame index
        text_28.tStart = t  # local t and not account for scr refresh
        text_28.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_28, 'tStartRefresh')  # time at next scr refresh
        text_28.setAutoDraw(True)
    
    # *key_resp_35* updates
    waitOnFlip = False
    if key_resp_35.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_35.frameNStart = frameN  # exact frame index
        key_resp_35.tStart = t  # local t and not account for scr refresh
        key_resp_35.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_35, 'tStartRefresh')  # time at next scr refresh
        key_resp_35.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_35.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_35.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_35.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_35.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_35_allKeys.extend(theseKeys)
        if len(_key_resp_35_allKeys):
            key_resp_35.keys = _key_resp_35_allKeys[-1].name  # just the last key pressed
            key_resp_35.rt = _key_resp_35_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wait_for_experimenterComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "wait_for_experimenter"-------
for thisComponent in wait_for_experimenterComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_28.started', text_28.tStartRefresh)
thisExp.addData('text_28.stopped', text_28.tStopRefresh)
# check responses
if key_resp_35.keys in ['', [], None]:  # No response was made
    key_resp_35.keys = None
thisExp.addData('key_resp_35.keys',key_resp_35.keys)
if key_resp_35.keys != None:  # we had a response
    thisExp.addData('key_resp_35.rt', key_resp_35.rt)
thisExp.addData('key_resp_35.started', key_resp_35.tStartRefresh)
thisExp.addData('key_resp_35.stopped', key_resp_35.tStopRefresh)
thisExp.nextEntry()
# the Routine "wait_for_experimenter" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruction_video"-------
continueRoutine = True
# update component parameters for each repeat
text_35.setText(video_instruction_text[language])
key_resp_49.keys = []
key_resp_49.rt = []
_key_resp_49_allKeys = []
# keep track of which components have finished
instruction_videoComponents = [text_35, key_resp_49]
for thisComponent in instruction_videoComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruction_videoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruction_video"-------
while continueRoutine:
    # get current time
    t = instruction_videoClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruction_videoClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_35* updates
    if text_35.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_35.frameNStart = frameN  # exact frame index
        text_35.tStart = t  # local t and not account for scr refresh
        text_35.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_35, 'tStartRefresh')  # time at next scr refresh
        text_35.setAutoDraw(True)
    
    # *key_resp_49* updates
    waitOnFlip = False
    if key_resp_49.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_49.frameNStart = frameN  # exact frame index
        key_resp_49.tStart = t  # local t and not account for scr refresh
        key_resp_49.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_49, 'tStartRefresh')  # time at next scr refresh
        key_resp_49.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_49.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_49.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_49.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_49.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_49_allKeys.extend(theseKeys)
        if len(_key_resp_49_allKeys):
            key_resp_49.keys = _key_resp_49_allKeys[-1].name  # just the last key pressed
            key_resp_49.rt = _key_resp_49_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction_videoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction_video"-------
for thisComponent in instruction_videoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_35.started', text_35.tStartRefresh)
thisExp.addData('text_35.stopped', text_35.tStopRefresh)
# check responses
if key_resp_49.keys in ['', [], None]:  # No response was made
    key_resp_49.keys = None
thisExp.addData('key_resp_49.keys',key_resp_49.keys)
if key_resp_49.keys != None:  # we had a response
    thisExp.addData('key_resp_49.rt', key_resp_49.rt)
thisExp.addData('key_resp_49.started', key_resp_49.tStartRefresh)
thisExp.addData('key_resp_49.stopped', key_resp_49.tStopRefresh)
thisExp.nextEntry()
# the Routine "instruction_video" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "play_video"-------
continueRoutine = True
routineTimer.add(600.000000)
# update component parameters for each repeat
# keep track of which components have finished
play_videoComponents = [movie]
for thisComponent in play_videoComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
play_videoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "play_video"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = play_videoClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=play_videoClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *movie* updates
    if movie.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        movie.frameNStart = frameN  # exact frame index
        movie.tStart = t  # local t and not account for scr refresh
        movie.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(movie, 'tStartRefresh')  # time at next scr refresh
        movie.setAutoDraw(True)
    if movie.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > movie.tStartRefresh + 600.0-frameTolerance:
            # keep track of stop time/frame for later
            movie.tStop = t  # not accounting for scr refresh
            movie.frameNStop = frameN  # exact frame index
            win.timeOnFlip(movie, 'tStopRefresh')  # time at next scr refresh
            movie.setAutoDraw(False)
    if movie.status == FINISHED:  # force-end the routine
        continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in play_videoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "play_video"-------
for thisComponent in play_videoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
movie.stop()

# ------Prepare to start Routine "introduction_60_sec_mood"-------
continueRoutine = True
# update component parameters for each repeat
text_3.setText(instruction_60_sec_mood_text[language])
key_resp_12.keys = []
key_resp_12.rt = []
_key_resp_12_allKeys = []
# keep track of which components have finished
introduction_60_sec_moodComponents = [text_3, key_resp_12]
for thisComponent in introduction_60_sec_moodComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introduction_60_sec_moodClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introduction_60_sec_mood"-------
while continueRoutine:
    # get current time
    t = introduction_60_sec_moodClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introduction_60_sec_moodClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # *key_resp_12* updates
    waitOnFlip = False
    if key_resp_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_12.frameNStart = frameN  # exact frame index
        key_resp_12.tStart = t  # local t and not account for scr refresh
        key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
        key_resp_12.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_12.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_12.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_12_allKeys.extend(theseKeys)
        if len(_key_resp_12_allKeys):
            key_resp_12.keys = _key_resp_12_allKeys[-1].name  # just the last key pressed
            key_resp_12.rt = _key_resp_12_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introduction_60_sec_moodComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introduction_60_sec_mood"-------
for thisComponent in introduction_60_sec_moodComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
# check responses
if key_resp_12.keys in ['', [], None]:  # No response was made
    key_resp_12.keys = None
thisExp.addData('key_resp_12.keys',key_resp_12.keys)
if key_resp_12.keys != None:  # we had a response
    thisExp.addData('key_resp_12.rt', key_resp_12.rt)
thisExp.addData('key_resp_12.started', key_resp_12.tStartRefresh)
thisExp.addData('key_resp_12.stopped', key_resp_12.tStopRefresh)
thisExp.nextEntry()
# the Routine "introduction_60_sec_mood" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "routine_60_Sec_mood"-------
continueRoutine = True
# update component parameters for each repeat
mood_voice.setText(mood_text[language])
mood_60_secs = microphone.AdvAudioCapture(name='mood_60_secs', saveDir=wavDirName, stereo=False, chnl=0)
key_resp_11.keys = []
key_resp_11.rt = []
_key_resp_11_allKeys = []
# keep track of which components have finished
routine_60_Sec_moodComponents = [mood_voice, mood_60_secs, Timer, key_resp_11, recording_image]
for thisComponent in routine_60_Sec_moodComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
routine_60_Sec_moodClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "routine_60_Sec_mood"-------
while continueRoutine:
    # get current time
    t = routine_60_Sec_moodClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routine_60_Sec_moodClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *mood_voice* updates
    if mood_voice.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        mood_voice.frameNStart = frameN  # exact frame index
        mood_voice.tStart = t  # local t and not account for scr refresh
        mood_voice.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mood_voice, 'tStartRefresh')  # time at next scr refresh
        mood_voice.setAutoDraw(True)
    
    # *mood_60_secs* updates
    if mood_60_secs.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        mood_60_secs.frameNStart = frameN  # exact frame index
        mood_60_secs.tStart = t  # local t and not account for scr refresh
        mood_60_secs.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mood_60_secs, 'tStartRefresh')  # time at next scr refresh
        mood_60_secs.status = STARTED
        mood_60_secs.record(sec=7200, block=False)  # start the recording thread
    
    if mood_60_secs.status == STARTED and not mood_60_secs.recorder.running:
        mood_60_secs.status = FINISHED
    
    # *Timer* updates
    if Timer.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        Timer.frameNStart = frameN  # exact frame index
        Timer.tStart = t  # local t and not account for scr refresh
        Timer.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Timer, 'tStartRefresh')  # time at next scr refresh
        Timer.setAutoDraw(True)
    if Timer.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Timer.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            Timer.tStop = t  # not accounting for scr refresh
            Timer.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Timer, 'tStopRefresh')  # time at next scr refresh
            Timer.setAutoDraw(False)
    if Timer.status == STARTED:  # only update if drawing
        Timer.setText(str(round(-routineTimer.getTime()-Timer.tStart)) + "\n\n" + seconds[language]
)
    
    # *key_resp_11* updates
    waitOnFlip = False
    if key_resp_11.status == NOT_STARTED and tThisFlip >= 30-frameTolerance:
        # keep track of start time/frame for later
        key_resp_11.frameNStart = frameN  # exact frame index
        key_resp_11.tStart = t  # local t and not account for scr refresh
        key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
        key_resp_11.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_11.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_11.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_11_allKeys.extend(theseKeys)
        if len(_key_resp_11_allKeys):
            key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
            key_resp_11.rt = _key_resp_11_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *recording_image* updates
    if recording_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        recording_image.frameNStart = frameN  # exact frame index
        recording_image.tStart = t  # local t and not account for scr refresh
        recording_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(recording_image, 'tStartRefresh')  # time at next scr refresh
        recording_image.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in routine_60_Sec_moodComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "routine_60_Sec_mood"-------
for thisComponent in routine_60_Sec_moodComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('mood_voice.started', mood_voice.tStartRefresh)
thisExp.addData('mood_voice.stopped', mood_voice.tStopRefresh)
# mood_60_secs stop & responses
mood_60_secs.stop()  # sometimes helpful
if not mood_60_secs.savedFile:
    mood_60_secs.savedFile = None
# store data for thisExp (ExperimentHandler)
thisExp.addData('mood_60_secs.filename', mood_60_secs.savedFile)
thisExp.addData('mood_60_secs.started', mood_60_secs.tStartRefresh)
thisExp.addData('mood_60_secs.stopped', mood_60_secs.tStopRefresh)
thisExp.nextEntry()
# check responses
if key_resp_11.keys in ['', [], None]:  # No response was made
    key_resp_11.keys = None
thisExp.addData('key_resp_11.keys',key_resp_11.keys)
if key_resp_11.keys != None:  # we had a response
    thisExp.addData('key_resp_11.rt', key_resp_11.rt)
thisExp.addData('key_resp_11.started', key_resp_11.tStartRefresh)
thisExp.addData('key_resp_11.stopped', key_resp_11.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('recording_image.started', recording_image.tStartRefresh)
thisExp.addData('recording_image.stopped', recording_image.tStopRefresh)
# the Routine "routine_60_Sec_mood" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "neutral_speech_instruction"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_25.keys = []
key_resp_25.rt = []
_key_resp_25_allKeys = []
text_17.setText(neutral_speech_instruction_text[language])
# keep track of which components have finished
neutral_speech_instructionComponents = [key_resp_25, text_17]
for thisComponent in neutral_speech_instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
neutral_speech_instructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "neutral_speech_instruction"-------
while continueRoutine:
    # get current time
    t = neutral_speech_instructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=neutral_speech_instructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_25* updates
    waitOnFlip = False
    if key_resp_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_25.frameNStart = frameN  # exact frame index
        key_resp_25.tStart = t  # local t and not account for scr refresh
        key_resp_25.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_25, 'tStartRefresh')  # time at next scr refresh
        key_resp_25.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_25.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_25.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_25.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_25.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_25_allKeys.extend(theseKeys)
        if len(_key_resp_25_allKeys):
            key_resp_25.keys = _key_resp_25_allKeys[-1].name  # just the last key pressed
            key_resp_25.rt = _key_resp_25_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_17* updates
    if text_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_17.frameNStart = frameN  # exact frame index
        text_17.tStart = t  # local t and not account for scr refresh
        text_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_17, 'tStartRefresh')  # time at next scr refresh
        text_17.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in neutral_speech_instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "neutral_speech_instruction"-------
for thisComponent in neutral_speech_instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_25.keys in ['', [], None]:  # No response was made
    key_resp_25.keys = None
thisExp.addData('key_resp_25.keys',key_resp_25.keys)
if key_resp_25.keys != None:  # we had a response
    thisExp.addData('key_resp_25.rt', key_resp_25.rt)
thisExp.addData('key_resp_25.started', key_resp_25.tStartRefresh)
thisExp.addData('key_resp_25.stopped', key_resp_25.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_17.started', text_17.tStartRefresh)
thisExp.addData('text_17.stopped', text_17.tStopRefresh)
# the Routine "neutral_speech_instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "neutral_speech_start_mic"-------
continueRoutine = True
# update component parameters for each repeat
neutral_speech_mic = microphone.AdvAudioCapture(name='neutral_speech_mic', saveDir=wavDirName, stereo=False, chnl=0)
neutral_speech_mic.record(sec=7200)
# keep track of which components have finished
neutral_speech_start_micComponents = []
for thisComponent in neutral_speech_start_micComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
neutral_speech_start_micClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "neutral_speech_start_mic"-------
while continueRoutine:
    # get current time
    t = neutral_speech_start_micClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=neutral_speech_start_micClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in neutral_speech_start_micComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "neutral_speech_start_mic"-------
for thisComponent in neutral_speech_start_micComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "neutral_speech_start_mic" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
neutral_speech = data.TrialHandler(nReps=3.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='neutral_speech')
thisExp.addLoop(neutral_speech)  # add the loop to the experiment
thisNeutral_speech = neutral_speech.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNeutral_speech.rgb)
if thisNeutral_speech != None:
    for paramName in thisNeutral_speech:
        exec('{} = thisNeutral_speech[paramName]'.format(paramName))

for thisNeutral_speech in neutral_speech:
    currentLoop = neutral_speech
    # abbreviate parameter names if possible (e.g. rgb = thisNeutral_speech.rgb)
    if thisNeutral_speech != None:
        for paramName in thisNeutral_speech:
            exec('{} = thisNeutral_speech[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "neutral_speech_recording"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_18.setText(neutral_speech_text[language][neutral_speech.thisN])
    key_resp_26.keys = []
    key_resp_26.rt = []
    _key_resp_26_allKeys = []
    # keep track of which components have finished
    neutral_speech_recordingComponents = [text_18, key_resp_26]
    for thisComponent in neutral_speech_recordingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    neutral_speech_recordingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "neutral_speech_recording"-------
    while continueRoutine:
        # get current time
        t = neutral_speech_recordingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=neutral_speech_recordingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_18* updates
        if text_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_18.frameNStart = frameN  # exact frame index
            text_18.tStart = t  # local t and not account for scr refresh
            text_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_18, 'tStartRefresh')  # time at next scr refresh
            text_18.setAutoDraw(True)
        
        # *key_resp_26* updates
        waitOnFlip = False
        if key_resp_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_26.frameNStart = frameN  # exact frame index
            key_resp_26.tStart = t  # local t and not account for scr refresh
            key_resp_26.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_26, 'tStartRefresh')  # time at next scr refresh
            key_resp_26.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_26.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_26.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_26.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_26.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_26_allKeys.extend(theseKeys)
            if len(_key_resp_26_allKeys):
                key_resp_26.keys = _key_resp_26_allKeys[-1].name  # just the last key pressed
                key_resp_26.rt = _key_resp_26_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in neutral_speech_recordingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "neutral_speech_recording"-------
    for thisComponent in neutral_speech_recordingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    neutral_speech.addData('text_18.started', text_18.tStartRefresh)
    neutral_speech.addData('text_18.stopped', text_18.tStopRefresh)
    # check responses
    if key_resp_26.keys in ['', [], None]:  # No response was made
        key_resp_26.keys = None
    neutral_speech.addData('key_resp_26.keys',key_resp_26.keys)
    if key_resp_26.keys != None:  # we had a response
        neutral_speech.addData('key_resp_26.rt', key_resp_26.rt)
    neutral_speech.addData('key_resp_26.started', key_resp_26.tStartRefresh)
    neutral_speech.addData('key_resp_26.stopped', key_resp_26.tStopRefresh)
    # the Routine "neutral_speech_recording" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 3.0 repeats of 'neutral_speech'

# get names of stimulus parameters
if neutral_speech.trialList in ([], [None], None):
    params = []
else:
    params = neutral_speech.trialList[0].keys()
# save data for this loop
neutral_speech.saveAsExcel(filename + '.xlsx', sheetName='neutral_speech',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
neutral_speech.saveAsText(filename + 'neutral_speech.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "neutral_speech_stop_mic"-------
continueRoutine = True
# update component parameters for each repeat

time.sleep(1)
neutral_speech_mic.stop()
# keep track of which components have finished
neutral_speech_stop_micComponents = []
for thisComponent in neutral_speech_stop_micComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
neutral_speech_stop_micClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "neutral_speech_stop_mic"-------
while continueRoutine:
    # get current time
    t = neutral_speech_stop_micClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=neutral_speech_stop_micClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in neutral_speech_stop_micComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "neutral_speech_stop_mic"-------
for thisComponent in neutral_speech_stop_micComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "neutral_speech_stop_mic" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "emotional_sentences_introduction"-------
continueRoutine = True
# update component parameters for each repeat
emotional_sentence_textfield.setText(emotional_sentence_intro[language])
key_resp_38.keys = []
key_resp_38.rt = []
_key_resp_38_allKeys = []
# keep track of which components have finished
emotional_sentences_introductionComponents = [emotional_sentence_textfield, key_resp_38]
for thisComponent in emotional_sentences_introductionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
emotional_sentences_introductionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "emotional_sentences_introduction"-------
while continueRoutine:
    # get current time
    t = emotional_sentences_introductionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=emotional_sentences_introductionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *emotional_sentence_textfield* updates
    if emotional_sentence_textfield.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        emotional_sentence_textfield.frameNStart = frameN  # exact frame index
        emotional_sentence_textfield.tStart = t  # local t and not account for scr refresh
        emotional_sentence_textfield.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(emotional_sentence_textfield, 'tStartRefresh')  # time at next scr refresh
        emotional_sentence_textfield.setAutoDraw(True)
    
    # *key_resp_38* updates
    waitOnFlip = False
    if key_resp_38.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_38.frameNStart = frameN  # exact frame index
        key_resp_38.tStart = t  # local t and not account for scr refresh
        key_resp_38.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_38, 'tStartRefresh')  # time at next scr refresh
        key_resp_38.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_38.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_38.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_38.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_38.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_38_allKeys.extend(theseKeys)
        if len(_key_resp_38_allKeys):
            key_resp_38.keys = _key_resp_38_allKeys[-1].name  # just the last key pressed
            key_resp_38.rt = _key_resp_38_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in emotional_sentences_introductionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "emotional_sentences_introduction"-------
for thisComponent in emotional_sentences_introductionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('emotional_sentence_textfield.started', emotional_sentence_textfield.tStartRefresh)
thisExp.addData('emotional_sentence_textfield.stopped', emotional_sentence_textfield.tStopRefresh)
# check responses
if key_resp_38.keys in ['', [], None]:  # No response was made
    key_resp_38.keys = None
thisExp.addData('key_resp_38.keys',key_resp_38.keys)
if key_resp_38.keys != None:  # we had a response
    thisExp.addData('key_resp_38.rt', key_resp_38.rt)
thisExp.addData('key_resp_38.started', key_resp_38.tStartRefresh)
thisExp.addData('key_resp_38.stopped', key_resp_38.tStopRefresh)
thisExp.nextEntry()
# the Routine "emotional_sentences_introduction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
emotional_sentences = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(emotional_sentences_path[language]),
    seed=None, name='emotional_sentences')
thisExp.addLoop(emotional_sentences)  # add the loop to the experiment
thisEmotional_sentence = emotional_sentences.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEmotional_sentence.rgb)
if thisEmotional_sentence != None:
    for paramName in thisEmotional_sentence:
        exec('{} = thisEmotional_sentence[paramName]'.format(paramName))

for thisEmotional_sentence in emotional_sentences:
    currentLoop = emotional_sentences
    # abbreviate parameter names if possible (e.g. rgb = thisEmotional_sentence.rgb)
    if thisEmotional_sentence != None:
        for paramName in thisEmotional_sentence:
            exec('{} = thisEmotional_sentence[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials_5 = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(emotions_path[language]),
        seed=None, name='trials_5')
    thisExp.addLoop(trials_5)  # add the loop to the experiment
    thisTrial_5 = trials_5.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
    if thisTrial_5 != None:
        for paramName in thisTrial_5:
            exec('{} = thisTrial_5[paramName]'.format(paramName))
    
    for thisTrial_5 in trials_5:
        currentLoop = trials_5
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
        if thisTrial_5 != None:
            for paramName in thisTrial_5:
                exec('{} = thisTrial_5[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "emotional_sentence_preview"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_41.keys = []
        key_resp_41.rt = []
        _key_resp_41_allKeys = []
        text_37.setText(emotional_sentence_preview_text[language])
        text_41.setText(emotional_sentence)
        text_42.setText(act_emotion_text[language])
        text_43.setText(emotion)
        text_44.setText(start_recording_text[language])
        # keep track of which components have finished
        emotional_sentence_previewComponents = [key_resp_41, text_37, text_41, text_42, text_43, text_44]
        for thisComponent in emotional_sentence_previewComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        emotional_sentence_previewClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "emotional_sentence_preview"-------
        while continueRoutine:
            # get current time
            t = emotional_sentence_previewClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=emotional_sentence_previewClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_resp_41* updates
            waitOnFlip = False
            if key_resp_41.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_41.frameNStart = frameN  # exact frame index
                key_resp_41.tStart = t  # local t and not account for scr refresh
                key_resp_41.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_41, 'tStartRefresh')  # time at next scr refresh
                key_resp_41.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_41.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_41.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_41.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_41.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_41_allKeys.extend(theseKeys)
                if len(_key_resp_41_allKeys):
                    key_resp_41.keys = _key_resp_41_allKeys[-1].name  # just the last key pressed
                    key_resp_41.rt = _key_resp_41_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_37* updates
            if text_37.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_37.frameNStart = frameN  # exact frame index
                text_37.tStart = t  # local t and not account for scr refresh
                text_37.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_37, 'tStartRefresh')  # time at next scr refresh
                text_37.setAutoDraw(True)
            
            # *text_41* updates
            if text_41.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_41.frameNStart = frameN  # exact frame index
                text_41.tStart = t  # local t and not account for scr refresh
                text_41.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_41, 'tStartRefresh')  # time at next scr refresh
                text_41.setAutoDraw(True)
            
            # *text_42* updates
            if text_42.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_42.frameNStart = frameN  # exact frame index
                text_42.tStart = t  # local t and not account for scr refresh
                text_42.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_42, 'tStartRefresh')  # time at next scr refresh
                text_42.setAutoDraw(True)
            
            # *text_43* updates
            if text_43.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_43.frameNStart = frameN  # exact frame index
                text_43.tStart = t  # local t and not account for scr refresh
                text_43.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_43, 'tStartRefresh')  # time at next scr refresh
                text_43.setAutoDraw(True)
            
            # *text_44* updates
            if text_44.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_44.frameNStart = frameN  # exact frame index
                text_44.tStart = t  # local t and not account for scr refresh
                text_44.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_44, 'tStartRefresh')  # time at next scr refresh
                text_44.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in emotional_sentence_previewComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "emotional_sentence_preview"-------
        for thisComponent in emotional_sentence_previewComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_41.keys in ['', [], None]:  # No response was made
            key_resp_41.keys = None
        trials_5.addData('key_resp_41.keys',key_resp_41.keys)
        if key_resp_41.keys != None:  # we had a response
            trials_5.addData('key_resp_41.rt', key_resp_41.rt)
        trials_5.addData('key_resp_41.started', key_resp_41.tStartRefresh)
        trials_5.addData('key_resp_41.stopped', key_resp_41.tStopRefresh)
        trials_5.addData('text_37.started', text_37.tStartRefresh)
        trials_5.addData('text_37.stopped', text_37.tStopRefresh)
        trials_5.addData('text_41.started', text_41.tStartRefresh)
        trials_5.addData('text_41.stopped', text_41.tStopRefresh)
        trials_5.addData('text_42.started', text_42.tStartRefresh)
        trials_5.addData('text_42.stopped', text_42.tStopRefresh)
        trials_5.addData('text_43.started', text_43.tStartRefresh)
        trials_5.addData('text_43.stopped', text_43.tStopRefresh)
        trials_5.addData('text_44.started', text_44.tStartRefresh)
        trials_5.addData('text_44.stopped', text_44.tStopRefresh)
        # the Routine "emotional_sentence_preview" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "emotional_sentence_recording"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_42.keys = []
        key_resp_42.rt = []
        _key_resp_42_allKeys = []
        emotional_sentence_mic = microphone.AdvAudioCapture(name='emotional_sentence_mic', saveDir=wavDirName, stereo=False, chnl=0)
        text_45.setText(stop_recording_text[language])
        text_46.setText(emotion)
        text_47.setText(act_emotion_text[language])
        text_48.setText(emotional_sentence)
        text_49.setText(emotional_sentence_read_text[language])
        # keep track of which components have finished
        emotional_sentence_recordingComponents = [key_resp_42, emotional_sentence_mic, text_45, text_46, text_47, text_48, text_49]
        for thisComponent in emotional_sentence_recordingComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        emotional_sentence_recordingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "emotional_sentence_recording"-------
        while continueRoutine:
            # get current time
            t = emotional_sentence_recordingClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=emotional_sentence_recordingClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_resp_42* updates
            waitOnFlip = False
            if key_resp_42.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_42.frameNStart = frameN  # exact frame index
                key_resp_42.tStart = t  # local t and not account for scr refresh
                key_resp_42.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_42, 'tStartRefresh')  # time at next scr refresh
                key_resp_42.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_42.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_42.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_42.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_42.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_42_allKeys.extend(theseKeys)
                if len(_key_resp_42_allKeys):
                    key_resp_42.keys = _key_resp_42_allKeys[-1].name  # just the last key pressed
                    key_resp_42.rt = _key_resp_42_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *emotional_sentence_mic* updates
            if emotional_sentence_mic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                emotional_sentence_mic.frameNStart = frameN  # exact frame index
                emotional_sentence_mic.tStart = t  # local t and not account for scr refresh
                emotional_sentence_mic.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(emotional_sentence_mic, 'tStartRefresh')  # time at next scr refresh
                emotional_sentence_mic.status = STARTED
                emotional_sentence_mic.record(sec=7200.0, block=False)  # start the recording thread
            
            if emotional_sentence_mic.status == STARTED and not emotional_sentence_mic.recorder.running:
                emotional_sentence_mic.status = FINISHED
            
            # *text_45* updates
            if text_45.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_45.frameNStart = frameN  # exact frame index
                text_45.tStart = t  # local t and not account for scr refresh
                text_45.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_45, 'tStartRefresh')  # time at next scr refresh
                text_45.setAutoDraw(True)
            
            # *text_46* updates
            if text_46.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_46.frameNStart = frameN  # exact frame index
                text_46.tStart = t  # local t and not account for scr refresh
                text_46.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_46, 'tStartRefresh')  # time at next scr refresh
                text_46.setAutoDraw(True)
            
            # *text_47* updates
            if text_47.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_47.frameNStart = frameN  # exact frame index
                text_47.tStart = t  # local t and not account for scr refresh
                text_47.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_47, 'tStartRefresh')  # time at next scr refresh
                text_47.setAutoDraw(True)
            
            # *text_48* updates
            if text_48.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_48.frameNStart = frameN  # exact frame index
                text_48.tStart = t  # local t and not account for scr refresh
                text_48.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_48, 'tStartRefresh')  # time at next scr refresh
                text_48.setAutoDraw(True)
            
            # *text_49* updates
            if text_49.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_49.frameNStart = frameN  # exact frame index
                text_49.tStart = t  # local t and not account for scr refresh
                text_49.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_49, 'tStartRefresh')  # time at next scr refresh
                text_49.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in emotional_sentence_recordingComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "emotional_sentence_recording"-------
        for thisComponent in emotional_sentence_recordingComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_42.keys in ['', [], None]:  # No response was made
            key_resp_42.keys = None
        trials_5.addData('key_resp_42.keys',key_resp_42.keys)
        if key_resp_42.keys != None:  # we had a response
            trials_5.addData('key_resp_42.rt', key_resp_42.rt)
        trials_5.addData('key_resp_42.started', key_resp_42.tStartRefresh)
        trials_5.addData('key_resp_42.stopped', key_resp_42.tStopRefresh)
        # emotional_sentence_mic stop & responses
        emotional_sentence_mic.stop()  # sometimes helpful
        if not emotional_sentence_mic.savedFile:
            emotional_sentence_mic.savedFile = None
        # store data for trials_5 (TrialHandler)
        trials_5.addData('emotional_sentence_mic.filename', emotional_sentence_mic.savedFile)
        trials_5.addData('emotional_sentence_mic.started', emotional_sentence_mic.tStartRefresh)
        trials_5.addData('emotional_sentence_mic.stopped', emotional_sentence_mic.tStopRefresh)
        trials_5.addData('text_45.started', text_45.tStartRefresh)
        trials_5.addData('text_45.stopped', text_45.tStopRefresh)
        trials_5.addData('text_46.started', text_46.tStartRefresh)
        trials_5.addData('text_46.stopped', text_46.tStopRefresh)
        trials_5.addData('text_47.started', text_47.tStartRefresh)
        trials_5.addData('text_47.stopped', text_47.tStopRefresh)
        trials_5.addData('text_48.started', text_48.tStartRefresh)
        trials_5.addData('text_48.stopped', text_48.tStopRefresh)
        trials_5.addData('text_49.started', text_49.tStartRefresh)
        trials_5.addData('text_49.stopped', text_49.tStopRefresh)
        # the Routine "emotional_sentence_recording" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 1.0 repeats of 'trials_5'
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'emotional_sentences'

# get names of stimulus parameters
if emotional_sentences.trialList in ([], [None], None):
    params = []
else:
    params = emotional_sentences.trialList[0].keys()
# save data for this loop
emotional_sentences.saveAsExcel(filename + '.xlsx', sheetName='emotional_sentences',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
emotional_sentences.saveAsText(filename + 'emotional_sentences.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "speaking_vowels_introduction"-------
continueRoutine = True
# update component parameters for each repeat
text_40.setText(speaking_vowels_intro[language])
key_resp_43.keys = []
key_resp_43.rt = []
_key_resp_43_allKeys = []
# keep track of which components have finished
speaking_vowels_introductionComponents = [text_40, key_resp_43]
for thisComponent in speaking_vowels_introductionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
speaking_vowels_introductionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "speaking_vowels_introduction"-------
while continueRoutine:
    # get current time
    t = speaking_vowels_introductionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=speaking_vowels_introductionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_40* updates
    if text_40.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_40.frameNStart = frameN  # exact frame index
        text_40.tStart = t  # local t and not account for scr refresh
        text_40.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_40, 'tStartRefresh')  # time at next scr refresh
        text_40.setAutoDraw(True)
    
    # *key_resp_43* updates
    waitOnFlip = False
    if key_resp_43.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_43.frameNStart = frameN  # exact frame index
        key_resp_43.tStart = t  # local t and not account for scr refresh
        key_resp_43.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_43, 'tStartRefresh')  # time at next scr refresh
        key_resp_43.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_43.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_43.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_43.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_43.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_43_allKeys.extend(theseKeys)
        if len(_key_resp_43_allKeys):
            key_resp_43.keys = _key_resp_43_allKeys[-1].name  # just the last key pressed
            key_resp_43.rt = _key_resp_43_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in speaking_vowels_introductionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "speaking_vowels_introduction"-------
for thisComponent in speaking_vowels_introductionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_40.started', text_40.tStartRefresh)
thisExp.addData('text_40.stopped', text_40.tStopRefresh)
# check responses
if key_resp_43.keys in ['', [], None]:  # No response was made
    key_resp_43.keys = None
thisExp.addData('key_resp_43.keys',key_resp_43.keys)
if key_resp_43.keys != None:  # we had a response
    thisExp.addData('key_resp_43.rt', key_resp_43.rt)
thisExp.addData('key_resp_43.started', key_resp_43.tStartRefresh)
thisExp.addData('key_resp_43.stopped', key_resp_43.tStopRefresh)
thisExp.nextEntry()
# the Routine "speaking_vowels_introduction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
vowels_as_long_as_possible_trial = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(vowels_path[language], selection='[0, 1]'),
    seed=None, name='vowels_as_long_as_possible_trial')
thisExp.addLoop(vowels_as_long_as_possible_trial)  # add the loop to the experiment
thisVowels_as_long_as_possible_trial = vowels_as_long_as_possible_trial.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisVowels_as_long_as_possible_trial.rgb)
if thisVowels_as_long_as_possible_trial != None:
    for paramName in thisVowels_as_long_as_possible_trial:
        exec('{} = thisVowels_as_long_as_possible_trial[paramName]'.format(paramName))

for thisVowels_as_long_as_possible_trial in vowels_as_long_as_possible_trial:
    currentLoop = vowels_as_long_as_possible_trial
    # abbreviate parameter names if possible (e.g. rgb = thisVowels_as_long_as_possible_trial.rgb)
    if thisVowels_as_long_as_possible_trial != None:
        for paramName in thisVowels_as_long_as_possible_trial:
            exec('{} = thisVowels_as_long_as_possible_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "phones_as_long_as_possible_preview"-------
    continueRoutine = True
    # update component parameters for each repeat
    textbox.setText(speaking_vowels_preview1[language] + "\n\n" + vowel_sentence + "\n\n" + speaking_vowels_preview2[language])
    key_resp_44.keys = []
    key_resp_44.rt = []
    _key_resp_44_allKeys = []
    # keep track of which components have finished
    phones_as_long_as_possible_previewComponents = [textbox, key_resp_44]
    for thisComponent in phones_as_long_as_possible_previewComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    phones_as_long_as_possible_previewClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "phones_as_long_as_possible_preview"-------
    while continueRoutine:
        # get current time
        t = phones_as_long_as_possible_previewClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=phones_as_long_as_possible_previewClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textbox* updates
        if textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textbox.frameNStart = frameN  # exact frame index
            textbox.tStart = t  # local t and not account for scr refresh
            textbox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
            textbox.setAutoDraw(True)
        
        # *key_resp_44* updates
        waitOnFlip = False
        if key_resp_44.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_44.frameNStart = frameN  # exact frame index
            key_resp_44.tStart = t  # local t and not account for scr refresh
            key_resp_44.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_44, 'tStartRefresh')  # time at next scr refresh
            key_resp_44.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_44.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_44.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_44.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_44.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_44_allKeys.extend(theseKeys)
            if len(_key_resp_44_allKeys):
                key_resp_44.keys = _key_resp_44_allKeys[-1].name  # just the last key pressed
                key_resp_44.rt = _key_resp_44_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in phones_as_long_as_possible_previewComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "phones_as_long_as_possible_preview"-------
    for thisComponent in phones_as_long_as_possible_previewComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    vowels_as_long_as_possible_trial.addData('textbox.started', textbox.tStartRefresh)
    vowels_as_long_as_possible_trial.addData('textbox.stopped', textbox.tStopRefresh)
    # check responses
    if key_resp_44.keys in ['', [], None]:  # No response was made
        key_resp_44.keys = None
    vowels_as_long_as_possible_trial.addData('key_resp_44.keys',key_resp_44.keys)
    if key_resp_44.keys != None:  # we had a response
        vowels_as_long_as_possible_trial.addData('key_resp_44.rt', key_resp_44.rt)
    vowels_as_long_as_possible_trial.addData('key_resp_44.started', key_resp_44.tStartRefresh)
    vowels_as_long_as_possible_trial.addData('key_resp_44.stopped', key_resp_44.tStopRefresh)
    # the Routine "phones_as_long_as_possible_preview" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "phones_as_long_possible_recording"-------
    continueRoutine = True
    # update component parameters for each repeat
    textbox_2.setText(speaking_vowels[language] + "\n\n" + vowel_sentence + "\n\n" + stop_vowels_recording[language])
    key_resp_45.keys = []
    key_resp_45.rt = []
    _key_resp_45_allKeys = []
    vowels_long_mic = microphone.AdvAudioCapture(name='vowels_long_mic', saveDir=wavDirName, stereo=False, chnl=0)
    # keep track of which components have finished
    phones_as_long_possible_recordingComponents = [textbox_2, key_resp_45, vowels_long_mic]
    for thisComponent in phones_as_long_possible_recordingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    phones_as_long_possible_recordingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "phones_as_long_possible_recording"-------
    while continueRoutine:
        # get current time
        t = phones_as_long_possible_recordingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=phones_as_long_possible_recordingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textbox_2* updates
        if textbox_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textbox_2.frameNStart = frameN  # exact frame index
            textbox_2.tStart = t  # local t and not account for scr refresh
            textbox_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbox_2, 'tStartRefresh')  # time at next scr refresh
            textbox_2.setAutoDraw(True)
        
        # *key_resp_45* updates
        waitOnFlip = False
        if key_resp_45.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_45.frameNStart = frameN  # exact frame index
            key_resp_45.tStart = t  # local t and not account for scr refresh
            key_resp_45.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_45, 'tStartRefresh')  # time at next scr refresh
            key_resp_45.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_45.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_45.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_45.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_45.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_45_allKeys.extend(theseKeys)
            if len(_key_resp_45_allKeys):
                key_resp_45.keys = _key_resp_45_allKeys[-1].name  # just the last key pressed
                key_resp_45.rt = _key_resp_45_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *vowels_long_mic* updates
        if vowels_long_mic.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            vowels_long_mic.frameNStart = frameN  # exact frame index
            vowels_long_mic.tStart = t  # local t and not account for scr refresh
            vowels_long_mic.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(vowels_long_mic, 'tStartRefresh')  # time at next scr refresh
            vowels_long_mic.status = STARTED
            vowels_long_mic.record(sec=7200.0, block=False)  # start the recording thread
        
        if vowels_long_mic.status == STARTED and not vowels_long_mic.recorder.running:
            vowels_long_mic.status = FINISHED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in phones_as_long_possible_recordingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "phones_as_long_possible_recording"-------
    for thisComponent in phones_as_long_possible_recordingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    vowels_as_long_as_possible_trial.addData('textbox_2.started', textbox_2.tStartRefresh)
    vowels_as_long_as_possible_trial.addData('textbox_2.stopped', textbox_2.tStopRefresh)
    # check responses
    if key_resp_45.keys in ['', [], None]:  # No response was made
        key_resp_45.keys = None
    vowels_as_long_as_possible_trial.addData('key_resp_45.keys',key_resp_45.keys)
    if key_resp_45.keys != None:  # we had a response
        vowels_as_long_as_possible_trial.addData('key_resp_45.rt', key_resp_45.rt)
    vowels_as_long_as_possible_trial.addData('key_resp_45.started', key_resp_45.tStartRefresh)
    vowels_as_long_as_possible_trial.addData('key_resp_45.stopped', key_resp_45.tStopRefresh)
    # vowels_long_mic stop & responses
    vowels_long_mic.stop()  # sometimes helpful
    if not vowels_long_mic.savedFile:
        vowels_long_mic.savedFile = None
    # store data for vowels_as_long_as_possible_trial (TrialHandler)
    vowels_as_long_as_possible_trial.addData('vowels_long_mic.filename', vowels_long_mic.savedFile)
    vowels_as_long_as_possible_trial.addData('vowels_long_mic.started', vowels_long_mic.tStart)
    vowels_as_long_as_possible_trial.addData('vowels_long_mic.stopped', vowels_long_mic.tStop)
    # the Routine "phones_as_long_possible_recording" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'vowels_as_long_as_possible_trial'

# get names of stimulus parameters
if vowels_as_long_as_possible_trial.trialList in ([], [None], None):
    params = []
else:
    params = vowels_as_long_as_possible_trial.trialList[0].keys()
# save data for this loop
vowels_as_long_as_possible_trial.saveAsExcel(filename + '.xlsx', sheetName='vowels_as_long_as_possible_trial',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
vowels_as_long_as_possible_trial.saveAsText(filename + 'vowels_as_long_as_possible_trial.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
vowels_5_secs = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(vowels_path[language]),
    seed=None, name='vowels_5_secs')
thisExp.addLoop(vowels_5_secs)  # add the loop to the experiment
thisVowels_5_sec = vowels_5_secs.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisVowels_5_sec.rgb)
if thisVowels_5_sec != None:
    for paramName in thisVowels_5_sec:
        exec('{} = thisVowels_5_sec[paramName]'.format(paramName))

for thisVowels_5_sec in vowels_5_secs:
    currentLoop = vowels_5_secs
    # abbreviate parameter names if possible (e.g. rgb = thisVowels_5_sec.rgb)
    if thisVowels_5_sec != None:
        for paramName in thisVowels_5_sec:
            exec('{} = thisVowels_5_sec[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "phones_5_secs_preview"-------
    continueRoutine = True
    # update component parameters for each repeat
    textbox_3.setText(speaking_vowels_preview1[language] + "\n\n" + vowel_sentence_5_secs + "\n\n" + speaking_vowels_5_secs_preview[language])
    key_resp_46.keys = []
    key_resp_46.rt = []
    _key_resp_46_allKeys = []
    # keep track of which components have finished
    phones_5_secs_previewComponents = [textbox_3, key_resp_46]
    for thisComponent in phones_5_secs_previewComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    phones_5_secs_previewClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "phones_5_secs_preview"-------
    while continueRoutine:
        # get current time
        t = phones_5_secs_previewClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=phones_5_secs_previewClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textbox_3* updates
        if textbox_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textbox_3.frameNStart = frameN  # exact frame index
            textbox_3.tStart = t  # local t and not account for scr refresh
            textbox_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbox_3, 'tStartRefresh')  # time at next scr refresh
            textbox_3.setAutoDraw(True)
        
        # *key_resp_46* updates
        waitOnFlip = False
        if key_resp_46.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_46.frameNStart = frameN  # exact frame index
            key_resp_46.tStart = t  # local t and not account for scr refresh
            key_resp_46.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_46, 'tStartRefresh')  # time at next scr refresh
            key_resp_46.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_46.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_46.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_46.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_46.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_46_allKeys.extend(theseKeys)
            if len(_key_resp_46_allKeys):
                key_resp_46.keys = _key_resp_46_allKeys[-1].name  # just the last key pressed
                key_resp_46.rt = _key_resp_46_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in phones_5_secs_previewComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "phones_5_secs_preview"-------
    for thisComponent in phones_5_secs_previewComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    vowels_5_secs.addData('textbox_3.started', textbox_3.tStartRefresh)
    vowels_5_secs.addData('textbox_3.stopped', textbox_3.tStopRefresh)
    # check responses
    if key_resp_46.keys in ['', [], None]:  # No response was made
        key_resp_46.keys = None
    vowels_5_secs.addData('key_resp_46.keys',key_resp_46.keys)
    if key_resp_46.keys != None:  # we had a response
        vowels_5_secs.addData('key_resp_46.rt', key_resp_46.rt)
    vowels_5_secs.addData('key_resp_46.started', key_resp_46.tStartRefresh)
    vowels_5_secs.addData('key_resp_46.stopped', key_resp_46.tStopRefresh)
    # the Routine "phones_5_secs_preview" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "phones_5_secs_recording"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    textbox_4.setText(speaking_vowels[language] + "\n\n" + vowel_sentence_5_secs + "\n\n" + speaking_vowels_5_secs[language])
    phone_5_secs_mic = microphone.AdvAudioCapture(name='phone_5_secs_mic', saveDir=wavDirName, stereo=False, chnl=0)
    # keep track of which components have finished
    phones_5_secs_recordingComponents = [textbox_4, phone_5_secs_mic, timer_vowels]
    for thisComponent in phones_5_secs_recordingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    phones_5_secs_recordingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "phones_5_secs_recording"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = phones_5_secs_recordingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=phones_5_secs_recordingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textbox_4* updates
        if textbox_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textbox_4.frameNStart = frameN  # exact frame index
            textbox_4.tStart = t  # local t and not account for scr refresh
            textbox_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbox_4, 'tStartRefresh')  # time at next scr refresh
            textbox_4.setAutoDraw(True)
        if textbox_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textbox_4.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                textbox_4.tStop = t  # not accounting for scr refresh
                textbox_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(textbox_4, 'tStopRefresh')  # time at next scr refresh
                textbox_4.setAutoDraw(False)
        
        # *phone_5_secs_mic* updates
        if phone_5_secs_mic.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            phone_5_secs_mic.frameNStart = frameN  # exact frame index
            phone_5_secs_mic.tStart = t  # local t and not account for scr refresh
            phone_5_secs_mic.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(phone_5_secs_mic, 'tStartRefresh')  # time at next scr refresh
            phone_5_secs_mic.status = STARTED
            phone_5_secs_mic.record(sec=5.0, block=False)  # start the recording thread
        
        if phone_5_secs_mic.status == STARTED and not phone_5_secs_mic.recorder.running:
            phone_5_secs_mic.status = FINISHED
        
        # *timer_vowels* updates
        if timer_vowels.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            timer_vowels.frameNStart = frameN  # exact frame index
            timer_vowels.tStart = t  # local t and not account for scr refresh
            timer_vowels.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(timer_vowels, 'tStartRefresh')  # time at next scr refresh
            timer_vowels.setAutoDraw(True)
        if timer_vowels.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > timer_vowels.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                timer_vowels.tStop = t  # not accounting for scr refresh
                timer_vowels.frameNStop = frameN  # exact frame index
                win.timeOnFlip(timer_vowels, 'tStopRefresh')  # time at next scr refresh
                timer_vowels.setAutoDraw(False)
        if timer_vowels.status == STARTED:  # only update if drawing
            timer_vowels.setText(str(max(round(routineTimer.getTime()-timer_vowels.tStart, 1), 0)))
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in phones_5_secs_recordingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "phones_5_secs_recording"-------
    for thisComponent in phones_5_secs_recordingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    vowels_5_secs.addData('textbox_4.started', textbox_4.tStartRefresh)
    vowels_5_secs.addData('textbox_4.stopped', textbox_4.tStopRefresh)
    # phone_5_secs_mic stop & responses
    phone_5_secs_mic.stop()  # sometimes helpful
    if not phone_5_secs_mic.savedFile:
        phone_5_secs_mic.savedFile = None
    # store data for vowels_5_secs (TrialHandler)
    vowels_5_secs.addData('phone_5_secs_mic.filename', phone_5_secs_mic.savedFile)
    vowels_5_secs.addData('phone_5_secs_mic.started', phone_5_secs_mic.tStart)
    vowels_5_secs.addData('phone_5_secs_mic.stopped', phone_5_secs_mic.tStop)
    vowels_5_secs.addData('timer_vowels.started', timer_vowels.tStartRefresh)
    vowels_5_secs.addData('timer_vowels.stopped', timer_vowels.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'vowels_5_secs'

# get names of stimulus parameters
if vowels_5_secs.trialList in ([], [None], None):
    params = []
else:
    params = vowels_5_secs.trialList[0].keys()
# save data for this loop
vowels_5_secs.saveAsExcel(filename + '.xlsx', sheetName='vowels_5_secs',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
vowels_5_secs.saveAsText(filename + 'vowels_5_secs.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "before_close_eyes"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
text_12.setText(before_close_eyes_text[language])
# keep track of which components have finished
before_close_eyesComponents = [key_resp_6, text_12]
for thisComponent in before_close_eyesComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
before_close_eyesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "before_close_eyes"-------
while continueRoutine:
    # get current time
    t = before_close_eyesClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=before_close_eyesClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_12* updates
    if text_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_12.frameNStart = frameN  # exact frame index
        text_12.tStart = t  # local t and not account for scr refresh
        text_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
        text_12.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in before_close_eyesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "before_close_eyes"-------
for thisComponent in before_close_eyesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_12.started', text_12.tStartRefresh)
thisExp.addData('text_12.stopped', text_12.tStopRefresh)
# the Routine "before_close_eyes" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "close_eyes"-------
continueRoutine = True
routineTimer.add(60.500000)
# update component parameters for each repeat
text_13.setText(close_eyes_text[language])
sound_4.setSound('1000', secs=0.5, hamming=True)
sound_4.setVolume(1.0, log=False)
# keep track of which components have finished
close_eyesComponents = [text_13, sound_4]
for thisComponent in close_eyesComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
close_eyesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "close_eyes"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = close_eyesClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=close_eyesClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_13* updates
    if text_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_13.frameNStart = frameN  # exact frame index
        text_13.tStart = t  # local t and not account for scr refresh
        text_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
        text_13.setAutoDraw(True)
    if text_13.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_13.tStartRefresh + 60.0-frameTolerance:
            # keep track of stop time/frame for later
            text_13.tStop = t  # not accounting for scr refresh
            text_13.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_13, 'tStopRefresh')  # time at next scr refresh
            text_13.setAutoDraw(False)
    # start/stop sound_4
    if sound_4.status == NOT_STARTED and tThisFlip >= 60.0-frameTolerance:
        # keep track of start time/frame for later
        sound_4.frameNStart = frameN  # exact frame index
        sound_4.tStart = t  # local t and not account for scr refresh
        sound_4.tStartRefresh = tThisFlipGlobal  # on global time
        sound_4.play(when=win)  # sync with win flip
    if sound_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > sound_4.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            sound_4.tStop = t  # not accounting for scr refresh
            sound_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(sound_4, 'tStopRefresh')  # time at next scr refresh
            sound_4.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in close_eyesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "close_eyes"-------
for thisComponent in close_eyesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_13.started', text_13.tStartRefresh)
thisExp.addData('text_13.stopped', text_13.tStopRefresh)
sound_4.stop()  # ensure sound has stopped at end of routine
thisExp.addData('sound_4.started', sound_4.tStartRefresh)
thisExp.addData('sound_4.stopped', sound_4.tStopRefresh)

# ------Prepare to start Routine "after_close_eyes"-------
continueRoutine = True
# update component parameters for each repeat
text_14.setText(after_close_eyes_text[language])
key_resp_22.keys = []
key_resp_22.rt = []
_key_resp_22_allKeys = []
# keep track of which components have finished
after_close_eyesComponents = [text_14, key_resp_22]
for thisComponent in after_close_eyesComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
after_close_eyesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "after_close_eyes"-------
while continueRoutine:
    # get current time
    t = after_close_eyesClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=after_close_eyesClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_14* updates
    if text_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_14.frameNStart = frameN  # exact frame index
        text_14.tStart = t  # local t and not account for scr refresh
        text_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
        text_14.setAutoDraw(True)
    
    # *key_resp_22* updates
    waitOnFlip = False
    if key_resp_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_22.frameNStart = frameN  # exact frame index
        key_resp_22.tStart = t  # local t and not account for scr refresh
        key_resp_22.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_22, 'tStartRefresh')  # time at next scr refresh
        key_resp_22.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_22.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_22.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_22.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_22.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_22_allKeys.extend(theseKeys)
        if len(_key_resp_22_allKeys):
            key_resp_22.keys = _key_resp_22_allKeys[-1].name  # just the last key pressed
            key_resp_22.rt = _key_resp_22_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in after_close_eyesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "after_close_eyes"-------
for thisComponent in after_close_eyesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_14.started', text_14.tStartRefresh)
thisExp.addData('text_14.stopped', text_14.tStopRefresh)
# check responses
if key_resp_22.keys in ['', [], None]:  # No response was made
    key_resp_22.keys = None
thisExp.addData('key_resp_22.keys',key_resp_22.keys)
if key_resp_22.keys != None:  # we had a response
    thisExp.addData('key_resp_22.rt', key_resp_22.rt)
thisExp.addData('key_resp_22.started', key_resp_22.tStartRefresh)
thisExp.addData('key_resp_22.stopped', key_resp_22.tStopRefresh)
thisExp.nextEntry()
# the Routine "after_close_eyes" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
affective_slide_01 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='affective_slide_01')
thisExp.addLoop(affective_slide_01)  # add the loop to the experiment
thisAffective_slide_01 = affective_slide_01.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisAffective_slide_01.rgb)
if thisAffective_slide_01 != None:
    for paramName in thisAffective_slide_01:
        exec('{} = thisAffective_slide_01[paramName]'.format(paramName))

for thisAffective_slide_01 in affective_slide_01:
    currentLoop = affective_slide_01
    # abbreviate parameter names if possible (e.g. rgb = thisAffective_slide_01.rgb)
    if thisAffective_slide_01 != None:
        for paramName in thisAffective_slide_01:
            exec('{} = thisAffective_slide_01[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "affective_slider"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_29.setText(affective_slider_instruction_text[language])
    arousel_slider_3.reset()
    pleasure_slider_3.reset()
    key_resp_36.keys = []
    key_resp_36.rt = []
    _key_resp_36_allKeys = []
    # keep track of which components have finished
    affective_sliderComponents = [text_29, arousel_slider_3, pleasure_slider_3, key_resp_36, arousal_low, arousal_high, pleasure_low, pleasure_high]
    for thisComponent in affective_sliderComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    affective_sliderClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "affective_slider"-------
    while continueRoutine:
        # get current time
        t = affective_sliderClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=affective_sliderClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_29* updates
        if text_29.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_29.frameNStart = frameN  # exact frame index
            text_29.tStart = t  # local t and not account for scr refresh
            text_29.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_29, 'tStartRefresh')  # time at next scr refresh
            text_29.setAutoDraw(True)
        
        # *arousel_slider_3* updates
        if arousel_slider_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            arousel_slider_3.frameNStart = frameN  # exact frame index
            arousel_slider_3.tStart = t  # local t and not account for scr refresh
            arousel_slider_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(arousel_slider_3, 'tStartRefresh')  # time at next scr refresh
            arousel_slider_3.setAutoDraw(True)
        
        # *pleasure_slider_3* updates
        if pleasure_slider_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pleasure_slider_3.frameNStart = frameN  # exact frame index
            pleasure_slider_3.tStart = t  # local t and not account for scr refresh
            pleasure_slider_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pleasure_slider_3, 'tStartRefresh')  # time at next scr refresh
            pleasure_slider_3.setAutoDraw(True)
        
        # *key_resp_36* updates
        waitOnFlip = False
        if key_resp_36.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_36.frameNStart = frameN  # exact frame index
            key_resp_36.tStart = t  # local t and not account for scr refresh
            key_resp_36.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_36, 'tStartRefresh')  # time at next scr refresh
            key_resp_36.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_36.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_36.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_36.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_36.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_36_allKeys.extend(theseKeys)
            if len(_key_resp_36_allKeys):
                key_resp_36.keys = _key_resp_36_allKeys[-1].name  # just the last key pressed
                key_resp_36.rt = _key_resp_36_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *arousal_low* updates
        if arousal_low.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            arousal_low.frameNStart = frameN  # exact frame index
            arousal_low.tStart = t  # local t and not account for scr refresh
            arousal_low.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(arousal_low, 'tStartRefresh')  # time at next scr refresh
            arousal_low.setAutoDraw(True)
        
        # *arousal_high* updates
        if arousal_high.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            arousal_high.frameNStart = frameN  # exact frame index
            arousal_high.tStart = t  # local t and not account for scr refresh
            arousal_high.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(arousal_high, 'tStartRefresh')  # time at next scr refresh
            arousal_high.setAutoDraw(True)
        
        # *pleasure_low* updates
        if pleasure_low.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pleasure_low.frameNStart = frameN  # exact frame index
            pleasure_low.tStart = t  # local t and not account for scr refresh
            pleasure_low.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pleasure_low, 'tStartRefresh')  # time at next scr refresh
            pleasure_low.setAutoDraw(True)
        
        # *pleasure_high* updates
        if pleasure_high.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pleasure_high.frameNStart = frameN  # exact frame index
            pleasure_high.tStart = t  # local t and not account for scr refresh
            pleasure_high.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pleasure_high, 'tStartRefresh')  # time at next scr refresh
            pleasure_high.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in affective_sliderComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "affective_slider"-------
    for thisComponent in affective_sliderComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    affective_slide_01.addData('text_29.started', text_29.tStartRefresh)
    affective_slide_01.addData('text_29.stopped', text_29.tStopRefresh)
    affective_slide_01.addData('arousel_slider_3.response', arousel_slider_3.getRating())
    affective_slide_01.addData('arousel_slider_3.rt', arousel_slider_3.getRT())
    affective_slide_01.addData('arousel_slider_3.started', arousel_slider_3.tStartRefresh)
    affective_slide_01.addData('arousel_slider_3.stopped', arousel_slider_3.tStopRefresh)
    affective_slide_01.addData('pleasure_slider_3.response', pleasure_slider_3.getRating())
    affective_slide_01.addData('pleasure_slider_3.rt', pleasure_slider_3.getRT())
    affective_slide_01.addData('pleasure_slider_3.started', pleasure_slider_3.tStartRefresh)
    affective_slide_01.addData('pleasure_slider_3.stopped', pleasure_slider_3.tStopRefresh)
    # check responses
    if key_resp_36.keys in ['', [], None]:  # No response was made
        key_resp_36.keys = None
    affective_slide_01.addData('key_resp_36.keys',key_resp_36.keys)
    if key_resp_36.keys != None:  # we had a response
        affective_slide_01.addData('key_resp_36.rt', key_resp_36.rt)
    affective_slide_01.addData('key_resp_36.started', key_resp_36.tStartRefresh)
    affective_slide_01.addData('key_resp_36.stopped', key_resp_36.tStopRefresh)
    affective_slide_01.addData('arousal_low.started', arousal_low.tStartRefresh)
    affective_slide_01.addData('arousal_low.stopped', arousal_low.tStopRefresh)
    affective_slide_01.addData('arousal_high.started', arousal_high.tStartRefresh)
    affective_slide_01.addData('arousal_high.stopped', arousal_high.tStopRefresh)
    affective_slide_01.addData('pleasure_low.started', pleasure_low.tStartRefresh)
    affective_slide_01.addData('pleasure_low.stopped', pleasure_low.tStopRefresh)
    affective_slide_01.addData('pleasure_high.started', pleasure_high.tStartRefresh)
    affective_slide_01.addData('pleasure_high.stopped', pleasure_high.tStopRefresh)
    # the Routine "affective_slider" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'affective_slide_01'

# get names of stimulus parameters
if affective_slide_01.trialList in ([], [None], None):
    params = []
else:
    params = affective_slide_01.trialList[0].keys()
# save data for this loop
affective_slide_01.saveAsExcel(filename + '.xlsx', sheetName='affective_slide_01',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
affective_slide_01.saveAsText(filename + 'affective_slide_01.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
PANAS_01 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(PANAS_path[language]),
    seed=None, name='PANAS_01')
thisExp.addLoop(PANAS_01)  # add the loop to the experiment
thisPANAS_01 = PANAS_01.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPANAS_01.rgb)
if thisPANAS_01 != None:
    for paramName in thisPANAS_01:
        exec('{} = thisPANAS_01[paramName]'.format(paramName))

for thisPANAS_01 in PANAS_01:
    currentLoop = PANAS_01
    # abbreviate parameter names if possible (e.g. rgb = thisPANAS_01.rgb)
    if thisPANAS_01 != None:
        for paramName in thisPANAS_01:
            exec('{} = thisPANAS_01[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "questionaire"-------
    continueRoutine = True
    # update component parameters for each repeat
    if language == 'de' :
        continueRoutine = False
    instructions_questionaire.setText(PANAS_text[language])
    question_slider.reset()
    question_text.setText(question)
    # keep track of which components have finished
    questionaireComponents = [instructions_questionaire, question_slider, question_text]
    for thisComponent in questionaireComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    questionaireClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "questionaire"-------
    while continueRoutine:
        # get current time
        t = questionaireClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=questionaireClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions_questionaire* updates
        if instructions_questionaire.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions_questionaire.frameNStart = frameN  # exact frame index
            instructions_questionaire.tStart = t  # local t and not account for scr refresh
            instructions_questionaire.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_questionaire, 'tStartRefresh')  # time at next scr refresh
            instructions_questionaire.setAutoDraw(True)
        
        # *question_slider* updates
        if question_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            question_slider.frameNStart = frameN  # exact frame index
            question_slider.tStart = t  # local t and not account for scr refresh
            question_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(question_slider, 'tStartRefresh')  # time at next scr refresh
            question_slider.setAutoDraw(True)
        
        # Check question_slider for response to end routine
        if question_slider.getRating() is not None and question_slider.status == STARTED:
            continueRoutine = False
        
        # *question_text* updates
        if question_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            question_text.frameNStart = frameN  # exact frame index
            question_text.tStart = t  # local t and not account for scr refresh
            question_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(question_text, 'tStartRefresh')  # time at next scr refresh
            question_text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in questionaireComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "questionaire"-------
    for thisComponent in questionaireComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    PANAS_01.addData('instructions_questionaire.started', instructions_questionaire.tStartRefresh)
    PANAS_01.addData('instructions_questionaire.stopped', instructions_questionaire.tStopRefresh)
    PANAS_01.addData('question_slider.response', question_slider.getRating())
    PANAS_01.addData('question_slider.rt', question_slider.getRT())
    PANAS_01.addData('question_slider.started', question_slider.tStartRefresh)
    PANAS_01.addData('question_slider.stopped', question_slider.tStopRefresh)
    # the Routine "questionaire" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'PANAS_01'

# get names of stimulus parameters
if PANAS_01.trialList in ([], [None], None):
    params = []
else:
    params = PANAS_01.trialList[0].keys()
# save data for this loop
PANAS_01.saveAsExcel(filename + '.xlsx', sheetName='PANAS_01',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
PANAS_01.saveAsText(filename + 'PANAS_01.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
PANAS_01_german = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(PANAS_path[language]),
    seed=None, name='PANAS_01_german')
thisExp.addLoop(PANAS_01_german)  # add the loop to the experiment
thisPANAS_01_german = PANAS_01_german.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPANAS_01_german.rgb)
if thisPANAS_01_german != None:
    for paramName in thisPANAS_01_german:
        exec('{} = thisPANAS_01_german[paramName]'.format(paramName))

for thisPANAS_01_german in PANAS_01_german:
    currentLoop = PANAS_01_german
    # abbreviate parameter names if possible (e.g. rgb = thisPANAS_01_german.rgb)
    if thisPANAS_01_german != None:
        for paramName in thisPANAS_01_german:
            exec('{} = thisPANAS_01_german[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "questionaire_german"-------
    continueRoutine = True
    # update component parameters for each repeat
    instructions_questionaire_4.setText(PANAS_text[language])
    question_slider_4.reset()
    question_text_4.setText(question)
    if language == 'en' :
        continueRoutine = False
    # keep track of which components have finished
    questionaire_germanComponents = [instructions_questionaire_4, question_slider_4, question_text_4]
    for thisComponent in questionaire_germanComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    questionaire_germanClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "questionaire_german"-------
    while continueRoutine:
        # get current time
        t = questionaire_germanClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=questionaire_germanClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions_questionaire_4* updates
        if instructions_questionaire_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions_questionaire_4.frameNStart = frameN  # exact frame index
            instructions_questionaire_4.tStart = t  # local t and not account for scr refresh
            instructions_questionaire_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_questionaire_4, 'tStartRefresh')  # time at next scr refresh
            instructions_questionaire_4.setAutoDraw(True)
        
        # *question_slider_4* updates
        if question_slider_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            question_slider_4.frameNStart = frameN  # exact frame index
            question_slider_4.tStart = t  # local t and not account for scr refresh
            question_slider_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(question_slider_4, 'tStartRefresh')  # time at next scr refresh
            question_slider_4.setAutoDraw(True)
        
        # Check question_slider_4 for response to end routine
        if question_slider_4.getRating() is not None and question_slider_4.status == STARTED:
            continueRoutine = False
        
        # *question_text_4* updates
        if question_text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            question_text_4.frameNStart = frameN  # exact frame index
            question_text_4.tStart = t  # local t and not account for scr refresh
            question_text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(question_text_4, 'tStartRefresh')  # time at next scr refresh
            question_text_4.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in questionaire_germanComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "questionaire_german"-------
    for thisComponent in questionaire_germanComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    PANAS_01_german.addData('instructions_questionaire_4.started', instructions_questionaire_4.tStartRefresh)
    PANAS_01_german.addData('instructions_questionaire_4.stopped', instructions_questionaire_4.tStopRefresh)
    PANAS_01_german.addData('question_slider_4.response', question_slider_4.getRating())
    PANAS_01_german.addData('question_slider_4.rt', question_slider_4.getRT())
    PANAS_01_german.addData('question_slider_4.started', question_slider_4.tStartRefresh)
    PANAS_01_german.addData('question_slider_4.stopped', question_slider_4.tStopRefresh)
    # the Routine "questionaire_german" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'PANAS_01_german'

# get names of stimulus parameters
if PANAS_01_german.trialList in ([], [None], None):
    params = []
else:
    params = PANAS_01_german.trialList[0].keys()
# save data for this loop
PANAS_01_german.saveAsExcel(filename + '.xlsx', sheetName='PANAS_01_german',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
PANAS_01_german.saveAsText(filename + 'PANAS_01_german.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "instruction_play_game"-------
continueRoutine = True
# update component parameters for each repeat
text.setText(instruction_play_game_text[language])
key_resp_47.keys = []
key_resp_47.rt = []
_key_resp_47_allKeys = []
# keep track of which components have finished
instruction_play_gameComponents = [text, key_resp_47]
for thisComponent in instruction_play_gameComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruction_play_gameClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruction_play_game"-------
while continueRoutine:
    # get current time
    t = instruction_play_gameClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruction_play_gameClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp_47* updates
    waitOnFlip = False
    if key_resp_47.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_47.frameNStart = frameN  # exact frame index
        key_resp_47.tStart = t  # local t and not account for scr refresh
        key_resp_47.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_47, 'tStartRefresh')  # time at next scr refresh
        key_resp_47.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_47.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_47.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_47.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_47.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_47_allKeys.extend(theseKeys)
        if len(_key_resp_47_allKeys):
            key_resp_47.keys = _key_resp_47_allKeys[-1].name  # just the last key pressed
            key_resp_47.rt = _key_resp_47_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction_play_gameComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction_play_game"-------
for thisComponent in instruction_play_gameComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_resp_47.keys in ['', [], None]:  # No response was made
    key_resp_47.keys = None
thisExp.addData('key_resp_47.keys',key_resp_47.keys)
if key_resp_47.keys != None:  # we had a response
    thisExp.addData('key_resp_47.rt', key_resp_47.rt)
thisExp.addData('key_resp_47.started', key_resp_47.tStartRefresh)
thisExp.addData('key_resp_47.stopped', key_resp_47.tStopRefresh)
thisExp.nextEntry()
# the Routine "instruction_play_game" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "play_game"-------
continueRoutine = True
# update component parameters for each repeat
os.system('start steam://rungameid/3350')
time.sleep(play_game_duration)
os.system('taskkill /IM steam.exe')
# keep track of which components have finished
play_gameComponents = []
for thisComponent in play_gameComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
play_gameClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "play_game"-------
while continueRoutine:
    # get current time
    t = play_gameClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=play_gameClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in play_gameComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "play_game"-------
for thisComponent in play_gameComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "play_game" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
nasa_txl = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(nasa_path[language]),
    seed=None, name='nasa_txl')
thisExp.addLoop(nasa_txl)  # add the loop to the experiment
thisNasa_txl = nasa_txl.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNasa_txl.rgb)
if thisNasa_txl != None:
    for paramName in thisNasa_txl:
        exec('{} = thisNasa_txl[paramName]'.format(paramName))

for thisNasa_txl in nasa_txl:
    currentLoop = nasa_txl
    # abbreviate parameter names if possible (e.g. rgb = thisNasa_txl.rgb)
    if thisNasa_txl != None:
        for paramName in thisNasa_txl:
            exec('{} = thisNasa_txl[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "nasa_txl_questionaire"-------
    continueRoutine = True
    # update component parameters for each repeat
    instructions_questionaire_2.setText(instruction_question)
    questionaire_answer.reset()
    question_text_2.setText(question)
    if language == 'de':
        continueRoutine = False
    # keep track of which components have finished
    nasa_txl_questionaireComponents = [instructions_questionaire_2, questionaire_answer, question_text_2, polygon]
    for thisComponent in nasa_txl_questionaireComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    nasa_txl_questionaireClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "nasa_txl_questionaire"-------
    while continueRoutine:
        # get current time
        t = nasa_txl_questionaireClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=nasa_txl_questionaireClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions_questionaire_2* updates
        if instructions_questionaire_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions_questionaire_2.frameNStart = frameN  # exact frame index
            instructions_questionaire_2.tStart = t  # local t and not account for scr refresh
            instructions_questionaire_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_questionaire_2, 'tStartRefresh')  # time at next scr refresh
            instructions_questionaire_2.setAutoDraw(True)
        # *questionaire_answer* updates
        if questionaire_answer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            questionaire_answer.frameNStart = frameN  # exact frame index
            questionaire_answer.tStart = t  # local t and not account for scr refresh
            questionaire_answer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(questionaire_answer, 'tStartRefresh')  # time at next scr refresh
            questionaire_answer.setAutoDraw(True)
        continueRoutine &= questionaire_answer.noResponse  # a response ends the trial
        
        # *question_text_2* updates
        if question_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            question_text_2.frameNStart = frameN  # exact frame index
            question_text_2.tStart = t  # local t and not account for scr refresh
            question_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(question_text_2, 'tStartRefresh')  # time at next scr refresh
            question_text_2.setAutoDraw(True)
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            polygon.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in nasa_txl_questionaireComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "nasa_txl_questionaire"-------
    for thisComponent in nasa_txl_questionaireComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    nasa_txl.addData('instructions_questionaire_2.started', instructions_questionaire_2.tStartRefresh)
    nasa_txl.addData('instructions_questionaire_2.stopped', instructions_questionaire_2.tStopRefresh)
    # store data for nasa_txl (TrialHandler)
    nasa_txl.addData('questionaire_answer.response', questionaire_answer.getRating())
    nasa_txl.addData('questionaire_answer.rt', questionaire_answer.getRT())
    nasa_txl.addData('questionaire_answer.started', questionaire_answer.tStartRefresh)
    nasa_txl.addData('questionaire_answer.stopped', questionaire_answer.tStopRefresh)
    # the Routine "nasa_txl_questionaire" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'nasa_txl'

# get names of stimulus parameters
if nasa_txl.trialList in ([], [None], None):
    params = []
else:
    params = nasa_txl.trialList[0].keys()
# save data for this loop
nasa_txl.saveAsExcel(filename + '.xlsx', sheetName='nasa_txl',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
nasa_txl.saveAsText(filename + 'nasa_txl.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
nasa_txl_german = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(nasa_path[language]),
    seed=None, name='nasa_txl_german')
thisExp.addLoop(nasa_txl_german)  # add the loop to the experiment
thisNasa_txl_german = nasa_txl_german.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNasa_txl_german.rgb)
if thisNasa_txl_german != None:
    for paramName in thisNasa_txl_german:
        exec('{} = thisNasa_txl_german[paramName]'.format(paramName))

for thisNasa_txl_german in nasa_txl_german:
    currentLoop = nasa_txl_german
    # abbreviate parameter names if possible (e.g. rgb = thisNasa_txl_german.rgb)
    if thisNasa_txl_german != None:
        for paramName in thisNasa_txl_german:
            exec('{} = thisNasa_txl_german[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "nasa_txl_questionaire_german"-------
    continueRoutine = True
    # update component parameters for each repeat
    instructions_questionaire_3.setText(instruction_question)
    questionaire_answer_2.reset()
    question_text_3.setText(question)
    if language == 'en':
        continueRoutine = False
    # keep track of which components have finished
    nasa_txl_questionaire_germanComponents = [instructions_questionaire_3, questionaire_answer_2, question_text_3, polygon_2]
    for thisComponent in nasa_txl_questionaire_germanComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    nasa_txl_questionaire_germanClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "nasa_txl_questionaire_german"-------
    while continueRoutine:
        # get current time
        t = nasa_txl_questionaire_germanClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=nasa_txl_questionaire_germanClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions_questionaire_3* updates
        if instructions_questionaire_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions_questionaire_3.frameNStart = frameN  # exact frame index
            instructions_questionaire_3.tStart = t  # local t and not account for scr refresh
            instructions_questionaire_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_questionaire_3, 'tStartRefresh')  # time at next scr refresh
            instructions_questionaire_3.setAutoDraw(True)
        # *questionaire_answer_2* updates
        if questionaire_answer_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            questionaire_answer_2.frameNStart = frameN  # exact frame index
            questionaire_answer_2.tStart = t  # local t and not account for scr refresh
            questionaire_answer_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(questionaire_answer_2, 'tStartRefresh')  # time at next scr refresh
            questionaire_answer_2.setAutoDraw(True)
        continueRoutine &= questionaire_answer_2.noResponse  # a response ends the trial
        
        # *question_text_3* updates
        if question_text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            question_text_3.frameNStart = frameN  # exact frame index
            question_text_3.tStart = t  # local t and not account for scr refresh
            question_text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(question_text_3, 'tStartRefresh')  # time at next scr refresh
            question_text_3.setAutoDraw(True)
        
        # *polygon_2* updates
        if polygon_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_2.frameNStart = frameN  # exact frame index
            polygon_2.tStart = t  # local t and not account for scr refresh
            polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
            polygon_2.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in nasa_txl_questionaire_germanComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "nasa_txl_questionaire_german"-------
    for thisComponent in nasa_txl_questionaire_germanComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    nasa_txl_german.addData('instructions_questionaire_3.started', instructions_questionaire_3.tStartRefresh)
    nasa_txl_german.addData('instructions_questionaire_3.stopped', instructions_questionaire_3.tStopRefresh)
    # store data for nasa_txl_german (TrialHandler)
    nasa_txl_german.addData('questionaire_answer_2.response', questionaire_answer_2.getRating())
    nasa_txl_german.addData('questionaire_answer_2.rt', questionaire_answer_2.getRT())
    nasa_txl_german.addData('questionaire_answer_2.started', questionaire_answer_2.tStartRefresh)
    nasa_txl_german.addData('questionaire_answer_2.stopped', questionaire_answer_2.tStopRefresh)
    # the Routine "nasa_txl_questionaire_german" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'nasa_txl_german'

# get names of stimulus parameters
if nasa_txl_german.trialList in ([], [None], None):
    params = []
else:
    params = nasa_txl_german.trialList[0].keys()
# save data for this loop
nasa_txl_german.saveAsExcel(filename + '.xlsx', sheetName='nasa_txl_german',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
nasa_txl_german.saveAsText(filename + 'nasa_txl_german.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
nasa_txl_comp = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(nasa_comparison_path[language]),
    seed=None, name='nasa_txl_comp')
thisExp.addLoop(nasa_txl_comp)  # add the loop to the experiment
thisNasa_txl_comp = nasa_txl_comp.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNasa_txl_comp.rgb)
if thisNasa_txl_comp != None:
    for paramName in thisNasa_txl_comp:
        exec('{} = thisNasa_txl_comp[paramName]'.format(paramName))

for thisNasa_txl_comp in nasa_txl_comp:
    currentLoop = nasa_txl_comp
    # abbreviate parameter names if possible (e.g. rgb = thisNasa_txl_comp.rgb)
    if thisNasa_txl_comp != None:
        for paramName in thisNasa_txl_comp:
            exec('{} = thisNasa_txl_comp[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "nasa_txl_comparison"-------
    continueRoutine = True
    # update component parameters for each repeat
    button_3.setText(word1)
    button_4.setText(word2)
    nasa_comparison_textf.setText(nasa_comparison_text[language])
    description1_textfield.setText(description1)
    description2_textfield.setText(description2)
    # keep track of which components have finished
    nasa_txl_comparisonComponents = [button_3, button_4, nasa_comparison_textf, description1_textfield, description2_textfield]
    for thisComponent in nasa_txl_comparisonComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    nasa_txl_comparisonClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "nasa_txl_comparison"-------
    while continueRoutine:
        # get current time
        t = nasa_txl_comparisonClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=nasa_txl_comparisonClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *button_3* updates
        if button_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button_3.frameNStart = frameN  # exact frame index
            button_3.tStart = t  # local t and not account for scr refresh
            button_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_3, 'tStartRefresh')  # time at next scr refresh
            button_3.setAutoDraw(True)
        if button_3.status == STARTED:
            # check whether button_3 has been pressed
            if button_3.isClicked:
                if not button_3.wasClicked:
                    button_3.timesOn.append(button_3.buttonClock.getTime()) # store time of first click
                    button_3.timesOff.append(button_3.buttonClock.getTime()) # store time clicked until
                else:
                    button_3.timesOff[-1] = button_3.buttonClock.getTime() # update time clicked until
                if not button_3.wasClicked:
                    continueRoutine = False  # end routine when button_3 is clicked
                    None
                button_3.wasClicked = True  # if button_3 is still clicked next frame, it is not a new click
            else:
                button_3.wasClicked = False  # if button_3 is clicked next frame, it is a new click
        else:
            button_3.buttonClock.reset() # keep clock at 0 if button hasn't started / has finished
            button_3.wasClicked = False  # if button_3 is clicked next frame, it is a new click
        
        # *button_4* updates
        if button_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button_4.frameNStart = frameN  # exact frame index
            button_4.tStart = t  # local t and not account for scr refresh
            button_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_4, 'tStartRefresh')  # time at next scr refresh
            button_4.setAutoDraw(True)
        if button_4.status == STARTED:
            # check whether button_4 has been pressed
            if button_4.isClicked:
                if not button_4.wasClicked:
                    button_4.timesOn.append(globalClock.getTime()) # store time of first click
                    button_4.timesOff.append(globalClock.getTime()) # store time clicked until
                else:
                    button_4.timesOff[-1] = globalClock.getTime() # update time clicked until
                if not button_4.wasClicked:
                    continueRoutine = False  # end routine when button_4 is clicked
                    None
                button_4.wasClicked = True  # if button_4 is still clicked next frame, it is not a new click
            else:
                button_4.wasClicked = False  # if button_4 is clicked next frame, it is a new click
        else:
            button_4.buttonClock.reset() # keep clock at 0 if button hasn't started / has finished
            button_4.wasClicked = False  # if button_4 is clicked next frame, it is a new click
        
        # *nasa_comparison_textf* updates
        if nasa_comparison_textf.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            nasa_comparison_textf.frameNStart = frameN  # exact frame index
            nasa_comparison_textf.tStart = t  # local t and not account for scr refresh
            nasa_comparison_textf.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nasa_comparison_textf, 'tStartRefresh')  # time at next scr refresh
            nasa_comparison_textf.setAutoDraw(True)
        
        # *description1_textfield* updates
        if description1_textfield.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            description1_textfield.frameNStart = frameN  # exact frame index
            description1_textfield.tStart = t  # local t and not account for scr refresh
            description1_textfield.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(description1_textfield, 'tStartRefresh')  # time at next scr refresh
            description1_textfield.setAutoDraw(True)
        
        # *description2_textfield* updates
        if description2_textfield.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            description2_textfield.frameNStart = frameN  # exact frame index
            description2_textfield.tStart = t  # local t and not account for scr refresh
            description2_textfield.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(description2_textfield, 'tStartRefresh')  # time at next scr refresh
            description2_textfield.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in nasa_txl_comparisonComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "nasa_txl_comparison"-------
    for thisComponent in nasa_txl_comparisonComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    nasa_txl_comp.addData('button_3.started', button_3.tStartRefresh)
    nasa_txl_comp.addData('button_3.stopped', button_3.tStopRefresh)
    nasa_txl_comp.addData('button_3.numClicks', button_3.numClicks)
    if button_3.numClicks:
       nasa_txl_comp.addData('button_3.timesOn', button_3.timesOn)
       nasa_txl_comp.addData('button_3.timesOff', button_3.timesOff)
    else:
       nasa_txl_comp.addData('button_3.timesOn', "")
       nasa_txl_comp.addData('button_3.timesOff', "")
    nasa_txl_comp.addData('button_4.numClicks', button_4.numClicks)
    if button_4.numClicks:
       nasa_txl_comp.addData('button_4.timesOn', button_4.timesOn)
       nasa_txl_comp.addData('button_4.timesOff', button_4.timesOff)
    else:
       nasa_txl_comp.addData('button_4.timesOn', "")
       nasa_txl_comp.addData('button_4.timesOff', "")
    nasa_txl_comp.addData('nasa_comparison_textf.started', nasa_comparison_textf.tStartRefresh)
    nasa_txl_comp.addData('nasa_comparison_textf.stopped', nasa_comparison_textf.tStopRefresh)
    nasa_txl_comp.addData('description1_textfield.started', description1_textfield.tStartRefresh)
    nasa_txl_comp.addData('description1_textfield.stopped', description1_textfield.tStopRefresh)
    nasa_txl_comp.addData('description2_textfield.started', description2_textfield.tStartRefresh)
    nasa_txl_comp.addData('description2_textfield.stopped', description2_textfield.tStopRefresh)
    # the Routine "nasa_txl_comparison" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'nasa_txl_comp'

# get names of stimulus parameters
if nasa_txl_comp.trialList in ([], [None], None):
    params = []
else:
    params = nasa_txl_comp.trialList[0].keys()
# save data for this loop
nasa_txl_comp.saveAsExcel(filename + '.xlsx', sheetName='nasa_txl_comp',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
nasa_txl_comp.saveAsText(filename + 'nasa_txl_comp.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
affective_slider_02 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='affective_slider_02')
thisExp.addLoop(affective_slider_02)  # add the loop to the experiment
thisAffective_slider_02 = affective_slider_02.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisAffective_slider_02.rgb)
if thisAffective_slider_02 != None:
    for paramName in thisAffective_slider_02:
        exec('{} = thisAffective_slider_02[paramName]'.format(paramName))

for thisAffective_slider_02 in affective_slider_02:
    currentLoop = affective_slider_02
    # abbreviate parameter names if possible (e.g. rgb = thisAffective_slider_02.rgb)
    if thisAffective_slider_02 != None:
        for paramName in thisAffective_slider_02:
            exec('{} = thisAffective_slider_02[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "affective_slider"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_29.setText(affective_slider_instruction_text[language])
    arousel_slider_3.reset()
    pleasure_slider_3.reset()
    key_resp_36.keys = []
    key_resp_36.rt = []
    _key_resp_36_allKeys = []
    # keep track of which components have finished
    affective_sliderComponents = [text_29, arousel_slider_3, pleasure_slider_3, key_resp_36, arousal_low, arousal_high, pleasure_low, pleasure_high]
    for thisComponent in affective_sliderComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    affective_sliderClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "affective_slider"-------
    while continueRoutine:
        # get current time
        t = affective_sliderClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=affective_sliderClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_29* updates
        if text_29.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_29.frameNStart = frameN  # exact frame index
            text_29.tStart = t  # local t and not account for scr refresh
            text_29.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_29, 'tStartRefresh')  # time at next scr refresh
            text_29.setAutoDraw(True)
        
        # *arousel_slider_3* updates
        if arousel_slider_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            arousel_slider_3.frameNStart = frameN  # exact frame index
            arousel_slider_3.tStart = t  # local t and not account for scr refresh
            arousel_slider_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(arousel_slider_3, 'tStartRefresh')  # time at next scr refresh
            arousel_slider_3.setAutoDraw(True)
        
        # *pleasure_slider_3* updates
        if pleasure_slider_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pleasure_slider_3.frameNStart = frameN  # exact frame index
            pleasure_slider_3.tStart = t  # local t and not account for scr refresh
            pleasure_slider_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pleasure_slider_3, 'tStartRefresh')  # time at next scr refresh
            pleasure_slider_3.setAutoDraw(True)
        
        # *key_resp_36* updates
        waitOnFlip = False
        if key_resp_36.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_36.frameNStart = frameN  # exact frame index
            key_resp_36.tStart = t  # local t and not account for scr refresh
            key_resp_36.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_36, 'tStartRefresh')  # time at next scr refresh
            key_resp_36.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_36.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_36.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_36.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_36.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_36_allKeys.extend(theseKeys)
            if len(_key_resp_36_allKeys):
                key_resp_36.keys = _key_resp_36_allKeys[-1].name  # just the last key pressed
                key_resp_36.rt = _key_resp_36_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *arousal_low* updates
        if arousal_low.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            arousal_low.frameNStart = frameN  # exact frame index
            arousal_low.tStart = t  # local t and not account for scr refresh
            arousal_low.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(arousal_low, 'tStartRefresh')  # time at next scr refresh
            arousal_low.setAutoDraw(True)
        
        # *arousal_high* updates
        if arousal_high.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            arousal_high.frameNStart = frameN  # exact frame index
            arousal_high.tStart = t  # local t and not account for scr refresh
            arousal_high.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(arousal_high, 'tStartRefresh')  # time at next scr refresh
            arousal_high.setAutoDraw(True)
        
        # *pleasure_low* updates
        if pleasure_low.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pleasure_low.frameNStart = frameN  # exact frame index
            pleasure_low.tStart = t  # local t and not account for scr refresh
            pleasure_low.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pleasure_low, 'tStartRefresh')  # time at next scr refresh
            pleasure_low.setAutoDraw(True)
        
        # *pleasure_high* updates
        if pleasure_high.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pleasure_high.frameNStart = frameN  # exact frame index
            pleasure_high.tStart = t  # local t and not account for scr refresh
            pleasure_high.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pleasure_high, 'tStartRefresh')  # time at next scr refresh
            pleasure_high.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in affective_sliderComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "affective_slider"-------
    for thisComponent in affective_sliderComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    affective_slider_02.addData('text_29.started', text_29.tStartRefresh)
    affective_slider_02.addData('text_29.stopped', text_29.tStopRefresh)
    affective_slider_02.addData('arousel_slider_3.response', arousel_slider_3.getRating())
    affective_slider_02.addData('arousel_slider_3.rt', arousel_slider_3.getRT())
    affective_slider_02.addData('arousel_slider_3.started', arousel_slider_3.tStartRefresh)
    affective_slider_02.addData('arousel_slider_3.stopped', arousel_slider_3.tStopRefresh)
    affective_slider_02.addData('pleasure_slider_3.response', pleasure_slider_3.getRating())
    affective_slider_02.addData('pleasure_slider_3.rt', pleasure_slider_3.getRT())
    affective_slider_02.addData('pleasure_slider_3.started', pleasure_slider_3.tStartRefresh)
    affective_slider_02.addData('pleasure_slider_3.stopped', pleasure_slider_3.tStopRefresh)
    # check responses
    if key_resp_36.keys in ['', [], None]:  # No response was made
        key_resp_36.keys = None
    affective_slider_02.addData('key_resp_36.keys',key_resp_36.keys)
    if key_resp_36.keys != None:  # we had a response
        affective_slider_02.addData('key_resp_36.rt', key_resp_36.rt)
    affective_slider_02.addData('key_resp_36.started', key_resp_36.tStartRefresh)
    affective_slider_02.addData('key_resp_36.stopped', key_resp_36.tStopRefresh)
    affective_slider_02.addData('arousal_low.started', arousal_low.tStartRefresh)
    affective_slider_02.addData('arousal_low.stopped', arousal_low.tStopRefresh)
    affective_slider_02.addData('arousal_high.started', arousal_high.tStartRefresh)
    affective_slider_02.addData('arousal_high.stopped', arousal_high.tStopRefresh)
    affective_slider_02.addData('pleasure_low.started', pleasure_low.tStartRefresh)
    affective_slider_02.addData('pleasure_low.stopped', pleasure_low.tStopRefresh)
    affective_slider_02.addData('pleasure_high.started', pleasure_high.tStartRefresh)
    affective_slider_02.addData('pleasure_high.stopped', pleasure_high.tStopRefresh)
    # the Routine "affective_slider" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'affective_slider_02'

# get names of stimulus parameters
if affective_slider_02.trialList in ([], [None], None):
    params = []
else:
    params = affective_slider_02.trialList[0].keys()
# save data for this loop
affective_slider_02.saveAsExcel(filename + '.xlsx', sheetName='affective_slider_02',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
affective_slider_02.saveAsText(filename + 'affective_slider_02.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
PANAS_02 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(PANAS_path[language]),
    seed=None, name='PANAS_02')
thisExp.addLoop(PANAS_02)  # add the loop to the experiment
thisPANAS_02 = PANAS_02.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPANAS_02.rgb)
if thisPANAS_02 != None:
    for paramName in thisPANAS_02:
        exec('{} = thisPANAS_02[paramName]'.format(paramName))

for thisPANAS_02 in PANAS_02:
    currentLoop = PANAS_02
    # abbreviate parameter names if possible (e.g. rgb = thisPANAS_02.rgb)
    if thisPANAS_02 != None:
        for paramName in thisPANAS_02:
            exec('{} = thisPANAS_02[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "questionaire"-------
    continueRoutine = True
    # update component parameters for each repeat
    if language == 'de' :
        continueRoutine = False
    instructions_questionaire.setText(PANAS_text[language])
    question_slider.reset()
    question_text.setText(question)
    # keep track of which components have finished
    questionaireComponents = [instructions_questionaire, question_slider, question_text]
    for thisComponent in questionaireComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    questionaireClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "questionaire"-------
    while continueRoutine:
        # get current time
        t = questionaireClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=questionaireClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions_questionaire* updates
        if instructions_questionaire.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions_questionaire.frameNStart = frameN  # exact frame index
            instructions_questionaire.tStart = t  # local t and not account for scr refresh
            instructions_questionaire.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_questionaire, 'tStartRefresh')  # time at next scr refresh
            instructions_questionaire.setAutoDraw(True)
        
        # *question_slider* updates
        if question_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            question_slider.frameNStart = frameN  # exact frame index
            question_slider.tStart = t  # local t and not account for scr refresh
            question_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(question_slider, 'tStartRefresh')  # time at next scr refresh
            question_slider.setAutoDraw(True)
        
        # Check question_slider for response to end routine
        if question_slider.getRating() is not None and question_slider.status == STARTED:
            continueRoutine = False
        
        # *question_text* updates
        if question_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            question_text.frameNStart = frameN  # exact frame index
            question_text.tStart = t  # local t and not account for scr refresh
            question_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(question_text, 'tStartRefresh')  # time at next scr refresh
            question_text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in questionaireComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "questionaire"-------
    for thisComponent in questionaireComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    PANAS_02.addData('instructions_questionaire.started', instructions_questionaire.tStartRefresh)
    PANAS_02.addData('instructions_questionaire.stopped', instructions_questionaire.tStopRefresh)
    PANAS_02.addData('question_slider.response', question_slider.getRating())
    PANAS_02.addData('question_slider.rt', question_slider.getRT())
    PANAS_02.addData('question_slider.started', question_slider.tStartRefresh)
    PANAS_02.addData('question_slider.stopped', question_slider.tStopRefresh)
    # the Routine "questionaire" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'PANAS_02'

# get names of stimulus parameters
if PANAS_02.trialList in ([], [None], None):
    params = []
else:
    params = PANAS_02.trialList[0].keys()
# save data for this loop
PANAS_02.saveAsExcel(filename + '.xlsx', sheetName='PANAS_02',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
PANAS_02.saveAsText(filename + 'PANAS_02.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
PANAS_02_german = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(PANAS_path[language]),
    seed=None, name='PANAS_02_german')
thisExp.addLoop(PANAS_02_german)  # add the loop to the experiment
thisPANAS_02_german = PANAS_02_german.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPANAS_02_german.rgb)
if thisPANAS_02_german != None:
    for paramName in thisPANAS_02_german:
        exec('{} = thisPANAS_02_german[paramName]'.format(paramName))

for thisPANAS_02_german in PANAS_02_german:
    currentLoop = PANAS_02_german
    # abbreviate parameter names if possible (e.g. rgb = thisPANAS_02_german.rgb)
    if thisPANAS_02_german != None:
        for paramName in thisPANAS_02_german:
            exec('{} = thisPANAS_02_german[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "questionaire_german"-------
    continueRoutine = True
    # update component parameters for each repeat
    instructions_questionaire_4.setText(PANAS_text[language])
    question_slider_4.reset()
    question_text_4.setText(question)
    if language == 'en' :
        continueRoutine = False
    # keep track of which components have finished
    questionaire_germanComponents = [instructions_questionaire_4, question_slider_4, question_text_4]
    for thisComponent in questionaire_germanComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    questionaire_germanClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "questionaire_german"-------
    while continueRoutine:
        # get current time
        t = questionaire_germanClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=questionaire_germanClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions_questionaire_4* updates
        if instructions_questionaire_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions_questionaire_4.frameNStart = frameN  # exact frame index
            instructions_questionaire_4.tStart = t  # local t and not account for scr refresh
            instructions_questionaire_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_questionaire_4, 'tStartRefresh')  # time at next scr refresh
            instructions_questionaire_4.setAutoDraw(True)
        
        # *question_slider_4* updates
        if question_slider_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            question_slider_4.frameNStart = frameN  # exact frame index
            question_slider_4.tStart = t  # local t and not account for scr refresh
            question_slider_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(question_slider_4, 'tStartRefresh')  # time at next scr refresh
            question_slider_4.setAutoDraw(True)
        
        # Check question_slider_4 for response to end routine
        if question_slider_4.getRating() is not None and question_slider_4.status == STARTED:
            continueRoutine = False
        
        # *question_text_4* updates
        if question_text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            question_text_4.frameNStart = frameN  # exact frame index
            question_text_4.tStart = t  # local t and not account for scr refresh
            question_text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(question_text_4, 'tStartRefresh')  # time at next scr refresh
            question_text_4.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in questionaire_germanComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "questionaire_german"-------
    for thisComponent in questionaire_germanComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    PANAS_02_german.addData('instructions_questionaire_4.started', instructions_questionaire_4.tStartRefresh)
    PANAS_02_german.addData('instructions_questionaire_4.stopped', instructions_questionaire_4.tStopRefresh)
    PANAS_02_german.addData('question_slider_4.response', question_slider_4.getRating())
    PANAS_02_german.addData('question_slider_4.rt', question_slider_4.getRT())
    PANAS_02_german.addData('question_slider_4.started', question_slider_4.tStartRefresh)
    PANAS_02_german.addData('question_slider_4.stopped', question_slider_4.tStopRefresh)
    # the Routine "questionaire_german" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'PANAS_02_german'

# get names of stimulus parameters
if PANAS_02_german.trialList in ([], [None], None):
    params = []
else:
    params = PANAS_02_german.trialList[0].keys()
# save data for this loop
PANAS_02_german.saveAsExcel(filename + '.xlsx', sheetName='PANAS_02_german',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
PANAS_02_german.saveAsText(filename + 'PANAS_02_german.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "introduction_60_sec_mood"-------
continueRoutine = True
# update component parameters for each repeat
text_3.setText(instruction_60_sec_mood_text[language])
key_resp_12.keys = []
key_resp_12.rt = []
_key_resp_12_allKeys = []
# keep track of which components have finished
introduction_60_sec_moodComponents = [text_3, key_resp_12]
for thisComponent in introduction_60_sec_moodComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introduction_60_sec_moodClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introduction_60_sec_mood"-------
while continueRoutine:
    # get current time
    t = introduction_60_sec_moodClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introduction_60_sec_moodClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # *key_resp_12* updates
    waitOnFlip = False
    if key_resp_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_12.frameNStart = frameN  # exact frame index
        key_resp_12.tStart = t  # local t and not account for scr refresh
        key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
        key_resp_12.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_12.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_12.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_12_allKeys.extend(theseKeys)
        if len(_key_resp_12_allKeys):
            key_resp_12.keys = _key_resp_12_allKeys[-1].name  # just the last key pressed
            key_resp_12.rt = _key_resp_12_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introduction_60_sec_moodComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introduction_60_sec_mood"-------
for thisComponent in introduction_60_sec_moodComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
# check responses
if key_resp_12.keys in ['', [], None]:  # No response was made
    key_resp_12.keys = None
thisExp.addData('key_resp_12.keys',key_resp_12.keys)
if key_resp_12.keys != None:  # we had a response
    thisExp.addData('key_resp_12.rt', key_resp_12.rt)
thisExp.addData('key_resp_12.started', key_resp_12.tStartRefresh)
thisExp.addData('key_resp_12.stopped', key_resp_12.tStopRefresh)
thisExp.nextEntry()
# the Routine "introduction_60_sec_mood" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "routine_60_Sec_mood"-------
continueRoutine = True
# update component parameters for each repeat
mood_voice.setText(mood_text[language])
mood_60_secs = microphone.AdvAudioCapture(name='mood_60_secs', saveDir=wavDirName, stereo=False, chnl=0)
key_resp_11.keys = []
key_resp_11.rt = []
_key_resp_11_allKeys = []
# keep track of which components have finished
routine_60_Sec_moodComponents = [mood_voice, mood_60_secs, Timer, key_resp_11, recording_image]
for thisComponent in routine_60_Sec_moodComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
routine_60_Sec_moodClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "routine_60_Sec_mood"-------
while continueRoutine:
    # get current time
    t = routine_60_Sec_moodClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routine_60_Sec_moodClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *mood_voice* updates
    if mood_voice.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        mood_voice.frameNStart = frameN  # exact frame index
        mood_voice.tStart = t  # local t and not account for scr refresh
        mood_voice.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mood_voice, 'tStartRefresh')  # time at next scr refresh
        mood_voice.setAutoDraw(True)
    
    # *mood_60_secs* updates
    if mood_60_secs.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        mood_60_secs.frameNStart = frameN  # exact frame index
        mood_60_secs.tStart = t  # local t and not account for scr refresh
        mood_60_secs.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mood_60_secs, 'tStartRefresh')  # time at next scr refresh
        mood_60_secs.status = STARTED
        mood_60_secs.record(sec=7200, block=False)  # start the recording thread
    
    if mood_60_secs.status == STARTED and not mood_60_secs.recorder.running:
        mood_60_secs.status = FINISHED
    
    # *Timer* updates
    if Timer.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        Timer.frameNStart = frameN  # exact frame index
        Timer.tStart = t  # local t and not account for scr refresh
        Timer.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Timer, 'tStartRefresh')  # time at next scr refresh
        Timer.setAutoDraw(True)
    if Timer.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Timer.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            Timer.tStop = t  # not accounting for scr refresh
            Timer.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Timer, 'tStopRefresh')  # time at next scr refresh
            Timer.setAutoDraw(False)
    if Timer.status == STARTED:  # only update if drawing
        Timer.setText(str(round(-routineTimer.getTime()-Timer.tStart)) + "\n\n" + seconds[language]
)
    
    # *key_resp_11* updates
    waitOnFlip = False
    if key_resp_11.status == NOT_STARTED and tThisFlip >= 30-frameTolerance:
        # keep track of start time/frame for later
        key_resp_11.frameNStart = frameN  # exact frame index
        key_resp_11.tStart = t  # local t and not account for scr refresh
        key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
        key_resp_11.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_11.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_11.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_11_allKeys.extend(theseKeys)
        if len(_key_resp_11_allKeys):
            key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
            key_resp_11.rt = _key_resp_11_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *recording_image* updates
    if recording_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        recording_image.frameNStart = frameN  # exact frame index
        recording_image.tStart = t  # local t and not account for scr refresh
        recording_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(recording_image, 'tStartRefresh')  # time at next scr refresh
        recording_image.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in routine_60_Sec_moodComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "routine_60_Sec_mood"-------
for thisComponent in routine_60_Sec_moodComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('mood_voice.started', mood_voice.tStartRefresh)
thisExp.addData('mood_voice.stopped', mood_voice.tStopRefresh)
# mood_60_secs stop & responses
mood_60_secs.stop()  # sometimes helpful
if not mood_60_secs.savedFile:
    mood_60_secs.savedFile = None
# store data for thisExp (ExperimentHandler)
thisExp.addData('mood_60_secs.filename', mood_60_secs.savedFile)
thisExp.addData('mood_60_secs.started', mood_60_secs.tStartRefresh)
thisExp.addData('mood_60_secs.stopped', mood_60_secs.tStopRefresh)
thisExp.nextEntry()
# check responses
if key_resp_11.keys in ['', [], None]:  # No response was made
    key_resp_11.keys = None
thisExp.addData('key_resp_11.keys',key_resp_11.keys)
if key_resp_11.keys != None:  # we had a response
    thisExp.addData('key_resp_11.rt', key_resp_11.rt)
thisExp.addData('key_resp_11.started', key_resp_11.tStartRefresh)
thisExp.addData('key_resp_11.stopped', key_resp_11.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('recording_image.started', recording_image.tStartRefresh)
thisExp.addData('recording_image.stopped', recording_image.tStopRefresh)
# the Routine "routine_60_Sec_mood" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "neutral_speech_instruction"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_25.keys = []
key_resp_25.rt = []
_key_resp_25_allKeys = []
text_17.setText(neutral_speech_instruction_text[language])
# keep track of which components have finished
neutral_speech_instructionComponents = [key_resp_25, text_17]
for thisComponent in neutral_speech_instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
neutral_speech_instructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "neutral_speech_instruction"-------
while continueRoutine:
    # get current time
    t = neutral_speech_instructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=neutral_speech_instructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_25* updates
    waitOnFlip = False
    if key_resp_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_25.frameNStart = frameN  # exact frame index
        key_resp_25.tStart = t  # local t and not account for scr refresh
        key_resp_25.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_25, 'tStartRefresh')  # time at next scr refresh
        key_resp_25.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_25.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_25.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_25.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_25.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_25_allKeys.extend(theseKeys)
        if len(_key_resp_25_allKeys):
            key_resp_25.keys = _key_resp_25_allKeys[-1].name  # just the last key pressed
            key_resp_25.rt = _key_resp_25_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_17* updates
    if text_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_17.frameNStart = frameN  # exact frame index
        text_17.tStart = t  # local t and not account for scr refresh
        text_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_17, 'tStartRefresh')  # time at next scr refresh
        text_17.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in neutral_speech_instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "neutral_speech_instruction"-------
for thisComponent in neutral_speech_instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_25.keys in ['', [], None]:  # No response was made
    key_resp_25.keys = None
thisExp.addData('key_resp_25.keys',key_resp_25.keys)
if key_resp_25.keys != None:  # we had a response
    thisExp.addData('key_resp_25.rt', key_resp_25.rt)
thisExp.addData('key_resp_25.started', key_resp_25.tStartRefresh)
thisExp.addData('key_resp_25.stopped', key_resp_25.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_17.started', text_17.tStartRefresh)
thisExp.addData('text_17.stopped', text_17.tStopRefresh)
# the Routine "neutral_speech_instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "neutral_speech_start_mic_2"-------
continueRoutine = True
# update component parameters for each repeat
neutral_speech_mic2 = microphone.AdvAudioCapture(name='neutral_speech_mic2', saveDir=wavDirName, stereo=False, chnl=0)
neutral_speech_mic2.record(sec=7200)
# keep track of which components have finished
neutral_speech_start_mic_2Components = []
for thisComponent in neutral_speech_start_mic_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
neutral_speech_start_mic_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "neutral_speech_start_mic_2"-------
while continueRoutine:
    # get current time
    t = neutral_speech_start_mic_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=neutral_speech_start_mic_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in neutral_speech_start_mic_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "neutral_speech_start_mic_2"-------
for thisComponent in neutral_speech_start_mic_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "neutral_speech_start_mic_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
neutral_speech2 = data.TrialHandler(nReps=3.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='neutral_speech2')
thisExp.addLoop(neutral_speech2)  # add the loop to the experiment
thisNeutral_speech2 = neutral_speech2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNeutral_speech2.rgb)
if thisNeutral_speech2 != None:
    for paramName in thisNeutral_speech2:
        exec('{} = thisNeutral_speech2[paramName]'.format(paramName))

for thisNeutral_speech2 in neutral_speech2:
    currentLoop = neutral_speech2
    # abbreviate parameter names if possible (e.g. rgb = thisNeutral_speech2.rgb)
    if thisNeutral_speech2 != None:
        for paramName in thisNeutral_speech2:
            exec('{} = thisNeutral_speech2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "neutral_speech_recording_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_50.setText(neutral_speech_text[language][neutral_speech2.thisN])
    key_resp_52.keys = []
    key_resp_52.rt = []
    _key_resp_52_allKeys = []
    # keep track of which components have finished
    neutral_speech_recording_2Components = [text_50, key_resp_52]
    for thisComponent in neutral_speech_recording_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    neutral_speech_recording_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "neutral_speech_recording_2"-------
    while continueRoutine:
        # get current time
        t = neutral_speech_recording_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=neutral_speech_recording_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_50* updates
        if text_50.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_50.frameNStart = frameN  # exact frame index
            text_50.tStart = t  # local t and not account for scr refresh
            text_50.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_50, 'tStartRefresh')  # time at next scr refresh
            text_50.setAutoDraw(True)
        
        # *key_resp_52* updates
        waitOnFlip = False
        if key_resp_52.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_52.frameNStart = frameN  # exact frame index
            key_resp_52.tStart = t  # local t and not account for scr refresh
            key_resp_52.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_52, 'tStartRefresh')  # time at next scr refresh
            key_resp_52.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_52.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_52.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_52.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_52.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_52_allKeys.extend(theseKeys)
            if len(_key_resp_52_allKeys):
                key_resp_52.keys = _key_resp_52_allKeys[-1].name  # just the last key pressed
                key_resp_52.rt = _key_resp_52_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in neutral_speech_recording_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "neutral_speech_recording_2"-------
    for thisComponent in neutral_speech_recording_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    neutral_speech2.addData('text_50.started', text_50.tStartRefresh)
    neutral_speech2.addData('text_50.stopped', text_50.tStopRefresh)
    # check responses
    if key_resp_52.keys in ['', [], None]:  # No response was made
        key_resp_52.keys = None
    neutral_speech2.addData('key_resp_52.keys',key_resp_52.keys)
    if key_resp_52.keys != None:  # we had a response
        neutral_speech2.addData('key_resp_52.rt', key_resp_52.rt)
    neutral_speech2.addData('key_resp_52.started', key_resp_52.tStartRefresh)
    neutral_speech2.addData('key_resp_52.stopped', key_resp_52.tStopRefresh)
    # the Routine "neutral_speech_recording_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 3.0 repeats of 'neutral_speech2'

# get names of stimulus parameters
if neutral_speech2.trialList in ([], [None], None):
    params = []
else:
    params = neutral_speech2.trialList[0].keys()
# save data for this loop
neutral_speech2.saveAsExcel(filename + '.xlsx', sheetName='neutral_speech2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
neutral_speech2.saveAsText(filename + 'neutral_speech2.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "neutral_speech_stop_mic_2"-------
continueRoutine = True
# update component parameters for each repeat

time.sleep(1)
neutral_speech_mic2.stop()
# keep track of which components have finished
neutral_speech_stop_mic_2Components = []
for thisComponent in neutral_speech_stop_mic_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
neutral_speech_stop_mic_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "neutral_speech_stop_mic_2"-------
while continueRoutine:
    # get current time
    t = neutral_speech_stop_mic_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=neutral_speech_stop_mic_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in neutral_speech_stop_mic_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "neutral_speech_stop_mic_2"-------
for thisComponent in neutral_speech_stop_mic_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "neutral_speech_stop_mic_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "eating_message"-------
continueRoutine = True
# update component parameters for each repeat
text_finish.setText(eating_message_text[language])
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
eating_messageComponents = [text_finish, key_resp_4]
for thisComponent in eating_messageComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
eating_messageClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "eating_message"-------
while continueRoutine:
    # get current time
    t = eating_messageClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=eating_messageClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_finish* updates
    if text_finish.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_finish.frameNStart = frameN  # exact frame index
        text_finish.tStart = t  # local t and not account for scr refresh
        text_finish.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_finish, 'tStartRefresh')  # time at next scr refresh
        text_finish.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in eating_messageComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "eating_message"-------
for thisComponent in eating_messageComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_finish.started', text_finish.tStartRefresh)
thisExp.addData('text_finish.stopped', text_finish.tStopRefresh)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
# the Routine "eating_message" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruction_dont_move"-------
continueRoutine = True
# update component parameters for each repeat
text_6.setText(dont_move_instruction_text[language])
key_resp_48.keys = []
key_resp_48.rt = []
_key_resp_48_allKeys = []
# keep track of which components have finished
instruction_dont_moveComponents = [text_6, key_resp_48]
for thisComponent in instruction_dont_moveComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruction_dont_moveClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruction_dont_move"-------
while continueRoutine:
    # get current time
    t = instruction_dont_moveClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruction_dont_moveClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
    # *key_resp_48* updates
    waitOnFlip = False
    if key_resp_48.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_48.frameNStart = frameN  # exact frame index
        key_resp_48.tStart = t  # local t and not account for scr refresh
        key_resp_48.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_48, 'tStartRefresh')  # time at next scr refresh
        key_resp_48.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_48.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_48.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_48.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_48.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_48_allKeys.extend(theseKeys)
        if len(_key_resp_48_allKeys):
            key_resp_48.keys = _key_resp_48_allKeys[-1].name  # just the last key pressed
            key_resp_48.rt = _key_resp_48_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction_dont_moveComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction_dont_move"-------
for thisComponent in instruction_dont_moveComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
# check responses
if key_resp_48.keys in ['', [], None]:  # No response was made
    key_resp_48.keys = None
thisExp.addData('key_resp_48.keys',key_resp_48.keys)
if key_resp_48.keys != None:  # we had a response
    thisExp.addData('key_resp_48.rt', key_resp_48.rt)
thisExp.addData('key_resp_48.started', key_resp_48.tStartRefresh)
thisExp.addData('key_resp_48.stopped', key_resp_48.tStopRefresh)
thisExp.nextEntry()
# the Routine "instruction_dont_move" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "dont_move_beep"-------
continueRoutine = True
routineTimer.add(180.500000)
# update component parameters for each repeat
text_7.setText(dont_move_text[language])
sound_1.setSound('1000', secs=0.5, hamming=True)
sound_1.setVolume(1.0, log=False)
# keep track of which components have finished
dont_move_beepComponents = [text_7, sound_1]
for thisComponent in dont_move_beepComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
dont_move_beepClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "dont_move_beep"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = dont_move_beepClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=dont_move_beepClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    if text_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_7.tStartRefresh + 180.0-frameTolerance:
            # keep track of stop time/frame for later
            text_7.tStop = t  # not accounting for scr refresh
            text_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
            text_7.setAutoDraw(False)
    # start/stop sound_1
    if sound_1.status == NOT_STARTED and tThisFlip >= 180.0-frameTolerance:
        # keep track of start time/frame for later
        sound_1.frameNStart = frameN  # exact frame index
        sound_1.tStart = t  # local t and not account for scr refresh
        sound_1.tStartRefresh = tThisFlipGlobal  # on global time
        sound_1.play(when=win)  # sync with win flip
    if sound_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > sound_1.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            sound_1.tStop = t  # not accounting for scr refresh
            sound_1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(sound_1, 'tStopRefresh')  # time at next scr refresh
            sound_1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in dont_move_beepComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "dont_move_beep"-------
for thisComponent in dont_move_beepComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)
sound_1.stop()  # ensure sound has stopped at end of routine
thisExp.addData('sound_1.started', sound_1.tStartRefresh)
thisExp.addData('sound_1.stopped', sound_1.tStopRefresh)

# ------Prepare to start Routine "after_close_eyes"-------
continueRoutine = True
# update component parameters for each repeat
text_14.setText(after_close_eyes_text[language])
key_resp_22.keys = []
key_resp_22.rt = []
_key_resp_22_allKeys = []
# keep track of which components have finished
after_close_eyesComponents = [text_14, key_resp_22]
for thisComponent in after_close_eyesComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
after_close_eyesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "after_close_eyes"-------
while continueRoutine:
    # get current time
    t = after_close_eyesClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=after_close_eyesClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_14* updates
    if text_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_14.frameNStart = frameN  # exact frame index
        text_14.tStart = t  # local t and not account for scr refresh
        text_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
        text_14.setAutoDraw(True)
    
    # *key_resp_22* updates
    waitOnFlip = False
    if key_resp_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_22.frameNStart = frameN  # exact frame index
        key_resp_22.tStart = t  # local t and not account for scr refresh
        key_resp_22.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_22, 'tStartRefresh')  # time at next scr refresh
        key_resp_22.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_22.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_22.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_22.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_22.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_22_allKeys.extend(theseKeys)
        if len(_key_resp_22_allKeys):
            key_resp_22.keys = _key_resp_22_allKeys[-1].name  # just the last key pressed
            key_resp_22.rt = _key_resp_22_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in after_close_eyesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "after_close_eyes"-------
for thisComponent in after_close_eyesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_14.started', text_14.tStartRefresh)
thisExp.addData('text_14.stopped', text_14.tStopRefresh)
# check responses
if key_resp_22.keys in ['', [], None]:  # No response was made
    key_resp_22.keys = None
thisExp.addData('key_resp_22.keys',key_resp_22.keys)
if key_resp_22.keys != None:  # we had a response
    thisExp.addData('key_resp_22.rt', key_resp_22.rt)
thisExp.addData('key_resp_22.started', key_resp_22.tStartRefresh)
thisExp.addData('key_resp_22.stopped', key_resp_22.tStopRefresh)
thisExp.nextEntry()
# the Routine "after_close_eyes" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
affective_slider_03 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='affective_slider_03')
thisExp.addLoop(affective_slider_03)  # add the loop to the experiment
thisAffective_slider_03 = affective_slider_03.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisAffective_slider_03.rgb)
if thisAffective_slider_03 != None:
    for paramName in thisAffective_slider_03:
        exec('{} = thisAffective_slider_03[paramName]'.format(paramName))

for thisAffective_slider_03 in affective_slider_03:
    currentLoop = affective_slider_03
    # abbreviate parameter names if possible (e.g. rgb = thisAffective_slider_03.rgb)
    if thisAffective_slider_03 != None:
        for paramName in thisAffective_slider_03:
            exec('{} = thisAffective_slider_03[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "affective_slider"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_29.setText(affective_slider_instruction_text[language])
    arousel_slider_3.reset()
    pleasure_slider_3.reset()
    key_resp_36.keys = []
    key_resp_36.rt = []
    _key_resp_36_allKeys = []
    # keep track of which components have finished
    affective_sliderComponents = [text_29, arousel_slider_3, pleasure_slider_3, key_resp_36, arousal_low, arousal_high, pleasure_low, pleasure_high]
    for thisComponent in affective_sliderComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    affective_sliderClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "affective_slider"-------
    while continueRoutine:
        # get current time
        t = affective_sliderClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=affective_sliderClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_29* updates
        if text_29.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_29.frameNStart = frameN  # exact frame index
            text_29.tStart = t  # local t and not account for scr refresh
            text_29.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_29, 'tStartRefresh')  # time at next scr refresh
            text_29.setAutoDraw(True)
        
        # *arousel_slider_3* updates
        if arousel_slider_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            arousel_slider_3.frameNStart = frameN  # exact frame index
            arousel_slider_3.tStart = t  # local t and not account for scr refresh
            arousel_slider_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(arousel_slider_3, 'tStartRefresh')  # time at next scr refresh
            arousel_slider_3.setAutoDraw(True)
        
        # *pleasure_slider_3* updates
        if pleasure_slider_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pleasure_slider_3.frameNStart = frameN  # exact frame index
            pleasure_slider_3.tStart = t  # local t and not account for scr refresh
            pleasure_slider_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pleasure_slider_3, 'tStartRefresh')  # time at next scr refresh
            pleasure_slider_3.setAutoDraw(True)
        
        # *key_resp_36* updates
        waitOnFlip = False
        if key_resp_36.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_36.frameNStart = frameN  # exact frame index
            key_resp_36.tStart = t  # local t and not account for scr refresh
            key_resp_36.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_36, 'tStartRefresh')  # time at next scr refresh
            key_resp_36.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_36.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_36.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_36.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_36.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_36_allKeys.extend(theseKeys)
            if len(_key_resp_36_allKeys):
                key_resp_36.keys = _key_resp_36_allKeys[-1].name  # just the last key pressed
                key_resp_36.rt = _key_resp_36_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *arousal_low* updates
        if arousal_low.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            arousal_low.frameNStart = frameN  # exact frame index
            arousal_low.tStart = t  # local t and not account for scr refresh
            arousal_low.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(arousal_low, 'tStartRefresh')  # time at next scr refresh
            arousal_low.setAutoDraw(True)
        
        # *arousal_high* updates
        if arousal_high.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            arousal_high.frameNStart = frameN  # exact frame index
            arousal_high.tStart = t  # local t and not account for scr refresh
            arousal_high.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(arousal_high, 'tStartRefresh')  # time at next scr refresh
            arousal_high.setAutoDraw(True)
        
        # *pleasure_low* updates
        if pleasure_low.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pleasure_low.frameNStart = frameN  # exact frame index
            pleasure_low.tStart = t  # local t and not account for scr refresh
            pleasure_low.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pleasure_low, 'tStartRefresh')  # time at next scr refresh
            pleasure_low.setAutoDraw(True)
        
        # *pleasure_high* updates
        if pleasure_high.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pleasure_high.frameNStart = frameN  # exact frame index
            pleasure_high.tStart = t  # local t and not account for scr refresh
            pleasure_high.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pleasure_high, 'tStartRefresh')  # time at next scr refresh
            pleasure_high.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in affective_sliderComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "affective_slider"-------
    for thisComponent in affective_sliderComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    affective_slider_03.addData('text_29.started', text_29.tStartRefresh)
    affective_slider_03.addData('text_29.stopped', text_29.tStopRefresh)
    affective_slider_03.addData('arousel_slider_3.response', arousel_slider_3.getRating())
    affective_slider_03.addData('arousel_slider_3.rt', arousel_slider_3.getRT())
    affective_slider_03.addData('arousel_slider_3.started', arousel_slider_3.tStartRefresh)
    affective_slider_03.addData('arousel_slider_3.stopped', arousel_slider_3.tStopRefresh)
    affective_slider_03.addData('pleasure_slider_3.response', pleasure_slider_3.getRating())
    affective_slider_03.addData('pleasure_slider_3.rt', pleasure_slider_3.getRT())
    affective_slider_03.addData('pleasure_slider_3.started', pleasure_slider_3.tStartRefresh)
    affective_slider_03.addData('pleasure_slider_3.stopped', pleasure_slider_3.tStopRefresh)
    # check responses
    if key_resp_36.keys in ['', [], None]:  # No response was made
        key_resp_36.keys = None
    affective_slider_03.addData('key_resp_36.keys',key_resp_36.keys)
    if key_resp_36.keys != None:  # we had a response
        affective_slider_03.addData('key_resp_36.rt', key_resp_36.rt)
    affective_slider_03.addData('key_resp_36.started', key_resp_36.tStartRefresh)
    affective_slider_03.addData('key_resp_36.stopped', key_resp_36.tStopRefresh)
    affective_slider_03.addData('arousal_low.started', arousal_low.tStartRefresh)
    affective_slider_03.addData('arousal_low.stopped', arousal_low.tStopRefresh)
    affective_slider_03.addData('arousal_high.started', arousal_high.tStartRefresh)
    affective_slider_03.addData('arousal_high.stopped', arousal_high.tStopRefresh)
    affective_slider_03.addData('pleasure_low.started', pleasure_low.tStartRefresh)
    affective_slider_03.addData('pleasure_low.stopped', pleasure_low.tStopRefresh)
    affective_slider_03.addData('pleasure_high.started', pleasure_high.tStartRefresh)
    affective_slider_03.addData('pleasure_high.stopped', pleasure_high.tStopRefresh)
    # the Routine "affective_slider" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'affective_slider_03'

# get names of stimulus parameters
if affective_slider_03.trialList in ([], [None], None):
    params = []
else:
    params = affective_slider_03.trialList[0].keys()
# save data for this loop
affective_slider_03.saveAsExcel(filename + '.xlsx', sheetName='affective_slider_03',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
affective_slider_03.saveAsText(filename + 'affective_slider_03.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
PANAS_03 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(PANAS_path[language]),
    seed=None, name='PANAS_03')
thisExp.addLoop(PANAS_03)  # add the loop to the experiment
thisPANAS_03 = PANAS_03.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPANAS_03.rgb)
if thisPANAS_03 != None:
    for paramName in thisPANAS_03:
        exec('{} = thisPANAS_03[paramName]'.format(paramName))

for thisPANAS_03 in PANAS_03:
    currentLoop = PANAS_03
    # abbreviate parameter names if possible (e.g. rgb = thisPANAS_03.rgb)
    if thisPANAS_03 != None:
        for paramName in thisPANAS_03:
            exec('{} = thisPANAS_03[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "questionaire"-------
    continueRoutine = True
    # update component parameters for each repeat
    if language == 'de' :
        continueRoutine = False
    instructions_questionaire.setText(PANAS_text[language])
    question_slider.reset()
    question_text.setText(question)
    # keep track of which components have finished
    questionaireComponents = [instructions_questionaire, question_slider, question_text]
    for thisComponent in questionaireComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    questionaireClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "questionaire"-------
    while continueRoutine:
        # get current time
        t = questionaireClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=questionaireClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions_questionaire* updates
        if instructions_questionaire.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions_questionaire.frameNStart = frameN  # exact frame index
            instructions_questionaire.tStart = t  # local t and not account for scr refresh
            instructions_questionaire.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_questionaire, 'tStartRefresh')  # time at next scr refresh
            instructions_questionaire.setAutoDraw(True)
        
        # *question_slider* updates
        if question_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            question_slider.frameNStart = frameN  # exact frame index
            question_slider.tStart = t  # local t and not account for scr refresh
            question_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(question_slider, 'tStartRefresh')  # time at next scr refresh
            question_slider.setAutoDraw(True)
        
        # Check question_slider for response to end routine
        if question_slider.getRating() is not None and question_slider.status == STARTED:
            continueRoutine = False
        
        # *question_text* updates
        if question_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            question_text.frameNStart = frameN  # exact frame index
            question_text.tStart = t  # local t and not account for scr refresh
            question_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(question_text, 'tStartRefresh')  # time at next scr refresh
            question_text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in questionaireComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "questionaire"-------
    for thisComponent in questionaireComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    PANAS_03.addData('instructions_questionaire.started', instructions_questionaire.tStartRefresh)
    PANAS_03.addData('instructions_questionaire.stopped', instructions_questionaire.tStopRefresh)
    PANAS_03.addData('question_slider.response', question_slider.getRating())
    PANAS_03.addData('question_slider.rt', question_slider.getRT())
    PANAS_03.addData('question_slider.started', question_slider.tStartRefresh)
    PANAS_03.addData('question_slider.stopped', question_slider.tStopRefresh)
    # the Routine "questionaire" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'PANAS_03'

# get names of stimulus parameters
if PANAS_03.trialList in ([], [None], None):
    params = []
else:
    params = PANAS_03.trialList[0].keys()
# save data for this loop
PANAS_03.saveAsExcel(filename + '.xlsx', sheetName='PANAS_03',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
PANAS_03.saveAsText(filename + 'PANAS_03.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
PANAS_03_german = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(PANAS_path[language]),
    seed=None, name='PANAS_03_german')
thisExp.addLoop(PANAS_03_german)  # add the loop to the experiment
thisPANAS_03_german = PANAS_03_german.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPANAS_03_german.rgb)
if thisPANAS_03_german != None:
    for paramName in thisPANAS_03_german:
        exec('{} = thisPANAS_03_german[paramName]'.format(paramName))

for thisPANAS_03_german in PANAS_03_german:
    currentLoop = PANAS_03_german
    # abbreviate parameter names if possible (e.g. rgb = thisPANAS_03_german.rgb)
    if thisPANAS_03_german != None:
        for paramName in thisPANAS_03_german:
            exec('{} = thisPANAS_03_german[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "questionaire_german"-------
    continueRoutine = True
    # update component parameters for each repeat
    instructions_questionaire_4.setText(PANAS_text[language])
    question_slider_4.reset()
    question_text_4.setText(question)
    if language == 'en' :
        continueRoutine = False
    # keep track of which components have finished
    questionaire_germanComponents = [instructions_questionaire_4, question_slider_4, question_text_4]
    for thisComponent in questionaire_germanComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    questionaire_germanClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "questionaire_german"-------
    while continueRoutine:
        # get current time
        t = questionaire_germanClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=questionaire_germanClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions_questionaire_4* updates
        if instructions_questionaire_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions_questionaire_4.frameNStart = frameN  # exact frame index
            instructions_questionaire_4.tStart = t  # local t and not account for scr refresh
            instructions_questionaire_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_questionaire_4, 'tStartRefresh')  # time at next scr refresh
            instructions_questionaire_4.setAutoDraw(True)
        
        # *question_slider_4* updates
        if question_slider_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            question_slider_4.frameNStart = frameN  # exact frame index
            question_slider_4.tStart = t  # local t and not account for scr refresh
            question_slider_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(question_slider_4, 'tStartRefresh')  # time at next scr refresh
            question_slider_4.setAutoDraw(True)
        
        # Check question_slider_4 for response to end routine
        if question_slider_4.getRating() is not None and question_slider_4.status == STARTED:
            continueRoutine = False
        
        # *question_text_4* updates
        if question_text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            question_text_4.frameNStart = frameN  # exact frame index
            question_text_4.tStart = t  # local t and not account for scr refresh
            question_text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(question_text_4, 'tStartRefresh')  # time at next scr refresh
            question_text_4.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in questionaire_germanComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "questionaire_german"-------
    for thisComponent in questionaire_germanComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    PANAS_03_german.addData('instructions_questionaire_4.started', instructions_questionaire_4.tStartRefresh)
    PANAS_03_german.addData('instructions_questionaire_4.stopped', instructions_questionaire_4.tStopRefresh)
    PANAS_03_german.addData('question_slider_4.response', question_slider_4.getRating())
    PANAS_03_german.addData('question_slider_4.rt', question_slider_4.getRT())
    PANAS_03_german.addData('question_slider_4.started', question_slider_4.tStartRefresh)
    PANAS_03_german.addData('question_slider_4.stopped', question_slider_4.tStopRefresh)
    # the Routine "questionaire_german" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'PANAS_03_german'

# get names of stimulus parameters
if PANAS_03_german.trialList in ([], [None], None):
    params = []
else:
    params = PANAS_03_german.trialList[0].keys()
# save data for this loop
PANAS_03_german.saveAsExcel(filename + '.xlsx', sheetName='PANAS_03_german',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
PANAS_03_german.saveAsText(filename + 'PANAS_03_german.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "finish_message"-------
continueRoutine = True
# update component parameters for each repeat
text_finished_message.setText(finish_text[language])
end_study.keys = []
end_study.rt = []
_end_study_allKeys = []
# keep track of which components have finished
finish_messageComponents = [text_finished_message, end_study]
for thisComponent in finish_messageComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
finish_messageClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "finish_message"-------
while continueRoutine:
    # get current time
    t = finish_messageClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=finish_messageClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_finished_message* updates
    if text_finished_message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_finished_message.frameNStart = frameN  # exact frame index
        text_finished_message.tStart = t  # local t and not account for scr refresh
        text_finished_message.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_finished_message, 'tStartRefresh')  # time at next scr refresh
        text_finished_message.setAutoDraw(True)
    
    # *end_study* updates
    waitOnFlip = False
    if end_study.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_study.frameNStart = frameN  # exact frame index
        end_study.tStart = t  # local t and not account for scr refresh
        end_study.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_study, 'tStartRefresh')  # time at next scr refresh
        end_study.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_study.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_study.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_study.status == STARTED and not waitOnFlip:
        theseKeys = end_study.getKeys(keyList=['space'], waitRelease=False)
        _end_study_allKeys.extend(theseKeys)
        if len(_end_study_allKeys):
            end_study.keys = _end_study_allKeys[-1].name  # just the last key pressed
            end_study.rt = _end_study_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finish_messageComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "finish_message"-------
for thisComponent in finish_messageComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_finished_message.started', text_finished_message.tStartRefresh)
thisExp.addData('text_finished_message.stopped', text_finished_message.tStopRefresh)
# check responses
if end_study.keys in ['', [], None]:  # No response was made
    end_study.keys = None
thisExp.addData('end_study.keys',end_study.keys)
if end_study.keys != None:  # we had a response
    thisExp.addData('end_study.rt', end_study.rt)
thisExp.addData('end_study.started', end_study.tStartRefresh)
thisExp.addData('end_study.stopped', end_study.tStopRefresh)
thisExp.nextEntry()
# the Routine "finish_message" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='semicolon')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
