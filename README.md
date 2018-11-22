# ISS Tracker - Tracking the International Space Station 
<img src="https://img.shields.io/aur/license/yaourt.svg"> <img src="https://img.shields.io/badge/python-3.x-brightgreen.svg"> <img src="https://img.shields.io/badge/release-v1.0-red.svg"> 

ISS Tracker is a simple script written in python which uses bunch of APIs to collect real-time information related to the International Space Station.

![2018-11-22_070833](https://user-images.githubusercontent.com/35377569/48876695-89ecd380-ee25-11e8-90c7-47ff1c4cfdd4.jpg)

### Features
- [x] Current ISS Location
- [x] ISS Pass Times (upcoming ISS passes for Colombo, Sri Lanka)
- [x] Number of People In Space
- [x] ISS TLE data
- [x] Google Map URL for ISS Current Location
- [x] Velocity | Visibility | Altitude 
- [x] Automatically refresh data after every 60 seconds
- [ ] Small site with ISS tracing map.

### How to Install and Run in Linux
[1] Enter the following command in the terminal to download it.

`git clone https://github.com/Sameera-Madhushan/ISS-Tracker`

[2] After downloading the program, enter the following command to navigate to the Digger directory and listing the contents

`cd ISS-Tracker && ls`

[3] Install dependencies 

`pip3 install -r requirements.txt`

[4] Now run the script with following command.

`python3 ISS-Tracker.py`


### How to Install and Run in Windows
[1] Download and run Python 2.7.x and Python 3.7 setup file from <a href="https://python.org" target="_blank"><span style="color: blue">Python.org</span></a>
  - In Install Python 3.7, enable Add Python 3.6 to PATH
  
[2] Download and run Git setup file from <a href="https://git-scm.com/" target="_blank"><span style="color: blue">Git-scm.com</span></a>, choose Use Git from Windows Command Propmt.

[3] Afther that, Run Command Propmt and enter these commands:

```
git clone https://github.com/Sameera-Madhushan/ISS-Tracker
cd ISS-Tracker
pip3 install -r requirements.txt
python3 ISS-Tracker.py
```

### Screenshot

![2018-11-22_073116](https://user-images.githubusercontent.com/35377569/48877323-c53cd180-ee28-11e8-817b-5188c270214c.jpg)

### Used APIs

https://wheretheiss.at/w/developer

http://open-notify.org/Open-Notify-API/











