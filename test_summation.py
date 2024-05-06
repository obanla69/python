from summation import summation
def test_summation_func():
    assert summation(1,2,3,4,5) == 15
    assert summation(5,7,9) == 21
    assert summation(2,3,6,7,7,8,10,40,20,25) == 128
   
    
from summation import obaLen
def test_obaLen_strings():
    assert obaLen("semicolon",) == 9 
    
	
from summation  import add_str
def test_add_str_strings():
    assert add_str("abc") == 'abcing'
    assert add_str("string") == 'stringly'
    assert add_str("on") == 'on'
    
    
from summation import sample
def test_sample_strings():
    assert sample ['welcome', 'out', 'weather', 'mobile', 'breakfast', 'journey'] == breakfast, 9
    
from summation import addup
def test_addup_strings():
    assert addup("semicolon") == "eioo"
