# -*- coding: utf-8 -*-
# app/__init__.py
from __future__ import print_function

import os
from os.path import join as opj

INF = float('inf')


class Session():

    """Contains session information for the AMRv2 memory task."""

    def __init__(self):
        pass

    def setup(self, session_info):
        self.dt = session_info.datetime
        self.attr_setup()
        self.config_setup()
        self.read_stim()

    def attr_setup(self):
        self.dt_str = self.dt.strftime('%Y_%m_%d-%H_%M_%S')
        self.app_dir = os.path.dirname(os.path.realpath(__file__))
        self.script_dir, _ = os.path.split(self.app_dir)
        self.ref_dir = opj(self.script_dir, 'app', 'static')
        self.root_dir, _ = os.path.split(self.script_dir)

    def config_setup(self):
        config_dict = {'num_exposures': 2,     # Number of study exposures
                       'study_triad_isi': 1.,  # Time btw triads, study (s)
                       'study_stim_dur': 1.,   # Time items displayed   (s)
                       'study_stim_isi': 0.,   # Time btw items, study  (s)
                       'test_stim_dur': 1.,    # Time items displayed   (s)
                       'test_stim_isi': 0.,    # Time btw items, test   (s)
                       'test_rsp_dur': INF,
                       'pause_dur': INF,
                       'blank_dur': 1.,
                       'fix_dur': 0.75,
                       'fix_jitter': 0.5}
        for k, v in config_dict.items():
            setattr(self, k, v)

    def read_stim(self):
        with open(opj(self.ref_dir, 'word_list.txt'), 'r') as f:
            self.stim_words = [i.strip() for i in f.readlines()]


session = Session()
