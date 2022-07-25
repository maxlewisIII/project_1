let statusButtons = document.getElementById('status-btn')
let reimbID = document.getElementById('reimb-id-btn')
let updateEntryButton = document.getElementById('update-entry-btn')

let today = new Date()


updateEntryButton.addEventListener('click', async () => {
    // let selectedRadioButton;
    // for (let radioBtn of statusButtons){
    //     if (radioBtn.checked){
    //         selectedRadioButton = radioBtn
    //         break;
    //     }
    // }

    let res = await fetch(`http://127.0.0.1:8082/reimbursements/6`, {
            // 'mode': 'no-cors',
            'credentials': 'include',
            'method': 'PUT',
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': JSON.stringify({
                "reimb_id": "6",
                "status": "approved",
                "submission_date": today

                // "reimb_id": reimbID.value,
                // "reimb_status": selectedRadioButton.value,
                // "submission_date": today
            })
        })

    if(res.status == 201) {
        
        // window.location.href = '/finance_manager.html'
    
    } else {
        console.log("update failed");
    }


})