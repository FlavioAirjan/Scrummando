var USER_ANSWERS = {}
var LETTERS = {1:"A",2:"B",3:"C",4:"D"}

function updateUserData(){
	radio_respostas = $("input[type=radio]:checked")
	radio_respostas.each(function(){
		questao = parseInt(this.getAttribute("name").substr(1))
		resposta = parseInt(this.getAttribute("value"))
		USER_ANSWERS[questao] = resposta
	})

	respostas_tabela = $(".resposta")
	$.each(USER_ANSWERS,function(key, value){
		$(respostas_tabela[key-1]).html(LETTERS[value])
	})
	
}

function createUserData(){
	max_q = $("#max_q").val()
	for (var i = 1; i <= max_q; i++) {
		USER_ANSWERS[i]	= ""
	}
}

function showPreviousQuesiton(){
	// Check max
	
	if($("#current_q").val() == 1){
		console.log("Min questions")
		return
	}
	current_q = $("#current_q").val()
	current_q--
	$("#current_q").val(current_q)
	$("#question_counter").html($("#current_q").val())
	$(".questao").hide()
	$($(".questao")[current_q-1]).show()
}

function showNextQuesiton(){
	// Check max
	
	if($("#max_q").val() == $("#current_q").val()){
		console.log("Max questions")
		return
	}
	current_q = $("#current_q").val()
	current_q++
	$("#current_q").val(current_q)
	$("#question_counter").html($("#current_q").val())
	$(".questao").hide()
	$($(".questao")[current_q-1]).show()
}

function manageQuestoes(){
	$(".questao").hide()
	$(".questao").first().show()
}

function showContent(Jcontent){
	$("#home").hide()
	$("#questoes_content").hide()
	$("#sobre").hide()
	Jcontent.show()
}

function makeBoldMenu(menu){
	$("#iniciarjogo_btn").css("font-weight","normal")
	$("#home_btn").css("font-weight","normal")
	$("#sobre_btn").css("font-weight","normal")
	$("#iniciarjogo_btn_falso").css("font-weight","normal")
	$("#hist_btn").css("font-weight","normal")
	$("#salvar_btn").css("font-weight","normal")
	$("#logout_btn").css("font-weight","normal")
	menu.style.fontWeight = "bold"
}

$("#register_btn").click(function(){
	var username = $("input[name=username]").val()
	var password = $("input[name=password]").val()
	console.log(username)
	console.log(password)

	$.post("add_user", {"username":username,"password":password},function(data){
		if(data.registered == true){
			$("#login_status").parent().show()
			$("#login_status").html("Usuário registrado com sucesso.")
		} else {
			$("#login_status").parent().show()
			$("#login_status").html("Favor tente registrar novamente.")
		}
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
        		$("#login_status").parent().show()
            }
	})
})

$("input[type=radio]").change(function(){
	updateUserData()
})


$("#novo_btn").click(function(){
	var login_row = document.getElementById("login_row")
	login_row.style.display = "none"

	var register_row = document.getElementById("register_row")
	register_row.style.display = "block"
})




$("#iniciarjogo_btn").click(function(){
       makeBoldMenu(this)
       showContent($("#questoes_content"))
})

$("#home_btn").click(function(){
	    makeBoldMenu(this)
    	showContent($("#home"))
})

$("#sobre_btn").click(function(){
		makeBoldMenu(this)
    	showContent($("#sobre"))
})

$("#iniciarjogo_btn_falso").click(function(){
	alert("Por favor, faça o login ou registre-se");
})

$("#hist_btn").click(function(){
    	makeBoldMenu(this)
})

$("#salvar_btn").click(function(){
    	makeBoldMenu(this)
})
$("#previous_btn").click(function(){
	showPreviousQuesiton()
    // var questao = document.getElementById("iniciar_jogo");
    // questao.number="1";
    // questao.style.display='block';
})
$("#next_btn").click(function(){
	showNextQuesiton()
    // var questao = document.getElementById("iniciar_jogo");
    // questao.number="1";
    // questao.style.display='block';
})

$(document).ready(function(){
	makeBoldMenu($("#home_btn")[0])
	showContent($("#home"))
	manageQuestoes()
	createUserData()
})
