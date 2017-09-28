#!/bin/bash

set -u

if [[ $# -ne 1 ]]; then
	printf "Usage: %s File\n" "$(basename "$0")"
	exit 1
fi

i=0
File=$1

while read -r Line; do
	let i++
	echo "$i $Line"
done < "$File"
