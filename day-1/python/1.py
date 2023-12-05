import re

with open("../input.txt") as input_file:

    file_lines = input_file.readlines()
    regex_pattern = re.compile("\d") # Using compile is better when doing a lot of matching

    total_sum = 0
    for line in file_lines:

        numbers = regex_pattern.findall(line) 
        
        calibration_value = int(numbers[0] + numbers[-1])
        total_sum += calibration_value

    print("Sum of all calibration values:", total_sum)


        
        



        

    