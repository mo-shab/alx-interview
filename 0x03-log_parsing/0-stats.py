#!/usr/bin/python3
"""Stats module."""


import sys
import signal

# Initialize variables
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
valid_status_codes = set(status_counts.keys())
line_count = 0

def print_statistics():
    """Prints the statistics collected so far."""
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

def process_line(line):
    global total_size, line_count

    # Expected format check
    try:
        parts = line.split()
        ip_address = parts[0]
        date = parts[3] + " " + parts[4]
        request = parts[5] + " " + parts[6] + " " + parts[7]
        status_code = int(parts[8])
        file_size = int(parts[9])

        # Validate that request format matches "GET /projects/260 HTTP/1.1"
        if request != '"GET /projects/260 HTTP/1.1"':
            return

        # Update total file size
        total_size += file_size

        # Update status code count if valid
        if status_code in valid_status_codes:
            status_counts[status_code] += 1

        line_count += 1

    except (IndexError, ValueError):
        # Skip lines that don't match the expected format or have invalid integers
        return

def handle_interrupt(signal, frame):
    """Handle keyboard interruption (CTRL + C)"""
    print_statistics()
    sys.exit(0)

# Register signal handler for keyboard interrupt
signal.signal(signal.SIGINT, handle_interrupt)

# Process stdin line by line
try:
    for line in sys.stdin:
        process_line(line)

        # Every 10 lines, print statistics
        if line_count % 10 == 0 and line_count > 0:
            print_statistics()

except KeyboardInterrupt:
    # Print statistics when interrupted by keyboard (CTRL + C)
    print_statistics()
    sys.exit(0)

# Final statistics when the input ends
print_statistics()
