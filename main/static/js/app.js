// app.js

function adicionar_carrinho(id_produto) {
    
    // adiciona produto ao carrinho
    axios.defaults.withCredentials = true;
    axios.get('/adicionar_carrinho/?id_produto=' + id_produto)
        .then(function(response){
            var total_produtos = response.data;
            document.getElementById('carrinho').innerText = total_produtos;
            console.log(response.data);
        });
}

function limpar_carrinho() {

    // limpar o carrinho
    axios.withCredentials = true;
    axios.get('/limpar_carrinho/')
        .then(function(response) {
            document.getElementById('carrinho').innerText = '';
            console.log(response.data);
        })
}