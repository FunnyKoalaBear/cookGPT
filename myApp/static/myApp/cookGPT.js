console.log("JS Loaded")

function getCookie(name) {
    let cookieValue = null;

    if (document.cookie && document.cookie !== "") {

        const cookies = document.cookie.split(";");

        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
        
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

const ingredients = [];

document.addEventListener("DOMContentLoaded", () => {

    document.querySelectorAll('.ingredient-btn').forEach(btn => {

        btn.addEventListener('click', function() {

            const ingredient = btn.getAttribute('data-item');
            const quantity = btn.getAttribute('data-quantity');
            const unit = btn.getAttribute('data-unit');
            const key = `${ingredient} (${quantity} ${unit})`;


            if (ingredients.includes(key)) {

                //remove ingredient if already selected
                const idx = ingredients.indexOf(key);
                if (idx > -1) ingredients.splice(idx, 1);

            } else {

                //add ingredient if not selected
                ingredients.push(`${ingredient} (${quantity} ${unit})`);

            }
            console.log('Selected ingredients:', ingredients);
        });

    });


    document.addEventListener("click", async function(event) {

        const query = document.getElementById("query")?.value || "";
        
        if (event.target && event.target.id === "generateRecipe") {
            console.log("Generate Recipe button clicked");
            
            if (ingredients.length !== 0 & query.length > 2) {

                //hiding prompt and ingredient box and heading
                document.getElementById("beforeGeneration").style.display = "none";


                //loading animation
                const loading = document.getElementById("loading");
                const heading = document.querySelector("#heading");
                loading.style.display = "block";
                heading.style.display = "none";


                try {
                    const response = await fetch("/myApp/generateRecipe/", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                            "X-CSRFToken": csrftoken
                        },
                        body: JSON.stringify({
                            ingredients: ingredients,
                            query: query
                        })
                    });

                    const result = await response.json();

                    if (response.status === 200) {
                        console.log("Recipe generated successfully:", result);

                        const recipeTag = document.querySelector("#recipe");
                        const recipeTitleTag = document.querySelector("#recipeTitle");
                        const recipeString = result.message;
                        const recipeTitle = result.recipeTitle || "Recipe";
                        
                        //updating ingredient box with recipe
                        recipeTitleTag.setAttribute("recipeTitle", recipeTitle);
                        recipeTitleTag.textContent = recipeTitle + "📄";
                        
                        
                        const formattedRecipe = recipeString
                            .replace(/Ingredients:/g, "<b>Ingredients:</b>") //adds bold tag for subheadings
                            .replace(/Instructions:/g, "<b>Instructions:</b>")
                            .replace(/\n/g, "<br>");  // preserve line breaks

                        recipeTag.setAttribute("recipe", formattedRecipe);
                        recipeTag.textContent = formattedRecipe;
                        recipeTag.innerHTML = formattedRecipe;

                        //hiding loading animation
                        loading.style.display = "none";

                        console.log(recipeTitle);


                        //displaying instructions box
                        document.getElementById("instructionsBox").style.display = "block"; 

                    }
                }
                catch (error) {
                    console.error("Error generating recipe:", error);

                    //updating instruction box with error message
                    const recipeTag = document.querySelector("#recipe");
                    const recipeTitleTag = document.querySelector("#recipeTitle");
                    const recipeString = "Error in generating recipe. Please try again.";
                    const recipeTitle = "Error";

                    //updating ingredient box with recipe
                    recipeTitleTag.setAttribute("recipeTitle", recipeTitle);
                    recipeTitleTag.textContent = recipeTitle;
                    
                    recipeTag.setAttribute("recipe", recipeString);
                    recipeTag.textContent = recipeString;

                    //displaying instructions box
                    document.getElementById("instructionsBox").style.display = "block"; 
                    
                    //hiding loading animation
                    loading.style.display = "none";
                    // return; //exit when error
                    
                }

            }
        }
    });


    document.addEventListener("click", async function(event) {

        const target = event.target;
        const isSaved = target.dataset.saved === "true"; ///checks if currently saved

        if (!isSaved) {
            if (target.id === "saveRecipe") {
            
                const recipeTitle = document.getElementById("recipeTitle").innerHTML;  // forms strings
                const recipe = document.getElementById("recipe").innerHTML;
                console.log("Saving recipe:", recipeTitle);
                console.log("Recipe content:", recipe);

                //changing button color after saving 
                target.style.backgroundColor = "blue";
                target.style.color = "white";
                target.innerHTML = "Saved!"
                target.dataset.saved = "true";

                //post logic 
                try {
                    const response = await fetch("/myApp/saveRecipe/", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                            "X-CSRFToken": csrftoken
                        },
                        body: JSON.stringify({
                            recipeTitle: recipeTitle,
                            recipe: recipe
                        })
                    });

                    if (response.ok) {
                        const result = await response.json();
                        console.log("Recipe saved successfully:", result);
                    } else {
                        console.error("Error saving recipe:", response.statusText);
                    }
                } catch (error) {
                    console.error("Error saving recipe:", error);
                }
            }
        } else {
            // --- Revert button to original state ---
            target.style.backgroundColor = "#16a34a"; // Tailwind green-600
            target.style.color = "white";
            target.innerHTML = "Save Recipe";
            target.dataset.saved = "false"; // mark as unsaved
            console.log("Recipe unsaved");
            //sending request to delete the saved meal 
            // const recipeId = this.dataset.id;
            // const url = this.action;
            // const csrfToken = this.querySelector('[name=csrfmiddlewaretoken]').value;

            // fetch(url, {
            //     method: 'POST',
            //     headers: {
            //         'X-CSRFToken': csrfToken,
            //         'X-Requested-With': 'XMLHttpRequest'
            //     }
            // })
            // .then(response => {
            //     if (response.ok) {
            //         document.getElementById(`recipe.${recipeId}`).style.display = 'none';
            //     } else {
            //         console.error('Failed to remove recipe');
            //     }
            // })
            // .catch(error => console.error('Error:', error));
        }

    });
});