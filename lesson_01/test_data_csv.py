import pytest
import csv

# Function to read data from the CSV file and return it as a list of tuples
def get_test_data_from_csv():
    with open('test_data.csv', newline='') as csvfile:
        reader = csv.reader(csvfile) #קורא את המידע מהקובץ
        next(reader) # Skip the header row
        return [(int(row[0]), int(row[1]), int(row[2])) for row in reader]

# Use @pytest.mark.parametrize to load data into the test
@pytest.mark.parametrize("num1, num2, result", get_test_data_from_csv())
def test_sum_operation(num1, num2, result):
# Validate that the sum of num1 and num2 equals result
    assert num1 + num2 == result

#reader = [ [5,3,8], [10,15,25] ,...]
#row = [5,3,8]