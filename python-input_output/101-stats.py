#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""

import sys

total_size = 0
count = 0
my_dict = {}
if __name__ == "__main__":
    try:
        for line in sys.stdin:
            try:
                parts = line.split()
                # print(parts)  # temporary debug line
                count += 1
                my_dict[parts[-2]] = my_dict.get(parts[-2], 0) + 1
                total_size += int(parts[-1])
                if count == 10:
                    count = 0
                    print(f"File size: {total_size}")
                    for key, value in sorted(my_dict.items()):
                        print(f"{key}: {value}")
            except:
                continue
    except KeyboardInterrupt:
        print(f"File size: {total_size}")
        for key, value in sorted(my_dict.items()):
            print(f"{key}: {value}")
