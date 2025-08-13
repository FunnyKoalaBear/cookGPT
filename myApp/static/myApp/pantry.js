console.log("JS loaded");

document.addEventListener("DOMContentLoaded", () => {

    const containers = document.querySelectorAll(".category-container");

    containers.forEach(container => {
        const list = container.querySelector(".category-list");
        const form = container.querySelector(".category-form");
        const input = container.querySelector(".category-input");
        const quantity = container.querySelector(".category-quantity");
        const unit = container.querySelector(".category-unit");



        form.addEventListener("submit", (event) => {
            event.preventDefault();  // Prevent form submission
            
            const item = input.value.trim();  
            const qty = quantity.value.trim();
            const selectedUnit = unit.value;

            if (item && qty && selectedUnit) {
                const li = document.createElement("li");
                li.className = "flex justify-between items-center border-b pb-1";
                li.dataset.qty = qty;  //qty of item stored

                //span element for item name
                const span = document.createElement("span");
                span.textContent = `${item} - ${qty} ${selectedUnit}`;

                console.log("Item text content:", span.textContent);  
                li.appendChild(span);

                //div for buttons
                const buttonDiv = document.createElement("div");
                buttonDiv.className = "space-x-2";
                

                //+ button
                const plusButton = document.createElement("button");
                plusButton.className = "px-2 py-1 bg-green-500 text-white rounded";
                plusButton.textContent = "+";

                //+ button functionality
                plusButton.addEventListener("click", () => {
                    //get current qty from data attribute
                    let currentQty = parseInt(li.dataset.qty);
                    currentQty++;
                    li.dataset.qty = currentQty;

                    
                    span.textContent = `${item} - ${currentQty} ${selectedUnit}`;
                });

                //- button
                const minusButton = document.createElement("button");
                minusButton.className = "px-2 py-1 bg-yellow-500 text-white rounded";
                minusButton.textContent = "-";

                //minus button functionality
                minusButton.addEventListener("click", () => {
                    //get current qty from data attribute
                    let currentQty = parseInt(li.dataset.qty);
                    currentQty--;
                    li.dataset.qty = currentQty;

                    span.textContent = `${item} - ${currentQty} ${selectedUnit}`;
                });

                //trash button 
                const trashButton = document.createElement("button");
                trashButton.className = "px-2 py-1 bg-red-500 text-white rounded";
                trashButton.textContent = "🗑️";

                //trash button functionality
                trashButton.addEventListener("click", () => {
                    list.removeChild(li);  //remove the li from the list
                    console.log("Item removed:", item, qty, selectedUnit);
                });
                
                //append buttons to the div
                buttonDiv.appendChild(plusButton);
                buttonDiv.appendChild(minusButton);
                buttonDiv.appendChild(trashButton);

                //append buttonDiv to the li
                li.appendChild(buttonDiv);

                //append li to list (final step to add everything to the list)
                list.appendChild(li); 
                input.value = ""; //resetting input field 
                quantity.value = ""; //resetting quantity field
                unit.value = ""; //resetting unit field
                console.log("Item added:", item, qty, selectedUnit);
            }
        });

    });
});
