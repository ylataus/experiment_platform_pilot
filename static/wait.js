$(function() {
    // When we're using HTTPS, use WSS too.
	alert("in function");
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
   
    var chatsock = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host  + window.location.pathname);
    alert(window.location.host);
    alert(window.location.pathname);


 chatsock.onmessage = function(message) {
        var data = JSON.parse(message.data);
	    alert("inside onmessage");   
	    alert(message.data);
	    //alert(data.url);
	    //window.location.replace(data.url);
	    if (data.notification == 'check status' ){
		//?how to call function check status??
		alert(data.notification);
		chatsock.send("hello world");
		}
	    if (data.notification == 'redirect to url' ){
		alert(data.notification);
		alert(data.url);
		window.location.replace(data.url);
		//?how to call function check status??
		//redirect
		}
        
              
    };


chatsock.onopen = function() {
    
        (function poll(){
            setTimeout(function(){
                chatsock.send("hello world");
                poll();
                },10000);
        })(); 
	
      
	 

    
    };

   


	

    
});

