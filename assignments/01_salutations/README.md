# Assignment 1: Salutations

Create Python program called `saluations.py` that will print a friendly greeting.

## Getting Started with new.py

You can start with the `new.py` program:

```
$ new.py -p 'Print greeting' salutations.py
Done, see new script "salutations.py."
```

Open the new `salutations.py` program and modify it to accept three optional arguments:

* `-g|--greeting`: A greeting, defaults to "Howdy"
* `-n|--name`: A name to greeting, defaults to "Stranger"
* `-e|--excited`: A flag to terminate the greeting with an exclamation point

The program should respond to `-h|--help` to print the following usage:

```
$ ./salutations.py -h
usage: salutations.py [-h] [-g str] [-n str] [-e]

Greetings and salutations

optional arguments:
  -h, --help            show this help message and exit
  -g str, --greeting str
                        The greeting (default: Howdy)
  -n str, --name str    Whom to greet (default: Stranger)
  -e, --excited         Include an exclamation point (default: False)
```

When run with no arguments, it should use the default values to print the following:

```
$ ./salutations.py
Howdy, Stranger.
```

The `-g|--greeting` option should cause it to use the provided greeting:

```
$ ./salutations.py -g Sup
Sup, Stranger.
```

The `-n|--name` option should cause it to use the provided name:

```
$ ./salutations.py -n Amanda
Howdy, Amanda.
```

The `-e|--excited` flag should cause the greeting to end with a bang:

```
$ ./salutations.py -e
Howdy, Stranger!
```

The program should accept any combination of the short or long names of the arguments:

```
$ ./salutations.py --greeting Sup --name Dude --excited
Sup, Dude!
```

## Testing

The test suite will require the modules pytest, flake8, and pylint which you can install with the following command:

```
$ python3 -m pip install pytest flake8 pylint
```

You can run the test suite with the following command:

```
$ pytest -xv --pylint --flake8 test.py
```

You can also use the Makefile shortcut:

```
$ make test
```

The tests include linting with `pylint` and `flake8`, so be sure that you format your code with something like `yapf` or `black` (which may need to be installed using the `pip` module above.

A passing test suite looks like this:

```
============================= test session starts ==============================
...
--------------------------------------------------------------------------------
Linting files
.
--------------------------------------------------------------------------------

test.py::PYLINT PASSED                                                   [ 11%]
test.py::FLAKE8 PASSED                                                   [ 22%]
test.py::test_exists PASSED                                              [ 33%]
test.py::test_usage PASSED                                               [ 44%]
test.py::test_defaults PASSED                                            [ 55%]
test.py::test_greeting PASSED                                            [ 66%]
test.py::test_name PASSED                                                [ 77%]
test.py::test_excited PASSED                                             [ 88%]
test.py::test_all_options PASSED                                         [100%]

============================== 9 passed in 0.51s ===============================
```

Your grade is whatever percentage of tests your code passes.

## Author

Ken Youens-Clark <kyclark@gmail.com>
