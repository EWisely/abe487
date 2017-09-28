#!/bin/bash

set -u

NUMBER=${2:-3}

if [[ $# -lt 1 ]] || [[ $# -gt 2 ]]; then 
	printf "Usage: %s FILE [NUM]\n" "$(basename "$0")"
	exit 1
fi

FILE=$1
if [[ ! -f "$FILE" ]]; then
        echo "\"$FILE\" is not a file"
        exit 1
fi

i=0
while read -r LINE; do
	if [[ "$i" -lt "$NUMBER" ]]; then
	echo $LINE
	fi
	let i++
done < "$FILE"

