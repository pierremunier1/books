
function inputForm() {  
    // analyze the text into the form to the server
    
      form = document.querySelector("#usertext-form");
    
      form.addEventListener("keyup", function(event)  {
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
                  picture:json["picture"],
                  author:json["author"]
                  
              };

                
              let newDiv_3 = document.createElement("div");
              newDiv_3.innerHTML = query["picture"];
              
              document.getElementById("imessages-description").appendChild(newDiv_3);

              });
})
}


