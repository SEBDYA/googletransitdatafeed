#!/usr/bin/python2.4

# Test the examples to make sure they are not broken

import os
import subprocess
import tempfile

def check_call(cmd, shell=True):
  """Convenience function that is in the docs for subprocess but not
  installed on my system."""
  retcode = subprocess.call(cmd, shell=shell)
  if retcode < 0:
    raise Exception("Child '%s' was terminated by signal %d" % (cmd,
      -retcode))
  elif retcode != 0:
    raise Exception("Child '%s' returned %d" % (cmd, retcode))


def PathInExamples(name):
  here = os.path.dirname(__file__)
  return os.path.join(here, '..', 'examples', name)


def test_shuttle_from_xmlfeed():
  (fd, tempfilepath) = tempfile.mkstemp("-YYYYMMDD.zip")
  # Open file handle causes an exception during remove in Windows
  os.close(fd)

  check_call([PathInExamples('shuttle_from_xmlfeed.py'),
              '--input',
              PathInExamples('shuttle_from_xmlfeed.xml'),
              '--output', tempfilepath,
              # rm the dated output file
              '--execute', 'rm -f %(path)s',
              # save the path of the dated output to tempfilepath
              '--execute', 'echo %%(path)s > %s' % tempfilepath
              ], shell=False)

  dated_path = open(tempfilepath).read().strip()
  if os.path.exists(dated_path):
    raise Exception('--execute failed to rm output')
  os.remove(tempfilepath)


def test_table():
  (fd, tempfilepath) = tempfile.mkstemp("-YYYYMMDD.zip")
  # Open file handle causes an exception during remove in Windows
  os.close(fd)
  check_call([PathInExamples('table.py'),
              '--input', PathInExamples('table.txt'),
              '--output', tempfilepath], shell=False)
  if not os.path.exists(tempfilepath):
    raise Exception('should have created output')
  os.remove(tempfilepath)


def test_small_builder():
  (fd, tempfilepath) = tempfile.mkstemp(".zip")
  # Open file handle causes an exception during remove in Windows
  os.close(fd)
  check_call([PathInExamples('small_builder.py'),
              '--output', tempfilepath], shell=False)
  if not os.path.exists(tempfilepath):
    raise Exception('should have created output')
  os.remove(tempfilepath)



if __name__ == '__main__':
  for (k, v) in locals().items():
    if k.startswith('test_'):
      v()
