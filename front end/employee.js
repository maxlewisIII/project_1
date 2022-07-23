let reimbTbody = document.getElementById('reimb-tbody');
let username = sessionStorage.getItem('username');
let firstname = sessionStorage.getItem('first_name');

document.addEventListener('click', async (e) => {
    e.preventDefault()
    
    try {
        let res = await fetch(`http://127.0.0.1:8082/users/1/reimbursements`, {
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
        amountCell.innerHTML = reimb.amount;
        
        let addedCell = document.createElement('td');
        addedCell.innerHTML = reimb.added;
        
        let resolvedCell = document.createElement('td');
        resolvedCell.innerHTML = reimb.resolved
        
        let statusCell = document.createElement('td');
        statusCell.innerHTML = reimb.status;
        
        let typeCell = document.createElement('td');
        typeCell.innerHTML = reimb.type
        
        let descriptionCell = document.createElement('td');
        descriptionCell.innerHTML = reimb.description
        
        let recieptCell = document.createElement('td');
        recieptCell.innerHTML = reimb.reciept
        
        let authorCell = document.createElement('td');
        authorCell.innerHTML = reimb.author
        
        let resolverCell = document.createElement('td');
        resolverCell.innerHTML = reimb.resolver

        row.appendChild(idCell);
        row.appendChild(amountCell);
        row.appendChild(addedCell);
        row.appendChild(resolvedCell);
        row.appendChild(statusCell);
        row.appendChild(typeCell);
        row.appendChild(descriptionCell);
        row.appendChild(recieptCell);
        row.appendChild(authorCell);
        row.appendChild(resolverCell);

        reimbTbody.appendChild(row);
    }
};
