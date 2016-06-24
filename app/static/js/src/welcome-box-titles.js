/**
 * On hover, shows the title for the the current element.
 */

$(".page-link-boxes").find("img").hover(function() {
    var pageTitle = $(this).parents(".box").children(".page-link-title");
    var newWidth = $(this).parent().css("width");
    $(pageTitle).slideDown(200);
    $(pageTitle).css("width", newWidth);
}, function() {
    var pageTitle = $(this).parents(".box").children(".page-link-title");
    $(pageTitle).slideUp(200);
});