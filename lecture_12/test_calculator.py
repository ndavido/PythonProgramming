#! /usr/bin/python3
import calculator

def test_calculator_add():
    assert calculator.calculator("add",1,1) == 2
    assert calculator.calculator("add",-1,1) == 0
    assert calculator.calculator("add",0,0) == 0

def test_calculator_multiply():
    assert calculator.calculator("multiply",1,1) == 1
    assert calculator.calculator("multiply",-1,1) == -1
    assert calculator.calculator("multiply",0,0) == 0
    assert calculator.calculator("multiply",3,3) == 9
    
def test_calculator_else():
    assert calculator.calculator("multipl",1,1) == ""
    assert calculator.calculator("ad",-1,1) == ""
    assert calculator.calculator("minus",0,0) == ""
    assert calculator.calculator("fyguhjb",3,3) == ""
