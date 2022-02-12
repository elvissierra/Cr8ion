function popupfunc(event) {
    const currentlyVisible = document.querySelector('.popup .show');
    if (currentlyVisible) {
        currentlyVisible.classList.toggle('show');
    }
    var popup = event.currentTarget.querySelector('.popuptext');
    popup.classList.toggle("show");
}


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

likebutton.onclick = function () { clickfunc() };

var likebutton = document.getElementById('likebutton');

var fire = likebutton.clicked;

function clickfunc() {
    if (likebutton.clicked) {
        likebutton.classList.toggle('fire');
    } else {
        likebutton.classList.toggle('fire')
    }
}

