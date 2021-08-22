# Setting Up a Development Environment

## Windows

Follow the directions to install [Windows Subsystem for Linux Installation Guide for Windows 10](https://docs.microsoft.com/en-us/windows/wsl/install-win10).

## Mac

Open Terminal.
Consider using [iTerm2](https://iterm2.com/).

## VS Code

If you don't have a preferred way to write and edit code, install [VS Code](https://code.visualstudio.com/).

## Python

If you have a recent Python in the 3.9 tree, you're all set.
To check, open a terminal and type this:

```
$ python3 --version
Python 3.9.1
```

If not, download the latest Python source code.
Build and install on your system.

```
$ wget https://www.python.org/ftp/python/3.9.6/Python-3.9.6.tgz
$ tar xvf Python-3.9.6.tgz
$ cd Python-3.9.6
$ ./configure && make install
```

## Author

Ken Youens-Clark <kyclark@gmail.com>
