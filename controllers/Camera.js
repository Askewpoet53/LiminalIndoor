class Camera {
  captureImage(callback) {
    var PiCamera = require("pi-camera");

    var camera = new PiCamera({
      mode: "photo",
      output: `./img.jpg`,
      width: 640,
      height: 480,
      nopreview: true
    });

    camera
      .snap()
      .then(result => {
        //Img captured
        callback(true);
      })
      .catch(error => {
        // Handle your error
        callback(false);
      });
  }
}
module.exports = Camera;
