#!/usr/bin/python2.5

# A really simple example of using transitfeed to build a Google Transit
# Feed Specification file.

import transitfeed
from optparse import OptionParser


parser = OptionParser()
(options, args) = parser.parse_args()

loader = transitfeed.Loader(
  args[0],
  extra_validation = False,
  load_stop_times = False)
schedule = loader.Load()
date_range = schedule.GetDateRange()

agency_names = []
for a in schedule.GetAgencyList():
  agency_names.append(transitfeed.EncodeUnicode(a.agency_name))
print ",".join(agency_names)
print "Date range: %s to %s" % date_range
