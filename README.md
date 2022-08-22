# Engine Speed Estimation

This repository contains an application that can plot, analyze and estimate engine speed
from an idling vehicle using acceleration data.


## Usage/Examples
Run the install.sh script to install in a virtual environment or run the installation
and execute as a Python module:

```console
juvenal@pi:~ $ cd engine-speed-fft/
juvenal@pi:~/engine-speed-fft $ pip3 install .
```
After installation, run the example script by calling the application without
arguments to use one of the examples on "data" folder:
```console
juvenal@pi:~/engine-speed-fft/ $ python3 speedfft/estimate.py
File: /home/juvenal/engine-speed-fft/data/sample_idle_data.csv
Importing data
Found 3 columns
Removing mean from acceleration data
Engine speed estimated: 782.22 RPM
Engine speed estimated: 791.21 RPM
```