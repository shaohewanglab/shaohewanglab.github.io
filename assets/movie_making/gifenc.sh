#!/bin/sh

palette="/tmp/palette.png"

### scale here is x:y, where -1 indicates maintaining the original scale
# filters="fps=12,scale=1280:-1:flags=lanczos"
filters="fps=24,scale=-1:500:flags=lanczos"

ffmpeg -v warning -i $1 -vf "$filters,palettegen=stats_mode=diff" -y $palette
# ffmpeg -v warning -i $1 -vf "$filters,palettegen" -y $palette
ffmpeg -v warning -i $1 -i $palette -lavfi "$filters [x]; [x][1:v] paletteuse" -y $2
