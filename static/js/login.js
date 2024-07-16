document.addEventListener("DOMContentLoaded", function() {
    const visibilityButton = document.querySelector(".visibility-image");
    const passwordInput = document.querySelector("#password-input");
    const rememberCheckbox = document.querySelector("#remember-me");
    const form = document.querySelector("#form");

    visibilityButton.addEventListener("click", () => {
        let path = visibilityButton.getAttribute("src") == "../static/img/visibility.png" ? "../static/img/visibility_off.png" : "../static/img/visibility.png";
        visibilityButton.setAttribute("src", path)
        let type = visibilityButton.getAttribute("src") == "../static/img/visibility.png" ? "password" : "text";
        passwordInput.setAttribute("type", type);
    });

    form.addEventListener("submit", (event) => {
        event.preventDefault();
        const usernameInput = document.querySelector("#username-input").value;
        const rememberCheckbox = document.querySelector("#rememberMe").checked;

        fetch('/check-username', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username: usernameInput })
        })
        .then(response => response.json())
        .then(data => {
            if (data.exists) {
                localStorage.setItem("rememberMe", rememberCheckbox);
                window.location.href = "/home/";
            } else {
                alert("Bu isimle biri yok.");
                window.location.reload();
            }
        })
    });
});