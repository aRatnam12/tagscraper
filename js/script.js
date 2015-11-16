$(document).ready(function() {
  console.log('working');

  $('#submit').click(function() {
    var $webpage = $('#webpage').val();
    console.log($webpage);
    //$.post('/', $webpage, function(response){
      //console.log(response);
    //});
  });
});