//script for hiding and showing cards/posts
$(".card").click(function() {
  console.log("Test");
  $(this).siblings().removeClass("showMe").addClass("hideMe");
  if ($(this).hasClass("hideMe") ) {
  	console.log("if statement invoked")
    $(this).removeClass("hideMe").addClass("showMe").hide().fadeIn(500);
    $(this).find(".mdl-card__actions").css("display", "none");
  }
});

$(document).ready(function() {
  $(".mdl-card__actions").each(function() {
    if ($(this).prop('scrollHeight') === 0) {
      $(this).removeClass(".mdl-card__actions");
    }
  });
});