## Introduction ##
This page describes the structure and controls of the TransXChange2GTFS converter configuration file. The individual controls are described in the sections below.

## Output Directory ##
Directory path to save the resulting google\_transit.zip file.

`output-directory=<output path>`

## Agency URL ##
The agency URL control is used to fill the agency\_url field in the GTFS agency.txt file with a value.

`url=<Agency URL>`

## Agency Timezone ##
The agency timzone control is used to fill the agency\_timezone field in the GTFS agency.txt file with a value.

`timezone=<value>`

Please refer to the [GTFS specification](http://code.google.com/transit/spec/transit_feed_specification.html#agency_txt___Field_Definitions) for a reference of the values used.

## Agency Language ##
The agency language control is used to fill the agency\_lang field in the GTFS agency.txt file with a value.

`lang=<language>`

## Agency Phone ##
The agency phone control is used to fill the agency\_phone field in the GTFS agency.txt file with a value.

`phone=<phone>`

## Agency shortname flag ##
Flag to determine whether OperatorShortName should be used to fill the agency\_name field in the GTFS agency.txt file. Default: false, which directing the converter to use the value of the OperatorNameOnLicence tag.

`useagencyshortname=<true|false>`

## Agency mapping ##
This control maps the agency\_id as captured from the operator registration into an agency\_name of the GTFS agency.txt file.
Use '=' to separate key ("agency"), agency\_id and the mapped agency name. Multiple agency mappings can be defined, using separate rows.
Example:
<pre>
agency:OId_LU=London Buses, operated by London United<br>
agency:OId_48=London Buses, operated by London General</pre>
The resulting output in agency.txt uses OId\_LU as agency\_id, and "London Buses, operated by London United" as agency\_name, and so forth.
Without this setting, agency\_names are populated with the values of the OperatorNameOnLicence or OperatorShortName tag, as directed by the agencyshortname control.

## Skip Empty Services ##
Services sometimes do not combine to a valid day pattern, and lead to the following types of records in a GTFS calendar.txt file:
<pre>
<service_id>,0,0,0,0,0,0,0,<start_date>,<end_date> </pre>
Services which do not contain a valid day pattern can be skipped by specifying:

`skipemptyservice=true`

As a side effect, specific non-service days (DaysOfNonOperation) are also skipped in the GTFS calendar\_dates.txt file, while records for specific active DaysOfOperation continue to be included in the GTFS calendar\_dates.txt file. Default value=false

## Default Route Type ##
The default route type control is used to fill the route\_type field in the GTFS routes.txt file. Refer to the [GTFS specification](http://code.google.com/transit/spec/transit_feed_specification.html#routes_txt___Field_Definitions) for a list of valid route types.

`default-route-type=[0|1|2|3|4|5|6|7]`

## Mode Override of Default Route Type ##
Services of a TransXChange feed that include Mode tags are mapped to a mode as defined in the configuration file.

`mode:<<Mode> tag value>=<GTFS mode value>`

Example:
<pre>
mode:rail=2<br>
mode:bus=3<br>
mode:ferry=4</pre>
With this mapping, occurrences of a Service Mode "bus" in the TransXChange feed will be set to value "3" in the route\_type field of the GTFS routes.txt file.

## Skip Orphaned Stops ##
TransXChange feeds sometimes contain stops that are not referenced in any of the services. Setting this control to true skips the stops not referenced by a service ("orphan stops"). Default value=false

`skiporhpanstops=<true|false>`

## Geocode Stop Coordinates Where Missing ##
The GTFS specification requires WGS-84 coordinates for each stop in the GTFS stops.txt file. Some coordinates for stops of a TransXChange input, possibly in concert with a NapTAN stop file, may not be available. With this option active, the converter makes an attempt to geocode the stop's coordinates, using Google's Maps API. (http://code.google.com/apis/maps/documentation/geocoding/)
The converter logs geocoding attempts in the console.
Note: Geocoded coordinates are expected to have insufficient accuracy for most uses. This feature allows to reach formal compliance to validate against the GTFS specification. Default value=false

`geocodemissingstops=<true|false>`

## NaPTAN Stop File ##
Path and filename of a NaPTAN version 1 CSV stop file.

`stopfile=<file name of optional stopfile name in NaPTAN CSV format>`

## NaPTAN Stop Name Helper Flag ##
Without the NaPTAN stop name helper activated, the converter combines the values of CommonName and LocalityName to stop\_name values. The NapTAN stop name helper implements the "usable stop name rules v4 for NaPTAN and NPTG databases". It unrolls the following stop\_name format from a NaPTAN version 1 CSV stop file, as follows:
<pre>
<LocalityName>,<Indicator><CommonName>(on <street>)[SMS: <NaptanCode>]</pre>
Default value=false

## NaPTAN Stop Column Pick ##
When a NaPTAN stop column pick is defined, the converter picks the value of the respective column (attribute) from a NaPTAN version 1 CSV stop file. A NaPTAN stop column pick definition in a configuration file overrides the NaPTAN stop name helper if activated. The columns are picked in the sequence they occur in the configuration file.
Example:
<pre>
naptanstopcolumn="CommonName"<br>
naptanstopcolumn="NatGazLocality"<br>
naptanstopcolumn="ATCOCode"<br>
</pre>
This results in stop\_names which are combinations of the stops' CommonName, NatGazLocality and ATCOCode.
Note that the respective values identify the columns in a NaPTAN version 1 CSV stop file. In the GTFS stops.txt file, the values of the picked columns are separated by a comma (,), or by the characters defined as the NaPTAN stop column separator.

## NaPTAN Stop Column Separator ##
The stop column separator works in conjunction with the NaPTAN stop name helper and NaPTAN stop column pick definitions. The value defined is used in place of the default comma (,).
Example:
<pre>
stopfilecolumnseparator=;-</pre>