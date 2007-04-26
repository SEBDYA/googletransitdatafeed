#!/usr/bin/python2.4

# Copyright (C) 2007 Google Inc.
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

"""
This file is the script used to create the standalone Windows executable
version of the feedvalidator program.

To run:
    C:\Python24\python feedvalidator-setup.py py2exe
    
This will create a dist/ directory containing feedvalidator.exe and its
associated support files, which can then be zipped up and distributed.
"""

from distutils.core import setup
import glob
import os.path

try:
  import py2exe
except ImportError, e:
  # Won't be able to generate win32 exe
  pass

options = {'py2exe': {'packages': ['pytz']}}  
scripts = ['feedvalidator.py', 'schedule_viewer.py']
setup(
    version='0.1.0',
    name='transitfeed',
    url='http://code.google.com/p/googletransitdatafeed/',
    py_modules=['transitfeed'],
    scripts=scripts,
    data_files=[('schedule_viewer_files', glob.glob(os.path.join('schedule_viewer_files', '*')))],
    console=scripts,
    options=options
    )

#    package_data={'schedule_viewer': ['schedule_viewer_files/*', 'schedule_viewer.html']}
