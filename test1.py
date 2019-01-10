import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("square", type=int,
#                     help="display a square of a given number")
# parser.add_argument("-v", "--verbose", action="store_true",
#                     help="increase output verbosity")
# args = parser.parse_args()
# answer = args.square**2
# if args.verbose:
#     print("the square of {} equals {}".format(args.square, answer))
# else:
#     print(answer)
#

import unittest

def plus (a ,b):
    return a+b+9

class test_plus(unittest.TestCase):
    def testEqualsum(self):
        self.assertEqual(plus(2,5),7)

    def testNotEqualsum(self):
        self.assertNotEqual(plus(2,5),9)

if __name__ == '__main__':
    unittest.main()
    assert 4== plus (2,4)
