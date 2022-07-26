let submitButton = document.getElementById("submit-btn");
let amountInput = document.getElementById("amount-input");
let typeInput = document.getElementById("type-input");
let descriptionInput = document.getElementById('description-input');
let username = sessionStorage.getItem('username');
let user_id = sessionStorage.getItem('user_id')
let today = new Date()

console.log(user_id)

// alert("!")
submitButton.addEventListener('click', async () => {
    
    let res = await fetch(`http://127.0.0.1:8082/users/${user_id}/reimbursements`, {
        // 'mode': 'no-cors',
        'credentials': 'include',
        'method': 'POST',
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': JSON.stringify({
            // "description": "grocery",
            // "receipt": null,
            // "reimb_amount": "2000",
            // "reimb_author": 1,
            // "reimb_id": 5,
            // "reimb_resolver": null,
            // "resolved_date": null,
            // "status": "pending",
            // "submission_date": null,
            // "type": "food"

            "reimb_amount": amountInput.value,
            "type": typeInput.value,
            "description": descriptionInput.value,
            "submission_date": today

            // "submission_date": "Sun, 24 Jul 2022 20:33:41 GMT"
            


        })
    })

if (res.status == 201) {

    window.location.href = '/employee.html'

}


})






// submitButton.addEventListener('click', submitFunc);

// async function submitFunc() {
//     try {
//         let res = await fetch('http://127.0.0.1:8082/users/1/reimbursements')

//     }



// }
