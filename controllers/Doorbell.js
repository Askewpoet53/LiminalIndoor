class Doorbell {
  constructor() {
    this.play = require("audio-play");
    this.load = require("audio-loader");
  }

  ring() {
    var sys = require("sys");
    var exec = require("child_process").exec;
    // this.load("./Data/doorbell/ring.mp3").then(this.play);
    
    
  }
}
module.exports = Doorbell;
