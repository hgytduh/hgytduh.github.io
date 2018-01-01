            $(document).ready(function () {
                $(".forumItem").click(function (event) {
                    window.location = $(this).data("url")
                });
            });