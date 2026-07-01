// script.js
// Day 17 — JavaScript interactivity


// ─────────────────────────────────────────
// FEATURE 1: Theme Toggle
// ─────────────────────────────────────────

const themeBtn = document.querySelector("#theme-toggle");

themeBtn.addEventListener("click", () => {
    document.body.classList.toggle("dark-theme");

    // Change button text/icon based on current theme
    if (document.body.classList.contains("dark-theme")) {
        themeBtn.textContent = "☀️ Light Mode";
    } else {
        themeBtn.textContent = "🌙 Dark Mode";
    }
});


// ─────────────────────────────────────────
// FEATURE 2: Dynamic List
// ─────────────────────────────────────────

const itemInput = document.querySelector("#item-input");
const addItemBtn = document.querySelector("#add-item-btn");
const learningList = document.querySelector("#learning-list");

let items = [];   // array to hold our list items

function renderList() {
    // Clear current list
    learningList.innerHTML = "";

    // Use forEach to render each item
    items.forEach((item, index) => {
        const li = document.createElement("li");
        li.className = "list-item";
        li.innerHTML = `
            <span>${item}</span>
            <button class="delete-btn" data-index="${index}">×</button>
        `;
        learningList.appendChild(li);
    });

    // Attach delete listeners to each delete button
    document.querySelectorAll(".delete-btn").forEach(btn => {
        btn.addEventListener("click", (e) => {
            const indexToRemove = parseInt(e.target.dataset.index);
            // filter creates a NEW array without the removed item
            items = items.filter((_, i) => i !== indexToRemove);
            renderList();
        });
    });
}

function addItem() {
    const value = itemInput.value.trim();
    if (value === "") return;   // don't add empty items

    items.push(value);          // add to array
    itemInput.value = "";       // clear input
    renderList();                // re-render the list
}

addItemBtn.addEventListener("click", addItem);

// Also allow pressing Enter to add
itemInput.addEventListener("keypress", (event) => {
    if (event.key === "Enter") {
        addItem();
    }
});


// ─────────────────────────────────────────
// FEATURE 3: Fetch API — Random Quote
// ─────────────────────────────────────────


const fetchQuoteBtn = document.querySelector("#fetch-quote-btn");
const quoteText = document.querySelector("#quote-text");
const quoteAuthor = document.querySelector("#quote-author");

async function fetchQuote() {
    quoteText.textContent = "Loading...";
    quoteAuthor.textContent = "";

    try {
        const response = await fetch("https://dummyjson.com/quotes/random");
        const data = await response.json();

        quoteText.textContent = `"${data.quote}"`;
        quoteAuthor.textContent = `— ${data.author}`;

    } catch (error) {
        quoteText.textContent = "Couldn't fetch a quote. Try again!";
        console.error("Fetch error:", error);
    }
}

fetchQuoteBtn.addEventListener("click", fetchQuote);


// ─────────────────────────────────────────
// Run once on page load
// ─────────────────────────────────────────

console.log("Day 17 — script.js loaded successfully!");