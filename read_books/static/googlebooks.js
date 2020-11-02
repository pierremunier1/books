
function inputForm() {  
    // analyze the text into the form to the server
    
      form = document.querySelector("#usertext-form");
    
      form.addEventListener("submit", function(event) {
          event.preventDefault();
    
          fetch("/ajax", {
            method:"POST",
            body: new FormData(form)
            })
          .then(response => response.json())
    
          .then(function (json) {console.log
              let query ={ 
                  response:json["response"],
              };

        
        });
})
}


