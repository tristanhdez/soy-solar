"use strict";


jQuery(document).ready(function() {
    $("#btns").click(function(e){
      e.preventDefault();
      $.ajax({
          type: "POST",
          url: "/ingc/chatbot_ingc",
          data: {
              question: $("#question").val().replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/'/g, "&#39;").replace(/"/g, "&#34;")
          },
          success: function(result) {
                let userDiv = document.createElement("div");
                const messagesContainer = document.getElementById("messages");
                userDiv.id = "user";
                userDiv.className = "response";
                userDiv.innerHTML = "<span>"+$("#question").val()+"</span><img src='/static/img/icons/fish.png' class='fish' alt='Icon' height='50px' width='50px'></img>";
                messagesContainer.appendChild(userDiv);
                let botDiv = document.createElement("div");
                let botImg = document.createElement("img");
                let botText = document.createElement("span");
                messagesContainer.appendChild(botDiv);
                messagesContainer.scrollTop = messagesContainer.scrollHeight - messagesContainer.clientHeight;
                botDiv.id = "bot";
                botImg.src = "/static/img/icons/solar.png";
                botImg.className = "avatar";
                botDiv.className = "bot response";
                botText.innerText = "Escribiendo...";
                botDiv.appendChild(botImg);
                botDiv.appendChild(botText);
                if (result.response == undefined){
                    setTimeout(()=>{
                        botText.innerText = `Este es tu actual tutor y la forma en el cómo te puedes comunicar con él/ella: ${result}`;
                    },500)
                    $("#question").val("")
                }else{
                    setTimeout(()=>{
                        botText.innerText = `${result.response}`;
                    },500)
                    $("#question").val("")
                }
          },
          error: function(result) {
              alert('Inténtalo Nuevamente');
          }
      });
    });
});
