#!/bin/sh
BAKDIR="data"
rm -rf $BAKDIR; mkdir $BAKDIR; chmod 755 $BAKDIR
 
venv/bin/python pfade_per_ziel.py

rsync -avz data/* tbx:~/smw.ffu/assets/data/pfade/

