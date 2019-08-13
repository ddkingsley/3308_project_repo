window.onload = function() {
	answerButton = document.createElement('button')
	answerButton.innerHTML = "Give me ze answer!";
	document.body.appendChild(answerButton)
	answerButton.addEventListener('click', get_answer)
}
function get_answer() {
  const answer = document.getElementById("circle_text");
  answer.style.fontSize = "50px";
  answer.textContent = generate_answer()
  if (answer.textContent == mystic_answers[9]) {
  	answer.style.fontSize = "40px";
  }
  if (answer.textContent == mystic_answers[7]) {
  	answer.style.fontSize = "200px";
  }
  //answer.textContent = "Nein!";
  document.body.removeChild(answerButton)
  next = document.createElement('button')
  next.innerHTML = "Would you like to try again?";
  document.body.appendChild(next)
  next.addEventListener('click', reset)
}
function reset() {
  const answer = document.getElementById("circle_text");
  answer.style.fontSize = "200px";
  answer.textContent = "9";
  document.body.removeChild(next)
  answerButton = document.createElement('button')
  answerButton.innerHTML = "Give me ze answer!";
  document.body.appendChild(answerButton)
  answerButton.addEventListener('click', get_answer)
}
const mystic_answers = ["Better not tell you now", "Yes", "Definitely", "Maybe", "No, but you're on the right track", 
"Not a chance!", "I guess so", "42", "Nein!", "I'm picking up on something involving carrots, are you sure you're concentrating hard enough?",
"Cosmic energies are telling me... no", "Does a bear deficate in the woods?", "I think you already know the answer"];
function generate_answer() {
	var answers_length = mystic_answers.length;
	var random_answer_index = Math.floor(Math.random() * answers_length) 
	//console.log(answers_length)
	//console.log(random_answer_index)
	//console.log(mystic_answers[random_answer_index])
	return mystic_answers[random_answer_index]
}
