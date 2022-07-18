"use strict";
/*
jQuery(document).ready(function() {
    $("#btns").click(function(e){
      e.preventDefault();
      $.ajax({
          type: "POST",
          url: "/student/chatbot_student",
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
*/
var $messages = $('.messages-content'),
    d, h, m;

$(window).load(function() {
  $messages.mCustomScrollbar();
  setTimeout(function() {
    fakeMessage();
  }, 100);
});

function updateScrollbar() {
  $messages.mCustomScrollbar("update").mCustomScrollbar('scrollTo', 'bottom', {
    scrollInertia: 10,
    timeout: 0
  });
}

function setDate(){
  d = new Date()
  if (m != d.getMinutes()) {
    m = d.getMinutes();
    $('<div class="timestamp">' + d.getHours() + ':' + m + '</div>').appendTo($('.message:last'));
  }
}

function insertMessage() {
    var msg = $('.message-input').val().replace(/</g, "&lt;").
    replace(/>/g, "&gt;").replace(/'/g, "&#39;")
    .replace(/"/g, "&#34;").normalize("NFD").toLowerCase()
    .replace(/\s+/g,"") //replace whitespaces.
    .replace(/[\u0300-\u036f]/g, "") //replace accents.
    .replace(/[!@#$%^&*?¿,.;:]/g,"") //replace invalid characters.;
    if ($.trim(msg) == '') {
      return false;
    }
    $('<div class="message message-personal">' + msg + '</div>').appendTo($('.mCSB_container')).addClass('new');
    setDate();
    updateScrollbar();
    gettingMessage();
}

$('.message-submit').click(function() {
  insertMessage();
});

$(window).on('keydown', function(e) {
  if (e.which == 13) {
    insertMessage();
    return false;
  }
})

function gettingMessage(){
    $.ajax({
        type: "POST",
        url: "/student/chatbot_student",
        data: {
            question: $(".message-input").val().replace(/</g, "&lt;").
            replace(/>/g, "&gt;").replace(/'/g, "&#39;")
            .replace(/"/g, "&#34;").normalize("NFD").toLowerCase()
            .replace(/\s+/g,"") //replace whitespaces.
            .replace(/[\u0300-\u036f]/g, "") //replace accents.
            .replace(/[!@#$%^&*?¿,.;:]/g,"") //replace invalid characters.
        },
        success: function(result) {
            $('<div class="message loading new"><figure class="avatar"><img src="/static/img/icons/solar_icon_chat.png" /></figure><span></span></div>').appendTo($('.mCSB_container'));
            updateScrollbar();

            setTimeout(()=>{
              $('.message.loading').remove();
              $('<div class="message new"><figure class="avatar"><img src="/static/img/icons/solar_icon_chat.png" /></figure>' + `${result}` + '</div>').appendTo($('.mCSB_container')).addClass('new');
              setDate();
              updateScrollbar();
            },500)
            $("#question").val("");
        },
        error: function(result) {
            alert('Inténtalo Nuevamente');
        }
    });
}


var Fake = '¡Hola! Soy Solar y seré tu asistente virtual. Si eres nuev@ y no tienes idea de qué preguntar y cómo, puedes checar en la sección Palabras Clave'


function fakeMessage() {
    if ($('.message-input').val() != '') {
      return false;
    }
    $('<div class="message loading new"><figure class="avatar"><img src="/static/img/icons/solar_icon_chat.png" /></figure><span></span></div>').appendTo($('.mCSB_container'));
    updateScrollbar();
  
    setTimeout(function() {
      $('.message.loading').remove();
      $('<div class="message new"><figure class="avatar"><img src="/static/img/icons/solar_icon_chat.png" /></figure>' + Fake + '</div>').appendTo($('.mCSB_container')).addClass('new');
      setDate();
      updateScrollbar();
    }, 500);
  
  }