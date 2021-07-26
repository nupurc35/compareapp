$( document ).ready(function() {
    console.log( "ready!" );
});

var apiBaseurl = 'api/smartPhones/'
$('#smartphone-1-select').change(function(){
  var smartPhoneId = this.value
 $.ajax(
    {
        type:"GET",
        url:apiBaseurl+smartPhoneId,
        success: function( data ) 
        {
             console.log(data)    
        },
		error: function(data) {             
			console.log(data)
		},
     })
})
$('#smartphone-2-select').change(function(){
alert('this is smartphone-2-select')
})  


