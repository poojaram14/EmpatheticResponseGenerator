var botui = new BotUI('genetic-counselor');

//global variables
let user_name = '', time_of_day = 'morning', feeling = 3, discussed_privacy = false, has_kids = false, reason = '',scale = 0

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
      content:'I know this can seem a little strange, I hope you are comfortable. '
      })
    }).then(async function (){
      const ignore = await  botui.action.button({
            delay: 1000,
            action: [{
              text: 'It\'s fine, thanks.',
            },{
              text: 'It is a little strange.',
            },{
              text: 'It\'s OK.',
            }]
          })//.then(function (){
          //   role_setting()
          // })
    })
};


greet()

