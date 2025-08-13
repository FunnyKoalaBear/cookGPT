console.log("JS loaded");

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

document.addEventListener("DOMContentLoaded", () => {

    const containers = document.querySelectorAll(".category-container");

    containers.forEach(container => {
        const list = container.querySelector(".category-list");
        const form = container.querySelector(".category-form");
        const input = container.querySelector(".category-input");
        const quantity = container.querySelector(".category-quantity");
        const unit = container.querySelector(".category-unit");

        form.addEventListener("submit", async(event) => {
            event.preventDefault();  // Prevent form submission
            
            const item = input.value.trim();  
            const qty = quantity.value.trim();
            const selectedUnit = unit.value;
            const category = container.querySelector("h2").textContent.trim() || "Unkown Category";  
            console.log("Form submitted for category:", category);
            
            console.log("Category:", category);
            console.log("Item:", item);
            console.log("Quantity:", qty);
            console.log("Selected Unit:", selectedUnit);

            if (item && qty && selectedUnit) {

                try { 
                    const response = await fetch("/myApp/updatePantry/", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                            "X-CSRFToken": csrftoken
                        },
                        body: JSON.stringify({
                            item: item,
                            quantity: qty,
                            unit: selectedUnit,
                            category: category
                        })
                    });

                    const result = await response.json();
                    console.log("Server response:", result);

                    if (response.status === 200) {
                        console.log("Item successfully added to pantry:");
                        
                        const li = document.createElement("li");
                        li.className = "flex justify-between items-center border-b pb-1";
                        li.dataset.qty = qty;  //qty of item stored
                        li.dataset.unit = selectedUnit;  //unit of item stored
                        li.dataset.item = item;  //item name stored

                        //span element for item name
                        const span = document.createElement("span");
                        span.textContent = `${item} - ${qty} ${selectedUnit}`;
                        li.appendChild(span);
                        console.log("Item text content:", span.textContent);  

                        //div for buttons
                        const buttonDiv = document.createElement("div");
                        buttonDiv.className = "space-x-2";
                        

                        const plusButton = document.createElement("button");
                        plusButton.className = "increment px-2 py-1 bg-green-500 text-white rounded";
                        plusButton.textContent = "+";

                        const minusButton = document.createElement("button");
                        minusButton.className = "decrement px-2 py-1 bg-yellow-500 text-white rounded";
                        minusButton.textContent = "-";

                        const trashButton = document.createElement("button");
                        trashButton.className = "trash px-2 py-1 bg-red-500 text-white rounded";
                        trashButton.textContent = "🗑️";
                        
                        //append buttons to the div
                        buttonDiv.appendChild(plusButton);
                        buttonDiv.appendChild(minusButton);
                        buttonDiv.appendChild(trashButton);

                        //append buttonDiv to the li
                        li.appendChild(buttonDiv);

                        //append li to list (final step to add everything to the list)
                        list.appendChild(li); 

                        //resetting form
                        input.value = ""; //resetting input field 
                        quantity.value = ""; //resetting quantity field
                        unit.value = ""; //resetting unit field
                        console.log("Item added:", item, qty, selectedUnit);


                    }


                }
                catch (error) {
                    console.error("Error sending data to server:", error);
                    return;  //exit if there's an error
                }

                
            }
            
        });

        //event delegation for increment/decrement/trash buttons

        list.addEventListener("click", async(e) => {
            let action = null;  
            const li = e.target.closest("li");
            if (!li) return; 

            const span = li.querySelector("span");
            let qty = parseFloat(li.dataset.qty);
            const unit = li.dataset.unit;
            const item = li.dataset.item;

            if (e.target.classList.contains("increment")) {
                qty++;
                li.dataset.qty = qty;  
                span.textContent = `${item} - ${qty} ${unit}`;
                action = "increment"

            } else if (e.target.classList.contains("decrement")) {
                qty = Math.max(0, qty - 1);
                li.dataset.qty = qty;  
                span.textContent = `${item} - ${qty} ${unit}`;
                action = "decrement"

            } else if (e.target.classList.contains("trash")) {
                li.remove();
                action = "trash";
            }

            if (action) {
                try {
                    const response = await fetch("/myApp/updateIngredient/", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "X-CSRFToken": csrftoken
                    },
                        body: JSON.stringify({
                            item: item,
                            action: action
                        })
                    });

                    const result = await response.json();
                    console.log("Server response:", result);


                } catch (error) {
                    console.error("Error updating pantry:", error);
                }

            };

        });
    });
});
