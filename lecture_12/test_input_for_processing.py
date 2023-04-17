#! /usr/bin/python3
import input_for_processing as ifp
import mock

def test_ask_from_user():
    with mock.patch('builtins.input', return_value="yes"):
        assert ifp.ask_from_user() == True
        
    with mock.patch('builtins.input', return_value="Yes"):
        assert ifp.ask_from_user() == False
        
    with mock.patch('builtins.input', return_value="wertyh"):
        assert ifp.ask_from_user() == False