### Possible Python Performance examples:
* General ideas:
    - Don't reinvent the wheel by writing your own versions of built-in functions.  
    Example of using len() function vs writing your own function that counts the number of elements by incrementing a variable.  
    Python 2.7.10 contains 76 built-in variables [source](https://docs.python.org/2/library/functions.html) - you won't need all of them (I don't remember when was the list time - if ever - I used _basestring()_, _execfile()_ or _reload()_), but it will take you just a moment to take a look at that list from time to time and keep it in the back of your head. If you want some more cool functions, there is the [itertools](https://docs.python.org/release/2.7.2/library/itertools.html) module that contains _fast, memory efficient tools that are useful by themselves or in combination_
* Lambdas:
    - There is usually no difference between using a lambda and a named function, so often named function is a better solution because it's more readable. Lambdas are nice as a short, simple one-liners that don't require a lot of explanation.
* List comprehension:
    - Example of list comprehension vs for loop (vs lambda) to filter a list of items
* Generators:
    - Example of finding the first element matching the criteria: comparing list comprehension (it's a totally wrong approach here, since we don't need the whole list) vs for loop (it's faster and seems like a good solution) vs generator (same performance as for loop, but this is a pythonic approach and you can get next elements basically for free)
* Python vs Java mocking:
    - [Reading file in Java](http://stackoverflow.com/questions/4716503/best-way-to-read-a-text-file)


* Sources:
    - [Raymond Hettinger talking about how Pythonic > PEP-8 during PyCon 2015](https://www.youtube.com/watch?v=wf-BqAjZb8M)
