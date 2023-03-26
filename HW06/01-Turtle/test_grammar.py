""" 
CS 5001
Pranchal Shah
HW 06

This file Tests for some of the required functions in the grammar.py file. 
One test function each for get_grammar and produce
One-line comment above each test function explaining what it is testing.
"""

import grammar

def test_get_grammar(case_number: int, grammar_string: str, 
                     dict_expected: str) -> str:
    """
    This function tests the get_grammar function in grammar.py
    It takes in the case number, the grammar string, and 
    the expected dictionary and prints the actual and expected results.

    Args:
        case_number (int): A unique identifier for the test case
        grammar_string (str): _description_
        expected_dict (str): _description_

    Returns:
        None. The function prints the actual and expected results
    """
    
    dict_actual = grammar.get_grammar(grammar_string)
    print(f"\nget_grammar, Test Case {case_number}:\
           \nOut:'{dict_actual}'\nExp:'{dict_expected}'")


def test_produce(case_number: int, grammar: dict, 
                 sequence_expected: str) -> str:
    """
    This function tests the produce function in grammar.py
    It takes in the case number, the grammar dictionary, and 
    the expected sequence and prints the actual and expected results.

    Args:
        case_number (int): A unique identifier for the test case
        grammar (dict): _description_
        sequence_expected (str): _description_

    Returns:
        None. The function prints the actual and expected results
    """
    
    sequence_actual = grammar.produce(grammar)
    print(f"\nproduce, Test Case {case_number}:\
           \nOut:'{sequence_actual}'\nExp:'{sequence_expected}'")
    
    
def main():
    """
    
    """
    print("-------------------Testing get_grammar-----------------------")
    
    # Ideal test case
    test_get_grammar(0, "symbols F+-\nstart F\nangle 90\niterations 3\nrule F F+F-F-F+F", 
                        {"symbols": "F+-", "start": "F", "angle": "90", "iterations": "3", "ruleF": "F+F-F-F+F"})
    # blank spaces - should work fine
    test_get_grammar(1, "\n\nsymbols F+-\n\n\nstart F\nangle 90\n\niterations 3\n\n\nrule F F+F-F-F+F", 
                        {"symbols": "F+-", "start": "F", "angle": "90", "iterations": "3", "ruleF": "F+F-F-F+F"})
    # only symbols, start, iterations - should work fine
    test_get_grammar(2, "\n\nsymbols F+-\n\n\nstart F\niterations 3", 
                        {'symbols': 'F+-', 'start': 'F', 'iterations': '3'})
    # missing one of the required keys - should raise error
    test_get_grammar(3, "\n\nsymbols F+-\nangle 90\n\niterations 3\n\n\nrule F F+F-F-F+F", 
                        "The grammar file is not formatted correctly")
    # a few extra keys - not supported
    test_get_grammar(4, "\n\nsymbols F+-\nstart F\nangle 90\niterations 3\nrule F F+F-F-F+F\nextra_key 1\nextra_key2 2",
                        "The grammar file is not formatted correctly")
    # commands not separated by new line - should raise error
    test_get_grammar(5, "symbols F+-start F angle 90 iterations 3 rule F F+F-F-F+F",
                        "The grammar file is not formatted correctly")
    # not separated by space - should raise error
    test_get_grammar(5, "\nsymbols F+- \nstartF\nangle90\niterations 3\nrule F F+F-F-F+F",
                        "The grammar file is not formatted correctly")
    # different orders - should work fine
    test_get_grammar(6, "symbols F+-\n\niterations 3\n\n\nangle 90 \nrule F F+F-F-F+F\nstart F",
                    {"symbols": "F+-", "iterations": "3", "angle": "90", "ruleF": "F+F-F-F+F","start": "F",})

    
    
if __name__ == "__main__":
    main()