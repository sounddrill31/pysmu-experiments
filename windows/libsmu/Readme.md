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

### `libsmu`: The Core Library for Interfacing with Analog Devices' SMUs

`libsmu` is a foundational, open-source software library developed by Analog Devices that provides a C++ application programming interface (API) for communicating with and controlling their USB-based source-measure units (SMUs). It serves as the primary software abstraction layer for interacting with the hardware, which in our case is the **ADALM1000 (M1K)**, the popular and affordable learning module.

Built upon the cross-platform `libusb` library, `libsmu` is designed to work on various operating systems, including Windows, MacOS, and Linux. It handles the low-level USB communication, allowing developers to focus on higher-level applications.

#### Purpose and Key Features

The main purpose of `libsmu` is to provide a standardized and robust way to control the functionalities of supported SMUs. This enables a wide range of applications, from educational software to automated test scripts.

Key features of `libsmu` include:

* **Session and Device Management:** It can detect and manage multiple connected devices, allowing for sessions that control one or more SMUs simultaneously.
* **Hardware Abstraction:** The library abstracts the specific hardware details of the SMU, providing a consistent interface for core operations.
* **Signal Control:** `libsmu` allows for precise control over sourcing voltage while measuring current (SVMI mode) and sourcing current while measuring voltage (SIMV mode).
* **Data Streaming:** It facilitates the continuous streaming of data to and from the device, which is crucial for applications requiring real-time data acquisition and waveform generation.
* **Mode Configuration:** Users can set the operational mode of each channel on the device (e.g., high impedance, voltage source, current source).

#### The Relationship Between `libsmu` and `pysmu`

The relationship between `libsmu` and `pysmu` is that of a core library and its language-specific binding:

* **`libsmu`** is the core engine, written in C++, that does the heavy lifting of communicating with the hardware.
* **`pysmu`** is the Python wrapper, or binding, for `libsmu`. It exposes the functions and classes of the C++ library to the Python environment.

In practical terms, when a user writes a Python script using `pysmu`, their commands are translated through the binding into calls to the underlying `libsmu` library, which then executes the commands on the ADALM1000 or other supported hardware. This architecture allows developers to leverage the ease and flexibility of Python for scripting and application development while still benefiting from the performance and low-level control of the C++ library.

In summary, `libsmu` is the essential software foundation that enables programmatic control of Analog Devices' educational SMUs, while `pysmu` makes this powerful functionality accessible and convenient for the large community of Python developers.
