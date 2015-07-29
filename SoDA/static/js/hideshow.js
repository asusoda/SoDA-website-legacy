//script for hiding and showing cards/posts



$(document).ready(function() {
  $(".card").first().removeClass("hideMe").addClass("showMe");
  $(".card").click(function() {
    $('.showMe').not(this).each(function() {
      $(this).removeClass("showMe").addClass("hideMe");
    });
    if ($(this).hasClass("hideMe") ) {
      $(this).removeClass("hideMe").addClass("showMe").hide().fadeIn(500);
   
    }

  });
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