=========
protolite
=========

Lightweight implementation of Google's Protocol Buffers in Python.

In benchmarks, the protolite encoder ran twice as fast as
Google's. Using Python's ``timeit`` module, the same data for both APIs was
encoded and decoded 10000 times. The lowest time of three attempts was
picked for each::

    protobuf:  3.6064529418945312 seconds
    protolite: 1.7224960327148438 seconds

If we take the ratio of these two times we see that protolite was
about two times faster than its counterpart.

Similarly, using Pypy we get about twice the speed::

    protobuf:  0.807873010635376 seconds
    protolite: 0.4414529800415039 seconds

The ``benchmark`` directory in the github_ repository contains the files
needed to re-run the tests . In addition, you will need the protobuf
Python_ library. Try it on your platform, but, keep your machine as quite
as possible so as to not skew the results::

    PYTHONPATH=$PYTHONPATH:$(pwd) python benchmark/benchmark.py

Pass the --pypy flag if you want to use Pypy in order to warm up the
Pypy JIT compiler and get a more accurate result::

    PYTHONPATH=$PYTHONPATH:$(pwd) pypy benchmark/benchmark.py --pypy

You can also make changes to the ``benchmark/messages.proto`` file to create
your own tests. You'll need to re-compile the ``messages.py`` and
``messages_pb2.py`` files in the ``benchmark`` directory afterwards by running
the ``make`` command inside the same directory. Of course, you will need protoc_
to compile Google's version.


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

    git clone https://github.com/thelinuxkid/python-protolite.git
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

printing
--------

The message objects also contain a pretty print method. Calling
``message.user.pprint(msg_enc)`` would produce::

    {
        "type": "STANDARD",
        "user_id": 123
    }


You can pass the keyword argument ``stream`` to ``pprint`` to write to
a stream different than sys.stdout.

parser
======

If you download the source code from github_ you will see a
``grammar`` directory at the root level. This directory contains all
the files used to create the parser and lexer in ``protolite.parser``,
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
are but move the \*.py files to protolite/parser to use your new parser
with ``python-protolitec``. If you want to use a different version of
Antlr do so at your own risk. You will likely need the new Antlr
version to match the Python runtime version in setup.py.

.. _protobuf:  https://code.google.com/p/protobuf
.. _pypi: https://pypi.python.org/pypi/python-protolite
.. _github: https://github.com/thelinuxkid/python-protolite
.. _antlr: http://antlr3.org/
.. _Python: https://pypi.python.org/pypi/protobuf
.. _protoc: https://code.google.com/p/protobuf/downloads/list
