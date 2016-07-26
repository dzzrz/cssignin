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
    var d = new Date();
	  var n = d.getHours();
	  if (n > 19 || n < 6)
	  // If time is after 7PM or before 6AM, apply night theme to ‘body’
	   document.body.className = "night";
	  else if (n > 16 && n < 19)
	  // If time is between 4PM – 7PM sunset theme to ‘body’
	   document.body.className = "sunset";
	  else
	  // Else use ‘day’ theme
	   document.body.className = "day";
});
