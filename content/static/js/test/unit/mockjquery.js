"use strict;"

var $;
/*$ = function(argument) {
    if ( argument === 'find' ) {
	alert("target is find!!");
	argument = { find : function (target) 
		     {
			 if ( target === 'button' ) {
			     return { prop : function (status, status_value) 
				      { alert("prop called with "+ status +", "+status_value+" !!"); } 
				    };
			 }
		     }
		   }
    }
    return argument
}*/
$ = function (argument) {
    argument = { find : function (target) {alert(target);} }
    return argument
}