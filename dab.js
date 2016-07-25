$(document).ready( function() {

  function displayTime() {
    var currentTime = new Date();
    var hours = currentTime.getHours();
    var minutes = currentTime.getMinutes();
    var ampm = hours >= 12 ? 'pm' : 'am';
     hours = hours % 12;
     hours = hours ? hours : 12; // the hour '0' should be '12'
     minutes = minutes < 10 ? '0'+minutes : minutes;

    var clockDiv = document.getElementById('clock');

    clockDiv.innerText = hours + ":" + minutes + " " + ampm;

  }

  displayTime();
  setInterval(displayTime, 1000);

});
