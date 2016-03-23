# Introduction #

Thank you for contributing to our project!

We use two common practices to help us maintain an acceptable quality level. Automated tests should be a quick way to completely exercise your change and will make sure it continues to work in the future. Code reviews done by at least one person other than the writer helps us coordinate our work and hopefully make writing software more fun. This page describes the best practices we expect you to follow when contributing to the transitfeed distribution. Please post to googletransitdatafeed@googlegroups.com if you have suggestions for improving this process or have questions about the change you want to make.

## Get source ##

See the Source tab above for instructions on downloading the source. Please checkout and modify the trunk to make it as easy as possible to merge your changes into the main distribution.

## Legal stuff ##

Our project uses the [Apache License 2.0](http://www.apache.org/licenses/). To ease distribution your contributions must be released under the same terms. You may release each change explicitly under the license or mail googletransitdatafeed@googlegroups.com saying that all your contributions to the transitfeed distribution may be released under the same terms as transitfeed itself.

## Python Style ##

To maintain a consistent style throughout the code and to help you avoid some common Python problems please follow this [style guide](http://google-styleguide.googlecode.com/svn/trunk/pyguide.html) except we have been using 2 space indents. As a last resort follow the style of surrounding code.


## Make and test changes ##

Before you request a review, you should ensure that all the unit tests pass. If you are fixing a bug or adding a new feature please add a test for it in the `test` directory. It's good to make sure that you've seen your tests fail (so that you know that they're being run). If necessary, temporarily break the code that the tests check to ensure that they fail in that case.

You'll want a copy of the [nose](http://somethingaboutorange.com/mrl/projects/nose/) tool for Python.  Once you have that installed, you can just run
```
$ nosetests
```
from the `trunk/python` directory to run all the tests in the project.

Note that in order to pass all the tests, you'll need to install some extra Python packages to support optional features of the code:
  * [pytz](http://pytz.sourceforge.net/)
  * [elementtree](http://effbot.org/zone/element-index.htm) (if running Python 2.4)
Both of these should be available through `easy_install`.

Your code should also run in python 2.4. Running `easy_install-2.4 nose` will create `nosetests-2.4` which runs the tests in 2.4. You may need to install other 2.4 specific libraries such as `python-pysqlite2`, another copy of `pytz`, etc.

## Request a review ##

We are currently using the [Rietveld Code Review Tool](http://codereview.appspot.com/) which has [its own instructions](http://code.google.com/p/rietveld/wiki/CodeReviewHelp).

When you want someone to review your code make a new codereview issue with your changes. If you select GoogleTransitDataFeed from the SVN Base make your diff or run the upload script [upload.py](http://codereview.appspot.com/static/upload.py) from the `trunk/` directory, not `trunk/python`. Enter googletransitdatafeed@googlegroups.com as the reviewer or CC. Then use the code review interface to mail a request for a review.

## Commit change to the trunk ##

Once your reviewer has given you a "looks good", you're ready to commit your code to the trunk.  Check that you are only submitting the expected changes and tests pass.
```
svn update
svn status  # Lists files modified and added to the working copy
svn diff  # Dump all changes
nosetests

# Make a file describing the changes. Start with a one line summary. Include the
# URL of the review at codereview.appspot.com.
$EDITOR changedesc.txt
svn commit -F changedesc.txt
```