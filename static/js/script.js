$(document).ready(function() {

  $('#submit').click(function(event) {
    event.preventDefault();
    var $webpage = $('#webpage').val();
    var data = {
      url: $webpage
    };
    $.ajax({
      url: "/summary/",
      type: "POST",
      data: {url: $webpage},
      dataType: "json",
      success: function (result) {
        $.each(result, function(key, val) {
          var listItem = $('<li>').appendTo('#summary');
          var tag = $('<a>', {
            id: key,
            text: key + ': ' + val,
            href: ''
          }).appendTo(listItem);
        });
      },
      error: function (xhr, ajaxOptions, thrownError) {
        console.log(xhr, ajaxOptions, thrownError);
      }
    });
  });
  
  $(document).on('click', 'a' , function(event) {
    event.preventDefault();
    console.log(event.target);
  });
});