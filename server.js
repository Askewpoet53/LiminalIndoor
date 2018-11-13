var express = require('express');
var app = express();


var Camera = require("./controllers/Camera");
var Doorbell = require("./controllers/Doorbell");

var cam = new Camera();
var bell = new Doorbell();

// app.use(express.statis('Data/img'))

// reply to request with "Hello World!"
app.get('/', function (req, res) {
  console.log("hello")
  res.sendFile('img.jpg');
  
});

//Camera module hangs 

app.get("/capture", (req, res) => {
  cam.captureImage(imgCaptured => {
    if (imgCaptured) {
      res.send("img Captured");
    } else {
      res.send("img not captured");
    }
  });
});

app.get("/ring", (req, res) => {
  bell.ring();
  res.send("hopefully the doorbell rang");
});


//start a server on port 80 and log its start to our console
var server = app.listen(80, function () {

  var port = server.address().port;
  console.log('Example app listening on port ', port);

});
