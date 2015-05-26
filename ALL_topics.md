### Possible Python Performance improvements and best practices:
* General ideas:
    - Don't reinvent the wheel by writing your own versions of built-in functions.
        + Example of using len() function vs writing your own function that counts the number of elements by incrementing a variable.
        + Example of using sum() vs for loop for adding elements
    Python 2.7.10 contains 76 built-in variables [source](https://docs.python.org/2/library/functions.html) - you won't need all of them (I don't remember when was the list time - if ever - I used _basestring()_, _execfile()_ or _reload()_), but it will take you just a moment to take a look at that list from time to time and keep it in the back of your head. If you want some more cool functions, there is the [itertools](https://docs.python.org/release/2.7.2/library/itertools.html) module that contains _fast, memory efficient tools that are useful by themselves or in combination_
    - _It's better to beg for forgiveness than to ask for permission_ give some examples where a code with exceptions handling is faster than code with __if__ statements
    - Mutable defaults: don't do stuff like __def foo(element, x=[])__, you will spend a lot of time debugging this error. Use **def foo(element, x=None):;if x in None:; x = []**
    - Parallel vs sequential variables assignment: parallel variables assignment is faster than sequential one (however, sequential assignment might be more clear for some):
    >>> %timeit q=1;w=2;e=3;r=4;t=5;y=6;u=7;i=8;o=9;p=0;
    10000000 loops, best of 3: 69.6 ns per loop
    >>> %timeit q,w,e,r,t,y,u,i,o,p = 1,2,3,4,5,6,7,8,9,0
    10000000 loops, best of 3: 49.4 ns per loop
* Control flow:
    - Loops:
        + You almost never need to use the **for** loop. Map/filter/reduce (functions are better solution. List comprehensions are the best solution.
        + If the body of a loop is simple, the interpreter overhead for the **for** loop itself can be quite big - in this case you can use **map()**. Map is _a for loop moved into C code_.[^1]
        + It's faster to perform an operation 1000 times inside a function, than calling the function 1000 times, for example:
        x = 0
        def do(num):
        &nbsp;global x
        &nbsp;x =+ 1
        for num in range(1000):
        &nbsp;do(num)
        is slower than:
        x = 0
        def do():
        &nbsp;global x
        &nbsp;for num in range(1000):
        &nbsp;&nbsp;x =+ 1
        do().[^1]
        + Don't make loops like that: **for i in range(0,len(list)):**. If you need a list with index use the enumerate() function
* Operators:
    - If checking for True/False the fastest way is __if element__ (vs __if element is True__ or __if element == True__)
* Structures:
    - General:
        + Using [] is faster than calling list(), using {} is faster than calling dict() because the first ones are _literal syntax_ so Python just creates bytecode for them, while the second one are _objects_ that need to be resolved [^3]
    - Lists:
        + Sorting lists is faster if you sort in place (**list.sort() vs sorted(list)**)
        + When using **sorted()** function you can specify **cmp()** function that is used to compare two elements or **key()** (Python 2.4 and up)function that will return a comparison key for each list element. Use the **key()** because it's faster (the **cmp()** is actually removed in Python 3) - cmp has to be evaluated for each comparison, while key only once per element
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
    - If you need to create a string from a list of words, it's faster to use **s = "".join(list)** than **for x in list: s += x**. The same if you need to call a function on each element of list: this **slist = [some_function(elt) for elt in somelist]; s = "".join(slist)** is faster than the for loop.[^1]
    - Using string formatting is faster than string concatenation: **out = "<html>%s%s%s%s</html>" % (head, prologue, query, tail)** is better than **out = "<html>" + head + prologue + query + tail + "</html>"** (and using **out = "<html>%(head)s%(prologue)s%(query)s%(tail)s</html>" % locals()** is more clear).[^1]
* Lambdas:
    - There is usually no difference between using a lambda and a named function, so often named function is a better solution because it's more readable. Lambdas are nice as a short, simple one-liners that don't require a lot of explanation.
    - Also, according to PEP-8 you should not assign lambda to a variable:
    Good: **def f(x): return 2*x**
    Bad: **f = lambda x: 2*x** - this is a duplication of def functionality and can cause confusion ([source](http://stackoverflow.com/questions/25010167/e731-do-not-assign-a-lambda-expression-use-a-def))
* Generators:
    - In short, generator expressions are like list comprehension but they don't generate the whole list at once (so they are faster if you don't need the whole list).
    - Example of finding the first element matching the criteria: comparing list comprehension (it's a totally wrong approach here, since we don't need the whole list) vs for loop (it's faster and seems like a good solution) vs generator (same performance as for loop, but this is a pythonic approach and you can get next elements basically for free)
* Functions:
    - each time you call function with dots inside (like **newlist.append** or **str.upper**, the function's reference is reevaluated. You can assign it to a variable like **append = newlist.append** and then use **append(element)** for a performance gain and a readability lost.[^1]
    - **range** vs **xrange**: in most cases xrange will have a better performance than range. However there are some situations where you actually want to use **range**:
        + when you actually need to initialize a list (for example to slice it), you would use **range**.
        + if you will iterate over the sequence multiple times, **range** will be faster, because **xrange** need to reconstruct the list every time.
        + **xrange** doesn't exist in Python 3. Remember to change it when porting (this can be easily done with automatic tools like **2to3**).[^2]
* Scope:
    - Python can access local variables faster than global variables, so if inside a function you assign **upper = str.upper** it will be faster than calling **str.upper()** but less readable.[^1]
    - Modules and namespaces:
        + If you have some modules that you will use only in some specific functions, it's faster to import than module inside function definition than in the global namespace (at the beginning of the file) - but you will lose some readability (it won't be obvious what modules are imported).[^1]
* Comparing with other languages:
    - Compare the 3 following ways to double the value of x: **x * 2**, **x << 1** and **x + x**. They perform the same operation, but the last version is faster (1,5 times faster) than the previous two. However, in C all those 3 operations would be translated to the same machine instruction- thus the execution time would be almost the same.
    - Python vs Java mocking:
        + [Reading file in Java](http://stackoverflow.com/questions/4716503/best-way-to-read-a-text-file) vs [Reading file in Python](http://stackoverflow.com/questions/8011797/open-read-and-close-a-file-in-1-line-of-code)
* Advanced profiling:
    - Always use profiling tools to find bottlenecks of your application. There is no point for you to try to optimize those parts of code that are already running fast or are called very rarely. Use module like **cProfile** (that replaced **hotshot**, that replaced **profile**) or **trace**.

* Sources:
    - [Raymond Hettinger talking about how Pythonic > PEP-8 during PyCon 2015](https://www.youtube.com/watch?v=wf-BqAjZb8M)

[^1]: https://wiki.python.org/moin/PythonSpeed/PerformanceTips
[^2]: http://stackoverflow.com/questions/135041/should-you-always-favor-xrange-over-range
[^3]: http://stackoverflow.com/questions/30216000/why-is-faster-than-list
