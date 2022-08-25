"use strict";
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

function insertMessage() {
  var msg_without_changes = $('.message-input').val().replace(/</g, "&lt;").
  replace(/>/g, "&gt;").replace(/'/g, "&#39;").replace(/"/g, "&#34;").normalize("NFD")
  var msg = $('.message-input').val().replace(/</g, "&lt;").
  replace(/>/g, "&gt;").replace(/'/g, "&#39;")
  .replace(/"/g, "&#34;").normalize("NFD").toLowerCase()
  .replace(/\s+/g,"") //replace whitespaces.
  .replace(/[\u0300-\u036f]/g, "") //replace accents.
  .replace(/[!@#$%^&*?¿,.;:]/g,"") //replace invalid characters.;
  if ($.trim(msg) == '') {
    return false;
  }
  $('<div class="message message-personal">' + msg_without_changes + '</div>').appendTo($('.mCSB_container')).addClass('new');
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
        url: "/guest/chatbot_student",
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
              updateScrollbar();
            },500)
            $("#question").val("");
        },
        error: function(result) {
            alert('Inténtalo Nuevamente');
        }
    });
}


const first_message = "¡Hola! Soy Solar ☀️🤖 y seré tu asistente virtual. \n Si no tienes idea de qué preguntar y/o cómo, puedes checar en la sección Palabras Clave 😊";

function fakeMessage() {
    if ($('.message-input').val() != '') {
      return false;
    }
    $('<div class="message loading new"><figure class="avatar"><img src="/static/img/icons/solar_icon_chat.png" /></figure><span></span></div>').appendTo($('.mCSB_container'));
    updateScrollbar();

    setTimeout(function() {
      $('.message.loading').remove();
      $('<div class="message new"><figure class="avatar"><img src="/static/img/icons/solar_icon_chat.png" /></figure>' + first_message + '</div>').appendTo($('.mCSB_container')).addClass('new');
      updateScrollbar();
    }, 500);

  }
