import requests
import time
import sys
import os

banner = r'''

           .       .                   .       .      .     .      .
          .    .         .    .            .     ______
      .           .             .               ////////
                .    .   ________   .  .      /////////     .    .
           .            |.____.  /\        ./////////    .
    .                 .//      \/  |\     /////////
       .       .    .//          \ |  \ /////////       .     .   .
                    ||.    .    .| |  ///////// .     .
     .    .         ||           | |//`,/////                .
             .       \\        ./ //  /  \/   .
  .                    \\.___./ //\` '   ,_\     .     .
          .           .     \ //////\ , /   \                 .    .
                       .    ///////// \|  '  |    .
      .        .          ///////// .   \ _ /          .
                        /////////                              .
                 .   ./////////     .     .
         .           --------   .                  ..             .
  .               .        .         .                       .
              ___ ___ ___   _____            _                      .
             |_ _/ __/ __| |_   _| _ __ _ __| |_____ _ _            
              | |\__ \__ \   | || '_/ _` / _| / / -_) '_|       .
             |___|___/___/   |_||_| \__,_\__|_\_\___|_|v1.0        .       

                    [Coded By Sameera a.k.a άλφα Χ]

'''

clear = lambda: os.system('cls')

def details():
    alpha = requests.get("https://api.wheretheiss.at/v1/satellites/25544").json()
    s = alpha["id"]
    print("NORAD ID = " + str(s))

    q = alpha["velocity"]
    r = alpha["visibility"]
    t = alpha["altitude"]

    print('\n'"Velocity: " + str(q) + "km/h")
    print("Visibility: " + str(r))
    print("Altitude: " + str(t) + "Km")

    people = requests.get("http://api.open-notify.org/astros.json").json()
    if (people['message'] == 'success'):
        print('\n'"Amount of People In Space Right Now: " + str(people["number"]))
        cosmonauts = people["people"]
        print('\n'"Names and Spacecraft of those People: ")
        for x in cosmonauts:
            print(x["name"] + ", Craft: " + str(x["craft"]))
    else:
        print("Invalid response.")

    position = requests.get("http://api.open-notify.org/iss-now.json").json()
    if (position['message'] == 'success'):
        location = position["iss_position"]
        lat = location["latitude"]
        lon = location["longitude"]
        tim = position["timestamp"]
        print('\n' "International Space Station Current Location\nLongitude = " + lon + "   Latitude = " + lat)
        print('\n'"ISS Time: " + str(tim) + "   " "#UNIX_TIME_STAMP")
    else:
        print("Invalid response.")

    pass_times = requests.get("http://api.open-notify.org/iss-pass.json?lat=6.9271&lon=79.8612").json()
    if (pass_times['message'] == 'success'):
        print('\n'"Upcoming ISS passes for Colombo, Sri Lanka:")
        beta = pass_times["request"]["passes"]
        print("Number of passes: " + str(beta) + '\n')
        for x in pass_times["response"]:
            p = time.ctime(x["risetime"])
            print(p + " " "|" + " " + "Duration - " + str(x["duration"]))
    else:
        print("Invalid response.")

    LATITUDE = lat
    LONGITUDE = lon
    BASE_URL = "https://www.google.com"

    url = (BASE_URL + "/maps?q={},{}&z=4").format(LATITUDE, LONGITUDE)

    tle = requests.get("https://api.wheretheiss.at/v1/satellites/25544/tles?format=text").text
    print('\n', tle)

    print('\n'"Google Map URL for ISS Current Location: " + url)
    time.sleep(60)

def connection(url='http://www.google.com/', timeout=5):
    try:
        req = requests.get(url, timeout=timeout)
        req.raise_for_status()
        return True
    except requests.HTTPError as e:
        print("Checking internet connection failed, status code {0}.".format(
        e.response.status_code))
    except requests.ConnectionError:
        print("No internet connection available.")
    return False

if connection() == True:
    print(banner)
    try:
        while True:
            details()
            clear()
    except(KeyboardInterrupt):
        print("Programme Interrupted")
else:
    sys.exit(0)

''' 
- References -
http://open-notify.org/
https://wheretheiss.at/w/developer
'''



