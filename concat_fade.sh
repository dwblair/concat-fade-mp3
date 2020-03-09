#!/bin/bash

ffmpeg -i r.mp3 -i r.mp3 -i r.mp3 -i r.mp3 -vn \
-filter_complex \
" \
[0][1]acrossfade=d=10:c1=tri:c2=tri[a01]; \
[a01][2]acrossfade=d=10:c1=tri:c2=tri[a02]; \
[a02][3]acrossfade=d=10:c1=tri:c2=tri" \
river_out.mp3