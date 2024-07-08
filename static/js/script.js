document.addEventListener("DOMContentLoaded",()=>{
    const visibilityButton=document.querySelector(".visibility-image");
    const passwordInput=document.querySelector("#password-input")
    const usernameInput=document.querySelector("input[name='username']")
    const submitButton=document.querySelector("#submit-button")
    const usernameRegex=/^(?=.*\d)[a-zA-Z0-9_]{4,24}$/;
    const passwordRegex=/^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{8,64}$/;

    visibilityButton.addEventListener("click",()=>{
        let path=visibilityButton.getAttribute("src")=="../static/img/visibility.png" ? "../static/img/visibility_off.png" : "../static/img/visibility.png";
        visibilityButton.setAttribute("src",path)
        let type=visibilityButton.getAttribute("src")=="../static/img/visibility.png" ? "password" : "text";
        passwordInput.setAttribute("type",type);
        
    })
    controlUsername();
    controlPassword();

    passwordInput.addEventListener("input",()=>{
        controlPassword();
    });

    usernameInput.addEventListener("input",()=>{
        controlUsername();
    });

    function onHover(){
        submitButton.style="transform: scale(1.05);";
    }

    function onLeave(){
        submitButton.style="transform: scale(1);";
    }

    function controlPassword(){
        if (passwordRegex.test(passwordInput.value)){
            passwordInput.style.borderColor="green";
            if(usernameRegex.test(usernameInput.value)){
                submitButton.disabled=false;
                submitButton.style.backgroundColor="#313a43";
                submitButton.addEventListener("mouseenter",onHover);
                submitButton.addEventListener("mouseleave",onLeave);
            }
        }else{
            passwordInput.style.borderColor="red";
            submitButton.disabled=true;
            submitButton.style.backgroundColor="#9fa8b5";
            submitButton.removeEventListener("mouseenter",onHover);
            submitButton.removeEventListener("mouseleave",onLeave);
        }
    }

    function controlUsername(){
        if (usernameRegex.test(usernameInput.value)){
            usernameInput.style.borderColor="green";
            if(passwordRegex.test(passwordInput.value)){
                submitButton.disabled=false;
                submitButton.style.backgroundColor="#313a43";
                submitButton.addEventListener("mouseenter",onHover);
                submitButton.addEventListener("mouseleave",onLeave);
            }
        }else{
            usernameInput.style.borderColor="red";
            submitButton.disabled=true;
            submitButton.style.backgroundColor="#9fa8b5";
            submitButton.removeEventListener("mouseenter",onHover);
            submitButton.removeEventListener("mouseleave",onLeave);
        }
    }

    
});