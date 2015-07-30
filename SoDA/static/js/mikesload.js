//Loading the html pages instead of django 
$( document ).ready(function() {
    function init(){
        $( '#main' ).load( 'main.html', function(){
                $( '#main_button' ).addClass('active');
                $( '#infobox' ).html($( '#main' ).html()).hide().show();
                $( '#infobox' ).attr('linked', '#main');
        });
        $( '#projects' ).load('projects.html');
        $( '#legacy' ).load('legacy.html');
        $( '#users' ).load('users.html');
        $( '#calendar' ).load('calendar.html');
        $( '#main_button' ).attr('linked', '#main');
        $( '#projects_button' ).attr('linked', '#projects');
        $( '#legacy_button' ).attr('linked', '#legacy');
        $( '#users_button' ).attr('linked', '#users');
        $( '#calendar_button' ).attr('linked', '#calendar');
    };
    init();
    $('#menu li').click(function(){
        if ($(this).attr('linked') != $( '#infobox' ).attr('linked')){
            $( '#infobox' ).html($($(this).attr('linked')).html());
            $('#menu li').removeClass('active');
            $('#' + $(this).attr('id')).addClass('active');
            $( '#infobox' ).attr('linked', $(this).attr('linked'));
            $( '.carousel' ).carousel(); //hacky fix, this toggles the carousel manually when the user clicks the menu button since it doesn't run automatically
        }
    });
});
