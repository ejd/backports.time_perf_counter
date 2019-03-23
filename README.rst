*********************************
 **backports.time_perf_counter**
*********************************

This package contains a backport_ of the `time.perf_counter()`_
function introduced in Python 3.3.  This package is intended for use
with Python versions older than 3.3 but will work just fine under
newer Pythons.  When used with Python 3.3 and newer, the main module
simply exports ``time.perf_counter()``.

The backported functionality is based on the pseudocode_ in :PEP:`418`
that describes how ``time.perf_counter()`` could be implemented.  When
used with Python versions older than 3.3, the exported
``perf_counter()`` function relies on the ``monotonic()`` function
provided by the monotonic_ package.

.. _backport: https://en.wikipedia.org/wiki/Backporting
.. _time.perf_counter(): https://docs.python.org/3.3/library/time.html#time.perf_counter
.. _pseudocode: https://www.python.org/dev/peps/pep-0418/#time-perf-counter
.. _monotonic: https://pypi.org/project/monotonic/

=======
 Usage
=======

I recommend not introducing a dependency on this package under Pythons
which provide ``time.perf_counter()``.  In your package's
``setup.py``:

.. code:: python

   import setuptools
   setuptools.setup(
       install_requires=[
           'backports.time_perf_counter; python_version < "3.3"'
       ]
   )

In the module that relies on ``perf_counter()``:

.. code:: python

   try:
       # Python >= 3.3
       from time import perf_counter
   except ImportError:
       # Python < 3.3
       from backports.time_perf_counter import perf_counter

=======
 Tests
=======

This package's tests use the builtin unittest_ and can be run without
first installing the package:

.. code:: console

   python setup.py test

The test cases are based on tests_ from the Python standard library's
``time`` module that exercise ``time.perf_counter()``.  There are an
admittedly small number of tests; pull requests with more tests are
welcome.

.. _unittest: https://docs.python.org/3/library/unittest.html
.. _tests: https://github.com/python/cpython/blob/master/Lib/test/test_time.py
