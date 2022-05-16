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


sidenav.onscroll = function () { stkyfunc() };

var snheader = document.getElementById('snheader');

var sticky = snheader.offsetTop;

function stkyfunc() {
    if (sidenav.pageYOffset >= sticky) {
        snheader.classList.add('sticky')
    } else {
        snheader.classList.remove('sticky');
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

