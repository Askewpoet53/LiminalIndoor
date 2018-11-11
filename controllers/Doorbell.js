class Doorbell {
  constructor() {
    this.play = require("audio-play");
    this.load = require("audio-loader");
  }

  ring() {
    this.load("./Data/doorbell/ring.mp3").then(this.play);
  }
}
module.exports = Doorbell;
