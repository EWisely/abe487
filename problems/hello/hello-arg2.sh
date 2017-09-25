#!/bin/bash

if [[ $# -ne 2 ]]; then
	printf "Usage: %s greeting name\n" "$(basename "$0")"
	exit 1
fi

echo "$1, $2!"
