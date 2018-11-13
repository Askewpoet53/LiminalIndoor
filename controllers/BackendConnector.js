class BackendConnector {
  constructor() {
    this.url = "https://bffb941270be7a5179d6130698ccefd2.balena-devices.com/api";
  }

  ringDoorBell(img, imgName, callback) {
    var axios = require("axios");
    var FormData = require("form-data");

    var data = new FormData();

    data.append("img", img, imgName);

    axios.post(this.url, data).then(response => {
      console.log(response.data);
      callback(response.data);
    });
  }
}

module.exports = BackendConnector;
