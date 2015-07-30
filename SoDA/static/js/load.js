var aboutUsContent;
var announcementsContent;
var calendarContent;
var competitionsContent;
var indexContent;
var sponsorsContent;
var selected;

$(document).ready(function() {

    aboutUsContent = "";
    announcementsContent = "";
    calendarContent = "";
    competitionsContent = "";
    indexContent = "";
    sponsorsContent = "";
    var content = $(".mdl-layout__content").html();
    switch(location.pathname.split("/")[2]) {
        case "":
            indexContent = content;
            selected = "index";
            break;
        case "about-us":
            aboutUsContent = content;
            selected = "about-us";
            break;
        case "announcements":
            announcementsContent = content;
            selected = "announcements";
            break;
        case "calendar":
            calendarContent = content;
            selected = "calendar";
            break;
        case "competitions":
            competitionsContent = content;
            selected = "competitions";
            break;
        case "sponsors":
            sponsorsContent = content;
            selected = "sponsors";
            break;
    }

    window.history.replaceState({"html": content}, "Software Developer's Association @ ASU", location.pathname);

});

window.onpopstate = function(e) {
    if (e.state) {
        $(".mdl-layout__content").html(e.state.html);
    }
};

$("#index_navbutton").click(function (e) {
    e.preventDefault();
    if (selected !== "index") {
        if (indexContent === "") {
            $.get("/", function (pageContent) {
                var elements = $(pageContent);
                indexContent = $(".mdl-layout__content", elements).html();
                $(".mdl-layout__content").html(indexContent);
                history.pushState({"html": indexContent}, "Software Developer's Association @ ASU", "/");
            });
        }
        else {
            $(".mdl-layout__content").html(indexContent);
            history.pushState({"html": indexContent}, "Software Developer's Association @ ASU", "/");
        }
        selected = "index";
    }
});

$("#about_us_navbutton").click(function (e) {
    e.preventDefault();
    if (selected !== "about-us") {
        if (aboutUsContent === "") {
            $.get("/post/about-us", function (pageContent) {
                var elements = $(pageContent);
                aboutUsContent = $(".mdl-layout__content", elements).html();
                $(".mdl-layout__content").html(aboutUsContent);
                history.pushState({"html": aboutUsContent}, "Software Developer's Association @ ASU", "/post/about-us");
            });
        }
        else {
            $(".mdl-layout__content").html(aboutUsContent);
            history.pushState({"html": aboutUsContent}, "Software Developer's Association @ ASU", "/post/about-us");
        }
        selected = "about-us";
    }
});

$("#announcements_navbutton").click(function (e) {
    e.preventDefault();
    if (selected !== "announcements") {
        if (announcementsContent === "") {
            $.get("/post/announcements", function (pageContent) {
                var elements = $(pageContent);
                announcementsContent = $(".mdl-layout__content", elements).html();
                $(".mdl-layout__content").html(announcementsContent);
                history.pushState({"html": announcementsContent}, "Software Developer's Association @ ASU", "/post/announcements");
            });
        }
        else {
            $(".mdl-layout__content").html(announcementsContent);
            history.pushState({"html": announcementsContent}, "Software Developer's Association @ ASU", "/post/announcements");
        }
        selected = "announcements";
    }
});

$("#calendar_navbutton").click(function (e) {
    e.preventDefault();
    if (selected !== "calendar") {
        if (calendarContent === "") {
            $.get("/post/calendar", function (pageContent) {
               var elements = $(pageContent);
                calendarContent = $(".mdl-layout__content", elements).html();
                $(".mdl-layout__content").html(calendarContent);
                history.pushState({"html": calendarContent}, "Software Developer's Association @ ASU", "/post/calendar");
            });
        }
        else {
            $(".mdl-layout__content").html(calendarContent);
            history.pushState({"html": calendarContent}, "Software Developer's Association @ ASU", "/post/calendar");
        }
        selected = "calendar";
    }
});

$("#competitions_navbutton").click(function (e) {
    e.preventDefault();
    if (selected !== "competitions") {
        if (competitionsContent === "") {
            $.get("/post/competitions", function (pageContent) {
               var elements = $(pageContent);
                competitionsContent = $(".mdl-layout__content", elements).html();
                $(".mdl-layout__content").html(competitionsContent);
                history.pushState({"html": competitionsContent}, "Software Developer's Association @ ASU", "/post/competitions");
            });
        }
        else {
            $(".mdl-layout__content").html(competitionsContent);
            history.pushState({"html": competitionsContent}, "Software Developer's Association @ ASU", "/post/competitions");
        }
        selected = "competitions";
    }
});

$("#sponsors_navbutton").click(function (e) {
    e.preventDefault();
    if (selected !== "sponsors") {
        if (sponsorsContent === "") {
            $.get("/post/sponsors", function (pageContent) {
               var elements = $(pageContent);
                sponsorsContent = $(".mdl-layout__content", elements).html();
                $(".mdl-layout__content").html(sponsorsContent);
                history.pushState({"html": sponsorsContent}, "Software Developer's Association @ ASU", "/post/sponsors");
            });
        }
        else {
            $(".mdl-layout__content").html(sponsorsContent);
            history.pushState({"html": sponsorsContent}, "Software Developer's Association @ ASU", "/post/sponsors");
        }
        selected = "sponsors";
    }
});