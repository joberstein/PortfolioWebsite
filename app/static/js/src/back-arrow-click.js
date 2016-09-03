/**
 * Goes back to the previous page on click.
 */

$(".back-row").click(function() {
   location.reload();
   $('html, body').animate({ scrollTop: 0 }, 0);
});
