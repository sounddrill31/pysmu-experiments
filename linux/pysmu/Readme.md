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

## Technical Details

### `pysmu`: A Python Interface for Source-Measure Units

`pysmu` is a Python module that serves as a set of bindings for `libsmu`, a library developed by Analog Devices. This powerful combination allows users to control and interact with USB-based source-measure units (SMUs), most notably the ADALM1000 (often referred to as the M1K).

In essence, `pysmu` acts as a bridge, enabling users to write Python scripts to harness the capabilities of SMU hardware. This opens the door to a wide range of applications in electronics, from educational exercises to sophisticated automated testing.

#### Key Functions and Applications:

The primary purpose of `pysmu` is to provide a programmatic interface to the core functionalities of a source-measure unit. This includes:

* **Voltage and Current Control:** Users can precisely set voltage and measure the resulting current, or vice-versa. This is fundamental for characterizing electronic components.
* **Waveform Generation:** The module can be used to generate various waveforms, which is essential for testing the dynamic behavior of circuits.
* **Data Acquisition:** `pysmu` allows for the continuous or buffered reading of data from the SMU, facilitating data logging and analysis.

These capabilities make `pysmu` a valuable tool for a diverse audience, including:

* **Students and Educators:** The ADALM1000, in conjunction with `pysmu`, provides an affordable and versatile platform for learning and teaching fundamental concepts in electronics.
* **Electronics Hobbyists and Makers:** The ability to automate measurements and experiments empowers hobbyists to undertake more complex projects and characterizations.
* **Engineers and Technicians:** In a professional setting, `pysmu` can be used for automated testing of components, rapid prototyping, and custom measurement setups.

#### Technical Details and Usage:

`pysmu` is built on top of `libsmu` and is typically installed alongside it. The installation process can vary depending on the user's operating system (Windows, Linux, or macOS). The official `libsmu` GitHub repository, maintained by Analog Devices, provides detailed instructions and the necessary files for installation.

Once installed, users can import the `pysmu` module into their Python scripts. The library provides classes and methods for managing sessions with connected devices, configuring channels, and sending and receiving data. For example, a user could write a script to sweep a voltage across a diode while measuring the current, thereby automatically generating the diode's characteristic I-V curve. This data can then be easily processed, analyzed, and visualized using other popular Python libraries such as NumPy and Matplotlib.

In summary, `pysmu` is a specialized yet highly effective tool that significantly enhances the utility of Analog Devices' source-measure units by making them programmable and accessible through the popular and versatile Python programming language.
