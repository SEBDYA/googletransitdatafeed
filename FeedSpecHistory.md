# NOTE #

The revision history for the General Transit Feed Specification is now hosted in the [Changes section](https://developers.google.com/transit/gtfs/changes) of the official GTFS documentation site.

This existing page is kept for historical purposes

## Introduction ##

This page documents the revisions that the [Google Transit Feed Specification](http://code.google.com/transit/spec/transit_feed_specification.htm) has had over its history.

#### September 26, 2011 ####
  * Added 'feed\_info' proposal to spec: [discussion](https://groups.google.com/group/gtfs-changes/browse_thread/thread/4a1d1ee28f68d86c)
#### September 6, 2011 ####
  * Added 'agency\_fare\_url' proposal to spec: [discussion](https://groups.google.com/group/gtfs-changes/browse_thread/thread/669f6b3c6d3b0a01/a20633df56424c5e)
  * Added 'exact\_times' proposal to spec: [discussion](https://groups.google.com/group/gtfs-changes/browse_thread/thread/9d917d95b43b4d0b/1298765a30b12edf)
#### March 30, 2009 ####
  * See http://groups.google.com/group/gtfs-changes/t/70bd44e2828aa4ac
#### February 26, 2009 ####
  * Removed most of the Google-specific feed submission instructions, since there are many other applications that consume GTFS data at this point.
  * Fixed a broken link in the sidebar to Orange County OCTA's public feed.
#### August 7, 2008 ####
  * Restored the stop\_url field, which was accidentally omitted in the August 6 version
  * Added agency\_phone to sample data
  * Added a mention of the data use agreement when submitting a feed to Google
## August 6, 2008 ##
  * Added transfers.txt file, allowing the feed publishers to provide hints on preferred transfer behavior ([original proposal](http://groups.google.com/group/gtfs-changes/browse_thread/thread/d2090e9e2f37697b))
  * Added location\_type and parent\_station fields to stops.txt, allowing stop points to be grouped into stations ([original proposal](http://groups.google.com/group/gtfs-changes/browse_frm/thread/49c180c99f5aff2c/f46db59beec6bdba))
  * Added agency\_phone field for providing voice telephone number for an agency ([original proposal](http://groups.google.com/group/gtfs-changes/browse_thread/thread/f08b6de7cb9ecaa0))
  * Added "Testing Your Feeds" section mentioning open-source testing tools
  * Added clarifications about CSV format, agency\_timezone, agency\_lang, route\_color, route\_text\_color, arrival\_time, departure\_time, calendar.txt vs. calendar\_dates.txt, fare tables, and frequencies.txt
  * Added link to feed history document, and corrected some public feed links
  * Updated example images to depict the current Google Maps UI
  * Updated/fixed sample data in document
## February 29, 2008 ##
  * Added the stop\_code field in stops.txt to allow for the specification of rider-facing stop codes ([original proposal](http://groups.google.com/group/gtfs-changes/browse_thread/thread/93d03de5f6197b17))
  * Clarified the descriptions of route\_short\_name and route\_long\_name in routes.txt
  * Clarified the descriptions of arrival\_time and departure\_time in stop\_times.txt
  * Fixed typos in the Sample Data section
#### November 20, 2007 ####
  * Clarified block\_id description
  * Changed language to de-emphasize Google Transit (since non-Google applications are using GTFS, and transit routing is now an integrated feature of Google Maps), and to fix assorted typos
  * Updated example screenshots to reflect the presentation of GTFS fields in the current Google Maps UI
  * Updated the Google contact email address for transit data providers
  * Updated formatting
#### October 5, 2007 ####
  * Changed stop\_sequence and shape\_pt\_sequence to allow for any increasing non-negative integers
  * Clarified descriptions and fixed typos
#### May 31, 2007 ####
  * Updated page style, made HTML cleaner and more accessible
  * Added links to public feed examples and other useful sites
  * Removed examples from individual field descriptions
## April 9, 2007 ##
  * Added section on [submitting a feed](http://code.google.com/transit/spec/transit_feed_specification.htm#transitFeedSubmit).
  * Added the [Demo Transit Agency Example](http://code.google.com/transit/spec/transit_feed_specification.htm#transitAgencyExample) feed and live demo.
  * Added note that `calendar.txt` can be omitted if all the service dates are defined in `calendar_dates.txt`.
  * Made the `agency_id` field optional in feeds containing only one agency.  This allows existing feeds without `agency_id` to remain valid.
  * Added fuller specification of `agency_url`, `stop_url`, and `route_url`, and additional example values for those fields.
  * Added `6` (Gondola) and `7` (Funicular) as valid `route_type` values.

#### March 8, 2007 ####
Minor edit to move the `stop_url` field from `stop_times.txt`, where it was incorrectly specified in the Feb. 28 update, to `stops.txt`, where it belongs.

#### March 5, 2007 ####
Minor edit to clarify the description of the `route_long_name` field.

## February 28, 2007 ##
[Headway](http://headwayblog.com/) has a comprehensive writeup of the [February 2007 changes](http://headwayblog.com/2007/03/02/google-feed-spec-update-2007-02/).

## November 29, 2006 ##
  * Added support for trip shape information via `shapes.txt`
  * Clarified the definition of `stop_sequence`
  * Marked `pickup_type` and `drop_off_type` optional

## October 31, 2006 ##
  * Added support for fare information
  * Removed dates from individual file names
  * Changed the `route_type` value definitions
  * Allowed for multiple feed files to be posted at the same time, as long as their service periods didn't overlap
  * Fixed `block_id` in `trips.txt` so that it was correctly marked _Optional_
  * Noted that column headers _must_ be included

#### September 29, 2006 ####
Minor edit to fix a couple errors in the examples.

## September 25, 2006 ##
Initial version.

## Original Files ##
The raw HTML files for each version of the specification are available below for historical reference.


|[March 30, 2009](http://googletransitdatafeed.googlecode.com/svn/wiki/files/FeedSpecHistory/transit_feed_specification-20090330.htm)|
|:-----------------------------------------------------------------------------------------------------------------------------------|
|[February 26, 2009](http://googletransitdatafeed.googlecode.com/svn/wiki/files/FeedSpecHistory/transit_feed_specification-20090226.htm)|
|[August 7, 2008](http://googletransitdatafeed.googlecode.com/svn/wiki/files/FeedSpecHistory/transit_feed_specification-20080807.htm)|
|[February 29, 2008](http://googletransitdatafeed.googlecode.com/svn/wiki/files/FeedSpecHistory/transit_feed_specification-20080229.htm)|
|[November 20, 2007](http://googletransitdatafeed.googlecode.com/svn/wiki/files/FeedSpecHistory/transit_feed_specification-20071120.htm)|
|[October 5, 2007](http://googletransitdatafeed.googlecode.com/svn/wiki/files/FeedSpecHistory/transit_feed_specification-20071005.htm)|
|[May 31, 2007](http://googletransitdatafeed.googlecode.com/svn/wiki/files/FeedSpecHistory/transit_feed_specification-20070531.htm)  |
|[April 9, 2007](http://googletransitdatafeed.googlecode.com/svn/wiki/files/FeedSpecHistory/transit_feed_specification-20070409.htm) |
|[March 8, 2007](http://googletransitdatafeed.googlecode.com/svn/wiki/files/FeedSpecHistory/transit_feed_specification-20070308.htm) |
|[March 5, 2007](http://googletransitdatafeed.googlecode.com/svn/wiki/files/FeedSpecHistory/transit_feed_specification-20070305.htm) |
|[February 28, 2007](http://googletransitdatafeed.googlecode.com/svn/wiki/files/FeedSpecHistory/transit_feed_specification-20070228.htm)|
|[November 29, 2006](http://googletransitdatafeed.googlecode.com/svn/wiki/files/FeedSpecHistory/transit_feed_specification-20061129.htm)|
|[October 31, 2006](http://googletransitdatafeed.googlecode.com/svn/wiki/files/FeedSpecHistory/transit_feed_specification-20061031.htm)|
|[September 29, 2006](http://googletransitdatafeed.googlecode.com/svn/wiki/files/FeedSpecHistory/transit_feed_specification-20060929.htm)|
|[September 25, 2006](http://googletransitdatafeed.googlecode.com/svn/wiki/files/FeedSpecHistory/transit_feed_specification-20060925.htm)|