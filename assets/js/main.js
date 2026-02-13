document.addEventListener('DOMContentLoaded',function(){
  // year placeholders
  var y=new Date().getFullYear();
  ['year','year2','year3','year4'].forEach(function(id){var el=document.getElementById(id);if(el)el.textContent=y});

  // mobile nav toggle
  var navToggle=document.getElementById('navToggle');
  var nav=document.getElementById('nav');
  if(navToggle && nav){navToggle.addEventListener('click',function(){nav.classList.toggle('open')})}

  // simple contact form UX
  var form=document.getElementById('contactForm');
  if(form){form.addEventListener('submit',function(e){e.preventDefault();alert('Thanks — your message has been recorded (demo).');form.reset();})}
});
