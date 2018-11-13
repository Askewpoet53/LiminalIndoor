class Camera {
  captureImage(callback) {
    console.log("in capture...");
    var PiCamera = require("pi-camera");

    var camera = new PiCamera({
      mode: "photo",
      output: `./Data/imgs/img.jpg`,
      width: 640,
      height: 480,
      nopreview: true
    });

    camera
      .snap()
      .then(result => {
        //Img captured
        console.log("...captured");
        console.log(result);
        callback(true);
      })
      .catch(error => {
        // Handle your error
        console.log("...error");
        console.log(error);
        callback(false);
      });
  }
}
module.exports = Camera;
