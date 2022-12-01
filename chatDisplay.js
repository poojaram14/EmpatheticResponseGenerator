var botui = new BotUI('genetic-counselor');

//global variables
let user_response='',user_name = '', time_of_day = 'morning', feeling = 3, discussed_privacy = false, has_kids = false, reason = '',scale = 0, send_back = 'empty'

function date(){
  var date = new Date();
  var current_hour = date.getHours();
  if(current_hour >= 5 && current_hour < 12){
    time_of_day = 'Morning'
  }else if(current_hour >= 12 && current_hour < 17){
    time_of_day = 'Afternoon'
  }else if(current_hour >= 17 && current_hour < 24){
    time_of_day = 'Evening'
  }
}

function greet () {
  return botui.message.add({
    loading: true,
    delay: 1000,
    type: 'text',
    content:'Good '+ time_of_day + '. I am Tanya.'
  }).then(function(){
return botui.message.add({ // show a message
          loading: true,
          delay: 1000,
          content: 'Whats your name?'
})
}).then(function () { // wait till its shown
      return botui.action.text({ // show 'text' action
        action: {
          placeholder: 'Your name'
        }
      })
  }).then(async function (res) { // get the result
      user_name = res.value
      const ignore = await botui.message.add({
        loading: true,
        delay: 1000,
        type: 'text',
        content: 'Great to meet you, ' + user_name + '!'
      })
  })
  .then(async function (){
    const ignore = await botui.message.add({
      loading: true,
      delay: 1000,
      type: 'text',
      content:'Hi'
      })
    }).then(function () { // wait till its shown
      return botui.action.text({ // show 'text' action
        action: {
          placeholder: 'Your Response'
        }
      })
    }).then(async function (res) { // get the result
      user_response = res.value
      const ignore = await botui.message.add({
        loading: true,
        delay: 1000,
        type: 'text',
        content: await get_response(user_response).then(function (response) {
          return response.json();
        }).then(function (text) {
          // console.log('POST response:');
          // console.log(text.response);
          return text.ai_response 
        })
      })
  })
};

async function get_response(query){
  
  return fetch('http://127.0.0.1:5000/aiResponse', {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
    },
    body: JSON.stringify({ "query": query })
    })
}


console.log(get_response("Hi, I feel sad"));

greet()

