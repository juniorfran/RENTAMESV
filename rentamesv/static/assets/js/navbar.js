$(function () {
    var isopen_usermenu = false;
    /**
     * Open and close usermenu event
     */
    $(".header .user-menu-toggle").on("click", function () {
      if(!isopen_usermenu) {
        // Show menu
        $(".header .user-menu").show();
        //Change arrow
        $(".user-menu-toggle .simple-arrow").removeClass("fa-chevron-down").addClass("fa-chevron-up");
        isopen_usermenu = true;
      } else {
        // Close menu
        $(".header .user-menu").hide();
        //Change arrow
        $(".user-menu-toggle .simple-arrow").removeClass("fa-chevron-up").addClass("fa-chevron-down");
        isopen_usermenu = false;
      }
    });
  });