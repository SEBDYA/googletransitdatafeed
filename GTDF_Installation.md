## Transxchange2GTFS Installation ##
The Transxchange2GTFS converter is released as a zip archive and as a tarball. Zip is probably the first choice on Windows, while Unix, OS/X and GNU Linux systems are likely better served by downloading a tarball. The contents of the zip archive and tarball are identical. Zip and tarball are only two different forms of packaging.

### System requirements ###
Java 1.5 or later is required. Download Java [here](http://java.sun.com/javase/downloads/index.jsp) if this is not the case.

### Installing The Runtime Release ###
The Transxchange2GTFS converter is a batch program that runs from a Command Line Interface (CLI) or a batch script.

#### Checking Java ####
First check if Java 1.5 or later is running on the system. Open a CLI (Command Line Interface) like a Command Prompt ("DOS Box") on Windows, or a terminal session on Unix, and enter
<br />
<pre>java -version</pre>
If this command results in an error message, Java needs to be installed. If the version does not show "1.5" or higher, Java needs to be updated.

#### Download And Unpack ####
Download the runtime release of TransXChange2GTFS, and unpack the release file (zip or tar). In case of Windows, the files of the zip archive can be extracted interactively. The ZIP program is built into Windows starting with Windows XP. On other operating system, tar is the likely choice. The tarball of TransXChange2GTFS unpacks with the following command:
<br />
<pre>tar xvf <filename></pre>
where filename is the filename of the release, e.g.
<br />
<pre>tar xvf TransXChange2GTFS_1.7.5.tar</pre>
for the tarball of version 1.7.5 of the TransXChange2GTFS program.

#### Test the installation ####
In a CLI session, change the directory to the program's directory, e.g.
<br />
<pre>cd TransXChange2GTFS_1.7.5</pre>
Start the program with the following command:
<br />
<pre>java -jar dist/transxchange2GoogleTransit.jar</pre>
The TransXChange2GTFS converter is installed correctly when the following message is displayed:
<br />
<pre>transxchange2GTFS 1.7.5<br>
Please refer to LICENSE file for licensing information<br>
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
<br>
Unknown end tag for </nowiki><br>
<br>
</pre>