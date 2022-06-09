var contentDivs = document.querySelectorAll(".sliddingDivs, .appearingDivs, .slidingAppearingDivsRight, .slidingAppearingDivsLeft");

window.addEventListener('load', onload);
window.addEventListener('scroll', checkContentDivs,false);

checkContentDivs();

function checkContentDivs() {
    var triggerHeight = window.innerHeight;

    contentDivs.forEach(function(div) {
        var divTop = div.getBoundingClientRect().top;
        if (divTop < triggerHeight) {
            div.classList.add('show');
        } else {
            div.classList.remove('show');
        }
    });
}

function revealMap(element,map_name){
    let map = document.getElementById(map_name);
    map.style.display = 'block';
    element.style.display = 'none';
}

function changeWindowStyle(){
    let window = document.getElementsByTagName('body')[0];
    window.style = 'height: auto!important;overflow-x: hidden!important;'
}

function loadingAnimations(){
    let divs = document.getElementsByClassName('loading_animation');

    for (let div of divs){
        div.classList.add('show');
    }
}

function onload(){
    changeWindowStyle();
    loadingAnimations();
}
