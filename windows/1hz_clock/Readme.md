# Programming for the ADALM1000 in Python
## EE1103L Electronics Lab - Addon Module
### BS in Electronic Systems - IIT Madras
#### Course Instructor : Dr.Janakiraman Viraraghavan
#### Control Code by Aditya Rao, 23f3000019@es.study.iitm.ac.in
#### Github : https://github.com/aditya-rao-iit-m/adalm1000
#### GNU GPL v3.0

1 Hz Clock Generator for ADALM1000 (Windows OS) - April 2024  

---

### Important Note:
- This program needs exclusive access to the ADALM1000 to function properly.  
- Pixelpulse / ALICE etc should not be open when running this program.  
- This program might not work properly with other versions of python. Its tested on Python ver 3.10.10 only, currently.  
- If the ADALM1000 is not found connected to USB, this program simply exits.  
- This is the Windows-64 bit version. Email me for Linux, Mac, Raspberry Pi versions with your OS name and version.  

---

### Pre-requisites and install instructions - Windows-64bit:
This program needs Python 3.10.10 and libsmu with pysmu python bindings installed properly on your Windows computer.

---

**Download link:**  
https://www.python.org/ftp/python/3.10.10/python-3.10.10-amd64.exe  
Run above exe file setup / installer : python version 3.10.10  

#### VERY IMPORTANT
Special care has to be taken while installing Python 3.10.10:  
1. First uninstall any older versions of python in your computer.  
2. Then while installing python ensure every check box is checked.  
3. At the beginning, there is a check box to install python in the Windows Path. **Very important to check this box.**  
4. Select custom installation, and check every box before proceeding.  
5. After installing python, **REBOOT the computer** before proceeding further.  

---

**Next install libsmu. The installer is available in the libsmu folder or you can download it from the link below:**  
https://github.com/analogdevicesinc/libsmu/releases/download/v1.0.4/libsmu-1.0.4-setup-x64.exe  
Run above exe file setup / installer : libsmu 1.0.4  

---

**To install the pysmu python bindings, just run this at the command prompt after downloading the whl file from the pysmu folder:**
```bash
pip install pysmu-1.0.4-cp39-cp39-win_amd64.whl
```

You must be able to see pysmu 1.0.4 when you run this at the command prompt:
```bash
pip list
```
---

Download the whl file from this repo's whl folder, to your local computer.
ar_iitm = Aditya Rao IIT Madras control transfer python library for the ADALM1000
This wheel file will be updated regularly with more functionality, and is platform independent.

Install the ar_iitm-1.0-py3-none-any.whl wheel file using the command:

```bash
pip install ar_iitm-1.0-py3-none-any.whl
```
---
## Hardware Connections
- Connect the **PIO1 pin** to your chip's clock pin (eg. Pin 2 of the 74LS163).  
- Connect the **GND pin** to the chip's ground (eg. Pin 8 of the 74LS163).  

---

## How to Use
After all installations:  
1. Connect the ADALM1000 to a USB port.  
2. Run the program by either:  
   - Executing `clock.exe` at the command prompt, **or**  
   - Clicking on the `clock` executable file.  

**Success indicator**: The blue notification LED will blink every second when the 1 Hz clock signal is generated successfully.  

---

## Concept and Program by
Aditya Rao  
`23f3000019@es.study.iitm.ac.in`  
BS in Electronic Systems  
IIT Madras  
Friday, 5th April 2024  




