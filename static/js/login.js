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

    const existingusernames = ["Hilmi10"]; // Burayı database'deki username'ler ile değiştireceğiz.

    form.addEventListener("submit", (event) => {
        const usernameInput = document.querySelector("#username"); // Kullanıcı adı girişi
        const rememberCheckbox = document.querySelector("#rememberMe"); // Remember me checkbox
    
        if (existingUsernames.includes(usernameInput.value)) {
            event.preventDefault(); // Form gönderimini durdur
            alert("Bu kullanıcı adı zaten mevcut. Lütfen başka bir kullanıcı adı seçin.");
        } else {
            localStorage.setItem("rememberMe", rememberCheckbox.checked);
        }
    });
})