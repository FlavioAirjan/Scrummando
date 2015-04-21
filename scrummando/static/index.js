$("#register_btn").click(function(){
	var username = $("input[name=username]").val()
	var password = $("input[name=password]").val()
	console.log(username)
	console.log(password)

	$.post("add_user", {"username":username,"password":password},function(data){
		console.log(data)
		location.reload()
	})
})

$("#login_btn").click(function(){
	var username = $("input[name=login_username]").val()
	var password = $("input[name=login_password]").val()
	console.log(username)
	console.log(password)

	$.post("login_user", {"username":username,"password":password},function(data){
		$("#login_status").html(data["status"])
	})
})

$(document).ready(function(){
	
})