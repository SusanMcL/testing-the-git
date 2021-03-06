# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 12:23:28 2015

@author: smcl
"""

"""
===========================
Run a very basic experiment
===========================

This example demonstrates an (almost) minimum working example of the
ExperimentController class.
"""
# Author: Eric Larson <larson.eric.d@gmail.com>
#
# License: BSD (3-clause)

import numpy as np

from expyfun import ExperimentController, analyze
from expyfun.visual import FixationDot
import matplotlib.pyplot as plt

print(__doc__)

# set configuration
fs = 24414.  # default for ExperimentController
dur = 1.0
tone = np.sin(2 * np.pi * 1000 * np.arange(int(fs * dur)) / float(fs))
tone *= 0.01 * np.sqrt(2)  # Set RMS to 0.01

with ExperimentController('testExp', participant='foo', session='001',
                          output_dir=None) as ec:
    ec.screen_prompt('Press a button when you hear the tone', max_wait=1)

    dot = FixationDot(ec)
    ec.clear_buffer()
    ec.load_buffer(tone)
    dot.draw()
    screenshot = ec.screenshot()  # only because we want to show it in the docs

    ec.identify_trial(ec_id='tone', ttl_id=[0, 0])
    ec.start_stimulus()
    presses = ec.wait_for_presses(dur)
    ec.stop()
    ec.trial_ok()
    print('Presses:\n{}'.format(presses))


plt.ion()
analyze.plot_screen(screenshot)
