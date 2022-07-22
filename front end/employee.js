


refreshButton.addEventListener('click', async (e) => {
    e.preventDefault()
    let res = await fetch(`http://127.0.0.1:8082/users/${username}/reimbursements`, {
        'credentials': 'include',
        'method': 'GET',
        'headers': {
            'Content-Type': 'application/json'}});
    
    let data = await res.json();
    console.log(q_status)

    reimbursementTbodyElement.innerHTML = ""

    addReimbursementsToTable(data.reimbursements);
})

function addReimbursementsToTable(reimb_obj) {
    console.log(typeof(reimb_obj))
      for (reimb of reimb_obj) {  
        let row = document.createElement('tr');

        let idCell = document.createElement('td');
        idCell.innerHTML = reimb.reimb_id
        let amntCell = document.createElement('td');
        amntCell.innerHTML = reimb.amount
        let submitCell = document.createElement('td');
        submitCell.innerHTML = reimb.submitted;
        let submitByCell = document.createElement('td');
        submitByCell.innerHTML = reimb.author
        let resolvedCell = document.createElement('td');
        resolvedCell.innerHTML = reimb.resolved;
        let resolvedByCell = document.createElement('td');
        resolvedByCell.innerHTML = reimb.resolver
        let statusCell = document.createElement('td');
        statusCell.innerHTML = reimb.status
        let typeCell = document.createElement('td');
        typeCell.innerHTML = reimb.type
        let descCell = document.createElement('td');
        descCell.innerHTML = reimb.description
        let receiptCell = document.createElement('td');
        receiptCell.innerHTML = reimb.receipt

        row.appendChild(idCell);
        row.appendChild(amntCell);
        row.appendChild(submitCell);
        row.appendChild(submitByCell);
        row.appendChild(resolvedCell);
        row.appendChild(resolvedByCell);
        row.appendChild(statusCell);
        row.appendChild(typeCell);
        row.appendChild(descCell);
        row.appendChild(receiptCell);

        reimbursementTbodyElement.appendChild(row);
    }
};