import timeit
import logging
import json
import argparse

log = logging.getLogger(__name__)
log.name = 'protolite benchmark'


protobuf_setup = """
import messages_pb2
"""
protobuf = """
user = messages_pb2.User(
    userID=1007843487950966784L,
    firstName='Foo',
    lastName='Bar',
    userType=messages_pb2.User.STANDARD,
    homeAddress=messages_pb2.USAddress(
        street='1 Main st',
        city='Springfield',
        state='MA',
        zipCode='12345-6789',
        country='USA',
    ),
    phoneNumbers=[
        messages_pb2.PhoneNumber(
            countryCode=1,
            number='222-222-2222',
        ),
        messages_pb2.PhoneNumber(
            countryCode=3,
            number='444-444-4444',
        ),
    ],
)

data = user.SerializeToString()
user = messages_pb2.User()
user.ParseFromString(data)
"""

protolite_setup = """
import messages
"""
protolite = """
user = {
    'user_id': 1007843487950966784L,
    'first_name': 'Foo',
    'last_name': 'Bar',
    'user_type': messages.user.STANDARD,
    'home_address': {
        'street': '1 Main st',
        'city': 'Springfield',
        'state': 'MA',
        'zip_code': '12345-6789',
        'country': 'USA',
    },
    'phone_numbers': [
        {
            'country_code': 1,
            'number': '222-222-2222',
        },
        {
            'country_code': 3,
            'number': '444-444-4444',
        },
    ],
}
data = messages.user.encode(user)
messages.user.decode(data)
"""


def benchmark():
    log.info('Calculating number of loops...')
    # In order to make the overhead insignificant run the benchmark at
    # least 100*overhead times.
    overhead = timeit.repeat(stmt='pass')
    target = min(overhead) * 100
    # Find the number of loops by trying successive powers of 10 until the total
    # time is >= overhead.
    loops = 0
    sample = 0
    while sample < target:
        loops += 1
        # Use the slowest of the two code samples, protobuf
        sample = timeit.timeit(
            stmt=protobuf,
            setup=protobuf_setup,
            number=10**loops,
        )
    loops = 10**loops
    if loops < 10000:
        loops = 10000
    repeat = 3

    log.info('Running protobuf benchmark...')
    times = timeit.repeat(
        stmt=protobuf,
        setup=protobuf_setup,
        repeat=repeat,
        number=loops,
    )
    buftime = min(times)
    log.info('Running protolite benchmark...')
    times = timeit.repeat(
        stmt=protolite,
        setup=protolite_setup,
        repeat=repeat,
        number=loops,
    )
    litetime = min(times)

    bufmsg = dict([
        ('loops', loops),
        ('repeat', repeat),
        ('secs', buftime),
        ('speed', litetime/buftime),
    ])
    litemsg = dict([
        ('loops', loops),
        ('repeat', repeat),
        ('secs', litetime),
        ('speed', buftime/litetime),
    ])
    results = dict([
        ('protobuf', bufmsg),
        ('protolite', litemsg),
    ])
    log.info('Results:')
    print json.dumps(results, indent=2)


def parse_args():
    parser = argparse.ArgumentParser(
        description='benchmark protolite',
    )
    parser.add_argument(
        '-p',
        '--pypy',
        action='store_true',
        default=False,
        help='warm up the Pypy JIT compiler (default: %(default)s)',
    )
    return parser.parse_args()


def warm_up():
    log.info('Warming up the Pypy JIT compiler...')
    timeit.repeat(
        stmt=protobuf,
        setup=protobuf_setup,
        repeat=3,
        number=10**4,
    )


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s.%(msecs)03d %(name)s: %(levelname)s: %(message)s',
        datefmt='%Y-%m-%dT%H:%M:%S',
    )
    args = parse_args()
    if args.pypy:
        warm_up()
    log.info('Starting benchmark...')
    benchmark()
