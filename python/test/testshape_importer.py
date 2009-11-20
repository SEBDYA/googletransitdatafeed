#!/usr/bin/python2.4
#
# Copyright 2008 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A smoke-test for the shape_importer script."""

import os
import unittest
import transitfeed
import util


class FullTests(util.TempDirTestCaseBase):
  def testCommandLineError(self):
    (out, err) = self.CheckCallWithPath(
        [self.GetPath('shape_importer.py'), '--bad_flag'], expected_retcode=2)
    self.assertMatchesRegex(r'no such option.*--bad_flag', err)
    self.assertMatchesRegex(r'--dest_gtfs', err)
    self.assertFalse(os.path.exists('transitfeedcrash.txt'))

  # TODO(Tom): Find an example shape file we can distribute and use it to
  # create an integration test.


if __name__ == '__main__':
  unittest.main()
