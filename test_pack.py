

from pally import oba_str

def test_pack_string():
	assert oba_str_string("madam") == "True"
	assert oba_str_string("malam") == "True"
	assert oba_str_string("dad") == "True"
	assert oba_str_string("mom") =="True"