import datetime
import os
import shutil
import sys

import piexif


SRC_DIR = sys.argv[1]
DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S'
START_DATE = datetime.datetime.strptime(sys.argv[2], DATETIME_FORMAT)
END_DATE = datetime.datetime.strptime(sys.argv[3], DATETIME_FORMAT)
DATETIME_RANGE = END_DATE - START_DATE

DEST_DIR = shutil.copytree(SRC_DIR, f'{SRC_DIR}-out')

with os.scandir(SRC_DIR) as d:
    # Make a list first because we need to know how many photos there are.
    photo_list = sorted([p.name for p in d if p.is_file(follow_symlinks=False)])

DATETIME_DELTA = DATETIME_RANGE / (len(photo_list) - 1)

for i, p in enumerate(photo_list):
    exif_data = piexif.load(f'{SRC_DIR}/{p}')
    timestamp = datetime.datetime.strftime(
        START_DATE + DATETIME_DELTA * i,
        '%Y:%m:%d %H:%M:%S')
    exif_data['Exif'][piexif.ExifIFD.DateTimeOriginal] = timestamp
    piexif.insert(piexif.dump(exif_data), f'{DEST_DIR}/{p}')


