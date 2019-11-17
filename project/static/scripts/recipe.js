let includeId = 1;
let excludeId = 1;

function checkCuisine() {
    let checkbox = document.getElementById("cuisine");
    let cuisines = document.getElementById("cuisines");
    if (checkbox.checked === false) {
        cuisines.style.display = "none";
    } else {
        cuisines.style.display = "inline-block";
    }
}

function generateIncludeRow() {
    let d = document.getElementById("include-ingredients");
    let node = document.createElement("INPUT");
    node.setAttribute("style", "display:block; margin-top: 2%");
    node.setAttribute("type", "text");
    node.setAttribute("id", "include" + includeId);
    d.appendChild(node);
    includeId++;
}

function getIncludeIngredients() {
    let ingredients = [];
    for (let i = 0; i < includeId; i++) {
        const id = "include" + i;
        let ing = document.getElementById(id);
        ingredients.push(ing.value);
    }
    console.log("include: ", ingredients);
    return ingredients;
}

function generateExcludeRow() {
    let d = document.getElementById("exclude-ingredients");
    let node = document.createElement("INPUT");
    node.setAttribute("style", "display:block; margin-top: 2%");
    node.setAttribute("type", "text");
    node.setAttribute("id", "exclude" + excludeId);
    d.appendChild(node);
    excludeId++;
}

function getExcludeIngredients() {
    let ingredients = [];
    for (let i = 0; i < excludeId; i++) {
        const id = "exclude" + i;
        let ing = document.getElementById(id);
        ingredients.push(ing.value);
    }
    console.log("exclude: ", ingredients);
    return ingredients;
}

function getQuery() {
    return document.getElementById("query").value;
}

function processJsonResponse(data) {
    console.log(JSON.stringify(data));
    data.forEach(recipe => console.log(recipe["title"]));
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

    $.post("http://127.0.0.1:5000/postmethod", JSON.stringify(postBody), function(data, status) {
        processJsonResponse(JSON.parse(data).map(recipe => JSON.parse(recipe)));
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
