import pytest
import rmp_ 

def test_blank_input():
    credentials = rmp_.get_prof_info("1112", "Daniel Berwik Evans")
    assert (credentials == {})

def test_correct_values():
	credentials = rmp_.get_prof_info("1112", "Graham Evans")
	assert(credentials["147788"]["name"] == "Graham Evans")
	print(credentials)
	assert(credentials["147788"]["would_take"] == "67%")

def test_incorrect_input_is_not_recognized():
    credentials = rmp_.get_prof_info("1112", "Daniel Berwik Evans")
    assert(credentials == {})

def test_bad_input_is_corrected():
    credentials = rmp_.get_prof_info("1112", "DaniEl BeRwick Evans")
    assert(credentials["2559143"]["name"] == "Daniel Berwick-Evans")
    assert(int(credentials["2559143"]["overall"]) == 4)
   



