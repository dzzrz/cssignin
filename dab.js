$(document).ready( function() {

  function displayTime() {
    var currentTime = new Date();
    var hours = currentTime.getHours();
    var minutes = currentTime.getMinutes();
    var meridiem = "AM";
      if (hours > 12) {
        hours = hours - 12;
        meridiem = "PM";
      }

      if (hours === 0) {
        hours = 12;
      }

    var clockDiv = document.getElementById('clock');

    clockDiv.innerText = hours + ":" + minutes + " " + meridiem;

  }

  displayTime();
  setInterval(displayTime, 1000);

});
