#!/usr/bin/python2.4
#
# Copyright 2007 Google Inc. All Rights Reserved.

"""One-line documentation for dump module.

A detailed description of dump.
"""

from transitfeed import *

s = Schedule()
s.Load('sample-feed.zip')

for r in s.GetRouteList():
  print r.route_long_name
  for pattern_id, trips in r.GetPatternIdTripDict().items():
    times = []  # list of lists. times[stop_count][time]
    for time_stops in zip(t.GetTimeStops() for t in trips):
      times.append(tuple(time_stop[0] for time_stop in time_stops))

    for i,time_stop in enumerate(trips[0].GetTimeStops()):
      stop_times = tuple(time_stop[2].stop_name) + times[i]
      print stop_times
      print '\t'.join(stop_times)
