# Programming for the ADALM1000 in Python
EE1103L Electronics Lab - Addon Module  
BS in Electronic Systems - IIT Madras  
Course Instructor : Dr.Janakiraman Viraraghavan  
Code repository by Aditya Rao, 23f3000019@es.study.iitm.ac.in  
April 2024  
Github Repo: https://github.com/aditya-rao-iit-m/adalm1000  
GNU GPL v3.0
April 2024

Important Note: 
This program needs exclusive access to the ADALM1000 to function properly.  
- Pixelpulse / ALICE etc should not be open when running this program.  
<!-- This program might not work properly with other versions of python. Its tested on Python ver 3.10.10 only, currently.-->
- If the ADALM1000 is not found connected to USB, this program simply exits.
[This is the Windows-64 bit version](1hzclock/clock.exe). Email me for Linux, Mac, Raspberry Pi versions with your OS name and version.

## New Instructions
### Windows

<!--
0. Install the latest Python3 from here: 



 -->


<!--
> [!NOTE]
> This allows you to use the latest python version with the pysmu. If you just need the 1Hz Clock then just download it from the link here and set it up: https://github.com/aditya-rao-iit-m/adalm1000/blob/main/1hzclock/clock.exe

Follow these steps to set up:
0. Install `pixi` from the link here: https://github.com/prefix-dev/pixi/releases/latest/download/pixi-x86_64-pc-windows-msvc.msi
1. Restart your system after a successful installation.
2. git clone step
3. pretty much the same as linux/osx from here
-->
### Linux/Mac
0. Ensure that `python3` and `git` are already installed and are accessible from the terminal! 
    - Linux: Use your default package manager. The command varies from system to system but it usually looks like this:
        - `sudo apt update; sudo apt install git python3 # Debian/Ubuntu`
        - `sudo zypper install python3 git # SUSE`
        - `sudo pacman -S git python # Arch`
        - `sudo dnf install python3 git # RHEL/Fedora`
        - `sudo apk install python3 git # Alpine`
    - Mac: Use brew to install these. That might need additional setup beforehand as well.
        - `brew install git python`

1. Install Prefix.Dev's `pixi` as per official instructions at https://pixi.sh/latest/#installation <!-- Instructions after here will work on Windows too provided deps like python3 and git are installed-->
2. Prepare workspace with the command
    ```bash
    git clone https://github.com/aditya-rao-iit-m/adalm1000; cd adalm1000
    ```
    ```bash
    cd adalm1000
    ```
3. Run the following Command to let `pixi` setup your environment
    ```bash
    pixi install
    ```
4. Have `pixi` prepare the WHL files
    ```bash
    pixi run setup_ar
    ```
5. Start `rgb_clock_test.py`
    ```bash
    pixi run start
    ```

## Old Instructions

> [!WARNING]
> These are previous instructions, used before we introduced `pixi`. Follow them if you're having trouble with the above!

Pre-requisites and install instructions - Windows-64bit :
This program needs Python 3.10.10 and libsmu with pysmu python bindings installed properly on your Windows computer.

************************

Download link: 
https://www.python.org/ftp/python/3.10.10/python-3.10.10-amd64.exe
Run above exe file setup / installer : python version 3.10.10

**** VERY IMPORTANT ****

Special care care has to be taken while installing Python 3.10.10
First uninstall any older versions of python in your computer.
Then while installing python ensure every check box is checked.
At the beginning, there is a check box to install python in the Windows Path. Very important to check this box.
Then select custom installation, and check every box before proceeding.
The after installing python, REBOOT the computer before you proceed further.....

************************

Next install libsmu
https://github.com/analogdevicesinc/libsmu/releases/download/v1.0.4/libsmu-1.0.4-setup-x64.exe
Run above exe file setup / installer : libsmu 1.0.4

************************

To install the pysmu python bindings, just run this at the command prompt:
```bash
pip install -i https://test.pypi.org/simple/ pysmu
```
You must be able to see pysmu 1.0.4 when you run this at the command prompt:

```bash
pip list
```
************************

Download the whl file from this repo's whl folder, to your local computer.
ar_iitm = Aditya Rao IIT Madras control transfer python library for the ADALM1000
This wheel file will be updated regularly with more functionality, and is platform independent.

install the ar_iitm-1.0-py3-none-any.whl wheel file using the command:
```bash
cd whl
```
```bash
pip install ar_iitm-1.0-py3-none-any.whl
```
************************

Just run the sample python programs, or even the ones you code, from the command prompt:

```bash
python rgb_clock_test.py
```

************************
### Credits

#### Concept and Program
Aditya Rao  
23f3000019@es.study.iitm.ac.in  
BS in Electronic Systems  
IIT Madras  
Friday, 5th April 2024  

#### Minor Documentation and Installation Improvements
Souhrud Reddy  
24f3100273@es.study.iitm.ac.in  
BS in Electronic Systems  
IIT Madras  
Thursday, 31st July 2025  
https://sounddrill31.github.io