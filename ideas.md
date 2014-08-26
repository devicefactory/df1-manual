# Motivating Ideas

* Rpi Motion Logger

  Stick a DF1 under a chair, record stream of data for events and answer questions like:
  - how often do you stand up
  - do you shake your legs when you are sitting down? how long?
  - can you infer how many bathroom breaks?

* iOS proximity triangulation

  Similar to estimote beacons, but can we do better?
  If you knew devices located in strategic places indoors, can you triangulate the exact position of your iphone by RSSI signals from multiple devices?

* BLE controlled robot

  How about node.js on rasperry pi hooked up to bunch of servos?
  You can make df1 into a BLE remote controller for a robot powered by DF1.

* Data analysis 1, motion classification

  Given 5Hz data, can you differentiate walking versus running?
  Walking up the stairs versus walking down stairs?
  Sitting down versus sitting up?
  If not feasible using 5Hz, how would be the minimum required frequency to detect this?
  Part of the work will involve writing a data logger that can stream bursts of relevant data to the remote receiver.
  The data needs to be first labelled with corresponding action. 
  Supervised learning methods can be trained on the data, and subsequently tested on out-of-sample data.

* Data analysis 2, acceleration, velocity, and distance

  Given a starting position, can you interpolate the acceleration values to calculate the final position of the device?
  Is it feasible to do this without Gyroscope data?

* Object orientation renderer

  Track the orientation of an object by attaching DF1's to it. For example, attach it on a doll.
  As you move the doll, track its euclidean vector position of the gravity with respect to the orientation of the accelerometer chip.
  Using packages like OpenGL, show the 3d rendered image that tracks such orientation.

* phone controller

  Associate tap events as an event on iPhone, such as vibrating the phone or even taking a photo.
  Associate sequence of taps for more set of events.
  For example, make the phone learn the sequence of taps. If similar tap pattern is detected, trigger a configured event.
  Freefall and shake accelerometer events can also be used.

* BLE Synchronized of LED's

  kLED's on DF1 can be toggled via UUID. Can a BLE central connect to multiple DF1's to create nice LED patterns?
  kTODO for me: support PWM on LED toggles.


