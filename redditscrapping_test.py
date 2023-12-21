from course-project-group-99.redditscrapping import get_num_reddit_titles
import pytest
import redditscrapping

def test_num_titles_per_call():
    number = get_num_reddit_titles()
    assert (number == 27)