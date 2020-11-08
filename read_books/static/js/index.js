
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

                  title:json["title"],
                  response:json["response"],
                  picture:json["picture"]
                  
              };
          
          let newDiv_2 = document.createElement("div");
            
          newDiv_2.innerHTML = query["title"];
          newDiv_2.className = "imessages-title text-align-center";
          document.getElementById("imessages-title").appendChild(newDiv_2);
          

          
          let newDiv_3 = document.createElement("div");
            
          newDiv_3.innerHTML = query["response"];
          newDiv_3.className = "imessages-description";
          document.getElementById("imessages-description").appendChild(newDiv_3);

          let newDiv_4 = document.createElement("div");
            
          newDiv_4.innerHTML = "<img class=imessages-picture src=" + query["picture"] + "</img>";
          newDiv_4.className = "imessages-picture";
          document.getElementById("imessages-picture").appendChild(newDiv_4);
          
        });
})
}


