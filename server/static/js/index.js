// Uploads the currently selected image to the handler server
// using AJAX calls

// NATIVE JS
$(document).ready(function () {
    alert("Sending request... Press OK to continue.");

    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://localhost:5000/');
    xhr.withCredentials = true;
    xhr.setRequestHeader('Content-Type', 'text/plain');
    xhr.send("This is sent from an AJAX caller.");
    alert(xhr.responseText);
});


// $(document).ready(function () {
//     $.ajax({
//         url: "http://google.com",
//         type: "get",
//         // dataType: "jsonp",
//         contentType: 'application/x-www-form-urlencoded',
//         success: function () {
//             alert("Request sent!");
//         },
//         error: function () {
//             alert("Failed!");
//         }
//     })
// });