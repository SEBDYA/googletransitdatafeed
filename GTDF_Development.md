# Introduction #
This page contains instructions how to create a development environment to maintain the transxchange2GTFS converter, using Eclipse.

# Details #
The following instructions assume the use of a command shell, terminal or equivalent.

## Download and Install Eclipse ##
Eclipse is available for download at http://www.eclipse.org. The Standard edition of Eclipse is recommended.

## Download and Install Java ##
Many computers are delivered with Java installed. This can be verified in a command shell (or equivalent) by calling Java directly:
<pre>java -version</pre>
If Java is installed, the resulting output should display the Java version, such as:
<pre>java version "1.5.0_14"<br>
Java(TM) 2 Runtime Environment, Standard Edition (build 1.5.0_14-b03)<br>
Java HotSpot(TM) Client VM (build 1.5.0_14-b03, mixed mode, sharing)</pre>
The code works with Java 1.5, or later. Java is available for download at http://java.sun.com

## Checkout the transxchange2GTFS Source Code ##
As project member, the source code can be checked out with commit privilege, as described in the [Source tab](http://code.google.com/p/googletransitdatafeed/source/checkout). Non-members are limited to check out the source code on a read-only basis only. Use the following syntax to check out the code into the current directory:
<pre>svn checkout http://googletransitdatafeed.googlecode.com/svn/trunk/java/Transxchange2GoogleTransit googletransitdatafeed-read-only</pre>
The directory name will drive the Eclipse project name. Rename it, as appropriate.

## Create New Eclipse Project from the Checked-out Source Code ##
Open Eclipse and select "New" -> "Java Project" from the "File" menu.
Select "Create project from existing source", and navigate to the root directory of the checked-out source code.
Click "Finish".
Verify the project by manually rebuilding the project. Select "Project" -> "Clean", select the project, and hit "OK".

## Running transxchange2GTFS is Eclipse ##
In Eclipse, select "Run as" -> "Java Application" from the "Run" menu. The Eclipse console  should display the output of transxchange2GoogleTransit, similar to:
<pre>transxchange2GTFS 1.7.5 Please refer to LICENSE file for licensing information<br>
<br>
Usage: $ transxchange2GoogleTransit <transxchange input filename> -c <configuration file name><br>
Usage: $ transxchange2GoogleTransit <transxchange input filename> <output-directory> -c <configuration file name><br>
Usage: $ transxchange2GoogleTransit <transxchange input filename> <output-directory> <agency name> -c <configuration file name><br>
Usage: $ transxchange2GoogleTransit <transxchange input filename> -<br>
<url> <timezone> <default route type> <output-directory> [<stopfile>]<br>
<br>
<timezone>: Please refer to<br>
http://code.google.com/transit/spec/transit_feed_specification.html<br>
<br>
for instructions about the values of the arguments <url>, <timezone> and <default route type>.<br>
</pre>
This output lists the command line parameters required to run the transxchange2GTFS converter. These are set in an Eclipse "Run Configuration". Please refer to the Eclipse documentation for details. A description of the transxchange2GTFS converter command line arguments is available on the [GTDF\_Manual](http://code.google.com/p/googletransitdatafeed/wiki/GTDF_Manual) wiki page