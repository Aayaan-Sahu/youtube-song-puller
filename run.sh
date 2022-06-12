#!/bin/bash

IFS=$'\n'
set -f
for i in $(cat < "song_file"); do
  echo "$i"
  youtube-dl -x --audio-format mp3 --add-metadata `python3 main.py $i`
done