let submitButton = document.getElementById("submit-btn");
let amountInput = document.getElementById("amount-input");
let typeInput = document.getElementById("type-input");
let descriptionInput = document.getElementById('description-input');
let username = sessionStorage.getItem('username');
let user_id = sessionStorage.getItem('user_id')
let today = new Date()

// console.log(user_id)

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

//replace placeholder text with image name



const fileInput = document.querySelector('#receipt-upload input[type=file]');
  


fileInput.onchange = () => {
    if (fileInput.files.length > 0) {
      const fileName = document.querySelector('#receipt-upload .file-name');
      fileName.textContent = fileInput.files[0].name;
      
    //   console.log(fileName)
    
    }
  }

  var img = document.querySelector('img');
  fileInput.addEventListener('change', function() {
    var url = URL.createObjectURL(fileInput.files[0]);
    console.log(url);
});










