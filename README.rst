=========
protolite
=========

Lightweight implementation of Google's Protocol Buffers in Python

description
===========

Protocol Buffers (protobuf_) is a data interchange format created by
Google. protolite is a rewrite of its encoder and file generator
specifically created and optimized for Python. The encoder is
optimized for speed taking the language's properties in mind. The
generator aims to provide ease-of-use and compatibility with the
language. For example, messages are implemented using only
dicts. Familiarity with protobuf is required in order to use protolite
effectively.


installation
============

You can download and install protolite from pypi_ with pip::

    pip install python-protolite

Alternatively, you can clone the repository containing the source code
from github_ and install protolite via setuptools::

    git clone https://github.com/littleinc/python-protolite.git
    cd python-protolite
    python setup.py install

usage
=====

generating files
----------------

protolite comes with a utility that generates Python files structured
for efficiency and readbility. After the installation you will have an
executable file called ``python-protolitec``. Its most simple usage
takes two positional arguments. The first is a list of the protobuf
definition files and the second a directory where to write the Python
version of those files::

    python-protolitec proto/*.proto python

The output files will retain the same file name as the source; only the
extension will be changed. For example, the file ``proto/messages.proto``
will produce the file ``python/messages.py``. You can use the ``--help``
flag to view the other options offered by ``python-protolitec``.

encoding
--------

Let's say you have a protobuf file called ``messages.proto`` containing::

    message User {
        optional uint32 userID = 1;
        enum UserType {
            STANDARD = 0;
            ADMIN = 1;
        }
        optional UserType type = 2;
    }

``python-protolite`` will create a Python module ``messages`` with a ``user``
object which has a ``decode`` and  an ``encode`` method. To encode a
message you would do something like::

    import messages

    msg_enc = {'user_id': 123, 'type': messages.user_type.STANDARD}
    data = messages.user.encode(msg_enc)

As you can see, ``python-protolite`` changes camel-case variable names to
underscore. On the other end, to decode the message you would do
something similar::

    import messages

    msg_dec = messages.user.decode(data)

The variable msg_dec will be equal to msg_enc.

parser
======

If you download the source code from github_ you will see a
``grammar`` directory at the root level. This directory contains all
the files used to create the parser and lexer in ``protolite.parse``,
the module used by ``python-protolitec`` to parse the protobuf
definition files. If you are familiar with Antlr_ you can edit the
``proto_lexer.g`` and ``proto_parser.g`` files in this directory to create a
new Python parser and/or lexer using the Antlr jar in the same directory::

    cd grammar
    java -jar antlr-3.1.3.jar -fo . proto_lexer.g
    java -jar antlr-3.1.3.jar -fo . proto_parser.g

This will create four files:  ``proto_lexer.py``,
``proto_lexer.tokens``, ``proto_parser.py`` and
``proto_parser.tokens``. You can leave the \*.tokens files where they
are but move the \*.py files to protolite/parse to use your new parser
with ``python-protolitec``. If you want to use a different version of
Antlr do so at your own risk. You will likely need the new Antlr
version to match the Python runtime version in setup.py.

.. _protobuf:  https://code.google.com/p/protobuf
.. _pypi: https://pypi.python.org/pypi/python-protolite
.. _github: https://github.com/littleinc/python-protolite
.. _antlr: http://antlr3.org/
