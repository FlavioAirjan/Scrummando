$("#register_btn").click(function(){
	var username = $("input[name=username]").val()
	var password = $("input[name=password]").val()
	console.log(username)
	console.log(password)

	$.post("add_user", {"username":username,"password":password},function(data){
		console.log(data)
	})
	
	var register_row = document.getElementById("register_row")
	register_row.style.display = "none"
        
        var login_row = document.getElementById("login_row")
	login_row.style.display = "block"
})

$("#login_btn").click(function(){
	var username = $("input[name=login_username]").val()
	var password = $("input[name=login_password]").val()
	console.log(username)
	console.log(password)

	$.post("login_user", {"username":username,"password":password},function(data){
		 if(data.logged){
                document.cookie = data.cookies[0][1];
                document.cookie = data.cookies[0][2];
                document.cookie = data.cookies[0][3];
                location.reload();
            } else {
        		$("#login_status").html(data["status"])
            }
	})
})

$("#novo_btn").click(function(){
	var login_row = document.getElementById("login_row")
	login_row.style.display = "none"

	var register_row = document.getElementById("register_row")
	register_row.style.display = "block"
})

 function diff(A, B) {
            return A.filter(function (a) {
                return B.indexOf(a) == -1;
            });
        }

        function show(shown) {
            var all = ['home', 'iniciar_jogo','sobre'];
            var hide_these = diff(all, shown);
            var hidden;
            document.getElementById(shown).style.display='block';
            for(hidden in hide_these)
                document.getElementById(hide_these[hidden]).style.display='none';
            $(".sidebar").slideToggle(600);
            return false;
        }

$("#iniciarjogo_btn").click(function(){
       show("iniciar_jogo")
})

$("#home_btn").click(function(){
    	show("home")
})

$("#sobre_btn").click(function(){
    	show("sobre")
})

$("#iniciarjogo_btn_falso").click(function(){
	alert("Por favor, faça o login ou registre-se");
})

$("#hist_btn").click(function(){
    	
})

$("#salvar_btn").click(function(){
    	
})

$("#next_btn").click(function(){
    var questao = document.getElementById("iniciar_jogo");
    questao.number="1";
    questao.style.display='block';
})

$(document).ready(function(){
	
})
