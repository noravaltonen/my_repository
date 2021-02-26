import simple_math
import pytest

def test_add():
	assert simple_math.simple_add(10,10) == 20

def test_sub():
	assert simple_math.simple_sub(3,2) == 1

def test_mult():
	assert simple_math.simple_mult(2,2) == 4

def test_div():
	assert simple_math.simple_div(10,2) == 5

def test_first():
	assert simple_math.poly_first(6,1,1) == 7

def test_second():
	assert simple_math.poly_second(6,1,1,3) == 115

