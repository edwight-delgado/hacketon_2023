function speak(text) {
  var msg = new SpeechSynthesisUtterance();
  var voices = window.speechSynthesis.getVoices();
  msg.lang = 'es-ES';
  msg.volume = 1; // 0 to 1
	msg.rate = 1; // 0.1 to 10
	msg.pitch = 0; //0 to 2
  msg.text = text;
  msg.voice = voices[4]
  msg.voiceURI = 'native';
  msg.onend = function(e) {

    console.log('Finished in ' + e.elapsedTime + ' seconds.');
   
   };
  //console.log(voices)
  window.speechSynthesis.speak(msg);
}

function questionToExecute(product) {
  let prompt = 'hasme una descripcion de muy breve del producto ' + product
  setTimeout(function() {  
    postData(url='http://127.0.0.1:8000/', {'data':prompt})
    .then((data) => {
      $("#chat-circle").toggle('scale');
      $(".chat-box").toggle('scale');

      //window.getElementById("#chat-circle").toggle('scale');
      //window.getElementById(".chat-box").toggle('scale');
      //console.log('chat:'+data); // JSON data parsed by `data.json()` call
      generate_message(data, 'self');
      //speak(data)
    }); 
    //generate_message(msg, 'user');  
  }, 1000)
} 


  var INDEX = 0; 
  function chatToExecute(){

    //e.preventDefault();
    var msg = $("#chat-input").val(); 
    if(msg.trim() == ''){
      return false;
    }
    generate_message(msg, 'self');
    var buttons = [
        {
          name: 'Existing User',
          value: 'existing'
        },
        {
          name: 'New User',
          value: 'new'
        }
      ];
    setTimeout(function() {  
      postData(url='http://127.0.0.1:8000/', {'data':msg})
      .then((data) => {
        
        //console.log('chat:'+data); // JSON data parsed by `data.json()` call
        generate_message(data, 'user');
        speak(data)
      }); 
      //generate_message(msg, 'user');  
    }, 1000)
    return false; 
  }


  

  function generate_message(msg, type) {
    INDEX++;
    var str="";
    str += "<div id='cm-msg-"+INDEX+"' class=\"chat-msg "+type+"\">";
    str += "          <span class=\"msg-avatar\">";
    str += "            <img src=\"https:\/\/image.crisp.im\/avatar\/operator\/196af8cc-f6ad-4ef7-afd1-c45d5231387c\/240\/?1483361727745\">";
    str += "          <\/span>";
    str += "          <div class=\"cm-msg-text\">";
    str += msg;
    str += "          <\/div>";
    str += "        <\/div>";
    $(".chat-logs").append(str);
    $("#cm-msg-"+INDEX).hide().fadeIn(300);
    if(type == 'self'){
     $("#chat-input").val(''); 
    }    
    $(".chat-logs").stop().animate({ scrollTop: $(".chat-logs")[0].scrollHeight}, 1000);    
  }  
  
  function generate_button_message(msg, buttons){    
    /* Buttons should be object array 
      [
        {
          name: 'Existing User',
          value: 'existing'
        },
        {
          name: 'New User',
          value: 'new'
        }
      ]
    */
    INDEX++;
    var btn_obj = buttons.map(function(button) {
       return  "              <li class=\"button\"><a href=\"javascript:;\" class=\"btn btn-primary chat-btn\" chat-value=\""+button.value+"\">"+button.name+"<\/a><\/li>";
    }).join('');
    var str="";
    str += "<div id='cm-msg-"+INDEX+"' class=\"chat-msg user\">";
    str += "          <span class=\"msg-avatar\">";
    str += "            <img src=\"https:\/\/image.crisp.im\/avatar\/operator\/196af8cc-f6ad-4ef7-afd1-c45d5231387c\/240\/?1483361727745\">";
    str += "          <\/span>";
    str += "          <div class=\"cm-msg-text\">";
    str += msg;
    str += "          <\/div>";
    str += "          <div class=\"cm-msg-button\">";
    str += "            <ul>";   
    str += btn_obj;
    str += "            <\/ul>";
    str += "          <\/div>";
    str += "        <\/div>";
    $(".chat-logs").append(str);
    $("#cm-msg-"+INDEX).hide().fadeIn(300);   
    $(".chat-logs").stop().animate({ scrollTop: $(".chat-logs")[0].scrollHeight}, 1000);
    $("#chat-input").attr("disabled", true);
  }
  
  $(document).delegate(".chat-btn", "click", function() {
    var value = $(this).attr("chat-value");
    var name = $(this).html();
    $("#chat-input").attr("disabled", false);
    generate_message(name, 'self');
  })
  
 
  $("#chat-circle").click(function() {  

    $("#chat-circle").toggle('scale');
    $(".chat-box").toggle('scale');
    setTimeout(function() {  
      prompt= 'inicial'


      postData(url='http://127.0.0.1:8000/', {'data':prompt})
      .then((data) => {
        
        //console.log('chat:'+data); // JSON data parsed by `data.json()` call
        generate_message(data, 'self');
        //speak(data)
      }); 
      //generate_message(msg, 'user');  
    }, 1000)
  })
  
  $(".chat-box-toggle").click(function() {
    $("#chat-circle").toggle('scale');
    $(".chat-box").toggle('scale');
  })
  


  async function postData(url = '', data={ 'data': '' }) {
    // Default options are marked with *
    console.log('url ',url,' data ',data)
    const response = await fetch(url, {
      method: 'POST', // *GET, POST, PUT, DELETE, etc.
      mode: 'cors', // no-cors, *cors, same-origin
      
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
        // 'Content-Type': 'application/x-www-form-urlencoded',
      },
      // manual, *follow, error
      // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
      body: JSON.stringify(data) // body data type must match "Content-Type" header
    });
    const res = await response.text();
      console.log(res);
    
    return res
  }


  document.addEventListener('DOMContentLoaded', () => {
    let chat_input = document.getElementById('chat-input') 
    window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    const recognition = new SpeechRecognition();
    recognition.interimResults = true;
    recognition.lang = "es-MX";
    recognition.addEventListener('result', e => {
      console.log(e.results);
      const transcript = Array.from(e.results).
      map(results => results[0]).
      map(result => result.transcript).join('');
      let script = transcript;
      if (e.results[0].isFinal) {
        console.log('script:',script)
        chat_input.value += script;
      }
    });
      recognition.addEventListener('end', () => {
        if (document.getElementById('toggle').checked) {
          recognition.start();
        } else {
          recognition.stop();
        }
      });
      const toggle = document.getElementById('toggle');
      toggle.addEventListener('change', e => {
        if (e.target.checked) {
          recognition.start();
        } else {
          recognition.abort();
          console.log('stopped');
        }
      });
  
  })


