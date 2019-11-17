function addPantryItem() {
  let a = document.getElementById("include0");
  let pantry = document.getElementById("pantry-items");
  pantry.innerHTML += a.value + "<br />";
}

var loadFile = function(event) {
	var image = document.getElementById('output');
	image.src = URL.createObjectURL(event.target.files[0]);
};
