// app.js

function adicionar_carrinho(id_produto) {
    
    axios.defaults.withCredentials = true
    axios.get('adicionar_carrinho/?id_produto=' + id_produto)
        .then(function(response){
            console.log(response.data)
        })
}