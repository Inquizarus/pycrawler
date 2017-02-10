#!/usr/bin/env python2

import unittest
import os
import shutil
import xmlrunner
import sys

if sys.argv[-1] != sys.argv[0]:
    test_search = "*{}*Test.py".format(sys.argv[1])
else:
    test_search = "*Test.py"

current_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = "{}/src".format(current_dir)
output_dir = "{}/test-reports".format(current_dir)
if os.path.isdir(output_dir):
    shutil.rmtree(output_dir)

suite = unittest.TestLoader().discover(src_dir, test_search)
result = xmlrunner.XMLTestRunner(output=output_dir, verbosity=2).run(suite)

if len(result.failures) > 0 or len(result.errors) > 0:
    sys.exit(1)
