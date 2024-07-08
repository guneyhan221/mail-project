document.addEventListener("DOMContentLoaded",()=>{
    const visibilityButton=document.querySelector(".visibility-image");
    const passwordInput=document.querySelector("#password-input")
    const usernameInput=document.querySelector("input[name='username']")
    const form=document.querySelector(".create-account-form")
    const usernameRegex=/^(?=.*\d)[a-zA-Z0-9_]{4,24}$/;
    const passwordRegex=/^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{8,64}$/;

    visibilityButton.addEventListener("click",()=>{
        let path=visibilityButton.getAttribute("src")=="../static/img/visibility.png" ? "../static/img/visibility_off.png" : "../static/img/visibility.png";
        visibilityButton.setAttribute("src",path)
        let type=visibilityButton.getAttribute("src")=="../static/img/visibility.png" ? "password" : "text";
        passwordInput.setAttribute("type",type);
        
    })

    passwordInput.addEventListener("input",()=>{
        if (passwordRegex.test(passwordInput.value)){
            passwordInput.style.borderColor="green";
        }else{
            passwordInput.style.borderColor="red";
        }
    });

    usernameInput.addEventListener("input",()=>{
        if (usernameRegex.test(usernameInput.value)){
            usernameInput.style.borderColor="green";
        }else{
            usernameInput.style.borderColor="red";
        }
    });

    form.addEventListener("submit",(e)=>{
        e.preventDefault();
        if(!passwordRegex.test(passwordInput.value)){
            window.location.href="/create-account";
            alert("Şifreniz gereksinimleri karşılamıyor!");
            return;
        }
        window.location.href="/submit";
    });
});