

sidenav.onscroll = function () { stkyfunc() };

var snheader = document.getElementById("snheader");

var sticky = snheader.offsetTop;

function stkyfunc() {
    if (sidenav.pageYOffset >= sticky) {
        snheader.classList.add("sticky")
    } else {
        snheader.classList.remove("sticky");
    }
}


function popupfunc(event) {
    const currentlyVisible = document.querySelector('.popup .show');
    if (currentlyVisible) {
        currentlyVisible.classList.toggle('show');
    }
    var popup = event.currentTarget.querySelector('.popuptext');
    popup.classList.toggle("show");
}

$(document).on('click', '#print-likes', function (e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '{% url "main:likes" %}',
        data: {
            printid: $('#print-likes').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            action: 'print'
        },
        success: function (json) {
            document.getElementById("like_count").innerHTML = json['result']
            console.log(json)
        },
        error: function (xhr, errmsg, err) {

        }
    });
})

//toggle thumbs down
//function myFunction(x) {
//  x.classList.toggle("fa-thumbs-down");
//}