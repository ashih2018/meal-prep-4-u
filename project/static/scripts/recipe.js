var includeId = 1;
var excludeId = 1;

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
  var node = document.createElement("INPUT");
  node.setAttribute("style", "display:block; margin-top: 2%");
  node.setAttribute("type", "text");
  node.setAttribute("id", "include" + includeId);
  d.appendChild(node);
  includeId++;
}

function getIncludeIngredients() {
  ingredients = [];
  for (var i = 0; i < includeId; i++) {
    const id = "include" + i;
    ing = document.getElementById(id);
    ingredients.push(ing.value);
  }
  console.log("include: ", ingredients);
  return ingredients;
}

function generateExcludeRow() {
  var d = document.getElementById("exclude-ingredients");
  var node = document.createElement("INPUT");
  node.setAttribute("style", "display:block; margin-top: 2%");
  node.setAttribute("type", "text");
  node.setAttribute("id", "exclude" + excludeId);
  d.appendChild(node);
  excludeId++;
}

function getExcludeIngredients() {
  ingredients = [];
  for (var i = 0; i < excludeId; i++) {
    const id = "exclude" + i;
    ing = document.getElementById(id);
    ingredients.push(ing.value);
  }
  console.log("exclude: ", ingredients);
  return ingredients;
}

function clickHandler() {
  const included = this.getIncludeIngredients();
  const excluded = this.getExcludeIngredients();
  const postBody = {
    included,
    excluded
  };
  $.post("/postmethod", {
    javascript_data: data
  });


  post("http://localhost:5000/api/load", postBody)
    .then(response => response.json())
    .then(data => {
      const targetElement = document.getElementById("output-text");

      data.forEach(recipe => {
        // const childElement = buildElementHtml
        console.log(recipe);
      });
    });
}
