/**
 * On click, shows a full page about the clicked portfolio piece.
 *
 * Requires the following data attributes:
 *  - index (int) - index of the piece that was clicked
 *  - section (string) - name of the current section
 */

$(".grid-square").click(function() {
    var gridImg = $(this).find("img");
    var index = gridImg.data("index");
    var section = gridImg.data("section");

    $.get("/portfolio/" + section + "/" + index, function( data ) {
        var $section = $(".section-content");
        $section.empty();
        $section.append(data);
        console.log(data);
    });
});