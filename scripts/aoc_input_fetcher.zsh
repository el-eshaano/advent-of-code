#!/bin/zsh

if [[ -z "$AOC_SESSION_COOKIE" || -z "$AOC_DAY" || -z "$AOC_YEAR" ]]; then
  echo "Error: AOC_SESSION_COOKIE, AOC_DAY, and AOC_YEAR environment variables are required."
  exit 1
fi

cd /home/eshaan/Personak/advent-of-code

formatted_day=$(printf "Day_%02d" "$AOC_DAY")
directory="${AOC_YEAR}/${formatted_day}"
mkdir -p "$directory"

input_file="${directory}/input.txt"

url="https://adventofcode.com/${AOC_YEAR}/day/${AOC_DAY}/input"
curl -s -b "session=${AOC_SESSION_COOKIE}" "$url" -o "$input_file"

if [[ $? -eq 0 ]]; then
  echo "input.txt for Advent of Code ${AOC_YEAR} Day ${AOC_DAY} downloaded successfully."
else
  echo "Failed to download input.txt. Please check your environment variables and internet connection."
fi

