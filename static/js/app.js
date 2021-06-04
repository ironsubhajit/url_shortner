$(document).on('submit', '#post-form', function(e){
    e.preventDefault(); // prevent default reloading page

    $.ajax({
        type: 'POST',
        url: '/create',
        data: {
            link: $('#link').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken').val(),
        },
        success: function(data){
            var newUrl = 'https://ur9.herokuapp.com/go/'+data;
            $('#recent').attr("href", newUrl);
            $('#recent').html("https://ur9.herokuapp.com/go/"+data);
        }
    });
});


// funtions for copy functionality
function outFunc() {
  var tooltip = $('.tooltiptext');
  tooltip.text("click to copy");
};

function copyToClipboard(link){

  // Create a dummy input to copy the string array inside it
  var dummy = document.createElement("input");

  // add element before js
  var main_content = $('.content')[0];
  main_content.appendChild(dummy);
  
  // Set its ID
  dummy.setAttribute("id", "dummy_id");
  
  // Output the var into it
  document.getElementById("dummy_id").value = link;
  
    // Select it
  dummy.select();
  
  // Copy its contents
  document.execCommand('copy');

  // Remove it as its not needed anymore
  main_content.removeChild(dummy);
};

function showCopyStatus(link) {
  alert(`Link Copied: ${link}`);
};


$('.clicktocopy').click(function() {
        
    // var link = $(".shortLink");
    var row_id = $(this).attr("id");
    // var row_id = $(event.target)[0].id;
    row_id = `#${row_id}`;

    // generate link id using row no
    var link_id = `#link${row_id.slice(-1)}`;

    var link = $(link_id).attr("href");

    copyToClipboard(link);

    // temp sol. for tooltip
    showCopyStatus(link);

    var tooltip = $('.tooltiptext');
    tooltip.text("Link Copied!");
});


// change input link placeholder with diff screen sizes
var changePlaceholder = function() {
  if ($(window).width() < 555 ) {
    $('#link').attr("placeholder", "L I N K");
  } else {
    $('#link').attr("placeholder", "E N T E R - L I N K");
  }
};

changePlaceholder();