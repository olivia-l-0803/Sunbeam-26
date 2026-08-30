const addbutn = document.getElementById("addBtn")



const closeButton = document.querySelector(".close-btn");
const modalWindow = document.querySelector(".addModal");


closeButton.addEventListener("click", function() {
  modalWindow.style.display = "none";
});


const addBtn = document.getElementById("addBtn");
const closeBtn = document.querySelector(".close-btn");
const addModal = document.querySelector(".addModal");

addBtn.addEventListener("click", function() {
  console.log("hello")
  addModal.style.display = "flex";  
});

closeBtn.addEventListener("click", function() {
  addModal.style.display = "none";  
});

window.addEventListener("click", function(event) {
  if (event.target === addModal) {
    addModal.style.display = "none";
  }
});


