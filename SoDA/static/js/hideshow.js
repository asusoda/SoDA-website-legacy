//script for hiding and showing cards/posts
/*
function hideShow() {
  $(".mdl-button").click(function() {
    $(this).parent(".showMe").not(this).each(function() {
      console.log('first show me and rest removed')
      $(this).removeClass("showMe").addClass("hideMe");
    });
    if($(this).parents('.hideMe').length) {
      console.log('remove hide for button press')
      $(this).parent('hideMe').removeClass('hideMe').addClass('showMe').hide.fadeIn(500);
    }
  });
}
*/
$(document).ready(function() {
 console.log('on ready test');
 $('.hideMe').first().removeClass('hideMe').addClass('showMe');
  $(".mdl-button").click(function() { 
    $(".mdl-button").parent().siblings('.mdl-card__supporting-text').children('.showMe').not(this).each(function() {
       $(".mdl-button").parent().siblings('.mdl-card__supporting-text').children('.showMe').removeClass("showMe").addClass("hideMe");
    });
    if($(this).parent().siblings('.mdl-card__supporting-text').children('.hideMe').length) {
      console.log('remove hide for button press');
      $(this).parent().siblings('.mdl-card__supporting-text').children('.hideMe').removeClass('hideMe').addClass('showMe').hide.fadeIn(500);
      $(this).children('.expand').addClass('dontShow');
    }
  });


  /*
  $(".card").first().removeClass("hideMe").addClass("showMe");
  $(".mdl-button").click(function() {
    $('.showMe').not(this).each(function() {
      $(this).removeClass("showMe").addClass("hideMe");
    });
    if ($(this).hasClass("hideMe") ) {
      $(this).removeClass("hideMe").addClass("showMe").hide().fadeIn(500);
   
    }

  }); */
})





/*
$(".card").click(function() {
  
  $(".showMore").css("display", "block");
  $('.showMe').not(this).each(function() {
    $(this).removeClass("showMe").addClass("hideMe");
    $(this).find(".mdl-card__actions").css("display","none");
  });
  if ($(this).hasClass("hideMe") ) {
    $(this).removeClass("hideMe").addClass("showMe").hide().fadeIn(500);
    $(this).find('div').hasClass(".mdl-card__actions").css("display", "none");
  }
});
//removes the find more tag when the card is expanded
$(document).ready(function() {
  $(".mdl-card__actions").each(function() {
    if ($(this).children(".showMe")) {
    	console.log("If past")
      $(this).removeClass(".mdl-card__actions");
    }
  });
}); */