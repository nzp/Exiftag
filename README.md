# Exiftag

A dead simple script to batch embed `DateTimeOriginal` Exif tag into photos.
Use case is tagging a bunch of scanned photos (from negatives or positives).
Since we usually don't know the exact time each photo was taken, the script works
by taking a date-time range, calculates the time delta, and applies that to
photos.  File names must be lexicographically ordered according to chronology 
for this to work correctly.  Requires Python > 3.6 (uses F-strings).

Usage:

    python exiftag.py DIRECTORY STARTDATETIME ENDDATETIME
    
Where:
* `DIRECTORY` is the path of directory containing the original photos,
relative to current directory.  The scrip makes a copy of this directory and
tags the copies.

* `STARTDATETIME` and `ENDDATETIME` are in ISO 8601 format
(`yyyy-mm-ddThh:mm:ss`).
