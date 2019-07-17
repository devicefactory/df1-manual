[BluKii](http://www.blukii.com/en/bts.php)
------------------------------------------

* similar to our first device
* their mention of 8051 core implies they are using the same TI cc2540 chip
* their accelerometer goes up to 16g (ours 8g)
* they have some DSP event functionality, but not as many as ours
  - we have tap and high-filtered shake events in addition to freefall or motion
* same battery cr2032
* LED is only green and red
* 22mm diameter, 7mm height
* their devkit is around 200 euros (expensive!)
* full suite of software examples


[Node+](http://variableinc.com/product/ios-platform-node/)
----------------------------------------------------------

* similar to our second device with 9-axis
* their sensors are modular, swappable - the main differentiating factor
* device looks a bit chunky though
* USB for both charging and data comm
* 16MByte flash for storage
* Claims output transformations like Quaternion, Yaw/Pitch/Roll - this implies they have beefier processor onboard with enough computing power to do matrix manipulations
* their motion sensor specs look similar to MPU-9150 (same one as ours)
* full suite of software examples, even Android API is there
* starting price is at $100


[Honorable mention:DJI](http://www.dji.com/)
--------------------------------------------

* just an amazing product.
* would love to work on a project with this kind of complexity in the future


Take-aways
----------

* Our platform route already has good competition, but it's not crowded yet
* Price point will be important. We need to go sub-100 and offer similar functionality.
* Nice documentation and software examples will be uber-important
* I think these products are slick, but I do feel like we can pull off something comparable or better.
  - we can get their products and learn from their platform, and improve it


[BLE Mini](http://redbearlab.com/blemini/)
------------------------------------------

* just BLE interface board that needs to be controlled via UART
* targets users who'd like to use it as module to talk BLE 
* uses cc2540 just as radio controller flashed with network processor firmware
* not very interesting.


[Coin](https://github.com/CoinApps/arduino-ble-dev-kit/wiki)
------------------------------------------------------------

* cc2540 + atmega328au development board, but looks like DIY
* also targets arduino users, but now the board contains both the arduino compatible mcu and cc2540
* no certification, hobby project?


[Cortado](https://launch.punchthrough.com/)
-------------------------------------------

* the most interesting of the bunch
* they first developed the BLE app called lightBlue. (pretty popular)
* then they designed a BLE module and went for modular certification with BOTH FCC, CE
* created an open source board much like "Coin" above, but much better software and features
* what's really cool about Cortado is that they send the compiled arduino program over BLE to flash the atmega chip.


[Estimote](http://estimote.com/)
--------------------------------

* just raised over 3.1M
* it's just BLE advertising. It does nothing but exposes specific major and minor ID's of the thing you want to identify
* the app does all the work. Upon retrieving the associated ID, it can give context-aware information to the user
* this is the market NFC wanted to target, and it's getting marginalized by BLE
* uses Nordic nRF51822 + accelerometer
* apple introduced iBeacon, which gave Estimote a boost. You can read about it here:
http://gigaom.com/2013/09/10/with-ibeacon-apple-is-going-to-dump-on-nfc-and-embrace-the-internet-of-things/
http://makezine.com/2014/01/03/reverse-engineering-the-estimote/  (Sandeep co-authored)
* device like Estimote does not give any access to the attached accelerometer
* in fact, BLE devices with pre-flashed firmware limits the user interaction with the hardware pretty significantly

I'd keep an eye on Cortado and the punchthrough design company. 
Interestingly enough, most of these products use cc2540.
And the ones that use cc2540 are just used as radio-only module. 
There does not seem to be any application logic built directly into cc2540.


Takeaways
---------

* We can create a device that exposes lots of useful UUIDs (BLE services) to the user
* where development kits are too barebones, we bring more finished product to market
* where finished products are too restrictive on their BLE usage, we open it up to give better access to underlying hardware


[Moov](http://preorder.moov.cc/)
--------------------------------

* wow. almost exactly what we had in mind, not to mention the name


[Fin](http://www.indiegogo.com/projects/fin-wearable-ring-make-your-palm-as-numeric-keypad-and-gesture-interface)
-----------------------------------------------------------------------------------------------------------------

* don't think they any any prototype yet
* gesture recognition

[Gecko](http://www.indiegogo.com/projects/gecko-make-your-smart-phone-smarter)
------------------------------------------------------------------------------

* these guys do have a prototype
* gesture recognition


[Ring](https://www.kickstarter.com/projects/1761670738/ring-shortcut-everything)
--------------------------------------------------------------------------------

* raised near 800k.
* impressive product - gesture recognition done right.
* It must be using accelerometer and gyro. I wonder what the power consumption is like
* The gesture tracking looks smooth... how much data can they transmit over BLE? Perhaps the data is interpolated on the central side?


[Pebble Bee](https://www.kickstarter.com/projects/192833321/pebblebee-the-most-versatile-ios-android-bluetooth?ref=live)
------------------------------------------------------------------------------------------------------------------------

* darn these guys totally beat us to it. They have multiple variants. One of them already has 9-axis
* price point is insane. $40 bucks for 9-axis one.
* check the PCB design. The cutout for the battery, resulting in crescent moon-shaped board.
* Qi wireless charging too???


[XY](https://www.kickstarter.com/projects/xyfindit/xy-the-secure-tracking-tag)
------------------------------------------------------------------------------

* smells and looks like [Tile](http://www.thetileapp.com/).


[Tile](http://www.thetileapp.com/)
----------------------------------

* they had good media coverage
* but treating the device as "disposable"? c'mon.


[Shine](http://www.misfitwearables.com/)
----------------------------------------

* prettiest and most polished device so far.
* they had 800k funding from indiegogo.
* worth a read: sparkfun's [teardown](https://learn.sparkfun.com/tutorials/teardown-misfit-shine/all) of the device.
* looks like their strategy is to place the algorithms inside of [gecko arm M3](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/3/EFM32LG295.pdf) chip.
* cc2541 is used for BLE, but doesn't looks like it's used for realtime accelerometer data transimission. Used only for sync-ing.
* [their accelerometer](https://cdn.sparkfun.com/assets/learn_tutorials/2/1/3/CD00274221.pdf) has ultra low power capabilities, but is not as feature rich as ours.


[DropCam](https://www.dropcam.com/)
-----------------------------------

* adds BLE monitoring to the camera with computer vision tech.
* BLE tabs are placed on door or windows to alert the camera of movement.
* Combine the in-house movement monitoring with image recognition algorithms on the cam.
* It's the realization of the door alarm idea we had with DF1.


[iFind](https://www.kickstarter.com/projects/yuansong84/ifind-the-worlds-first-battery-free-item-locating)
----------------------------------------------------------------------------------------------------------

* claims battery free operation with physical device dimensions 32 x 27 x 2.4mm.
* even if RF induction can generate sufficient power for BLE, I doubt it can be realized in that form-factor.
* should be interesting to see how this one pans out.
