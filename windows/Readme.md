# Programming for the ADALM1000 in Python

---

## EE1103L Electronics Lab - Addon Module

* **Course:** BS in Electronic Systems - IIT Madras
* **Instructor:** Dr. Janakiraman Viraraghavan
* **Code Repository:** Aditya Rao, `23f3000019@es.study.iitm.ac.in`
* **GitHub:** [https://github.com/aditya-rao-iit-m/adalm1000](https://github.com/aditya-rao-iit-m/adalm1000)
* **License:** GNU GPL v3.0
* **Date:** April 2024

---

## Important Notes

⚠️ This program needs **exclusive access** to the ADALM1000 to function properly. Applications like Pixelpulse / ALICE etc., should not be open when running this program.

If the ADALM1000 is not found connected to USB, this program will simply exit.

This is the Windows-64 bit version. Email me for Linux, Mac, or Raspberry Pi versions with your OS name and version. This program might not work properly with other versions of python. It is tested on **Python ver 3.10.10** and **3.13.5** only, at the moment.

---

## Pre-requisites and Installation (Windows-64bit)

This program requires Python 3.10.10 and `libsmu` with `pysmu` python bindings installed properly on your Windows computer.

### 1. Install Python

You can download either of the following versions:
* **Python 3.13.5:** [python-3.13.5-amd64.exe](https://www.python.org/ftp/python/3.13.5/python-3.13.5-amd64.exe)
* **Python 3.10.10:** [python-3.10.10-amd64.exe](https://www.python.org/ftp/python/3.10.10/python-3.10.10-amd64.exe)

> #### **** VERY IMPORTANT ****
>
> Special care has to be taken while installing Python.
> 1.  First, uninstall any older versions of Python from your computer.
> 2.  During installation, ensure **every checkbox is checked**.
> 3.  At the beginning of the setup, there is a checkbox to **add Python to the Windows Path**. It is very important to check this box.
> 4.  Select **custom installation**, and check every box before proceeding.
> 5.  After installing Python, **REBOOT** the computer before you proceed further.

### 2. Install `libsmu`

Download and run the installer for `libsmu` v1.0.4.
* **Download Link:** [libsmu-1.0.4-setup-x64.exe](https://github.com/analogdevicesinc/libsmu/releases/download/v1.0.4/libsmu-1.0.4-setup-x64.exe)

### 3. Install `pysmu` Python Bindings

To install the `pysmu` python bindings, run the following command at the command prompt:

```bash
pip install -i [https://test.pypi.org/simple/](https://test.pypi.org/simple/) pysmu
```

You can verify the installation by running `pip list`, and you should see `pysmu 1.0.4` in the output.

```bash
pip list
```

### 4. Install the `ar_iitm` Library

`ar_iitm` is the Aditya Rao IIT Madras control transfer python library for the ADALM1000. This wheel file will be updated regularly with more functionality and is platform-independent.

1.  Download the `.whl` file from this repo's `whl` folder to your local computer.
2.  Install the `ar_iitm-1.0-py3-none-any.whl` wheel file using the command:

```bash
pip install ar_iitm-1.0-py3-none-any.whl
```

---

## Running the Programs

Run the sample python programs, or your own code, from the command prompt like this:

```bash
python rgb_clock_test.py
```
