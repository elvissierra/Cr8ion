

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

