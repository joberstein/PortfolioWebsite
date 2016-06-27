
var portfolioPages = ["apps", "animation", "drawing", "games", "websites"];

$(".portfolio-lander-button").click(function() {
    var randomIdx = Math.floor(Math.random() * portfolioPages.length);
    location.href = location.pathname + "/" + portfolioPages[randomIdx];
});