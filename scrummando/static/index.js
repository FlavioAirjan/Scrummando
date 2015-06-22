var USER_ANSWERS = {}
var LETTERS = {1:"A",2:"B",3:"C",4:"D"}

function saveGame(){
	var q_id_answers = {}
	$.each(USER_ANSWERS,function(key,value){
		q_id_answers[value[0]] = value[1]
	})
	$.post("save",q_id_answers,function(data){
		if(data["game_saved"]){
			alert("Jogo Salvo com sucesso.")
			location.reload()
		}
	})
}

function updateUserData(){
	radio_respostas = $("input[type=radio]:checked")
	radio_respostas.each(function(){
		questao = parseInt(this.getAttribute("name").substr(1))
		resposta = parseInt(this.getAttribute("value"))
		questao_id = parseInt(this.getAttribute("data-q-id"))
		USER_ANSWERS[questao] = [questao_id, resposta]
	})

	respostas_tabela = $(".resposta_tabela")
	$.each(USER_ANSWERS,function(key, value){
		$(respostas_tabela[key-1]).html(LETTERS[value[1]])
	})
	
}

function createUserData(){
	count = 1
	$(".questao_id").each(function(){
		USER_ANSWERS[count]	= [parseInt(this.value),0]
		count++
	})
		
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
	$("#historico").hide()
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
		showContent($("#historico"))
    	makeBoldMenu(this)
})

$("#salvar_btn").click(function(){
    	makeBoldMenu(this)
    	saveGame()
})
$("#previous_btn").click(function(){
	showPreviousQuesiton()
})
$("#next_btn").click(function(){
	showNextQuesiton()
})
$("#submit_btn").click(function(){
	//Check All answers answered
	all_answered = true
	$.each(USER_ANSWERS,function(key,value){
		if(value[1] == 0){
			all_answered = false
		}
	})
	if(all_answered == false){
		alert("Por favor, responda todas as questões.")
		return
	}

	var q_id_answers = {}
	$.each(USER_ANSWERS,function(key,value){
		q_id_answers[value[0]] = value[1]
	})
	$.post("submit_answers",q_id_answers,function(data){
		if(data["game_submitted"]){
			alert("Analisando... confira sua pontuação na seção históricos.")
			location.reload()
		}
	})
})
$("#load_msg").click(function(){
	$(this).hide()
})

$(document).ready(function(){
	makeBoldMenu($("#home_btn")[0])
	showContent($("#home"))
	manageQuestoes()
	createUserData()
	updateUserData()
})
