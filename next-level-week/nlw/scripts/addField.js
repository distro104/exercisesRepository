

// Procura o botao
a = document.querySelector("#add-time").addEventListener('click',cloneField);
//Quando clicar no botão:

function cloneField() {
    const newFieldContainer = document.querySelector('.schedule-item').cloneNode(true);

    const fields = newFieldContainer.querySelectorAll('input');
    console.log(fields);

    fields.forEach(
        function(field) {
            field.value = ""
        }
    )

    document.querySelector('#schedule-items').appendChild(newFieldContainer)
    
}