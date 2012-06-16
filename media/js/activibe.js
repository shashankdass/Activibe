function submitStatus(stats){
	alert("ok" + ", " + stats);
	//document.getElementById("user_id").value=id;
	document.getElementById("user_status").value=stats;
	document.forms['my_status'].submit();
}	
