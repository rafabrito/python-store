from django.core.management.base import BaseCommand
# from faker import Faker
from main.models import Produto


class Command(BaseCommand):
    help  = "Command information"

    def handle(self, *args, **kwargs):

        # faker = Faker('pt-BR')
        Produto.objects.create(categoria='homem', nome_produto='Tshirt Vermelha', descricao='Ab laborum, commodi aspernatur, quas distinctio cum quae omnis autem ea, odit sint quisquam similique! Labore aliquam amet veniam ad fugiat optio.', imagem='tshirt_vermelha.png', preco=45.70, stock=100, visivel=1, created_at='2021-02-06 19:45:18', updated_at='2021-02-06 19:45:25')
        Produto.objects.create(categoria='homem', nome_produto='Tshirt Azul', descricao='Possimus iusto esse atque autem rem, porro officiis sapiente quos velit laboriosam id expedita odio obcaecati voluptate repudiandae dignissimos eveniet repellat blanditiis.', imagem='tshirt_azul.png', preco=55.25, stock=100, visivel=1, created_at='2021-02-06 19:45:19', updated_at='2021-02-06 19:45:25')
        Produto.objects.create(categoria='homem', nome_produto='Tshirt Verde', descricao='Nostrum quisquam dolorum dolor autem accusamus fugit nesciunt, atque et? Quis eum nemo quidem officia cum dolorem voluptates! Autem, earum. Similique, fugit.', imagem='tshirt_verde.png', preco=35.15, stock=100, visivel=1, created_at='2021-02-06 19:45:20', updated_at='2021-02-06 19:45:26')
        Produto.objects.create(categoria='homem', nome_produto='Tshirt Amarela', descricao='Molestiae quaerat distinctio, facere perferendis necessitatibus optio repellat alias commodi voluptatem velit corrupti natus exercitationem quos amet facilis sint nulla delectus.', imagem='tshirt_amarela.png', preco=32.00, stock=100, visivel=1, created_at='2021-02-06 19:45:20', updated_at='2021-02-06 19:45:27')
        Produto.objects.create(categoria='mulher',nome_produto='Vestido Vermelho', descricao='Labore voluptatem sed in distinctio iste tempora quo assumenda impedit illo soluta repudiandae animi earum suscipit, sequi excepturi inventore magnam velit voluptatibus.', imagem='vestido_vermelho.png', preco=75.20, stock=100, visivel=1, created_at='2021-02-06 19:45:21', updated_at='2021-02-06 19:45:27')
        Produto.objects.create(categoria='mulher',nome_produto='Vertido Azul', descricao='Provident ipsum earum magnam odit in, illum nostrum est illo pariatur molestias esse delectus aliquam ullam maxime mollitia tempore, sunt officia suscipit.', imagem='vestido_azul.png', preco=86.00, stock=100, visivel=1, created_at='2021-02-06 19:45:21', updated_at='2021-02-06 19:45:28')
        Produto.objects.create(categoria='mulher',nome_produto='Vestido Verde', descricao='Qui aliquid sed quisquam autem quas recusandae labore neque laudantium iusto modi repudiandae doloremque ipsam ad omnis inventore, cum ducimus praesentium. Consectetur!', imagem='vestido_verde.png', preco=48.85, stock=100, visivel=1, created_at='2021-02-06 19:45:22', updated_at='2021-02-06 19:45:28')
        Produto.objects.create(categoria='mulher',nome_produto='Vestido Amarelo', descricao='Aspernatur labore corporis modi quis temporibus eos hic? Sed fugiat, repudiandae distinctio, labore temporibus, non magni consectetur dolorum earum amet impedit nesciunt.', imagem='vestido_amarelo.png', preco=46.45, stock=100, visivel=1, created_at='2021-02-06 19:45:22', updated_at='2021-02-06 19:45:29')