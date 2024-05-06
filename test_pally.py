

from pally import panda

def test_pally_returns_true():
	assert panda('madam') == True
	assert panda('12121') == True

def test_pally_returns_false():
	assert panda('ball') == False
	assert panda('10111') == False
   
   def test_pally_returns_false():
	assert panda('10') == False
    assert panda('10111') == False
	
   