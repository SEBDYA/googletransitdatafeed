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

"""Unit tests for the kmlwriter module."""

import os
import StringIO
import tempfile
import unittest
import kmlparser
import kmlwriter
import transitfeed

try:
  import xml.etree.ElementTree as ET  # python 2.5
except ImportError, e:
  import elementtree.ElementTree as ET  # older pythons


def DataPath(path):
  """Return the path to a given file in the test data directory.

  Args:
    path: The path relative to the test data directory.

  Returns:
    The absolute path.
  """
  here = os.path.dirname(__file__)
  return os.path.join(here, 'data', path)


class TestKMLStopsRoundtrip(unittest.TestCase):
  """Checks to see whether all stops are preserved when going to and from KML.
  """

  def setUp(self):
    fd, self.kml_output = tempfile.mkstemp('kml')
    os.close(fd)

  def tearDown(self):
    os.remove(self.kml_output)

  def runTest(self):
    gtfs_input = DataPath('good_feed.zip')
    feed1 = transitfeed.Loader(gtfs_input).Load()
    kmlwriter.KMLWriter().Write(feed1, self.kml_output)
    feed2 = transitfeed.Schedule()
    kmlparser.KmlParser().Parse(self.kml_output, feed2)

    stop_name_mapper = lambda x: x.stop_name

    stops1 = set(map(stop_name_mapper, feed1.GetStopList()))
    stops2 = set(map(stop_name_mapper, feed2.GetStopList()))

    self.assertEqual(stops1, stops2)


class TestGenerateFlattenedTripPattern(unittest.TestCase):
  """Checks KMLWriter._GenerateFlattenedPattern() for various cases."""

  def setUp(self):
    self.feed = transitfeed.Loader(DataPath('flatten_feed.zip')).Load()
    self.kmlwriter = kmlwriter.KMLWriter()

  def _ValidateComponents(self, components):
    """Validates components returned by _GenerateFlattenedPattern().

    This checks that each component is disjoint and that each component
    contains at least two nodes.

    Args:
      components: The result of a call to _GenerateFlattenedPattern.
    """
    stop_to_component_num = {}
    for component_num in range(len(components)):
      for stop in components[component_num]:
        existing_component_num = stop_to_component_num.setdefault(
            stop, component_num)
        self.assertEqual(existing_component_num, component_num)
    for pattern in components:
      stops = set(pattern)
      self.assert_(len(stops) > 1)

  def _GetEdgeSet(self, components):
    """Returns the set of edges in flattened graph.

    The edges are represented by tuples (from_stop_id, to_stop_id). The
    flattened graph is undirected so for every edge (u, v) in the set, (v, u)
    is also in the set.

    Args:
      components: The result of a call to _GenerateFlattenedPattern.

    Returns:
      The set of edges.
    """
    edges = set()
    for pattern in components:
      pattern_ids = [stop.stop_id for stop in pattern]
      edges.update(zip(pattern_ids[:-1], pattern_ids[1:]))
      pattern_ids.reverse()
      edges.update(zip(pattern_ids[:-1], pattern_ids[1:]))
    return edges

  def _MakeUndirected(self, edges):
    """Returns an undirected version of the edges.

    The edges are represented by tuples (u, v). The set is extended so that if
    (u, v) is in the set then so is (v, u).

    Args:
      edges: The set of edges. This is not modified.

    Returns:
      The new undirected set of edges.
    """
    new_edges = set(edges)
    for from_node, to_node in edges:
      new_edges.add((to_node, from_node))
    return new_edges

  def _TestComponents(self, components, expected_num_components,
                      expected_graph):
    """Checks that the flattened graph is the same as the expected graph.

    This calls _ValidateComponents(), checks that the number of components
    is equal to expected_num_components and checks that the flattened graph is
    identical to the expected graph.

    Args:
      components: The result of a call to _GenerateFlattenedPattern.
      expected_num_components: The expected number of graph components.
      expected_graph: The expected set of graph edges.
    """
    self._ValidateComponents(components)
    self.assertEquals(len(components), expected_num_components)
    self.assertEquals(self._GetEdgeSet(components), expected_graph)

  def testSingleTrip(self):
    expected_graph = self._MakeUndirected(
        [('stop1', 'stop2'), ('stop2', 'stop3')])
    route = self.feed.GetRoute('route_1')
    components = self.kmlwriter._GenerateFlattenedPattern(route)
    self._TestComponents(components, 1, expected_graph)

  def testTwoTripsOneComponent(self):
    expected_graph = self._MakeUndirected(
        [('stop1', 'stop2'), ('stop2', 'stop3'),
         ('stop2', 'stop4'), ('stop4', 'stop5')])
    route = self.feed.GetRoute('route_2')
    components = self.kmlwriter._GenerateFlattenedPattern(route)
    self._TestComponents(components, 1, expected_graph)

  def testTwoTripsTwoComponents(self):
    expected_graph = self._MakeUndirected(
        [('stop1', 'stop2'), ('stop2', 'stop3'),
         ('stop4', 'stop5'), ('stop5', 'stop6')])
    route = self.feed.GetRoute('route_3')
    components = self.kmlwriter._GenerateFlattenedPattern(route)
    self._TestComponents(components, 2, expected_graph)

  def testTwoEqualTrips(self):
    expected_graph = self._MakeUndirected(
        [('stop1', 'stop2'), ('stop2', 'stop3')])
    route = self.feed.GetRoute('route_4')
    components = self.kmlwriter._GenerateFlattenedPattern(route)
    self._TestComponents(components, 1, expected_graph)

  def testOneStop(self):
    expected_graph = set()
    route = self.feed.GetRoute('route_5')
    components = self.kmlwriter._GenerateFlattenedPattern(route)
    self._TestComponents(components, 0, expected_graph)

  def testNoStops(self):
    expected_graph = set()
    route = self.feed.GetRoute('route_6')
    components = self.kmlwriter._GenerateFlattenedPattern(route)
    self._TestComponents(components, 0, expected_graph)


class TestKMLGeneratorMethods(unittest.TestCase):
  """Tests the various KML element creation methods of KMLWriter."""

  def setUp(self):
    self.kmlwriter = kmlwriter.KMLWriter()
    self.parent = ET.Element('parent')

  def _ElementToString(self, root):
    """Returns the node as an XML string.

    Args:
      root: The ElementTree.Element instance.

    Returns:
      The XML string.
    """
    output = StringIO.StringIO()
    ET.ElementTree(root).write(output, 'utf-8')
    return output.getvalue()

  def testCreateFolderVisible(self):
    element = self.kmlwriter._CreateFolder(self.parent, 'folder_name')
    self.assertEqual(self._ElementToString(element),
                     '<Folder><name>folder_name</name></Folder>')

  def testCreateFolderNotVisible(self):
    element = self.kmlwriter._CreateFolder(self.parent, 'folder_name',
                                           visible=False)
    self.assertEqual(self._ElementToString(element),
                     '<Folder><name>folder_name</name>'
                     '<visibility>0</visibility></Folder>')

  def testCreateFolderWithDescription(self):
    element = self.kmlwriter._CreateFolder(self.parent, 'folder_name',
                                           description='folder_desc')
    self.assertEqual(self._ElementToString(element),
                     '<Folder><name>folder_name</name>'
                     '<description>folder_desc</description></Folder>')

  def testCreatePlacemark(self):
    element = self.kmlwriter._CreatePlacemark(self.parent, 'abcdef')
    self.assertEqual(self._ElementToString(element),
                     '<Placemark><name>abcdef</name></Placemark>')

  def testCreatePlacemarkWithStyle(self):
    element = self.kmlwriter._CreatePlacemark(self.parent, 'abcdef',
                                              style_id='ghijkl')
    self.assertEqual(self._ElementToString(element),
                     '<Placemark><name>abcdef</name>'
                     '<styleUrl>#ghijkl</styleUrl></Placemark>')

  def testCreatePlacemarkNotVisible(self):
    element = self.kmlwriter._CreatePlacemark(self.parent, 'abcdef',
                                              visible=False)
    self.assertEqual(self._ElementToString(element),
                     '<Placemark><name>abcdef</name>'
                     '<visibility>0</visibility></Placemark>')

  def testCreatePlacemarkWithDescription(self):
    element = self.kmlwriter._CreatePlacemark(self.parent, 'abcdef',
                                              description='ghijkl')
    self.assertEqual(self._ElementToString(element),
                     '<Placemark><name>abcdef</name>'
                     '<description>ghijkl</description></Placemark>')

  def testCreateLineString(self):
    coord_list = [(1.0, 2.0), (3.0, 4.0), (5.0, 6.0)]
    element = self.kmlwriter._CreateLineString(self.parent, coord_list)
    self.assertEqual(self._ElementToString(element),
                     '<LineString><tessellate>1</tessellate>'
                     '<coordinates>%f,%f %f,%f %f,%f</coordinates>'
                     '</LineString>' % (2.0, 1.0, 4.0, 3.0, 6.0, 5.0))

  def testCreateLineStringForShape(self):
    shape = transitfeed.Shape('shape')
    shape.AddPoint(1.0, 1.0)
    shape.AddPoint(2.0, 4.0)
    shape.AddPoint(3.0, 9.0)
    element = self.kmlwriter._CreateLineStringForShape(self.parent, shape)
    self.assertEqual(self._ElementToString(element),
                     '<LineString><tessellate>1</tessellate>'
                     '<coordinates>%f,%f %f,%f %f,%f</coordinates>'
                     '</LineString>' % (1.0, 1.0, 4.0, 2.0, 9.0, 3.0))


class TestRouteKML(unittest.TestCase):
  """Tests the routes folder KML generation methods of KMLWriter."""

  def setUp(self):
    self.feed = transitfeed.Loader(DataPath('flatten_feed.zip')).Load()
    self.kmlwriter = kmlwriter.KMLWriter()
    self.parent = ET.Element('parent')

  def _CheckMultiGeometry(self, placemark, num_children):
    """Checks a Placemark with geometry from multiple LineStrings.

    This checks that the placemark has a MultiGeometry child and that
    this contains num_children LineStrings as its children.

    Args:
      placemark: The placemark ElementTree.Element instance.
      num_children: The expected number of LineStrings.
    """
    multi_geometry = placemark.find('MultiGeometry')
    self.assert_(multi_geometry is not None)
    self.assertEquals(len(multi_geometry), num_children)
    for element in multi_geometry:
      self.assertEquals(element.tag, 'LineString')

  def testCreateRouteFlattenedPlacemark(self):
    placemark = self.kmlwriter._CreateRouteFlattenedPlacemark(
        self.parent, self.feed.GetRoute('route_3'))
    self._CheckMultiGeometry(placemark, 2)

  def testCreateRouteShapePlacemarkOneTripOneShape(self):
    placemark = self.kmlwriter._CreateRouteShapePlacemark(
        self.feed, self.parent, self.feed.GetRoute('route_1'))
    self._CheckMultiGeometry(placemark, 1)

  def testCreateRouteShapePlacemarkTwoTripsTwoShapes(self):
    placemark = self.kmlwriter._CreateRouteShapePlacemark(
        self.feed, self.parent, self.feed.GetRoute('route_2'))
    self._CheckMultiGeometry(placemark, 2)

  def testCreateRouteShapePlacemarkTwoTripsOneShape(self):
    placemark = self.kmlwriter._CreateRouteShapePlacemark(
        self.feed, self.parent, self.feed.GetRoute('route_3'))
    self._CheckMultiGeometry(placemark, 1)

  def testCreateRouteShapePlacemarkTwoTripsNoShape(self):
    placemark = self.kmlwriter._CreateRouteShapePlacemark(
        self.feed, self.parent, self.feed.GetRoute('route_4'))
    self.assertEquals(placemark, None)

  def testCreateRoutesFolderNoRoutes(self):
    schedule = transitfeed.Schedule()
    folder = self.kmlwriter._CreateRoutesFolder(schedule, self.parent)
    self.assert_(folder is None)

  def testCreateRoutesFolderNoRoutesWithRouteType(self):
    folder = self.kmlwriter._CreateRoutesFolder(self.feed, self.parent, 999)
    self.assert_(folder is None)

  def _TestCreateRoutesFolder(self, show_trips):
    self.kmlwriter.show_trips = show_trips
    folder = self.kmlwriter._CreateRoutesFolder(self.feed, self.parent)
    self.assertEquals(folder.tag, 'Folder')
    styles = self.parent.findall('Style')
    self.assertEquals(len(styles), len(self.feed.GetRouteList()))
    route_folders = folder.findall('Folder')
    self.assertEquals(len(route_folders), len(self.feed.GetRouteList()))
    if not show_trips:
      for route_folder in route_folders:
        self.assert_(route_folder.find('Folder') is None)

  def testCreateRoutesFolder(self):
    self._TestCreateRoutesFolder(False)

  def testCreateRoutesFolderShowTrips(self):
    self._TestCreateRoutesFolder(True)

  def testCreateRoutesFolderWithRouteType(self):
    folder = self.kmlwriter._CreateRoutesFolder(self.feed, self.parent, 1)
    route_folders = folder.findall('Folder')
    self.assertEquals(len(route_folders), 1)


class TestShapesKML(unittest.TestCase):
  """Tests the shapes folder KML generation methods of KMLWriter."""

  def setUp(self):
    self.flatten_feed = transitfeed.Loader(DataPath('flatten_feed.zip')).Load()
    self.good_feed = transitfeed.Loader(DataPath('good_feed.zip')).Load()
    self.kmlwriter = kmlwriter.KMLWriter()
    self.parent = ET.Element('parent')

  def testCreateShapesFolderNoShapes(self):
    folder = self.kmlwriter._CreateShapesFolder(self.good_feed, self.parent)
    self.assertEquals(folder, None)

  def testCreateShapesFolder(self):
    folder = self.kmlwriter._CreateShapesFolder(self.flatten_feed, self.parent)
    placemarks = folder.findall('Placemark')
    self.assertEquals(len(placemarks), 3)
    for placemark in placemarks:
      self.assert_(placemark.find('LineString') is not None)


class TestStopsKML(unittest.TestCase):
  """Tests the stops folder KML generation methods of KMLWriter."""

  def setUp(self):
    self.feed = transitfeed.Loader(DataPath('flatten_feed.zip')).Load()
    self.kmlwriter = kmlwriter.KMLWriter()
    self.parent = ET.Element('parent')

  def testCreateStopsFolderNoStops(self):
    schedule = transitfeed.Schedule()
    folder = self.kmlwriter._CreateStopsFolder(schedule, self.parent)
    self.assert_(folder is None)

  def testCreateStopsFolder(self):
    folder = self.kmlwriter._CreateStopsFolder(self.feed, self.parent)
    placemarks = folder.findall('Placemark')
    self.assertEquals(len(placemarks), len(self.feed.GetStopList()))


class TestTripsKML(unittest.TestCase):
  """Tests the trips folder KML generation methods of KMLWriter."""

  def setUp(self):
    self.feed = transitfeed.Loader(DataPath('flatten_feed.zip')).Load()
    self.kmlwriter = kmlwriter.KMLWriter()
    self.parent = ET.Element('parent')

  def testCreateTripsFolderForRouteNoTrips(self):
    route = self.feed.GetRoute('route_7')
    folder = self.kmlwriter._CreateTripsFolderForRoute(self.parent, route)
    self.assert_(folder is None)

  def testCreateTripsFolderForRoute(self):
    route = self.feed.GetRoute('route_2')
    folder = self.kmlwriter._CreateTripsFolderForRoute(self.parent, route)
    placemarks = folder.findall('Placemark')
    trip_placemarks = set()
    for placemark in placemarks:
      trip_placemarks.add(placemark.find('name').text)
    self.assertEquals(trip_placemarks, set(['route_2_1', 'route_2_2']))


if __name__ == '__main__':
  unittest.main()
