// app.js

function adicionar_carrinho(id_produto) {
    
    // adiciona produto ao carrinho
    axios.defaults.withCredentials = true;
    axios.get('/adicionar_carrinho/?id_produto=' + id_produto)
        .then(function(response){
            
            var total_produtos = response.data;
            document.getElementById('carrinho').innerText = total_produtos;

        });
}