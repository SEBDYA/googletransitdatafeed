#!/usr/bin/python2.4

# Code shared between tests.

import os
import subprocess
import tempfile
import unittest
import sys
import cStringIO as StringIO


def check_call(cmd, expected_retcode=0, **kwargs):
  """Convenience function that is in the docs for subprocess but not
  installed on my system. Raises an Exception if the return code is not
  expected_retcode. Returns a tuple of strings, (stdout, stderr)."""
  try:
    if 'stdout' in kwargs or 'stderr' in kwargs:
      raise Exception("Don't pass stdout or stderr")
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, **kwargs)
    (out, err) = p.communicate()
    retcode = p.returncode
  except Exception, e:
    raise Exception("When running %s: %s" % (cmd, e))
  if retcode < 0:
    raise Exception("Child '%s' was terminated by signal %d" % (cmd,
      -retcode))
  elif retcode != expected_retcode:
    raise Exception("Child '%s' returned %d" % (cmd, retcode))
  return (out, err)

class TempDirTestCaseBase(unittest.TestCase):
  """Make a temporary directory the current directory before running the test
  and remove it after the test.
  """
  def setUp(self):
    self.tempdirpath = tempfile.mkdtemp()
    self._oldcwd = os.getcwd()
    os.chdir(self.tempdirpath)

  def tearDown(self):
    os.chdir(self._oldcwd)
    # Remove everything in self.tempdirpath
    for root, dirs, files in os.walk(self.tempdirpath, topdown=False):
      for name in files:
        os.remove(os.path.join(root, name))
      for name in dirs:
        os.rmdir(os.path.join(root, name))

  def GetExamplePath(self, name):
    """Return the full path of a file in the examples directory"""
    return self.GetPath('examples', name)

  def GetPath(self, *path):
    """Return the absolute path of path, relative to cwd when test was
    started."""
    here = os.path.dirname(__file__)  # Relative to _oldcwd
    return os.path.join(self._oldcwd, here, '..', *path)

  def CheckCallWithPath(self, cmd, expected_retcode=0):
    """Run cmd[0] with args cmd[1:], pointing PYTHONPATH to the root
    of this source tree. Raises an Exception if the return code is not
    expected_retcode. Returns a tuple of strings, (stdout, stderr)."""
    env = {'PYTHONPATH': self.GetPath()}
    cmd = [sys.executable] + cmd
    return check_call(cmd, expected_retcode=expected_retcode, shell=False,
                      env=env)
