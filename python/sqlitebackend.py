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

from pysqlite2 import dbapi2 as sqlite
import transitfeed

class SQLiteBackend(object):
  _TABLES = ['db_metadata', 'agency', 'stops', 'routes', 'stop_times', 'trips']
  _EMPTY_AGENCY_ID = 'empty-agency-id'
  
  def __init__(self, filename):
    self.filename = filename
    self.db = sqlite.connect(filename)
    self._SetupTables()
    
  def Clear(self):
    cur = self.db.cursor()
    for table in self._TABLES:
      cur.execute('DROP TABLE %s' % table)
    self.db.commit()
    self._SetupTables()
    
  def _AddObject(self, table_name, field_list, new_object):
    cur = self.db.cursor()
    field_names = ', '.join(field_list)
    blanks = ', '.join(['?'] * len(field_list))
    cur.execute('INSERT INTO %s (%s) values (%s)' %
                (table_name, field_names, blanks),
                new_object.GetFieldValuesTuple())
    self.db.commit()
    
  def _GetObjectById(self, table_name, field_names, id_field, id):  
    cur = self.db.cursor()
    field_list = ', '.join(field_names)
    cur.execute('SELECT %s FROM %s WHERE %s=?' %
                (field_list, table_name, id_field), (str(id), ))
    return cur.fetchone()

  def _GetObjectsById(self, table_name, field_names, id_field, id):  
    cur = self.db.cursor()
    field_list = ', '.join(field_names)
    cur.execute('SELECT %s FROM %s WHERE %s=?' %
                (field_list, table_name, id_field), (str(id), ))
    return cur.fetchall()

  def _RemoveObjectById(self, table_name, id_field, id):  
    cur = self.db.cursor()
    cur.execute('DELETE FROM %s WHERE %s=?' %
                (table_name, id_field), (str(id), ))
    self.db.commit()

  def AddAgency(self, agency):
    real_id = agency.agency_id
    if not real_id:
      agency.agency_id = self._EMPTY_AGENCY_ID
    self._AddObject('agency', transitfeed.Agency._FIELD_NAMES, agency)
    agency.agency_id = real_id
    
  def GetAgency(self, agency_id):
    if not agency_id:
      agency_id = self._EMPTY_AGENCY_ID
    results = self._GetObjectById('agency', transitfeed.Agency._FIELD_NAMES,
                                  'agency_id', agency_id)
    if not results:
      return None
      
    return transitfeed.Agency(field_list=results)
  
  def _MakeAgencyEmpty(self, x):
    if x == self._EMPTY_AGENCY_ID:
      return None
    else:
      return x
  
  def GetAgencyIDs(self):
    cur = self.db.cursor()
    cur.execute('SELECT agency_id FROM agency')
    ids = map(lambda x: x[0], cur.fetchall())
    return map(self._MakeAgencyEmpty, ids)

  def AddStop(self, stop):
    self._AddObject('stops', transitfeed.Stop._FIELD_NAMES, stop)
    
  def GetStop(self, stop_id):
    results = self._GetObjectById('stops', transitfeed.Stop._FIELD_NAMES,
                                  'stop_id', stop_id)
    if not results:
      return None
      
    return transitfeed.Stop(field_list=results)
    
  def GetStopIDs(self):
    cur = self.db.cursor()
    cur.execute('SELECT stop_id FROM stops')
    return map(lambda x: x[0], cur.fetchall())
    
  def AddStopTime(self, stop_time):
    self._AddObject('stop_times', transitfeed.StopTime._FIELD_NAMES, stop_time)
    
  def GetStopTimesForStop(self, stop_id):
    results = self._GetObjectsById('stop_times',
                                   transitfeed.StopTime._FIELD_NAMES,
                                   'stop_id', stop_id)
    return map(lambda x: transitfeed.StopTime(field_list=x), results)
  
  def GetStopTimesForTrip(self, trip_id):
    results = self._GetObjectsById('stop_times',
                                   transitfeed.StopTime._FIELD_NAMES,
                                   'trip_id', trip_id)
    return map(lambda x: transitfeed.StopTime(field_list=x), results)

  def AddRoute(self, route):
    self._AddObject('routes', transitfeed.Route._FIELD_NAMES, route)

  def GetRoute(self, route_id):
    results = self._GetObjectById('routes', transitfeed.Route._FIELD_NAMES,
                                  'route_id', route_id)
    if not results:
      return None

    return transitfeed.Route(field_list=results)

  def GetRouteIDs(self):
    cur = self.db.cursor()
    cur.execute('SELECT route_id FROM routes')
    return map(lambda x: x[0], cur.fetchall())

  def _CreateTable(self, table_name, field_names):
    cur = self.db.cursor()
    column_names = ', '.join(map(lambda x: '%s TEXT' % x, field_names))
    cur.execute('CREATE TABLE %s (%s)' % (table_name, column_names))
    self.db.commit()
  
  def _SetupTables(self):
    exists = self.db.execute('SELECT COUNT(*) from sqlite_master where name=?',
                             ('db_metadata',)).fetchone()[0]
    if exists:
      return
    
    cur = self.db.cursor()
    cur.execute('CREATE TABLE db_metadata ('
                'format_version INTEGER, '
                'source_file_name TEXT)')
    self.db.commit()
    
    self._CreateTable('agency', transitfeed.Agency._FIELD_NAMES)
    self._CreateTable('stops', transitfeed.Stop._FIELD_NAMES)
    self._CreateTable('routes', transitfeed.Route._FIELD_NAMES)
    self._CreateTable('trips', transitfeed.Trip._FIELD_NAMES)
    self._CreateTable('stop_times', transitfeed.StopTime._FIELD_NAMES)
