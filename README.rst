map()
-----
::

    map() applies the function func to all the elements of the sequence seq.

* syntax
::

    map(func, seq)

* Info
::

    The first argument func is the name of a function and
    the second a sequence (e.g. a list) seq.


* It returns a new list with the elements changed by func

* Additional Info
::

    map() can be applied to more than one list. The lists have to have the same length.
    map() will apply its lambda function to the elements of the argument lists,
    i.e. it first applies to the elements with the 0th index,
    then to the elements with the 1st index until the n-th index is reached
