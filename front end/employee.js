let reimbTbody = document.getElementById('reimb-tbody');
let username = sessionStorage.getItem('username');
let logoutButton = document.getElementById('logout-btn')

let user_id = sessionStorage.getItem('user_id')

document.addEventListener('DOMContentLoaded', async () => {

    
    try {
        let res = await fetch(`http://127.0.0.1:8082/users/${user_id}/reimbursements`, {
        // 'mode': 'no-cors',
        'credentials': 'include',
        'method': 'GET',
        'headers': {
            'Content-Type': 'application/json'}});
        

        let data = await res.json();

        addReimbsToTable(data.reimbursements);
    } catch(err) {
        console.log(err);
    }
}
);


function addReimbsToTable(reimb_obj) {
      for (reimb of reimb_obj){

        let row = document.createElement('tr');

        let idCell = document.createElement('td');
        idCell.innerHTML = reimb.reimb_id;
        
        let amountCell = document.createElement('td');
        amountCell.innerHTML = reimb.reimbursement_amount;
        
        let addedCell = document.createElement('td');
        addedCell.innerHTML = reimb.submission_date;
        
        let resolvedCell = document.createElement('td');
        resolvedCell.innerHTML = reimb.resolved_date
        
        let statusCell = document.createElement('td');
        statusCell.innerHTML = reimb.status;
        
        let typeCell = document.createElement('td');
        typeCell.innerHTML = reimb.type
        
        let descriptionCell = document.createElement('td');
        descriptionCell.innerHTML = reimb.description
        
        let receiptCell = document.createElement('td');
        receiptCell.innerHTML = reimb.receipt
        
        let authorCell = document.createElement('td');
        authorCell.innerHTML = reimb.reimb_author
        
        let resolverCell = document.createElement('td');
        resolverCell.innerHTML = reimb.reimb_resolver

        row.appendChild(idCell);
        row.appendChild(amountCell);
        row.appendChild(addedCell);
        row.appendChild(resolvedCell);
        row.appendChild(statusCell);
        row.appendChild(typeCell);
        row.appendChild(descriptionCell);
        row.appendChild(receiptCell);
        row.appendChild(authorCell);
        row.appendChild(resolverCell);

        reimbTbody.appendChild(row);
    }
};

logoutButton.addEventListener('click', async (e) => {
    e.preventDefault()
    let res = await fetch('http://127.0.0.1:8082/logout', {
        
        'credentials': 'include',
        'method': 'POST',
        'headers': {
            'Content-Type': 'application/json'
        },
    })

    if (res.status == 200) {
        console.log("Logout successful")
        window.location.href="./login.html"
    }
});
