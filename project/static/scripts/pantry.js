function addPantryItem() {
  let a = document.getElementById("include0");
  let pantry = document.getElementById("pantry-items");
  pantry.innerHTML += a.value + "<br />";
}
