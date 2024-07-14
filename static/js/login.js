document.addEventListener("DOMContentLoaded", function(){
    const visibilityButton=document.querySelector(".visibility-image");
    const passwordInput=document.querySelector("#password-input");
    const rememberCheckbox=document.querySelector("#remember-me");
    const form=document.querySelector("#form");

    visibilityButton.addEventListener("click",()=>{
        let path=visibilityButton.getAttribute("src")=="../static/img/visibility.png" ? "../static/img/visibility_off.png" : "../static/img/visibility.png";
        visibilityButton.setAttribute("src",path)
        let type=visibilityButton.getAttribute("src")=="../static/img/visibility.png" ? "password" : "text";
        passwordInput.setAttribute("type",type);
        
    })



    const existingusernames = ["Hilmi"];

    form.addEventListener("submit", (event) => {
        const usernameInput = document.querySelector("#username-input"); // Kullanıcı adı girişi
        const rememberCheckbox = document.querySelector("#rememberMe"); // Remember me checkbox
    
        if (existingusernames.includes(usernameInput.value)) {
            event.preventDefault();
            localStorage.setItem("rememberMe", rememberCheckbox.checked);
            window.location.href = "/home/";
        } else {
            alert("Bu isimle biri yok.")
            window.location.reload();
        }
    });
})