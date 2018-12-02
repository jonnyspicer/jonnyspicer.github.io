document.addEventListener("DOMContentLoaded", function(event) {

  // Mobile hamburger menu
  document.querySelector('.hamburger').addEventListener('click', function(event){
    document.querySelector('.hamburger').classList.toggle('is-active');
    document.querySelector('.desktop-nav').classList.toggle('expanded');
  });

  // Archive accordions
  var leaves = document.querySelectorAll('.accordion-title');
  for(var i = 0; i < leaves.length; i++){
    leaves[i].addEventListener('click', function(event){
      this.classList.toggle('accordion-title-display');
      this.nextElementSibling.classList.toggle('accordion-leaf-display');
    })
  }

});
