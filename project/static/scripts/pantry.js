onLoad();

function addPantryItem() {
  let a = document.getElementById("include0");
  let pantry = document.getElementById("pantry-items");
  pantry.innerHTML += a.value + "<br />";
}

var loadFile = function(event) {
  var image = document.getElementById("output");
  image.src = URL.createObjectURL(event.target.files[0]);
};

function onLoad() {
  let pantry = document.getElementById("pantry-items");
  $.post("http://127.0.0.1:5000/pantrymethod", {}, function(data, status) {
    var ingredients = (JSON.parse(data));
    console.log(ingredients);
    for (let i = 0; i < ingredients['produce'].length; i++) {
        console.log(ingredients['produce'][i])
        console.log(ingredients['produce'][i].value)
        pantry.innerHTML += ingredients['produce'][i] + "<br />";
    }
  });
}
