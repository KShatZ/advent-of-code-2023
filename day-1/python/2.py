import re
import time

start = time.time()


pattern = re.compile("(?=(one|two|three|four|five|six|seven|eight|nine|\d))") 
num_conversion = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

# test_string = "8nine37bpkmtghhnc2hnreightwohvs"
# a = pattern.findall(test_string)
# print(a)



values = []

with open("../input.txt") as file:

    file_lines = file.readlines()

    total_sum = 0
    for line in file_lines:
        
        numbers = pattern.findall(line)

        first = numbers[0]        
        last = numbers[-1]
    
        if len(first) > 1:
            first = num_conversion[first]

        if len(last) > 1:
            last = num_conversion[last]

        calibration_value = int(first + last)
        values.append(calibration_value)
    
        total_sum += calibration_value

    print("The total sum:", total_sum)
end = time.time()
print(f"Total time {end - start}")


        