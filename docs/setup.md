# Setting Up a Development Environment

## GitHub

The following will help you create a GitHub account and copy the course repo into your account:

* Go to [GitHub](http://github.com)
* Create a (free) user account
* Go to [the course repo](https://github.com/kyclark/be434-fall-2021)
* Click the "Fork" button (upper-right)

To check out the code locally, I recommend that you configure your SSH keys.
Open a terminal, and do this:

```
ls ~/.ssh
```

If you get an error because that directory does not exist, then run this command:

```
ssh-keygen
```

Press "Enter" repeatedly to accept the default answers (unless you really want to type a passphrase when using your key).
Then try again:

```
$ ls ~/.ssh
codecommit      config          id_rsa.pub
codecommit.pub  id_rsa          known_hosts
```

If all goes well, you should have an _id_rsa_ file, which is a **private** SSH key that should be kept private.
Do not share the contents of this file or copy it anywhere.
You can use the `cat` command to look at the contents of the **public** SSH key in _id_rsa.pub_:

```
cat ~/.ssh/id_rsa.pub
```

Copy all the text you see from "ssh-rsa" to the end.
Then go to your [GitHub settings](https://github.com/settings/profile), click on "SSH and GPG keys," then click the big green "New SSH key" button.
Give the new key a name like "laptop" (you may add keys from other machines like the HPC) and paste in the contents of the **public** key.
Click the "Add SSH key" button to save your new key.

Next, go to the [course repository](https://github.com/kyclark/be434-fall-2021) and click the "Fork" button so as to make a copy of the code into your account. 
Add my GitHub username "kyclark" as a Collaborator on your repo so that I can push and pull code, and then email me your GitHub ID and the URL for your repo. 
All your assignments will be pushed to GitHub where I will pull the code to my machine for checking. 
At the end of the semester, you will have a public repository of code you can share to show proficiency in Python coding and testing.

With that, you now should be able _clone_ or copy down the contents of the repo onto your local machine (e.g., your laptop, but you could also clone it to any machine like a remote server, an AWS VM, the UA HPC, etc.).
Be sure to replace _YOUR_GITHUB_ID_ with your GitHub ID:

```
git clone git@github.com:YOUR_GITHUB_ID/be434-fall-2021.git
```

If that goes well, you should have a _be434-fall-2021_ directory.
Go into that directory:

```
cd be434-fall-2021
```

You will need to configure my original GitHub repo as an _upstream_ source with the following command:

```
git remote add upstream https://github.com/kyclark/be434-fall-2021.git
```

I will make updates to the repo throughout the semester to add new materials and assignments.
You will use this command to _pull_ my changes into your repo:

```
git pull upstream main
```


## Windows

Follow the directions to install [Windows Subsystem for Linux Installation Guide for Windows 10](https://docs.microsoft.com/en-us/windows/wsl/install-win10).

## Mac

* Open Terminal or consider using [iTerm2](https://iterm2.com/).
* Install Xcode command-line utilities.

## VS Code

If you don't have a preferred way to write and edit code, install [VS Code](https://code.visualstudio.com/).

## Python

It's possible you have Python installed, but it's likely that it's version 2.x which is no longer maintained and should not be used.
To find out, run this command:

```
$ python --version
Python 2.7.16
```

You may still have a Python 3.x available as `python3`.
If you have a recent Python in the 3.9 tree, you're all set:

```
$ python3 --version
Python 3.9.1
```

### Installing on macOS with Homebrew

Fingers crossed that this works:

```
brew install python3
```

If that works:

```
$ which python3
/opt/homebrew/bin/python3
$ python3 --version
Python 3.9.6
```

### Downloading and Building Python from Source

If you do not have Python installed and you are not running the Apple M1 processor, you can download the latest Python source code:

```
wget https://www.python.org/ftp/python/3.9.6/Python-3.9.6.tgz
```

If you don't have `wget`, consider installing it.
If you are on macOS, I would recommend you learn how to use [Homebrew](https://brew.sh/).
Alternately, you can use [`curl`](https://curl.se/):

```
curl https://www.python.org/ftp/python/3.9.6/Python-3.9.6.tgz --output Python-3.9.6.tgz
```

The `.tgz` is a Gzipped-compressed _tar_ (tape archive) file, AKA a _tarball_.
You can use `tar` with the following flags:

* `-x`: extract
* `-v`: verbose
* `-f`: the filename of the tar file

You can unpack the tarball like so:

```
tar -x -v -f Python-3.9.6.tgz
```

As these are single-character _short_ flag, they can be combined like `-xvf`.
The order of `xv` and `vx` is not important, but the `-f` must come last as it need to precede the tarball filename.
Oddly, `tar` doesn't even require the dash, so it's quite common to see this like so:

```
tar xvf Python-3.9.6.tgz
```

That should emit around 4500 lines of text explaining the files that are being unpacked.
If you would rather not see that, then omit the `-v` flag.

```
tar xf Python-3.9.6.tgz
```

Use the `cd` (_change directory_) command to go into the new _Python-3.9.6_ directory:

```
cd Python-3.9.6
```

Use `ls` (_list_) to look at the files:

```
$ ls
CODE_OF_CONDUCT.md  Makefile.pre.in     Programs/           configure*
Doc/                Misc/               Python/             configure.ac
Grammar/            Modules/            README.rst          install-sh*
Include/            Objects/            Tools/              netlify.toml
LICENSE             PC/                 aclocal.m4          pyconfig.h.in
Lib/                PCbuild/            config.guess*       setup.py
Mac/                Parser/             config.sub*
```

Run the _configure.sh_ program to find all the important elements on your system that will be needed to build Python such as a C compiler.
This may require you to install said C compiler.
For instance, on macOS you will probably need to install Xcode's command-line utilities.

```
./configure --enable-optimizations
```

If everything goes well, the last line should be this:

```
creating Makefile
```

That means you have a _Makefile_, which means you can run `make` to build Python.
This step may take a while:

```
make
```

If that succeeds, you should be able to run **`make install`** to copy the new Python binary to location like `/usr/local/bin`.

## Author

Ken Youens-Clark <kyclark@gmail.com>
