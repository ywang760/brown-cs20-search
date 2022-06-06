from index import *
import pytest

def test_word_to_frequency():
    """Tests word frequncies given various different # of appearances of words
    """
    test1 = index('2pageWiki.xml', 'titles.txt', 'documents.txt', 'words.txt')
    assert test1.word_to_frequency(['a']) == {'a': 1.0}
    assert test1.word_to_frequency(['a', 'a']) == {'a': 1.0}
    assert test1.word_to_frequency(['a', 'a', 'b', 'b']) == {'a': 1.0, 'b': 1.0}
    assert test1.word_to_frequency(['a', 'a', 'b']) == {'a': 1.0, 'b': 0.5}
    assert test1.word_to_frequency(['a', 'a', 'b'] * 12) == {'a': 1.0, 'b': 0.5}
    assert test1.word_to_frequency(['a', 'a', 'a', 'b', 'c', 'c', 'c', 'b']) == {'a': 1.0, 'b': 0.66667, 'c': 1.0}
    assert test1.word_to_frequency(['a', 'a', 'a', 'b', 'c', 'c', 'c', 'b', 'c']) == {'a': 0.75, 'b': 0.5, 'c': 1.0}
    assert test1.word_to_frequency(['a'] * 1000) == {'a': 1.0}

#Testing 
def test_2pageWiki():
    """Tests various data structures and methods created by loading index.py in a 2
    page wiki
    """
    test2 = index('2pageWiki.xml', 'titles.txt', 'documents.txt', 'words.txt')
    # Test the fields in the constructor are correctly populated
    assert test2.pageid_to_text == {0: ['a'], 1: ['b', 'anoth', 'sentenc', 'sentenc', 'hello']}
    assert test2.title_list == ['a', 'b']
    assert test2.title_to_links == {'a': [], 'b': []}
    assert test2.pagecount == 2
    # Test calculate_term_relevance and pagerank
    assert test2.calculate_term_relevances() == defaultdict(dict,
            {'a': {0: 0.69315},
             'b': {1: 0.34657},
             'anoth': {1: 0.34657},
             'sentenc': {1: 0.69315},
             'hello': {1: 0.34657}})
    assert test2.pagerank(test2.dict_to_weight_mat()) == [0.5, 0.5]

def test_3pageWiki():
    """Tests various data structures and methods created by loading index.py in a 3
    page wiki
    """
    test3 = index('3pageWiki.xml', 'titles.txt', 'documents.txt', 'words.txt')
    assert test3.pageid_to_text == {6: ['comput', 'work'], 1: ['scienc', 'word', 'word', 'word'], 4: ['is', 'cool', 'cooooool']}
    assert test3.title_list == ['computer', 'science', 'is cool']
    assert test3.title_to_links == {'computer': ['science', 'is cool'], 'science': ['computer', 'is cool'], 'is cool': []}
    assert test3.pagecount == 3
    # Test calculate_term_relevance and pagerank
    assert test3.calculate_term_relevances() == defaultdict(dict,
            {'comput': {6: 1.09861},
             'work': {6: 1.09861},
             'scienc': {1: 0.3662},
             'word': {1: 1.09861},
             'is': {4: 1.09861},
             'cool': {4: 1.09861},
             'cooooool': {4: 1.09861}})
    assert test3.pagerank(test3.dict_to_weight_mat()) == [0.3333333333333333, 0.3333333333333333, 0.3333333333333333]

#Testing 
def test_4pageWiki():
    """Tests various data structures and methods created by loading index.py in a 4
    page wiki
    """
    test4 = index('4pageWiki.xml', 'titles.txt', 'documents.txt', 'words.txt')
    # Test the fields in the constructor are correctly populated
    assert test4.pageid_to_text == {4092: ['mous', 'look', 'mous', 'cute'], 
    49: ['cute', 'mous', 'absolut'], 
    9810: ['veri', 'cute', 'mous', 'mous', 'cute'],
    8878: ['stupid', 'cat', 'ye', 'cat', 'stupid']}
    assert test4.title_list == ['mouse', 'cute mouse', 'very cute mouse', 'stupid cat']
    assert test4.title_to_links == {'mouse': ['cute mouse'],
    'cute mouse': [], 'very cute mouse': ['mouse'], 'stupid cat': []}
    assert test4.pagecount == 4
    # Test calculate_term_relevance and pagerank
    assert test4.calculate_term_relevances() == defaultdict(dict,
            {'mous': {4092: 1.38629, 49: 0.69315, 9810: 0.28768},
             'look': {4092: 0.69315},
             'cute': {4092: 0.69315, 49: 0.69315, 9810: 0.28768},
             'absolut': {49: 1.38629},
             'veri': {9810: 0.69315},
             'stupid': {8878: 1.38629},
             'cat': {8878: 1.38629},
             'ye': {8878: 0.69315}})
    assert test4.pagerank(test4.dict_to_weight_mat()) == [0.3283993097780433,
    0.35547922013879185, 0.1776411411146682, 0.13843616550755367]

