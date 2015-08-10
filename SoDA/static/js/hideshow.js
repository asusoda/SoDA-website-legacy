//script to expand and hide cards 
$(document).ready(function() {
 $('.hideMe').first().removeClass('hideMe').addClass('showMe');
 $('.mdl-button').first().addClass('dontShow');
  $(".mdl-button").click(function() { 
    $('html,main').animate({scrollTop: $(this).parent().siblings('.mdl-card__media').offset().top},1000);
    $(".mdl-button").parent().siblings('.mdl-card__supporting-text').children('.showMe').not(this).each(function() {
      $(".mdl-button").parent().siblings('.mdl-card__supporting-text').children('.showMe').removeClass("showMe").addClass("hideMe");
      $(".mdl-button").removeClass('dontShow');
    });
    if($(this).parent().siblings('.mdl-card__supporting-text').children('.hideMe').length) {
      $(this).parent().siblings('.mdl-card__supporting-text').children('.hideMe').removeClass('hideMe').addClass('showMe');
      $(this).addClass('dontShow');
    }
  });
})


