let reimbID = document.getElementById('reimb-id-input')
let updateEntryButton = document.getElementById('update-entry-btn')
let statusButtons = document.querySelectorAll('input[name="status"]')
let reimbResolver = sessionStorage.getItem('reimb_resolver')

let today = new Date()

updateEntryButton.addEventListener('click', async () => {
    let selectedRadioButton;
    for (let radioBtn of statusButtons){
        if (radioBtn.checked){
            selectedRadioButton = radioBtn
            break;
        }
    }

    let res = await fetch(`http://127.0.0.1:8082/reimbursements/${reimbID.value}`, {
            // 'mode': 'no-cors',
            'credentials': 'include',
            'method': 'PUT',
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': JSON.stringify({

                "status": selectedRadioButton.value,
                "submission_date": today,
                "reimb_resolver": reimbResolver.value
                
            })
        })

    if(res.status == 201) {

        console.log("success")
        window.location.href = '/finance_manager.html'
        
    
    } else {
        console.log("update failed");
    }


})