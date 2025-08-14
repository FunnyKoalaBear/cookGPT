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

                        recipeTitleTag.setAttribute("recipeTitle", recipeTitle);
                        recipeTitleTag.textContent = recipeTitle;
                        
                        recipeTag.setAttribute("recipe", recipeString);
                        recipeTag.textContent = recipeString;

                        console.log(recipeTitle);

                    }
                }
                catch (error) {
                    console.error("Error generating recipe:", error);
                    return; //exit when error
                }

            }
        }
    });
});