import os.path
import sys

# handle too few/too many arguments
if len(sys.argv) != 2:
    sys.exit(f'{sys.argv[0]}: expected 1 argument, got {len(sys.argv) - 1}')

# get the input file location, check it exists
inputfile = sys.argv[1]
if not os.path.isfile(inputfile):
    sys.exit(f'{sys.argv[0]}: file not found or permission denied: {inputfile}')

# get the patient name from the input file location
# "foobar" is the patient name for location /some/path/foobar.txt 
patientname, _ = os.path.splitext(os.path.basename(inputfile))

print(f'Input file location: {inputfile}')
print(f'Patient name: {patientname}')