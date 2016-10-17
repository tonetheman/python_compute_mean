Look first at version 1 and 13

What is the difference?
If I were writing this in C/C++ I would use version 13.

What is an iterator?
It is an object that knows how to iterate a container.

What is an iterator in python?
It is something that has a "magic method" named __iter__ defined

What is iterable?
Anything that defines that magic __iter__ method. Even if it does not work right.

There is tons more to be said about iterators and generators...
not here
http://anandology.com/python-practice-book/iterators.html

Look at mean2
What is reduce and operator?

reduce
This is a built in (comes with python for free). It takes a function and an iterable.
It also takes a default value too. reduce takes a sequence of values and "reduces"
it down to 1 value. It does that with repeated calls to the function.

reduce is not magic really...
Look at tony_reduce.py

what is the standard library operators?
https://docs.python.org/2/library/operator.html
It is really is standard operations (like addition, subtraction, comparison...)
Defined in functions.

python has a built-in (for free) function called sum?
Who knew. You SHOULD really take time to look at all the python built in functions.
