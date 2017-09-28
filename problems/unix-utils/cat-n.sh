#!/bin/bash

set -u

if [[ $# -ne 1 ]]; then
	printf "Usage: %s file\n" "$(basename "$0")"
	exit 1
fi

file=$1
           
if [[ ! -f "$file" ]]; then
	echo "\"$file\" is not a file"
	exit 1
fi

i=0

while read -r Line; do
	let i++
	echo "$i $Line"
done < "$file"

