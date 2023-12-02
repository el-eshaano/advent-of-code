#!/bin/zsh

function update_aoc_env() {


    local current_year=$(date +"%Y")
    local current_day=$(date +"%d")

    if [[ $(date +"%m") -eq 12 && $current_day -le 25 ]]; then

        if [[ -z "$AOC_DAY" || -z "$AOC_YEAR" || "$AOC_DAY" -ne "$current_day" || "$AOC_YEAR" -ne "$current_year" ]]; then

            export AOC_DAY=$current_day
            export AOC_YEAR=$current_year
        fi
    fi
}
