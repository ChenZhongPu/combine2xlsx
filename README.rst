combine2xlsx
============

combine2xlsx is a utility to combine multi Microsoft Excel files into a large one(.xlsx).
Currently it only supports xls and xlsx files as input.

Go to `combine2xlsx in pypi`_.

.. _combine2xlsx in pypi: https://pypi.python.org/pypi/combine2xlsx


Why Should I Use This?
-----------------------

The maximum row number of xls is only 65536. Thus, you cannot merge it as an xls file.
And the xlwt module doesn't support the xls format.

Secondly, the pandas module's API seems to be simple enough, but it is quite slow, and memory-inefficient.


Demo
-----

First, you can install it via 

.. code-block:: bash

	 $ pip3 install combine2xlsx

Example:

.. code-block:: python

	import combine2xlsx
	combine2xlsx.combine(['input1.xls', 'input2.xlsx'], 'outputname.xlsx')


Contibuting
-----------

1. Folk the `repository <https://github.com/ChenZhongPu/combine2xlsx>`_ on GitHub.
2. Make a branch off of master and commit your changes to it.
3. Submit a Pull Request to the master branch on GitHub.

If you'd like to have a development environment for combine2xlsx, you should create a
virtualenv and then do ``pip install -e .`` from within the directory.