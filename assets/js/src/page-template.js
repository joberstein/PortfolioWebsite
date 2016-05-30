/**
 *  =======================
 *    page-template.js
 *  =======================
 *
 *  Loads page elements that appear on all pages:
 *  	- Header fragment, and then applies event handlers to the nav links.
 *  	- Footer fragment which appears at the bottom of each page.
 */

var $currentPage,
    selectedClass = "selected",
    navLinkSelector = ".link";

$("header").load("../assets/html/fragments/_header.html", function() {
    var splitUrl = window.location.href.split("/"),
        pageName = splitUrl[splitUrl.length - 2];

    $.each( $(navLinkSelector), function(index, val) {
        if ($(val).text().toLowerCase() === pageName.toLowerCase()) {
            $(val).addClass(selectedClass);
            $currentPage = $(val);
        }
    });
});

$("footer").load("../assets/html/fragments/_footer.html");

window.onbeforeunload = function() {
    if ($currentPage) {
        $currentPage.removeClass(selectedClass);
    }
};
