// Parameters: unlockedState and lockedState
// These parameters are in microseconds.
// The servo pulse determines the degree
// at which the horn is positioned. In our
// case, we get about 100 degrees of rotation
// from 1ms-2.2ms pulse width. You will need
// to play with these settings to get it to
// work properly with your door lock
//
// Parameters: motorPin
// The GPIO pin the signal wire on your servo
// is connected to
//
// Parameters: buttonPin
// The GPIO pin the signal wire on your button
// is connected to. It is okay to have no button connected
//
// Parameters: ledPin
// The GPIO pin the signal wire on your led
// is connected to. It is okay to have no ledconnected
//
// Parameter: blynkToken
// The token which was generated for your blynk
// project
//
// **************************************** //

class DoorLock {
  constructor() {
    this.unlockedState = 1000;
    this.lockedState = 2200;

    this.motorPin = 14;
    this.buttonPin = 4;
    this.ledPin = 17;

    this.locked = true;

    //Set up Servo
    this.Gpio = require("onoff").Gpio;
    this.motor = new Gpio(this.motorPin, "out");
    // this.button = new Gpio(buttonPin, {
    //   mode: Gpio.INPUT,
    //   pullUpDown: Gpio.PUD_DOWN,
    //   edge: Gpio.FALLING_EDGE
    // });
    // this.led = new Gpio(ledPin, { mode: Gpio.OUTPUT });
  }

  lockDoor(callback) {
    this.motor.writeSync(this.lockedState);
    this.locked = true;
    callback("door locked");

    setTimeout(() => {
      this.motor.unexport();
    }, 1500);
  }
  unlockDoor(callback) {
    this.motor.writeSync(this.unlockedState);
    this.locked = false;
    callback("door locked");

    setTimeout(() => {
      this.motor.unexport();
    }, 1500);
  }
}

module.exports = DoorLock;
