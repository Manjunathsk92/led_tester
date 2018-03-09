#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `led_tester` package."""
import sys
sys.path.append('.')
sys.path.append('/Users/manjunathsanjivkulkarni/Desktop/UCD_sem_2/Software_Engineering/assignment3/led_tester')
import pytest

from click.testing import CliRunner

#from led_tester import led_tester
from led_tester import cli
from led_tester import utils
import re



def test_command_line_interface():
	ifile = '../data/test_data.txt'
	N, instructions = utils.parseFile(ifile)
	print("N is ", N)
	print("instructions", instructions)
	assert N is not None
#print(sys.path)
test_command_line_interface()	


