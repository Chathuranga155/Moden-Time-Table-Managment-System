
   
   


let navOpen = false; // Track if the nav is open

function openNav() {
    document.getElementById("offcanvas").style.width = "300px";
    document.getElementById("main").style.marginLeft = "300px";
    document.getElementById("offcanvas").style.marginTop = "85px";
    document.getElementById("overlay").classList.add("show"); // Show overlay
    navOpen = true; // Set navOpen to true
    document.body.addEventListener('click', outsideClickListener); // Add click listener
}

function closeNav() {
    document.getElementById("offcanvas").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
    document.getElementById("overlay").classList.remove("show"); // Hide overlay
    navOpen = false; // Set navOpen to false

    // Delay the removal of the click listener for smoother transition
    setTimeout(() => {
        document.body.removeEventListener('click', outsideClickListener); // Remove click listener
    }, 300); // Match this with your CSS transition duration
}

// Function to detect clicks anywhere in the body
function outsideClickListener(event) {
    const offcanvas = document.getElementById("offcanvas");
    const openBtn = document.querySelector(".openbtn");

    // Check if the nav is open and if the click was outside the off-canvas menu and the button
    if (navOpen && !offcanvas.contains(event.target) && !openBtn.contains(event.target)) {
        closeNav(); // Close the menu
    }
}