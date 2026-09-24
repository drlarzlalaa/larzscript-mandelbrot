#!/bin/sh
# Whole pictures and totals against tools/reference.py (the same iteration in Python), for several windows.
check() {
  # args: xmin xmax ymin ymax width height max
  mine=$($LZ render --xmin=$1 --xmax=$2 --ymin=$3 --ymax=$4 --width=$5 --height=$6 --max=$7 | md5sum | cut -c1-32)
  ref=$(python3 tools/reference.py render $1 $2 $3 $4 $5 $6 $7 | md5sum | cut -c1-32)
  smine=$($LZ stats --xmin=$1 --xmax=$2 --ymin=$3 --ymax=$4 --width=$5 --height=$6 --max=$7)
  sref=$(python3 tools/reference.py stats $1 $2 $3 $4 $5 $6 $7)
  if [ "$mine" = "$ref" ] && [ "$smine" = "$sref" ]; then echo "window $1..$2 x $3..$4, $5x$6, max $7: same as reference ($smine)"; else echo "window $1..$2 x $3..$4, $5x$6, max $7: DIFFERENT"; fi
}
check -2.2 0.8 -1.2 1.2 70 28 100
check -2.0 0.5 -1.25 1.25 40 20 50
check -0.8 -0.7 0.05 0.15 60 30 300
check -0.7436 -0.7434 0.1317 0.1319 40 20 500
check -1.5 -1.2 -0.2 0.2 50 20 1000
check 0.25 0.35 -0.05 0.05 30 15 200
check -2 2 -2 2 80 40 20
check -0.1 0.1 0.6 0.9 60 30 150
check -1.8 -1.7 -0.05 0.05 40 20 400
