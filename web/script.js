function getDomain(url, subdomain) {
  subdomain = subdomain || false;
  url = url.replace(/(https?:\/\/)?(www.)?/i, '');
  if (!subdomain) {
      url = url.split('.');
      url = url.slice(url.length - 2).join('.');
  }
  if (url.indexOf('/') !== -1) {
      return url.split('/')[0];
  }
  return url;
}
function ValidURL(str) {
    var regex = /(?:https?):\/\/(\w+:?\w*)?(\S+)(:\d+)?(\/|\/([\w#!:.?+=&%!\-\/]))?/;
    if(!regex.test(str)) {
        document.getElementById("p1").innerHTML = '';
        document.getElementById("error").innerHTML = 'Please make sure that you have entered the abbreviated form correctly';
        document.getElementById("search_box").style.borderColor = '#FF4B4B';
        document.getElementById("search_box").style.boxShadow = '0 0 10px #FB2F2F';
        document.getElementById("destination").innerHTML = ''
        document.getElementById("dest").innerHTML = '';
        document.getElementById("source").innerHTML = '';
        document.getElementById("sourcetext").innerHTML = "";
        document.getElementById("source").innerHTML = '';
        document.getElementById("sourcedomaintext").innerHTML = "";
        document.getElementById("sourcedomain").innerHTML = '';
        document.getElementById("destdomaintext").innerHTML = '';
        document.getElementById("destdomain").innerHTML = '';
      return false;
    } else {
      return true;
    }
  }
var input = document.getElementById("input_box");
input.addEventListener("keypress", function(event) {
    var url = input.value;
    if (event.key === "Enter") {
        if (ValidURL(url) === true) {
            document.getElementById("error").innerHTML = '';
            document.getElementById("search_box").style.borderColor = 'none';
            document.getElementById("search_box").style.boxShadow = 'rgba(0, 0, 0, 0.20) 0px 5px 15px 0px';
            document.getElementById("p1").style.color = "";
            document.getElementById("p1").innerHTML = '';
            document.getElementById("destination").innerHTML = ""
            document.getElementById("dest").innerHTML = '';
            document.getElementById("sourcetext").innerHTML = "";
            document.getElementById("source").innerHTML = '';
            document.getElementById("sourcedomaintext").innerHTML = "";
            document.getElementById("sourcedomain").innerHTML = '';
            document.getElementById("destdomaintext").innerHTML = "";
            document.getElementById("destdomain").innerHTML = ''
            document.getElementById("wait").src = './wait.gif';
            document.getElementById("load").innerHTML = 'Loading ...';
            axios.get('https://stormapi-v1.herokuapp.com/api/?url=' + url)
            .then(function (response) {
              document.getElementById("wait").src = '';
              document.getElementById("load").innerHTML = '';
              document.getElementById("error").innerHTML = '';
              document.getElementById("search_box").style.borderColor = 'none';
              document.getElementById("search_box").style.boxShadow = 'rgba(0, 0, 0, 0.20) 0px 5px 15px 0px';
              document.getElementById("p1").style.color = "#000000";
              document.getElementById("p1").innerHTML = url.toUpperCase();;
              document.getElementById("destination").innerHTML = "Destination URL"
              document.getElementById("dest").innerHTML = response.data;
              document.getElementById("sourcetext").innerHTML = "Source URL";
              document.getElementById("source").innerHTML = url;
              document.getElementById("sourcedomaintext").innerHTML = "Source Domain";
              document.getElementById("sourcedomain").innerHTML = getDomain(url, true);
              document.getElementById("destdomaintext").innerHTML = "Destination Domain";
              document.getElementById("destdomain").innerHTML = getDomain(response.data, true);
        })
        }
        }
});
