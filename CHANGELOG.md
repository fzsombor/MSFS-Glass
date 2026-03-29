# Change Log

**Update 12/22/2025 Version 2.2.0 Changelog:**
- Bumping SDK version to 1.5.7 (SU4)
- Fixing North rotation bug


**Update 06/22/2025 Version 2.1.0 Changelog:**
- **Displaying flight plan on map if available (and next GPS waypoint if not)**
- Running MSFS Glass is now possible without changing into its directory. (Including external launch scirpts like Stream Deck or MSFS EXE.xml)
- Bumping SDK version to 1.4.2 (SU2)
- Updating Python and JS dependencies
- 8.33kHz COM direct input support
- Fixing CORS issues with CDNs
- Fixing B737Max's FMC, now it is using the Captain's FMC instead of the FO.



**Update 03/16/2025 Version 2.0.0-beta Changelog:**
- First binary release to the public
- Adding multiple control profiles for aircraft commonly used in MSFS 2024 career mode
- Refining UI, removing quirks and bugs

**Known issues:**
- G1000 Range and FMS knobs are only working if they remain unchanged within the sim. (Their inputEvents always return 0 upon change which is an MSFS/SimConnect bug, so they are implemented with a clumsy workaround that stores their value in the application & are not synced with the sim.)
- MSFS 2024 flight plan files has changed, the flight plan is present in a separate .PLN file and not the .FLT file, so the flight path is not displayed on the map. Only the 1st waypoint based on the GPS. I plan to add this feature, but an ICAO facility lookup needs to be implemented as the Lat/Lon information is not displayed anymore in the flightplan, only ICAO codes.
- Unfortunately I had to remove KML support for now, Maplibre is not displaying the custom graphics one can put in KML files.
- Airplane and avionics in MSFS 2024 have been created by multiple dev teams, the behavior of these are really different, so feature parity between the different planes is impossible

**Update 01/04/2025 - 03/01/2025 Version 2.0.0-alpha-3 Changelog:**
- Credit where credit is due:
   - [https://github.com/mracko/MSFS-Mobile-Companion-App](https://github.com/mracko/MSFS-Mobile-Companion-App/)
   - [https://github.com/odwdinc/Python-SimConnect](https://github.com/odwdinc/Python-SimConnect)
- Created a new repo due to abandoning the original repos
- Updated DLL and header definitions to the SDK of MSFS2024
- **Rebranding MSFS 2020 Mobile Companion App to MSFS Glass**
- Bumped SimConnect version to SDK 1.2.2
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
- **NO BINARIES HAVE BEEN BUILT FOR THIS VERSION**
- Paid 3rd party aircraft support removed due to the removal of MobiFlight. Might get re-added later if they become available on Marketplace & InputEvents/LVars can be used to control them


**v1.9.1 November 3, 2021:**
- Added controls profile for the Ju-52 Classic and Retrofit by Asobo
- Improved UI for all NAV controls
- Removed pop-up for panel switches
- Added approximate G-forces at touchdown in the Data tab

**v1.9 August 30, 2021:**
- Updated and improved controls profile for FBW's A32NX stable v0.6.3 and development version
- Added feature to upload custom KML files (thanks to @luka97)
- Added ADF 1/2 selector for PMDG's DC-6
- Added feature to hide the plane icon on the map. The lower left map button has 3 states now: "Follow plane" -> "Unfollow plane" -> "Hide plane"

**v1.8.2 July 11, 2021:**
- Added controls profile for the DC-6 by PMDG. Supports NAV, ADF, COM, XPNDR, Gyropilot and the Artificial Flight Engineer.
- Minor UI improvements.

**v1.8.1 June 14, 2021:**
- CPU performance issue hotfix.

**v1.8 June 14, 2021:**
- Added controls profile for the FG-1D Corsair by MilViz.
- Improved UI especially for the default AP and the PA-28R.
- Added ability to read L:vars thanks to https://github.com/Koseng/MSFSPythonSimConnectMobiFlightExtension

**v1.7 May 14, 2021:**
- Added controls profile for MB-339 and Long-EZ by IndiaFoxtEcho.
- Added gear, flaps, spoilers and trim (elevator, rudder and aileron) controls.
- Added press-and-hold button functionality for frequency tune buttons.
- Improved performance for map tracking (fixed jagged lines).
- Fixed logo lights button status being mapped to cabin lights.

**v1.6.1 April 20, 2021:**
- Added controls profile for CRJ-550/700 (Aerosoft). The profile includes controls for FCP, Side Panel, NAV, and COM and introduces press-and-hold button functionality for knobs.
- Updated controls profile for PA-28R (Just Flight) to reflect v0.4.0 changes.
- Fixed zoom when double-tapping on iOS.

**v1.6 March 29, 2021:**
- Added aircraft controls profile selection.
- Added controls profiles for GNS430/530, G1000, A32NX (FBW), and PA-28R (Just Flight).
- Added integration with Mobiflight WASM Event Module.
- Added Data tab with IAS, ALT, HDG data
- Added Sync HDG bug to current heading
- Fixed NAV frequency display UI for iOS (padding for NAV frequency display)

**v1.5.2 Hotfix March 4, 2021:**
- Fixed bug for iOS devices not being able to type in decimal numbers in COM/NAV frequencies.

**v1.5.1 Hotfix February 8, 2021:**
- Fixed Load Flight Plan not working on Steam versions.

**v1.5 February 5, 2021:**
- Added landscape mode (split-screen for map and controls).
- Added option to load your current flight plan.
- Switched active and stand-by NAV/COM displays.

**v1.4 January 6, 2021:**
- Dedicated A320 autopilot controls (tested with default A320 and FBW A32NX v0.5.1).
- Various UI fixes, especially for iOS devices.
- UI improvements for color-blind users.

**v1.3 December 16, 2020:**
- FLC autopilot implemented.
- Added GPS track line for the VFR map.
- Added light controls.
- Added pitot heat and deicing controls (deicing controls may be limited depending on the plane, windshield deicing is not yet supported by SimConnect).

**v1.2 November 20, 2020:**
- Added COM1/2 and transponder.
- Added vertical speed at touchdown.
- Added simulation rate controls.
- Improved stability and performance. Multiple devices/browsers can now connect to the app concurrently.
- Added dark moving map style.
- Fixed default moving map not displaying.
- Various minor bug fixes.

**v1.1 November 11, 2020:**
- Improved AP functionality. ALT AP can now be used with current or set altitude.
- Added autothrottle toggle.
- Added NAV1/NAV2 source switch for AP and/or CDI.
- Added ADF direct frequency tune option.
- Improved UI for the NAV tab.
- The application doesn't crash when launching before MSFS is running.
- Various other minor bug fixes.

**v1.0 November 3, 2020:**
- Initial release.
- Moving Map (Open Street Maps).
- NAV 1 frequency and OBS 1 selection.
- NAV 2 frequency and OBS 2 selection.
- ADF frequency and ADF card selection.
- Autopilot with altitude, vertical speed, and airspeed settings.
- Gyro drift and altimeter pressure settings.
