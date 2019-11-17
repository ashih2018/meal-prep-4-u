function checkCuisine() {
  var checkbox = document.getElementById("cuisine");
  var cuisines = document.getElementById("cuisines");
  if (checkbox.checked == false) {
    cuisines.style.display = "none";
  } else {
    cuisines.style.display = "inline-block";
  }
}

function generateIncludeRow() {
  var d = document.getElementById("include-ingredients");
  d.innerHTML += "<p><input type='text' name='food'>";
}

function generateExcludeRow() {
  var d = document.getElementById("exclude-ingredients");
  d.innerHTML += "<p><input type='text' name='food'>";
}
