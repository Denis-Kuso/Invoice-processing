# Deliveroo 
> A script that extracts total money earned from a number of invoice files issued by Deliveroo

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information

Delivery couriers are considered self-employed and thus need to report their earnings.
However, how much they earn is sent to them on a weekly basis in invoice files. Hence, there is a task involved ,that basically repeats itself, either each week or more likely, when "doing your taxes" is due.
Hence, this script:

- Automates the process of opening each invoice and summing up all the earnings
- Reduces chances of typing errors when transfering data or calculating on the fly
- Drastically reduces time taken to get total money earned (normal rider would have $\ge$ 52 files to open)

## Usage

How does one go about using it?

One could just type
```{bash}
>python3 extractfees
```
and would receive feedback on the optional/positional arguments and the usage.
![](.images/feedback-on-usage.png)

Thus, the following is the proper basic usage, where `<name_of_source_dir>` contains the invoice files.
```{bash}
>python3 extractfees <name_of_source_dir>
```
The output will then look like this:

![](.images/feedback-on-output.png)


Using the optional `-p` or the verbose option `--print` the user would get each filename and the fee extracted from it displayed, as opposed to just the final sum.

## Project status

- In development

## Technologies used

- Python version: 3.8.1
- Libraries used: see requirements.txt

## Room for improvement

Room for improvement:

- Add GUI for those (most) not comfortable with the command line
- Enable creation of descriptive statistics (frequency, central tendency, variation)

To do:

- Add "setup" section
- Add ability of bulk renaming of invoice files by invoice period

## Contact

- kuso.cm@gmail.com
