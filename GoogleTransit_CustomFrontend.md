## Your Google Transit Custom Frontend ##
### or: How to drive [Google Transit](http://www.google.com/transit) directly from a third party web site ###

[This  post on the Google Transit group](http://groups.google.com/group/googletransit/browse_thread/thread/799160f6189c8a84) illustrates the problem:

"I administer a weekly club e-newsletter. We have many events, and I
want to encourage our members to use public transportation, so I
provide links to Google Transit. I would like to be able to provide our members with a link to the Google Transit main page, http://maps.google.com/transit, but with the <b>End Address</b> and <b>Arrive By</b> fields completed. That way, they could just enter their starting address and click Get Directions."

The solution is not a direct answer to the question. Instead of filling in fields of Google Transit's original frontend, the answer is to call the backend of Google Transit directly from the first party web site code. The relevant query elements are part of a RESTful call of Google Transit. Below a code snippet that can be used in a web site's HTML code to create a request to Google Transit:

<pre>
<html><br>
<body><br>
<br>
<form action="http://www.google.com/transit"><br>
<input type="hidden" name="ie" value="UTF8"><br>
<input type="hidden" name="f" value="d"><br>
Start adress<br>
<input type="text" style="width:20em" size="20" name="saddr" tabindex="1" maxlength="2048"/><br>
<br>e.g. 4412 se 17th ave, Portland, OR<br>
<br>
<!-- Code meeting location, date and time below --><br>
<input type="hidden" name="daddr" value="Burnside St & SW Broadway, Portland, OR"<br>
<input type="hidden" name="ttype" value="arr"><br>
<input type="hidden" name="date" value="2/13"><br>
<input type="hidden" name="time" value="7:30pm"><br>
<br>
<!-- Optional location hint to help a partial address in saddr work. Get the sll<br>
and sspan values by moving the map over the area of interest in clicking on "Link".<br>
If you edit these don't forgot to remove them from the html comment. --><br>
<!-- <input type="hidden" name="sspan" value="0.1232,0.2211"><br>
<input type="hidden" name="sll" value="37.7587,-122.4415"><br>
--><br>
<br>
<br><input type="submit" value="Get Directions" /><br>
<br>
<br>
Unknown end tag for </form><br>
<br>
<br>
<br>
<br>
<br>
Unknown end tag for </body><br>
<br>
<br>
<br>
<br>
Unknown end tag for </html><br>
<br>
<br>
</pre>

This code snippet creates an input field for the start address, and backfills the remaining data with hardcoded destination address, date and time. In the code snippet, the meeting would take place at Burnside St & SW Broadway, Portland, OR on 2/13 at 7:30.
For better formatting, it is possible to integrate the input field in other elements like a table.

The following web sites demonstrates how this can look:
  * http://healthierplanethealthieryou.com/index.html
  * http://www.underwater-society.org/uwhockey/sanfran/WhereAndWhen.html