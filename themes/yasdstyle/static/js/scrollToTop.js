// scrollToTop.js

document.addEventListener("DOMContentLoaded", function() {
    var fixedParagraph = document.getElementById("topbar");

    // 监听页面滚动事件
    window.addEventListener("scroll", function() {
        // 如果页面滚动超过一定高度，显示回到顶部的段落，否则隐藏
        if (window.scrollY > 100) {
            fixedParagraph.style.display = "block";
        } else {
            fixedParagraph.style.display = "none";
        }
    });

    // 监听点击事件
    fixedParagraph.addEventListener("click", function() {
        scrollToTop();
    });

    // 滚动到页面顶部的函数
    function scrollToTop() {
        // 平滑滚动到顶部
        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
    }
});
