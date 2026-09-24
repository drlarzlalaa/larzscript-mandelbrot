#!/bin/sh
# -0.75 + 0.1i is near the "neck" of the set and takes 33 steps to escape; 0 and -2 never escape; 1 + i escapes in 2.
$LZ point
$LZ point --re=0 --im=0
$LZ point --re=-2 --im=0
$LZ point --re=1 --im=1
$LZ point --re=-0.1 --im=0.75 --max=500
