const buttons = Array.from(document.getElementById('buttons').getElementsByTagName('button'));

buttons.forEach(element => {
    element.addEventListener('click', event => {
        buttons.forEach(element => element.classList.remove('active'));
        element.classList.add('active');
    })
});
