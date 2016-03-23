## Introduction to TransXChange2GTFS ##
This page describes the use of the TransXChange2GTFS converter. The purpose of the converter is to generate [GTFS](http://code.google.com/transit/spec/transit_feed_specification.htm) files from [TransXChange](http://www.transxchange.org.uk) standard data (Version 2.2 and later). Download the converter [here](http://code.google.com/p/googletransitdatafeed).

## Manual ##
Transxchange2GTFS has been tested to run on [Windows XP](http://www.microsoft.com/windowsxp/default.mspx), Max OS/X 10.6.6 and [GNU Linux](http://en.wikipedia.org/wiki/Linux) (Distribution: [Debian](http://www.debian.org)). The converter requires Java SE 1.5 or later.

Follow these steps:
  * Download the current release of TransXChange2GTFS from the GoogleTransitDataFeed [Google Code](http://code.google.com/p/googletransitdatafeed) web site, and install it on your computer
  * Copy your transit data to your computer, or make it visible through your computer network
  * Run the TransXChange2GTFS converter to generate a GTFS feed from the orginating TransXChange data
  * Post the zipped file set for upload to [Google Transit](http://www.google.com/transit)

Below an example to illustrate the use of the converter. Next, we will look at the converter's command line arguments to complement your transit data.

### Running An Example ###
Transit data following [GTFS](http://code.google.com/transit/spec/transit_feed_specification.htm) consists of a set of files that is wrapped into an archive (zip file). Let's turn to one of the six examples included in the download of TransXChange2GTFS, the Express route example. The corresponding GTFS feed file set is generated as follows:
  * Start a CLI (Command Line Interface) session. In Windows, open a Command Prompt (DOS Box). With Linux or OS/X, open a terminal (command shell).
  * Change the directory to the location of the TransXChange2GTFS converter.
  * Run the converter for the Express route example.

In Windows:

`tXCh2GT examplesInput/express.xml http://www.aagency.org Europe/London 3 examplesOutput`

Linux and OS/X work similar:

`./tXCh2GT.sh examplesInput/express.xml http://www.aagency.org Europe/London 3 examplesOutput`

The converter starts with the following prompt:
`transxchange2GTFS 1.7.5`
It should not display any error messages. If this is not the case, verify that the installation has been completed and that you are executing the commands in the correct directory. After the converter completed successfully, the resulting file set can be shown with the following Windows (DOS) command:

`dir examplesOutput`

On Linux and OS/X:

`ls -l examplesOutput`

You should find the following list of files (Windows):

<pre> Directory of C:\mytransformations\examplesOutput<br>
06/20/2007  10:00 PM    <DIR>         .<br>
06/20/2007  10:00 PM    <DIR>          ..<br>
06/20/2007  10:00 PM               121 agency.txt<br>
06/20/2007  10:00 PM               125 calendar.txt<br>
06/20/2007  10:00 PM               422 calendar_dates.txt<br>
06/20/2007  10:00 PM             1,951 google_transit.zip<br>
06/20/2007  10:00 PM               308 routes.txt<br>
06/20/2007  10:00 PM               558 stops.txt<br>
06/20/2007  10:00 PM             1,041 stop_times.txt<br>
06/20/2007  10:00 PM               194 trips.txt<br>
8 File(s)          4,720 bytes<br>
</pre>
### Converting TransXChange Data ###
Let's assume the TransXChange input has the filename myData.xml, and it is stored in the directory C:\SD\myTransitData (Windows).

Next, find answers to the following questions:
  * What is your organization's web site url?
(Example: http://www.myagency.org)
  * What is your organization's time zone? Find your time zone [here](http://en.wikipedia.org/wiki/List_of_tz_zones)
(Example: Europe/London)
  * What is your transportation mode?
0 - Tram, 1 - Subway, 2 - Rail, 3 - Bus, 4 - Ferry, 5 - Cable car, 6 - Gondola, 7 - Funicular

(Example: 3)
  * What is the output directoy?
(Example: C:\SD\myGoogleFiles)

Using the exemplary answers above, the CLI commands for the converter are as follows. Windows:

`tXCh2GT C:\mytransformations\myData.xml http://www.myagency.org Europe/London 3 C:\mytransformations\myGoogleFiles`

On Linux and OS/X, we assume the transit data is located in the user's home directory:

`./tXCh2GT.sh ~/mytransformations/myTransitData\myData.xml http://www.myagency.org Europe/London 3 ~/mytransformations/myGoogleFiles`

In addition to individual TransXChange input files, the converter is also able to process a set of TransXChange files from a zip archive. Use the zip filename as input filename, and a single set of GTFS files is generated containing the converted superset of the inputfiles of the zip file.

#### Including a NaPTAN format stop file ####
The Transxchange2GTFS converter accepts a Version 1 CSV [NaPTAN ](http://www.naptan.org.uk/) formatted stop file. Mainly, this is used for stop coordinate look-ups in the "Lon" and "Lat" columns of the stop file. The stop file is passed as an optional command line argument, e.g.:

`./tXCh2GT.sh ~/mytransformations/myTransitData\myData.xml http://www.myagency.org Europe/London 3 ~/mytransformations/myGoogleFiles Stops.csv`

#### Using a Configuration File ####
In place of command line options such as agency URL or timezone, the converter offers the use of a configuration file. Advanced controls such as the handling of orphan stops or empty services can be used through a configuration file only. The [TransXChange2GTFS converter configuration file](GTDF_ConfigurationFile.md) is described on a separate wiki page.

## Bugs And Issues ##
Does the convert crash or generate inaccurate results? Possibly. Bugs are a reality, and the converter might not be fitted to all specific in-and-outs of your specific transit data. With future development of the converter, reported bugs will be worked out, and the "footprint" of the converter will expand as it is being "rubbed" against transit data of different transit operators. Bring on the challenges.

Bugs and issues are tracked on the Google Code page. Navigate to the [Issues](http://code.google.com/p/googletransitdatafeed/issues/list) tab for a list and status of known bugs and issues