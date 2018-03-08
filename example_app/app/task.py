# encoding: utf-8
# app\task.py
from __future__ import print_function

import random

from psychopy import core

import display
import interact


def setup(session):
    """TODO: Docstring for runTask.

    :num_pieces: TODO
    :puzzle_start: TODO
    :puzzle_solution: TODO
    :auto_run: TODO
    :returns: TODO

    """
    session.clock = core.MonotonicClock()
    session.display = display.Display(session)


def run(session):
    """Present all trials from all blocks in order, recording output for each.

    :session: An AMRv2 Session object.

    :returns: True if successful, False if not.
    """
    session.display.present_blank()
    session.display.present_pre_instructions()
    _ = interact.get_response(session.clock, max_wait=session.pause_dur,
                              keys=interact.UTIL_KEYS)
    for trial in range(20):
        session.display.present_fixation()
        random.shuffle(session.stim_words)
        session.display.present_trial(session.stim_words[0],
                                      session.stim_words[1])
        rsp = interact.get_response(session.clock,
                                    max_wait=99,
                                    keys=interact.TEST_KEYS)
    session.display.present_blank(session.blank_dur)
    session.display.present_post_instructions()
    _ = interact.get_response(session.clock, max_wait=session.pause_dur,
                              keys=interact.UTIL_KEYS)
