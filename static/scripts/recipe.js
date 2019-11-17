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
    return ingredients;
}

function getQuery() {
    return document.getElementById("query").value;
}

function processJsonResponse(data) {
    console.log(JSON.stringify(data));
    data.forEach(recipe => console.log(recipe["title"]));

    const targetElement = document.getElementById("resultsContainer");
    let i = 0;
    data.forEach(recipe => {
        const recipeDiv = document.createElement("div");
        recipeDiv.setAttribute("id", "result" + i);
        const recipeLink = document.createElement("a");
        recipeLink.setAttribute("href", recipe["sourceUrl"]);
        recipeLink.innerHTML = "<h3>" + recipe["title"] + "</h3>";
        recipeDiv.innerHTML += recipeLink.outerHTML;
        const recipeImg = document.createElement("img");
        recipeImg.setAttribute("src", recipe["imageUrl"]);
        recipeImg.setAttribute("class", "resultImage");
        recipeImg.setAttribute("alt", recipe["title"]);
        recipeDiv.innerHTML += recipeImg.outerHTML;
        recipeDiv.innerHTML += "<p>";
        recipeDiv.innerHTML += "Time: " + recipe["requiredTime"] + " minutes<br />";
        recipeDiv.innerHTML += "Ingredients: <br />";

        const ingredientsList = document.createElement("ul");
        recipe["ingredients"].forEach(ingredient => {
            ingredientsList.innerHTML += `<li>${ingredient["originalString"]}</li>`;
        });
        recipeDiv.innerHTML += ingredientsList.outerHTML;
        recipeDiv.innerHTML += "</p>";

        targetElement.appendChild(recipeDiv);
        console.log(recipeDiv);
        i++;
    });

}

function clickHandler() {
    const query = this.getQuery();
    const included = this.getIncludeIngredients();
    const excluded = this.getExcludeIngredients();
    const postBody = {
        "query": query,
        "includeIngredients": included,
        "excludeIngredients": excluded
    };

    $.post("http://127.0.0.1:5000/postmethod", JSON.stringify(postBody), function(data, status) {
        processJsonResponse(JSON.parse(data).map(recipe => JSON.parse(recipe)));
    });
}
