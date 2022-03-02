  $(document).ready(function() {
    
    $('#subscribe-btn').click(function(e){
      e.preventDefault();
      var seralizeData=$("#email_form").serialize();
      $.ajax({
        url:'Ajax',
        data:seralizeData,
        type: 'post',
        success: function(one,two,there){
          alert('check your Mail !');
        },
        error: function(one,two,there){
          alert('Please Enter a valid email');
        }
      })
    });
  });

  $(document).ready(function() {
    
    $('#send_btn').click(function(e){
      e.preventDefault();
      var hh=$("#message_form").serialize();
      $.ajax({
        url:'Contact_Us',
        data:hh,
        type: 'post',
        success: function(one,two,there){
          alert('Thank you for sending this message :)')
        },
        error: function(one,two,there){
          console.log(hh)
          console.log(one);
          console.log(two);
          console.log(there);
        }
      })
    });
  });
