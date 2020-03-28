jQuery(document).ready(function() {
    jQuery('.novantas-more').magnificPopup({
        type: 'inline',
        preloader: false,
    });


   /* below code was added 8/8/2017 */
   jQuery( ".novantas-more" ).click( function() {
      jQuery( '#novantas_button_input' ).val( jQuery(this).attr('novantas_button_id') );
   });


});

var url = location.search;
if (url.match('/novantas-message/')) {
	    jQuery(window).load(function () {
	        jQuery.magnificPopup.open({
	        	items: {src: '#novantas-message'},
	            type: 'inline',
	       		preloader: false,
	        }, 0);
	    });
}

function getCookie(cname) {
	    var name = cname + "=";
	    var ca = document.cookie.split(';');
	    for(var i = 0; i < ca.length; i++) {
	        var c = ca[i];
	        while (c.charAt(0) == ' ') {
	            c = c.substring(1);
	        }
	        if (c.indexOf(name) == 0) {
	            return c.substring(name.length, c.length);
	        }
	    }
	    return "";
	}

function checkCookie() {
    domain = getCookie("novantas_view");
    if (domain == "") {
        domain = "Domain Not Set"
    } 
}
