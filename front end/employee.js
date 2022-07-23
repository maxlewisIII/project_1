// let allFilter = document.getElementById('all-filter');



document.addEventListener('DOMContentLoaded', async () => {
    try {
        let res = await fetch(`http://127.0.0.1:8082/users/1/reimbursements`); 
        if (res.status == 200) {
            console.log(resp.json())
        }
        let data = await res.json(); 

        addPokemonToTable(data);
    } catch(err) {
        console.log(err);
    }
});
