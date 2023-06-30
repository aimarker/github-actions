# test_1.py
import os
import sys

from script import addition

sys.path.insert(0, '/Users/abhs/aimlops/github-projects/github-actions')


def test_add():
    subj = addition(2, 3)
    assert subj == 5
