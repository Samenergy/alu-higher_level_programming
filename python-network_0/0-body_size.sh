#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

url="$1"

# Send request and store the response in a temporary file
response=$(mktemp)
curl -s "$url" -o "$response"

# Get the size of the response body in bytes
size=$(stat -c %s "$response")

# Display the size of the response body
echo "Size of the response body: $size bytes"

# Clean up temporary files
rm "$response"

