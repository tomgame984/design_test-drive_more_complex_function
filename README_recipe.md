# {{PROBLEM}} Function Design Recipe

## 1. Describe the Problem

As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied, telling them their current age and the required age (16).

As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.

As an admin
So that invalid entries are rejected
I want to generate an exception when the date of birth isn't the right type or format.



## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def check_age(birthday):
    """Extracts uppercase words from a string

    Parameters: (list all parameters and their types)
        birthday: string 

    Returns: (state the return value and its type)
        a success message or a denied message

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a date string in the incorrect format
It returns exception message
"""
check_age("----") => "Exception - incorrect format"

"""
Given a date string in the correct but under 16
It returns access denied
"""
check_age("2020-02-05") => "ACCESS DENIED! You are 4 years old, but need to be 16 to gain access"

"""
Given a date string in the correct format and over 16
It returns access granted
"""
check_age("1984-02-09") => "ACCESS GRANTED"

"""
Given a date string in the correct but under 16
It returns access denied
"""
check_age("2008-02-06") => "ACCESS DENIED! You are 15 years old, but need to be 16 to gain access"

"""
Given a date string in the correct format and over 16
It returns access granted
"""
check_age("2008-02-05") => "ACCESS GRANTED"

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
