### Possible Python Performance examples:
* General ideas:
    - Don't reinvent the wheel by writing your own versions of built-in functions.  
        + Example of using len() function vs writing your own function that counts the number of elements by incrementing a variable.
        + Example of using sum() vs for loop for adding elements
    Python 2.7.10 contains 76 built-in variables [source](https://docs.python.org/2/library/functions.html) - you won't need all of them (I don't remember when was the list time - if ever - I used _basestring()_, _execfile()_ or _reload()_), but it will take you just a moment to take a look at that list from time to time and keep it in the back of your head. If you want some more cool functions, there is the [itertools](https://docs.python.org/release/2.7.2/library/itertools.html) module that contains _fast, memory efficient tools that are useful by themselves or in combination_
    - _It's better to beg for forgiveness than to ask for permission_ give some examples where a code with exceptions handling is faster than code with __if__ statements
* Control flow:
    - Don't make loops like that: **for i in range(0,len(list)):**. If you need a list with index use the enumerate() function
* Operators:
    - If checking for True/False the fastest way is __if element__ (vs __if element is True__ or __if element == True__)
* Structures:
    - Lists:
        + Sorting lists is faster if you sort in place (**list.sort() vs sorted(list)**)
        + List comprehension:
            * Example of list comprehension vs for loop (vs lambda) to filter a list of items
            * __in__ operator vs for loop to check if element is in a list
        + There are bad ways to check if a list is empty: **if list == []** or **if len(list) <= 0** but there is also a good way to do that **if not list**
    - Tuples:
    - Sets:
        + Sets vs lists:
            * Lookup time in a set is constant (so it's faster than in a list) but it costs you the overhead to convert list to a set (so in general if you are checking if one element belongs to a collection, use list, if you are checking for multiple elements, convert to a set)
            * Removing duplicates - you get it for free if you convert list to a set (but if the order is important use [OrderedSet](http://code.activestate.com/recipes/576694/))
            * Sets have a lot of useful functions for checking the intersection, union, difference, sub- and super-sets that you don't have in lists: Give a few examples.
    - Dictionaries:
        + Lookup time is constant (same as for sets), so it's faster than with lists
        + Initializing a dictionary: __d = {} vs d = dict()__ (first one is faster, but compare it with different Python compilers)
        + To get an element from the dictionary use __dict.get(key)__ function instead of doing __if key in dict: dict[key]__
        + Example of dictionary comprehension (for example to get a dictionary {number: number**2}) vs for loop
* Strings:
    - example of string formatting vs string concatenation: __"Hello " + s + " !" vs "Hello %s !" % s__
* Lambdas:
    - There is usually no difference between using a lambda and a named function, so often named function is a better solution because it's more readable. Lambdas are nice as a short, simple one-liners that don't require a lot of explanation.
    - Also, according to PEP-8 you should not assign lambda to a variable:  
    Good: **def f(x): return 2*x**  
    Bad: **f = lambda x: 2*x** - this is a duplication of def functionality and can cause confusion ([source](http://stackoverflow.com/questions/25010167/e731-do-not-assign-a-lambda-expression-use-a-def))
* Generators:
    - Example of finding the first element matching the criteria: comparing list comprehension (it's a totally wrong approach here, since we don't need the whole list) vs for loop (it's faster and seems like a good solution) vs generator (same performance as for loop, but this is a pythonic approach and you can get next elements basically for free)
* Python vs Java mocking:
    - [Reading file in Java](http://stackoverflow.com/questions/4716503/best-way-to-read-a-text-file) vs [Reading file in Python](http://stackoverflow.com/questions/8011797/open-read-and-close-a-file-in-1-line-of-code)


* Sources:
    - [Raymond Hettinger talking about how Pythonic > PEP-8 during PyCon 2015](https://www.youtube.com/watch?v=wf-BqAjZb8M)
