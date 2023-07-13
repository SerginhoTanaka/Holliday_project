var select = document.getElementById("selectedYear");

var anoAtual = new Date().getFullYear();
var anoInicio = 1900; 
var anoFim = anoAtual + 10; 

for (var i = anoInicio; i <= anoFim; i++) {
  var option = document.createElement("option");
  option.text = i;
  option.value = i;
  select.appendChild(option);
}