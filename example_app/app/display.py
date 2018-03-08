# encoding: utf-8
# app/display.py
import collections
import os
from os.path import join as opj

import numpy as np
from psychopy import visual
from psychopy import core

study_pos_array = np.array([])

POSITIONS = {'bot_left':   [-10.,  -8.660],
             'bot_right':   [10.,  -8.660],
             'top_center':   [0.,   8.660],
             'mid_left':   [-10.,   0.],
             'mid_center':   [0.,   0.],
             'mid_right':   [10.,   0.],
             'far_left':   [-10., -10.],
             'far_right':  [10.,  -10.]}
STUDY_POS_LABELS = ('top_center', 'bot_left', 'bot_right')


class Display():
    """
    An object containing the elements of an AMR display.
    """

    def __init__(self, session):
        """Initializiation."""
        self.monitor = getattr(session, 'monitor', None)
        if self.monitor is None:
            self.monitor = "testMonitor"
        self.win = visual.Window([1024, 768],
                                 monitor=self.monitor,
                                 units='deg',
                                 fullscr=True)
        self.win.mouseVisible = False
        session.frame_rate = 60

    def present_pre_instructions(self):
        text = 'Do the words rhyme?'
        stim_text = visual.TextStim(self.win, text, pos=(0., 0.),
                                    units='deg', wrapWidth=20)
        stim_text.draw()
        self.win.flip()

    def present_post_instructions(self):
        text = ('You have completed this portion of the task.\n\n'
                'Please wait for instructions.')
        stim_text = visual.TextStim(self.win, text, pos=(0., 0.),
                                    units='deg', wrapWidth=20)
        stim_text.draw()
        self.win.flip()

    def present_fixation(self, dur=1., jitter=0.):
        text = '+'
        stim_text = visual.TextStim(self.win, text, pos=(0., 0.),
                                    units='deg')
        stim_text.draw()
        self.win.flip()
        core.wait(dur + np.random.uniform() * jitter)

    def present_blank(self, dur=1.):
        self.win.flip()
        self.win.flip()
        core.wait(dur)

    def present_trial(self, left_word, right_word):
        text = left_word + '\t\t\t' + right_word
        stim_text = visual.TextStim(self.win, text, pos=(0., 0.),
                                    units='deg', wrapWidth=20)
        y_text = visual.TextStim(self.win, 'Yes', pos=POSITIONS['far_left'],
                                 units='deg')
        n_text = visual.TextStim(self.win, 'No', pos=POSITIONS['far_right'],
                                 units='deg')
        stim_text.draw()
        y_text.draw()
        n_text.draw()
        self.win.flip()


if __name__ == '__main__':
    pass
