

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


function popupfunc() {
    var btn = document.getElementById("popup");
    btn.classList.toggle("show");
}

