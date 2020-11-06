
function inputForm() {  
    // analyze the text into the form to the server
    
      form = document.querySelector("#usertext-form");
    
      form.addEventListener("submit", function(event) {
          event.preventDefault();
    
          fetch("/ajax", {
            method:"post",
            body: new FormData(form),
            dataType: "json",
            })
          .then(response => response.json())
    
          .then(function (json) {console.log
              let query ={ 
                  response:json["response"],
              };
              
          let newDiv_2 = document.createElement("imessages");
            newDiv_2.innerHTML = ["Voici un article lié à ce lieu..."]+query["response"]+(
              '<a href="'+query["url"]+'">-En savoir plus sur Wikipedia.</a>'
            );
            newDiv_2.className = "from-them";
            document.getElementById("imessages").appendChild(newDiv_2);
            let div = document.getElementById("imessages");
            div.scrollTop = div.scrollHeight;
        
        });
})
}


