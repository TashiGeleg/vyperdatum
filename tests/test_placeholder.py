import pytest
import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

import web_api.vdatum_web_api as test

if __name__ == '__main__':
    print(test.vdatum_web_api(-70.7, 43, 0, s_v_frame='MLLW', t_v_frame='NAVD88'))


def test_add():
    assert 3+3 == 6

def test_subtract():
    assert 3-2 == 0

