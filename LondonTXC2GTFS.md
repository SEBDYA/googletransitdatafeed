## Introduction ##
This page describes how to create GTFS file sets from the Transport for London TransXChange export stream, assuming the use of the TransXChange2GTFS converter. There is a series of dependencies that need to be satisfied, which are described below. A sample Converter Script and a series of sample configuration files should help jump start the setup of a conversion environment. Starting from scratch, please expect to spend a few hours setting up the TransXChange Converter and modifying the sample Converter Script to your needs. Converting the London export stream to GTFS is not trivial, and at this point, somewhat incomplete. The resulting GTFS files however pass GTFS validation, but unfortunately cannot be used without consideration for a few caveats, which are explained below. As of March 2011, the problems surrounding the TransXChange export stream have been reported to Transport for London, and we can be hopeful that these will be resolved in the future.

## The TransXChange2GTFS Converter ##
The TransXChange2GTFS converter v1.7.0 or later is required. It is available for download [here](http://code.google.com/p/googletransitdatafeed).

## Transport for London TransXChange export stream and NaPTAN Download ##
Transport for London (TfL) makes the schedule and network data for the following public transport services available to the public:
  * London Underground
  * Docklands Light Rail (DLR)
  * River Service
  * Tramlink
  * London Buses
Download the TfL export stream [here](http://www.tfl.gov.uk/businessandpartners/syndication/). Click on "Get data feeds" and select "Journey Planner Timetables". The TfL export stream does not contain stop coordinates, which are required to generate valid GTFS file sets. In the UK, stop coordinates are managed in a national database. NaPTAN downloads are available from the [Department for Transport website](http://www.dft.gov.uk/public-transportdatamanagement/DataUser_Login.aspx). The TransXChange Converter accepts exports of this database in the NaPTAN version 1 format. It is recommended to use a full, i.e. nation wide, export of stops.

| **Caveat**: The referential integrity of stops between the TfL export stream and the national database is not guaranteed. This means that stops of the TfL export stream are not necessarily included in the NaPTAN download. The TransXChange2GTFS converter offers a feature that allows the geo-coding of stop coordinates by stop name. It is used by the sample Converter Script and associated sample configuration files to augment missing stop coordinates. Note that geo-coded stop coordinates drive "too fast travel" warnings when the resulting GTFS file sets are validated. It is expected that geo-coded stop coordinates are not accurate enough for many applications. |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Caveat**: As of March 2011, the TfL export stream does not allow to correlate VehicleJourneys (trips) that start after midnight to the correct calendar day. Example of this problem: Line: Hammersmith. Corresponding TransXChange file: `output_txc_01HAM_.xml` VehicleJourney: 01HAM0R457 DepartureTime: 00:15:30 ServiceRef: SId\_01HAM0 / DaysOfWeek: MondayToFriday This VehicleJourney technically falls on a Monday calendar day at 00:15:30. This is a problem - the last VehicleJourney on a Sunday night ends before this time and there are no more trains in service at that time. When converted to GTFS, this problem propagates to the stop times in stop\_times.txt. The stop times are rolled out accordingly. **Warning**: The stop times in such cases are not necessarily correct. |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Note**: As of March 2011, individual lines are represented by multiple line IDs. This is common throughout the entire TransXChange export files. |
|:---------------------------------------------------------------------------------------------------------------------------------------------------|

| **Caveat**: As of March 2011, the TransXChange exports include only a single Destination for a direction on a London Underground line. This seems incorrect. More detailed destinations can be looked up on the journeyplanner web site. Although this passes GTFS validation, it introduces misleading trip Destinations. As an example, LId\_01DIS0 and the associated services only include the Destination "Upminster" although the Destinations vary by individual trip. |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Note**: As of March 2011, a common imperfection are overlapping DaysOfNonOperation in VehicleJourney definitions. Example: File output\_txc\_24165g.xml, VehicleJourney 24165gg2R1650176, ServiceRef SId\_24165g2 defines NonOperatingDays as follows: ` <DaysOfNonOperation><DateRange><StartDate>2010-11-06</StartDate><EndDate>2010-11-06</EndDate></DateRange><DateRange><StartDate>2010-11-06</StartDate><EndDate>2011-12-03</EndDate></DateRange></DaysOfNonOperation>` Day 2010-11-06 hits calendar\_dates.txt twice, causing a warning when validated with the GTFS feedvalidator. |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|




## The Sample Converter Script ##
The sample Converter Script is posted [here](LondonConvertScript.md). Beyond the executable script code, this file includes sample configuration files for the conversion of the various TfL services, and a small set of stations and piers to manually augment the NaPTAN exported stops file.

Please update the script variable TXC2GTFS to point to the location of the TransXChange converter JAR file. The automatic download of the export stream is commented out. Automatic download from the TfL web site is not available to the public at this time. Instead, download the TfL export stream as described above.

The sample Converter Script generates separate GTFS file sets for the following services:
  * London Underground
  * DLR
  * River Service
  * Tramlink
  * London Buses (Operators with digit OIds)
  * Individual GTFS file sets for each cross-boundary service permit (Operators with letter OIds)
This split into the distinct rail, ferry and bus services is somewhat arbitrary. The sample Converter Script could be modified to convert the entire TfL export stream into a single GTFS file set. Considering the modal split between ferry, rail and bus, it would however be expected that the TfL export stream would at least be separated into London Underground (Subway), DLR (Light rail), River Service (ferry service), Tramlink (Light rail) and London Buses (Buses), encompassing all bus operators with digit and letter OId codes.

### Sample Configuration Files ###
The Converter Script includes the content of a series of reference files. There are five converter configuration files. They steer the conversion of the five modes operated under the TfL brands.

### Manual augmentation of Stops.csv ###
The Convert Script includes a few rows to manually augment the Stops.csv provided through the national database export. These are stations and piers missing from the national database, but referenced from the TfL export stream. This manual augmentation eliminates the need for the geocoding of stop coordinates of the affected stops.

### Operator Churn ###
From time to time, TfL removes or introduces operators in the TfL export stream. The sample Converter Script discovers missing or new operators and prompts if operators are missing before the conversion begins. Please update the sample Converter Script following the removal or introduction of operators.

### Platform Discussion ###
The TransXChange Converter and the Converter Script have been tested on OS X (10.6.6), Linux (Debian Etch) and MS Windows (XP). This section describes platform specific requirements to run the converter script.

#### Linux ####
The installation of a Jave Runtime Environment (JRE) and ZIP may be required.

#### OS X ####
The converter and script should run without the need for the installation of additional software.

#### MS Windows ####
The installation of a an Unix-line environment is required for the Converter Script. The Converter Script has been tested with [Cygwin](http://www.cygwin.com).