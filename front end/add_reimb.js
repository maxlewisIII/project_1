let submitButton = document.getElementById("submit-btn");
let amountInput = document.getElementById("amount-input");
let typeInput = document.getElementById("typeInput");
let descriptionInput = document.getElementById('description-input');


submitButton.addEventListener('click', async () => {
    let res = await fetch('http://127.0.0.1:8082/users/1/reimbursements', {
        'credentials': 'include',
        'method': 'POST',
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': JSON.stringify({
            "amount": amountInput.value,
            "type": typeInput.value,
            "description": descriptionInput.value
        })
    })

if (res.status == 201) {

    window.location.href = 'employee.html'

}


})






// submitButton.addEventListener('click', submitFunc);

// async function submitFunc() {
//     try {
//         let res = await fetch('http://127.0.0.1:8082/users/1/reimbursements')

//     }



// }
