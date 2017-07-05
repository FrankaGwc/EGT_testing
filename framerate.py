#!/usr/bin/python
""" Simple script to count simple things
This scripts crawls through text files outputted from (AFAIK) BeGaze.
It does the following two things:

1. Calculate some ratio which is (Number of Samples - Time in ms) / Time in ms
2. Count the number of times the frequency is deviating from original value,
   should be in range 955-1000 (ms I guess)
"""

from __future__ import division
import glob


# Open the file/files.
print "Reading the files in the current directory."

# Ask for the study time/duration.
TIME = input("Please enter the time for the samples in minutes: \n")
FrameRate = input('Please enter the frame rate that is being tested: \n')
N = FrameRate/1000
print N

if not isinstance(TIME, int):

    raise Exception("Time is not integer, please give integer values" \
            "in Seconds.")

FILES = [files for files in glob.glob("*.txt")]


def get_timestamps(file_path):
    """Read file(s) from the current directory."""

    lines = []

    with open(file_path, 'r') as text_file:
        # Read the file ...
        if text_file is "":
            raise Exception("Could not find the right text file(s).")

        for line in text_file.readlines():
            line = line[0:9]
            if line.isdigit():
                lines.append(line)

    return lines


def count_frequency_deviation(timestamps):
    print "Count the deviations in frequency, Torlerated range is:" + str(FrameRate) + "(+-) 5"

    deviation_count = 0

    while len(timestamps) > 0:

        delta = int(timestamps.pop()) - int(timestamps.pop())

        if delta <= FrameRate/N-10 and delta >= FrameRate/N+10:
            deviation_count += 1
    print timestamps
    return deviation_count


def parse_values():
    """Function to parse values and return required information."""

    for file_name in FILES:

        timestamps = get_timestamps(file_name)

        print "Processing text file: " + file_name
        number_of_samples = len(timestamps)
        print "Number of timestamps: " + str(number_of_samples)
        time_ms = TIME * 60 * 1000 * N
        ratio_one = (time_ms-number_of_samples) / time_ms * 100
        print "Calculated DropOut:" + str(ratio_one) + "%"

        deviation_count = count_frequency_deviation(timestamps)
        print "Deviation from frequencies happened: " + str(deviation_count) \
                + " times"


if __name__ == "__main__":

    parse_values()
