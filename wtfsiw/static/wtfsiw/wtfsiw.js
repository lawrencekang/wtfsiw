$( document ).ready(function() {
// Attach event listener
  $(document.body).on('click', 'div.noGo', function(){
    console.log('clicked');
    var nextLoc = generateNextLoc();
    var dataToSend = {
      userAddress:localStorage.getItem('userAddress'),
      randomLoc: nextLoc
    };

    $.get('/wtfsiw/results/', dataToSend, function(data){
      $('div.app').html(data);
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
  $.ajax({
    type: 'POST',
    url: '/wtfsiw/',
    data: position,
    success: function(result){
      if (result === null)
        {return "null, yo. something wrong with your address - try searching again.";}
      result = JSON.parse(result);
      var userAddress = result[0];
      var yelpResults = result[1];
      /* Save the Yelp API results in localStorage, and randomly generate the first location */
      localStorage.setItem('userAddress', userAddress);
      localStorage.setItem('yelpResults', yelpResults);
      var yelpResultsParsed = JSON.parse(yelpResults);
      var randomIndex = Math.floor(Math.random()*yelpResultsParsed.length);
      var randomLoc = yelpResultsParsed[randomIndex];
      dataToSend = {
        userAddress: userAddress,
        randomLoc: randomLoc
      };
      $.post('/wtfsiw/results/', dataToSend
        // , 
        // function(data){
        // console.log(data);
        // $('div.app').html(data);}
        );
    },
    error: function(error){
      console.log(error);
    }
  });
}

getLocation();

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




