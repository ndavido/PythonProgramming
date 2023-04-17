#! /usr/bin/python3

import input_while_true
import mock

def test_while_true_input():
    with mock.patch('builtins.input', side_effect=["five","no",1]):
        assert input_while_true.ask_number_from_user() == 1
