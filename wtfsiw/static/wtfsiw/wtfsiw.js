$( document ).ready(function() {
// Attach event listener
  $(document.body).on('click', 'div.noGo', function(){
    var nextLoc = generateNextLoc();
    var dataToSend = {
      userAddress:localStorage.getItem('userAddress'),
      random_result: nextLoc
    };
    $.post('/wtfsiw/titleblock_map/', dataToSend, function(data){
      console.log('clicked', data);
      $('.titleblock.map').html(data);
    });
  });
});

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(sendPosition);
    } else {
        console.log("Why you no position?");
    }
}

  // Generate CSRF token for AJAX request below 
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !=='') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

/* Set header on AJAX request */

function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

/* AJAX POST to send HTML5 position to Django server*/
function sendPosition(position) {
  $('#loading').text('looking up a place to work');
  $.post('/wtfsiw/results/', position, function(data){
    document.open();
    document.write(data);
    document.close();
  });
}


// Functions needed for the Results template

var resultsFunc = function(data){

  if (!localStorage.getItem('yelpResults'))
    localStorage.setItem('yelpResults', data.yelpResults);

  if (data.userAdress !== localStorage.getItem('userAddress'))
    localStorage.setItem('userAddress', data.userAddress);

  if (localStorage.getItem('localStorage')){}
};

var generateNextLoc = function(){
  var storedResultsParsed = JSON.parse(localStorage.getItem('yelpResults'));
  var randomIndex = Math.floor(Math.random()*storedResultsParsed.length);
  var randomLoc = storedResultsParsed[randomIndex];

  return randomLoc;
};




