#!/bin/sh


# Loop through all attached batteries.

for battery in /sys/class/power_supply/BAT?
do
    # Get its remaining capacity and charging status.
    capacity=$(cat "$battery"/capacity) || exit
    status=$(cat "$battery"/status)

    if [ $status = "Unknown" ]; then
        status="Charging"

    fi

    # Print all results
    printf "%s%% \t %s\n" $capacity $status

done

