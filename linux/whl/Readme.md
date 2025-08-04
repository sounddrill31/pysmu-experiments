# Programming for the ADALM1000 in Python

EE1103L Electronics Lab - Addon Module BS in Electronic Systems - IIT Madras
A Python library and set of tools for the Analog Devices ADALM1000 Active Learning Module.

---

## EE1103L Electronics Lab - Addon Module - Linux
This repository contains supplementary materials for the EE1103L Electronics Lab course.

- **Course:** BS in Electronic Systems - IIT Madras
- **Course Instructor:** Dr. Janakiraman Viraraghavan
- **GitHub:** [aditya-rao-iit-m/adalm1000](https://github.com/aditya-rao-iit-m/adalm1000)
- **License:** GNU GPL v3.0

## Original Concept and Program
- **Author:** Aditya Rao (`23f3000019@es.study.iitm.ac.in`)
- **Program:** BS in Electronic Systems, IIT Madras
- **Date:** Friday, 5th April 2024

## Installation
Just download this whl and install:

`pip install ar_iitm-1.0-py3-none-any.whl`

## Warning
The core functions are wrapped into a whl to prevent low level calls being modified with the wrong hex codes.
Using the wrong hex codes can potentially brick the ADALM1000. 
Using the core functions from this whl file is recommended as its tested to be safe and will not brick the ADALM1000.
