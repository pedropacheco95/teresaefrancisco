var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
    showSlides(slideIndex += n);
}

function currentSlide(element) {
    showSlides(slideIndex = parseInt(element.getAttribute('value')));
}

function showSlides(n) {
    var i;
    var slides = document.getElementsByClassName("mySlides");
    var dots = document.getElementsByClassName("demo");
    if (n > slides.length) {slideIndex = 1}
    if (n < 1) {slideIndex = slides.length}
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    if (slides[slideIndex-1]){
        slides[slideIndex-1].style.display = "block";
    }
    if (dots[slideIndex-1]){
        dots[slideIndex-1].className += " active";
    }
}
