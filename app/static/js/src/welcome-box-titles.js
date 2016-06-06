/**
 * On hover, shows the title for the the current element.
 */

$(".page-link-boxes .box a img").hover(function() {
    var pageTitle = $(this).parents(".box").children(".page-link-title");
    $(pageTitle).slideDown(200);
    $(pageTitle).css("display", "table");
}, function() {
    var pageTitle = $(this).parents(".box").children(".page-link-title");
    $(pageTitle).slideUp(200);
});