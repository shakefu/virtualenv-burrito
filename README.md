# Virtualenv Burrito #

With one command, have a working Python [virtualenv](http://pypi.python.org/pypi/virtualenv) +
[virtualenvwrapper](http://pypi.python.org/pypi/virtualenvwrapper)
environment.

This is a fork updated to work with Python 3 and the latest versions of pip,
setuptools, virtualenv and virtualenvwrapper.

Original script by [brainsik](https://github.com/brainsik). If you click
*donate* you'll be donating to him, which you should.

[![Build Status](https://api.travis-ci.org/shakefu/virtualenv-burrito.svg?branch=master)](https://travis-ci.org/shakefu/virtualenv-burrito)
[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=DSKBAGSZJEF28&lc=US&item_name=Virtualenv%20Burrito&currency_code=USD&bn=PP%2dDonationsBF%3abtn_donate_LG%2egif%3aNonHosted)

## Requirements ##

Python 2.6, 2.7 and 3.4 or higher on Linux or OS X. To check your Python
version, run:

    python -V

## Install ##

    curl -sL https://raw.githubusercontent.com/shakefu/virtualenv-burrito/master/virtualenv-burrito.sh | $SHELL

If you're behind a proxy, make sure your shell has the proper `http_proxy` and
`https_proxy` variables set.

If you're using a Linux desktop terminal, you may need to configure it to use a
"login shell". For gnome-terminal this can be done by running:

    gconftool-2 -t bool -s /apps/gnome-terminal/profiles/Default/login_shell true

## Use ##

See the
[virtualenvwrapper quickstart](https://virtualenvwrapper.readthedocs.io/en/latest/install.html#quick-start)
or read the
[virtualenvwrapper command reference](https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html).

### Quickstart ###

To create a new virtualenv:

    mkvirtualenv newname

Once activated, `pip install <package>` (_without_ using sudo) whichever Python
packages you want. They'll only be available in that virtualenv. You can make
as many virtualenvs as you want.

To switch between virtualenvs:

    workon othername

### Upgrade ###

To upgrade to the latest virtualenv + virtualenvwrapper packages:

    virtualenv-burrito upgrade

## Why ##

To get Python coders coding.

Virtualenv Burrito was inspired by
[Pycon sprinters](http://us.pycon.org/2011/sprints/) who wasted time getting
virtualenv setup so they could start hacking on code. It's sadly
complicated to quickly setup the wonderful virtualenv + virtualenvwrapper
environment. Depending on your system you may end up yak shaving with
setuptools, distribute, virtualenv, virtulenvwrapper, .bashrc, PyPI,
apt-get/MacPorts, and more.

A second feature is the ability to upgrade to newer versions of virtualenv and
virtualenvwrapper with a single command.

## Multiple Pythons ##

Both `virtualenv` and `virtualenvwrapper` let you specify which Python
interpreter the virtualenv should use via the `-p` switch. For example:

    mkvirtualenv -p /path/to/some/python coolname

This creates a virtualenv called “coolname” which uses `/path/to/some/python`
as its interpreter. This was tested with [PyPy](http://pypy.org/) and it
worked great.

## Credits ##

The real hard work is done by the creators of
[Virtualenv](http://www.virtualenv.org/) and
[Virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/).
Virtualenv is maintained by [Ian Bicking](http://ianbicking.org/).
Virtualenvwrapper is maintained by [Doug Hellman](http://www.doughellmann.com/).

## Advanced ##

If you have a sophisticated shell environment or customized install scripts,
you may want to prevent the install script (virtualenv-burrito.sh) from
modifying your dot profile. To do this, either use the `--exclude-profile`
option or set the environment variable `exclude_profile` to a non-empty value:

    curl -sL https://raw.githubusercontent.com/shakefu/virtualenv-burrito/master/virtualenv-burrito.sh | exclude_profile=1 $SHELL

## Uninstall ##

1. Edit your shell profile (e.g., .profile, .bash_profile, etc.) and remove the
   few lines of code added.
2. `rm -rf ~/.venvburrito`

## Caveat emptor ##

This simple script is meant for people who do not have virtualenv installed.
