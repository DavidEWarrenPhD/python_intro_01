# encoding: utf-8
# app/interact.py
from __future__ import print_function
# from builtins import input

import collections
import datetime

# from psychopy import visual
from psychopy import event

import objects as obj


TEST_KEYS = ('z', 'slash')
UTIL_KEYS = ('space',)
NO_KEYS = ()


def get_session_info():
    """Get session information on command line."""
    dt = datetime.datetime.now()
    exp_id = raw_input("Experimenter ID: ")
    par_id = raw_input("Participant ID: ")
    visit = None
    while visit not in ('1', '2'):
        visit = raw_input("Visit (1 or 2): ")
    cb = None
    cb_range = [str(i) for i in range(1, 1000)]
    while cb not in cb_range:
        cb = raw_input("Counterbalancing (1-???): ")
    session_info_items = tuple('datetime exp_id par_id visit cb'.split())
    SessionInfo = collections.namedtuple('SessionInfo', session_info_items)
    return SessionInfo(dt, exp_id, par_id, visit, cb)


def get_response(clock, max_wait=None, keys=None):
    """Returns a response and response time."""
    Response = collections.namedtuple('Response',
                                      'start_time key latency'.split())
    if max_wait is None:
        max_wait = obj.INF
    t0 = clock.getTime()
    ret = event.waitKeys(maxWait=max_wait, timeStamped=clock, keyList=keys)
    if ret is None:
        return Response(t0, 'NA', 0.)
    if len(ret) > 1:
        ret = ret[0]
    ret = ret[0]
    key, timestamp = ret
    rt = timestamp - t0
    return Response(t0, key, rt)
