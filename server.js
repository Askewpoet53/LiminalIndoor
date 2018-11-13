var express = require("express");
var axios = require("axios");
var app = express();

var Camera = require("./controllers/Camera");
var Doorbell = require("./controllers/Doorbell");
var BackendConnector = require("./controllers/BackendConnector");

var cam = new Camera();
var bell = new Doorbell();
var BackController = new BackendController();
// app.use(express.statis('Data/img'))

// reply to request with "Hello World!"
app.get("/", function(req, res) {
  console.log("hello");
  res.sendFile(__dirname + "/img.jpg");
});

//Camera module hangs

app.get("/capture", (req, res) => {
  
});

app.get("/ring", (req, res) => {
  cam.captureImage((imgCaptured, results) => {
    if (imgCaptured) {
      console.log(resuls);
      // BackController.ringDoorBell()
    } else {
      res.send("Error with camera please try again");
    }
  });
});

//start a server on port 80 and log its start to our console
var server = app.listen(80, function() {
  var port = server.address().port;
  console.log("Example app listening on port ", port);
});
