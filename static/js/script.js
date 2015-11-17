$(document).ready(function() {
  console.log('working');

  $('#submit').click(function(event) {
    event.preventDefault();
    var $webpage = $('#webpage').val();
    var data = {
      url: $webpage
    };
    console.log(data);
    $.ajax({
      url: "/url/",
      type: "POST",
      data: {url: $webpage},
      dataType: "json",
      success: function (result) {
        console.log(result);
      },
      error: function (xhr, ajaxOptions, thrownError) {
        console.log(xhr, ajaxOptions, thrownError);
      }
    });
  });
});