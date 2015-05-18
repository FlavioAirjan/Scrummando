$("#register_btn").click(function(){
	var username = $("input[name=username]").val()
	var password = $("input[name=password]").val()
	console.log(username)
	console.log(password)

	$.post("add_user", {"username":username,"password":password},function(data){
		console.log(data)
		location.reload()
	})
	
	var register_row = document.getElementById("register_row")
	register_row.style.display = "hidden"
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

$("#novo_btn").click(function(){
	var login_row = document.getElementById("login_row")
	login_row.style.display = "hidden"
	
	var register_row = document.getElementById("register_row")
	register_row.style.display = "block"
})

$(document).ready(function(){
	
})