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

function getQuery() {
    return document.getElementById("query").value;
}

function processJsonResponse(data) {
    console.log(data);
}

function clickHandler() {
  const query = this.getQuery();
  const included = this.getIncludeIngredients();
  const excluded = this.getExcludeIngredients();
  console.log(included);
  console.log(excluded);
  const postBody = {
    "query": query,
    "includeIngredients": included,
    "excludeIngredients": excluded
  };

//  var xhr = new XMLHttpRequest();
//    xhr.open("POST", 'http://127.0.0.1:5000/postmethod', true);
//
//    //Send the proper header information along with the request
//    // xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
//
//  xhr.onreadystatechange = function() { // Call a function when the state changes.
//    if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
//        console.log(Http.responseText);
//    }
//}
//  xhr.send("query=j&includeIngredients=b,c&excludeIngredients=d,e");
//

// xhr.send(new Int8Array());
// xhr.send(document);

  $.post("http://127.0.0.1:5000/postmethod", JSON.stringify(postBody), function(data, status) {
    processJsonResponse(JSON.parse(JSON.parse(data)[0]));
  });


//  post("http://localhost:5000/api/load", postBody)
//    .then(response => response.json())
//    .then(data => {
//      const targetElement = document.getElementById("output-text");
//
//      data.forEach(recipe => {
//        // const childElement = buildElementHtml
//        console.log(recipe);
//      });
//    });
}
