#!/bin/bash
# Automatically sorts images into Dewey + Letter folders

SOURCE_DIR="unsorted"
TARGET_DIR="static/images"

for file in "$SOURCE_DIR"/*; do
  # Extract filename parts using regex
  [[ $(basename "$file") =~ _([A-Z])-([0-9]{3}) ]] || continue
  letter="${BASH_REMATCH[1]}"
  dewey="${BASH_REMATCH[2]}"

  # Map Dewey to human-readable folder name
  case $dewey in
    000) category="000_General-Knowledge" ;;
    100) category="100_Philosophy-Psychology" ;;
    200) category="200_Religion" ;;
    300) category="300_Social-Sciences" ;;
    400) category="400_Language" ;;
    500) category="500_Science" ;;
    600) category="600_Technology" ;;
    700) category="700_Arts-Recreation" ;;
    800) category="800_Literature" ;;
    900) category="900_History-Geography" ;;
    *) continue ;;
  esac

  # Create directory if missing
  mkdir -p "$TARGET_DIR/$category/$letter"

  # Move file
  mv "$file" "$TARGET_DIR/$category/$letter/"
  echo "Moved $(basename "$file") → $category/$letter/"
done
