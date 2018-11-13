var express = require("express");
var axios = require("axios");
var app = express();
var bodyParser = require("body-parser");

app.use(
  bodyParser.urlencoded({
    extended: false,
    limit: "500mb",
    parameterLimit: 1000000
  })
);

var Camera = require("./controllers/Camera");
var Doorbell = require("./controllers/Doorbell");
var BackendConnector = require("./controllers/BackendConnector");

var cam = new Camera();
var bell = new Doorbell();
var BackController = new BackendConnector();
// app.use(express.statis('Data/img'))

// reply to request with "Hello World!"
app.get("/", function(req, res) {
  console.log("hello");
  res.sendFile(__dirname + "/img.jpg");
});

//Camera module hangs

app.get("/capture", (req, res) => {});

app.post("/ring", (req, res) => {
  console.log(req.body);

  if (req.body.doorID) {
    cam.captureImage(imgCaptured => {
      if (imgCaptured) {
        BackController.ringDoorBell("./img.jpg", "img", result => {
          console.log(result);
          res.send(result);
        });
      } else {
        res.send("Error with camera please try again");
      }
    });
  }else{
    res.send("doorID not found");
  }
});

//start a server on port 80 and log its start to our console
var server = app.listen(80, function() {
  var port = server.address().port;
  console.log("Example app listening on port ", port);
});
