var footerCol = document.querySelector('.footer-col');
var text = footerCol.querySelector('small');

function startScroll() {
  var scrollPosition = 0;
  var scrollInterval = setInterval(function() {
    scrollPosition++;
    if (scrollPosition > text.offsetWidth) {
      scrollPosition = 0;
    }
    footerCol.scrollLeft = scrollPosition;
  }, 15);
}

footerCol.addEventListener('mouseover', function() {
  text.innerHTML = 'Hola profe';
  startScroll();
});

footerCol.addEventListener('mouseout', function() {
    text.innerHTML = '<img src="img/dance-dog.gif" alt="icono" height="30px" width="30px" style="vertical-align: middle;">&copy;<b>Todos los derechos reservados</b>';
    startScroll();
  });

  function mOver(obj) {
    obj.innerHTML = "Hola profe";
    var marquee = obj.querySelector('marquee');
    marquee.start();
  }
  
  function mOut(obj) {
    obj.innerHTML = '<small>&copy;<b>Todos los derechos reservados</b></small>';
    var marquee = obj.querySelector('marquee');
    marquee.start();
  }
