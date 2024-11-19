function popupfunc(event) {
    const currentlyVisible = document.querySelector('.popup .show');
    if (currentlyVisible) {
        currentlyVisible.classList.toggle('show');
    }
}

function popin(){
    var x = document.getElementById('demo');
    if (x.style.display === 'none'){
        x.style.display = 'block';
    } else {
        x.style.display = 'none';
    }
}


var sidenav = document.getElementById('sidenav');
var snheader = document.getElementById('snheader');
if (sidenav && snheader)
    sidenav.onscroll = function () {stkyfunc()};
    var sticky = snheader.offsetTop;

sidenav.onscroll = function () { stkyfunc() };

    function stkyfunc() {
        if (sidenav.pageYOffset >= sticky) {
            snheader.classList.add('sticky')
        } else {
            snheader.classList.remove('sticky');
        }
    }

var likebutton = document.getElementById('likebutton');
if (likebuton) {
    likebutton.onclick = function () { clickfunc() };
}
function clickfunc() {
        likebutton.classList.toggle('fire');
    }