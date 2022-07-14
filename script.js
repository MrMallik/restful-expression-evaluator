function handleSubmit() {
    
    url = 'https://exprevalapp.herokuapp.com/expression'

    document.getElementById("results").innerHTML = "Loading...";

    const expr = { "expression": document.getElementById("expression").value };

    let options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify(expr)
    }

    let fetchRes = fetch(url, options);

    fetchRes.then(res => res.json())
            .then(d => { document.getElementById("results").innerHTML = JSON.stringify(d); })
}