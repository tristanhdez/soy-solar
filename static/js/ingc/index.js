"use strict";

jQuery(document).ready(function() {
    $("#btns").click(function(e){
      e.preventDefault();
      $.ajax({
          type: "POST",
          url: "/ingc/chatbot_ingc",
          data: {
              question: $("#question").val().replace(/</g, "&lt;").
              replace(/>/g, "&gt;").replace(/'/g, "&#39;")
              .replace(/"/g, "&#34;").normalize("NFD").toLowerCase()
              .replace(/\s+/g,"") //replace whitespaces.
              .replace(/[\u0300-\u036f]/g, "") //replace accents.
              .replace(/[!@#$%^&*?¿,.;:]/g,"") //replace invalid characters.
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
                setTimeout(()=>{
                    botText.innerText = `${result}`;
                },500)
                $("#question").val("")
          },
          error: function(result) {
              alert('Inténtalo Nuevamente');
          }
      });
    });
});
