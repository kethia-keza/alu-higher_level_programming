#!/bin/bash
# Displays the size of the body of the response of a given URL
curl -s "$1" | wc -c
