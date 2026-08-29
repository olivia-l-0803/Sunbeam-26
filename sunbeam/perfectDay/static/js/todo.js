const buttons = document.getElementsByClassName('doneToggle');

Array.from(buttons).forEach(button => { // for each button in buttons
    button.addEventListener('click', () => { 
        id = button.dataset
        const inputValue = document.getElementById('username').value; 
        console.log('User entered:', inputValue);
  });
});