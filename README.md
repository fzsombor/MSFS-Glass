# MSFS Glass
MSFS Glass is a tool that allows you to control essential aircraft instruments such as NAV/COM frequencies, autopilot or lights using almost any mobile device, laptop or PC. MSFS Glass is forever free to use & open source.

![MSFS-Glass-cover.png](images/MSFS-Glass-cover.png)

### MSFS Glass features

- Track your plane on an interactive moving map
- UIs tailored for specific planes:
  - NAV 1/2 frequency and OBS 1/2 selection
  - ADF frequency and ADF card selection
  - COM 1/2 and transponder selection
  - Autopilot with altitude, vertical speed, and airspeed settings
  - Avionics controls
  - Gyro drift and altimeter pressure settings
  - Light controls
  - Pitot heat and deicing controls
  - Gear, flaps and spoilers
  - Trim
- Generic controls for all aircraft
- Simulation rate controls
- Portrait and Landscape mode to support all devices with a browser


### Supported Control Profiles
MSFS Glass has built-in support for the following aircraft:
- Default GNS430/530 and G1000 (to be used with default MSFS planes and other third-party planes without dedicated control profiles)
- Airbus A320neo
- Airbus A321
- Beechcraft Bonaza G36
- Boeing 737 Max
- Cessna 172 G1000
- Cessna 208
- Cessna 400
- Cirrus Vision Jet G2
- CubCrafters XCub
- CubCrafters NXCub
- Daher TBM 930
- DC-3
- Diamond DA-40NG
- Diamond DA-62
- DracoX
- JMB VL-3
- Pilatus PC-12

## Update 03/16/2025 Version 2.0.0-beta
- Credit where credit is due:
   - [https://github.com/mracko/MSFS-Mobile-Companion-App](https://github.com/mracko/MSFS-Mobile-Companion-App/)
   - [https://github.com/odwdinc/Python-SimConnect](https://github.com/odwdinc/Python-SimConnect)
   - [https://github.com/hankhank10/MSFS2020-cockpit-companion](https://github.com/hankhank10/MSFS2020-cockpit-companion)
- Created a new repo due to abandoning the original repos
- Updated DLL and header definitions to the SDK of MSFS2024
- **Rebranding MSFS 2020 Mobile Companion App to MSFS Glass**
- Bumped SimConnect version to SDK 1.2.4
- **Implemented [Input events](https://docs.flightsimulator.com/html/Programming_Tools/SimConnect/SimConnect_API_Reference.htm#inputevents) to be able to control avionics without an external WASM (MobiFlight) module**
- **Implemented LVar getting and setting without the need of a WASM module**
- Merged some pull requests on the original repos
- Cherry-picked changes from each repo to have all the changes in one place
- Updated OpenAIP integration for aviation maps to load
- Added API key inputs for OpenAIP
- Optimizing imports and memory footprint
- Created a framework for logging including debug log level and logging to file for easier debugging
- MSFS Glass now can be launched before the sim, it will try to connect every 5 seconds
- **Maplibre GL JS is the new map framework instead of Leaflet**
- Optimized performance by simplifying SimVar getting and setting. The number of variables we get from the Sim is not affecting the performance anymore. The UI now subscribes for data, that arrives periodically (quicker than before for important data, and maybe slower for not so important). Furthermore, MSFS will now only send data if it has changed in the simulator. We store the data locally in the backend, so the UI/API does not need to wait for the simulator. (This can cause late/missed data though, but we are more okay with that than UI freezes.)
- Cleaned up unnecessary async operations
- Reduced global variable usage
- Cleaned up multithreading. Current implementation runs on 3 threads:
  - Simconnect library Callback function
  - Simconnect client code for interacting with the frontend
  - Webserver
- Resolved a memory leak during getting SimVars
- Cleand up and unified logging for easier debugging
- Small UI fixes
- Small fixes for Simconnect library
- Code reformatting and clean-up
- **Major frontend revamp**
- **Automatic UI selection for the (supported) selected plane**
- Supports 17 airplanes with tailored UIs
- Paid 3rd party aircraft support removed due to the removal of MobiFlight. Might get re-added later if they become available on Marketplace & InputEvents/LVars can be used to control them

## Requirements
 - [Microsoft Visual C++ 2015 Redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170#latest-microsoft-visual-c-redistributable-version)
 - Make sure your PC and your mobile device are connected to the same local network and that your home network is set to *Private* in your Network Profile settings. You can find a short guide on how to set your network to private [here](https://support.microsoft.com/en-us/windows/make-a-wi-fi-network-public-or-private-in-windows-10-0460117d-8d3e-a7ac-f003-7a0da607448d). 
 - You may need to register on the webpage of [OpenAIP](https://www.openaip.net/) to access the aviation layer. After registering, you can go to the [API Clients](https://www.openaip.net/user/api-clients) page and create a new one. You need to copy the API key and put it in your `config.ini` as `openaipapikey = [OpenAip API key here]`


## How do I install MSFS Glass?
1. Download the latest build [here](https://github.com/fzsombor/MSFS-Glass/releases) to the PC where you run MSFS 2024
2. Unzip it to the location of your choice on your computer. Make sure that the glass_server_2.0.0_beta.exe and the config.ini files are in the same folder.

## How do I run MSFS Glass?
**Don't install the app on your mobile device. Download and run it on your PC.   This creates a local web server to which you connect from your mobile device via an IP address.**
1. Open the **config.ini** file, that you’ve unzipped together with the glass_server_2.0.0_beta.exe and this guide, and change the `msfsbasedir` to reflect your Microsoft Flight Simulator installation folder. Hint:
   - MS Store users: C:\Users\\_YOURUSERNAME_\AppData\Local\Packages\Microsoft.Limitless_8wekyb3d8bbwe
2. You may 
2. Run glass_server_2.0.0_beta.exe & start Microsoft Flight Simulator that
   - A Microsoft Defender security window may open when launching glass_server_2.0.0_beta.exe for the first time. Allow the "unrecognized app" to run. Additionally, a Windows Security Alert Window may open when you launch glass_server_2.0.0_beta.exe for the first time. Allow private network access for glass_server_2.0.0_beta.exe in the Windows Security Alert Window.
3. A command line window will open that will give you instructions on the IP-address where you can access the MSFS Glass. Don't close the command line window.
4. Open the IP-address in your mobile device's web browser. The IP address will most likely be something like `192.168.xxx.yyy:4000`.

*Note: You can launch MSFS Glass directly from your PC's browser. In that case, just type in localhost:4000 in your browser's url bar.* 

## Troubleshooting
If you encounter any issue feel free to contact me, or open a [GitHub issue](https://github.com/fzsombor/MSFS-Glass/issueshttps://github.com/fzsombor/MSFS-Glass/issues) or [discussion](https://github.com/fzsombor/MSFS-Glass/discussions). 
You can help in the troubleshooting by enabling `debug` level logging in the application:
1. Open the `config.ini` file at the location of MSFS Glass
2. Change `loglevel` to `debug`
3. Add the line `logfile = glass.log` to your configurations
4. Upload the contents of your log file
5. Make sure to disable debug level logging if you are done, it can affect performance

## Known issues
- G1000 Range and FMS knobs are only working if they remain unchanged within the sim. (Their inputEvents always return 0 upon change which is an MSFS/SimConnect bug, so they are implemented with a clumsy workaround that stores their value in the application & are not synced with the sim.)
- MSFS 2024 flight plan files have changed, the flight plan is present in a separate .PLN file and not the .FLT file, so the flight path is not displayed on the map. Only the 1st waypoint based on the GPS. I plan to add this feature, but an ICAO facility lookup needs to be implemented as the Lat/Lon information is not displayed anymore in the flightplan, only ICAO codes.
- Unfortunately, I had to remove KML support for now, Maplibre is not displaying the custom graphics one can put in KML files.
- Airplane and avionics in MSFS 2024 have been created by multiple dev teams, the behavior of these is really different, so feature parity between the different planes is impossible.
- Map controls are limited when in follow mode, zoom, rotate, align to North will only work for 0.2s and then suddenly stops. This is due to how the plane icon is refreshed, which is a blocking operation for the map.
- MSFS 2020 connection might work for some extent, but it is not tested.
- Xbox support is not possible due to the lack of SimConnect SDK in the Xbox release

## Credits
MSFS Glass is based on the [MFSS Mobile Companion App](https://github.com/mracko/MSFS-Mobile-Companion-App) that is a fork of [Python-SimConnect](https://pypi.org/project/SimConnect/) project. The original Flask webapp implementation done by the [MSFS-2020 Cockpit Companion](https://github.com/hankhank10/MSFS2020-cockpit-companion).


## Donation
If you like this tool and would like to support the development, please consider donating by clicking on the link below. The idea is to implement as many MSFS planes as possible, so I plan to use this as a fund to purchase payware aircraft or the Aviator Edition of the game and incorporate them in this tool. Whether you can support the development or not, please feel free to share what planes or features you would like to see in MSFS Glass.

[![donate_paypal.png](static/img/donate_paypal.png)](https://www.paypal.com/donate/?hosted_button_id=JQ36HM86VSNYE)

Happy flying!
