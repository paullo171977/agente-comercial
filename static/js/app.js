document.addEventListener("DOMContentLoaded", function () {

    const btnMenu = document.getElementById("btnMenu");
    const sidebar = document.getElementById("sidebar");
    const overlay = document.getElementById("sidebarOverlay");

    function fecharMenu() {
        sidebar.classList.remove("show");
        overlay.classList.remove("show");

        if (btnMenu) {
            btnMenu.setAttribute("aria-expanded", "false");
        }
    }

    if (btnMenu && sidebar && overlay) {

        btnMenu.addEventListener("click", function () {

            const aberto = sidebar.classList.toggle("show");

            overlay.classList.toggle("show", aberto);

            btnMenu.setAttribute(
                "aria-expanded",
                String(aberto)
            );

        });

        overlay.addEventListener("click", fecharMenu);

        document.addEventListener("keydown", function (event) {
            if (event.key === "Escape") {
                fecharMenu();
            }
        });

    }

});