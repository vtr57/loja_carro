from django.test import TestCase
from ..models import Endereco

class EnderecoModelTest(TestCase):

    def setUp(self):
        '''
        Este método cria um objeto Endereco que será usado nos testes. Ele é executado antes de cada método de teste.
        '''
        self.endereco = Endereco.objects.create(
            rua='Rua das Flores',
            cidade='Florianópolis',
            estado='Santa Catarina',
            numero='123'
        )

    def test_endereco_creation(self):
        '''
        Verifica se o objeto Endereco foi criado corretamente e se a representação em string do objeto é a esperada.
        '''
        self.assertTrue(isinstance(self.endereco, Endereco))
        self.assertEqual(self.endereco.__str__(), self.endereco.rua)

    def test_rua_max_length(self):
        '''
        Verificam se o tamanho máximo dos campos está correto (255 caracteres).
        '''
        max_length = self.endereco._meta.get_field('rua').max_length
        self.assertEqual(max_length, 255)

    def test_cidade_max_length(self):
        '''
        Verificam se o tamanho máximo dos campos está correto (255 caracteres).
        '''
        max_length = self.endereco._meta.get_field('cidade').max_length
        self.assertEqual(max_length, 255)

    def test_estado_max_length(self):
        '''
        Verificam se o tamanho máximo dos campos está correto (255 caracteres).
        '''
        max_length = self.endereco._meta.get_field('estado').max_length
        self.assertEqual(max_length, 255)

    def test_numero_max_length(self):
        '''
        Verificam se o tamanho máximo dos campos está correto (255 caracteres).
        '''
        max_length = self.endereco._meta.get_field('numero').max_length
        self.assertEqual(max_length, 255)

    def test_endereco_str_method(self):
        '''
        Verifica se o método __str__ da classe Endereco retorna a string correta.
        '''
        self.assertEqual(str(self.endereco), 'Rua das Flores')

    def test_endereco_empty_fields(self):
        '''
        Testa a criação de um Endereco com campos vazios, esperando que levante um erro.
        '''
        with self.assertRaises(ValueError):
            Endereco.objects.create(
                rua='',
                cidade='',
                estado='',
                numero=''
            )

    def test_endereco_partial_fields(self):
        '''
        Testa a criação de um Endereco com alguns campos vazios, esperando que levante um erro.
        '''
        with self.assertRaises(ValueError):
            Endereco.objects.create(
                rua='Rua das Palmeiras',
                cidade='São Paulo',
                estado='',
                numero=''
            )



from ..models import Loja_Unidade
from phonenumber_field.phonenumber import PhoneNumber

class LojaUnidadeModelTest(TestCase):

    def setUp(self):
        '''
        Cria um objeto Endereco e um objeto Loja_Unidade que serão usados nos testes. Ele é executado antes de cada método de teste.
        '''
        self.endereco = Endereco.objects.create(
            rua='Rua das Flores',
            cidade='Florianópolis',
            estado='Santa Catarina',
            numero='123'
        )
        self.loja_unidade = Loja_Unidade.objects.create(
            nome='Loja Central',
            telefone=PhoneNumber.from_string(phone_number='+5511999999999', region='BR'),
            instagram='lojacentral',
            facebook='lojacentralfb',
            endereco_fk=self.endereco
        )

    def test_loja_unidade_creation(self):
        '''
        Verifica se o objeto Loja_Unidade foi criado corretamente e se a representação em string do objeto é a esperada.
        '''
        self.assertTrue(isinstance(self.loja_unidade, Loja_Unidade))
        self.assertEqual(self.loja_unidade.__str__(), self.loja_unidade.nome)

    def test_nome_max_length(self):
        '''
        Verifica se o tamanho máximo do campo nome está correto (255 caracteres).
        '''
        max_length = self.loja_unidade._meta.get_field('nome').max_length
        self.assertEqual(max_length, 255)

    def test_telefone_unique(self):
        '''
        Verifica se o campo telefone é único.
        '''
        field = self.loja_unidade._meta.get_field('telefone')
        self.assertTrue(field.unique)

    def test_instagram_max_length(self):
        '''
        Verificam se o tamanho máximo dos campos instagram e facebook está correto (255 caracteres).
        '''
        max_length = self.loja_unidade._meta.get_field('instagram').max_length
        self.assertEqual(max_length, 255)

    def test_facebook_max_length(self):
        '''
        Verificam se o tamanho máximo dos campos instagram e facebook está correto (255 caracteres).
        '''
        max_length = self.loja_unidade._meta.get_field('facebook').max_length
        self.assertEqual(max_length, 255)

    def test_endereco_fk(self):
        '''
        Verifica se a chave estrangeira endereco_fk está corretamente associada ao objeto Endereco.
        '''
        self.assertEqual(self.loja_unidade.endereco_fk, self.endereco)

    def test_loja_unidade_str_method(self):
        '''
        Verifica se o método __str__ da classe Loja_Unidade retorna a string correta.
        '''
        self.assertEqual(str(self.loja_unidade), 'Loja Central')

    def test_loja_unidade_empty_fields(self):
        '''
        Testa a criação de uma Loja_Unidade com campos vazios, esperando que levante um erro.
        '''
        with self.assertRaises(ValueError):
            Loja_Unidade.objects.create(
                nome='',
                telefone='',
                endereco_fk=self.endereco
            )

    def test_loja_unidade_partial_fields(self):
        '''
        Testa a criação de uma Loja_Unidade com alguns campos opcionais vazios (instagram e facebook), garantindo que eles sejam definidos como strings vazias.
        '''
        loja_unidade = Loja_Unidade.objects.create(
            nome='Loja Secundária',
            telefone=PhoneNumber.from_string(phone_number='+5511988888888', region='BR'),
            endereco_fk=self.endereco
        )
        self.assertEqual(loja_unidade.instagram, '')
        self.assertEqual(loja_unidade.facebook, '')



from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Vendedor, Endereco, Loja_Unidade
from phonenumber_field.phonenumber import PhoneNumber

class VendedorModelTest(TestCase):

    def setUp(self):
        '''
        Cria um objeto Endereco, um objeto Loja_Unidade, um objeto User e um objeto Vendedor que serão usados nos testes. Ele é executado antes de cada método de teste.
        '''
        self.endereco = Endereco.objects.create(
            rua='Rua das Flores',
            cidade='Florianópolis',
            estado='Santa Catarina',
            numero='123'
        )
        self.loja_unidade = Loja_Unidade.objects.create(
            nome='Loja Central',
            telefone=PhoneNumber.from_string(phone_number='+5511999999999', region='BR'),
            instagram='lojacentral',
            facebook='lojacentralfb',
            endereco_fk=self.endereco
        )

    def tearDown(self):
        '''
        Limpa a base de dados após cada teste.
        '''
        User.objects.all().delete()
        Vendedor.objects.all().delete()
        Endereco.objects.all().delete()
        Loja_Unidade.objects.all().delete()

    def create_vendedor(self, username, telefone='+5511988888888', instagram='vendedorinsta', facebook='vendedorfb'):
        vendedor = Vendedor.objects.create_user(
            username=username,
            password='password123',
            telefone=PhoneNumber.from_string(phone_number=telefone, region='BR'),
            instagram=instagram,
            facebook=facebook,
            loja_fk=self.loja_unidade
        )
        return vendedor

    def test_vendedor_creation(self):
        '''
        Verifica se o objeto Vendedor foi criado corretamente e se a representação em string do objeto é a esperada.
        '''
        vendedor = self.create_vendedor(username='vendedor1')
        self.assertTrue(isinstance(vendedor, Vendedor))
        self.assertEqual(str(vendedor), 'vendedor1')

    def test_telefone_unique(self):
        '''
        Verifica se o campo telefone é único.
        '''
        vendedor = self.create_vendedor(username='vendedor2')
        field = vendedor._meta.get_field('telefone')
        self.assertTrue(field.unique)

    def test_instagram_max_length(self):
        '''
        Verifica se o tamanho máximo do campo instagram está correto (255 caracteres).
        '''
        vendedor = self.create_vendedor(username='vendedor3')
        max_length = vendedor._meta.get_field('instagram').max_length
        self.assertEqual(max_length, 255)

    def test_facebook_max_length(self):
        '''
        Verifica se o tamanho máximo do campo facebook está correto (255 caracteres).
        '''
        vendedor = self.create_vendedor(username='vendedor4')
        max_length = vendedor._meta.get_field('facebook').max_length
        self.assertEqual(max_length, 255)

    def test_loja_fk(self):
        """
        Verifica se a chave estrangeira loja_fk está corretamente associada ao objeto Loja_Unidade.
        """
        vendedor = self.create_vendedor(username='vendedor5')
        self.assertEqual(vendedor.loja_fk, self.loja_unidade)

    def test_vendedor_str_method(self):
        '''
        Verifica se o método __str__ da classe Vendedor retorna a string correta.
        '''
        vendedor = self.create_vendedor(username='vendedor6')
        self.assertEqual(str(vendedor), 'vendedor6')

    def test_vendedor_empty_fields(self):
        '''
        Testa a criação de um Vendedor com campos obrigatórios vazios, esperando que levante um erro.
        '''
        with self.assertRaises(ValueError):
                Vendedor.objects.create_user(
                username='vendedor7',
                password='password123',
                telefone='',
                instagram='',
                facebook='',
                loja_fk=self.loja_unidade
            )

    def test_vendedor_partial_fields(self):
        '''
        Testa a criação de um Vendedor com alguns campos opcionais vazios (instagram e facebook), garantindo que eles sejam definidos como strings vazias.
        '''
        vendedor = self.create_vendedor(username='vendedor8', instagram='', facebook='')
        self.assertEqual(vendedor.instagram, '')
        self.assertEqual(vendedor.facebook, '')

    def test_vendedor_username_inheritance(self):
        """
        Verifica se o username do Vendedor é herdado corretamente do User.
        """
        vendedor = self.create_vendedor(username='vendedor9')
        self.assertEqual(vendedor.username, 'vendedor9')





from django.test import TestCase
from ..models import Carro

class CarroModelTest(TestCase):

    def setUp(self):
        """
        Cria um objeto Carro que será usado nos testes. Ele é executado antes de cada método de teste.
        """
        self.carro = Carro.objects.create(
            marca='Toyota',
            ano='2020',
            modelo='Corolla',
            preco=75000.00,
            km=15000,
            cor='Preto',
            opcionais='Ar condicionado, Direção hidráulica',
            descricao='Carro bem conservado, com baixa quilometragem.'
        )

    def test_carro_creation(self):
        '''
        Verifica se o objeto Carro foi criado corretamente e se a representação em string do objeto é a esperada.
        '''
        self.assertTrue(isinstance(self.carro, Carro))
        self.assertEqual(self.carro.__str__(), self.carro.marca)

    def test_marca_max_length(self):
        '''
         Verifica se o tamanho máximo do campo marca está correto (100 caracteres).
        '''
        max_length = self.carro._meta.get_field('marca').max_length
        self.assertEqual(max_length, 100)

    def test_ano_max_length(self):
        '''
        Verifica se o tamanho máximo do campo ano está correto (9 caracteres).
        '''
        max_length = self.carro._meta.get_field('ano').max_length
        self.assertEqual(max_length, 9)

    def test_modelo_max_length(self):
        '''
        Verifica se o tamanho máximo do campo modelo está correto (100 caracteres).
        '''
        max_length = self.carro._meta.get_field('modelo').max_length
        self.assertEqual(max_length, 100)

    def test_preco_max_digits(self):
        '''
        Verifica se o número máximo de dígitos do campo preco está correto (10 dígitos).
        '''
        max_digits = self.carro._meta.get_field('preco').max_digits
        self.assertEqual(max_digits, 10)

    def test_preco_decimal_places(self):
        '''
        Verifica se o número de casas decimais do campo preco está correto (2 casas decimais).
        '''
        decimal_places = self.carro._meta.get_field('preco').decimal_places
        self.assertEqual(decimal_places, 2)

    def test_km_is_integer(self):
        '''
        Verifica se o campo km é um inteiro.
        '''
        self.assertTrue(isinstance(self.carro.km, int))

    def test_cor_max_length(self):
        '''
        Verifica se o tamanho máximo do campo cor está correto (100 caracteres).
        '''
        max_length = self.carro._meta.get_field('cor').max_length
        self.assertEqual(max_length, 100)

    def test_opcionais_max_length(self):
        '''
        Verifica se o tamanho máximo do campo opcionais está correto (500 caracteres).
        '''
        max_length = self.carro._meta.get_field('opcionais').max_length
        self.assertEqual(max_length, 500)

    def test_descricao_max_length(self):
        '''
        Verifica se o tamanho máximo do campo descricao está correto (500 caracteres).
        '''
        max_length = self.carro._meta.get_field('descricao').max_length
        self.assertEqual(max_length, 500)

    def test_carro_str_method(self):
        '''
        Verifica se o método __str__ da classe Carro retorna a string correta.
        '''
        self.assertEqual(str(self.carro), 'Toyota')

    def test_carro_empty_fields(self):
        '''
        Testa a criação de um Carro com campos opcionais (opcionais e descricao) vazios, garantindo que eles sejam definidos como strings vazias.
        '''
        carro = Carro.objects.create(
            marca='Honda',
            ano='2018',
            modelo='Civic',
            preco=85000.00,
            km=20000,
            cor='Branco'
        )
        self.assertEqual(carro.opcionais, '')
        self.assertEqual(carro.descricao, '')

from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Cliente
from datetime import date

class ClienteModelTest(TestCase):
    
    def setUp(self):
        """
        Configura um vendedor e um cliente para usar nos testes.
        """
        self.endereco = Endereco.objects.create(
            rua='Rua das Flores',
            cidade='Florianópolis',
            estado='Santa Catarina',
            numero='123'
        )
        self.loja_unidade = Loja_Unidade.objects.create(
            nome='Loja Central',
            telefone=PhoneNumber.from_string(phone_number='+5511999999999', region='BR'),
            instagram='lojacentral',
            facebook='lojacentralfb',
            endereco_fk=self.endereco
        )
        self.vendedor = Vendedor.objects.create_user(
            username='vendedor',
            password='password123',
            telefone=PhoneNumber.from_string(phone_number='+5511999999999', region='BR'),
            instagram='instagram',
            facebook='facebook',
            loja_fk=self.loja_unidade
        )
        self.cliente = Cliente.objects.create_user(
            username="cliente1",
            password="password123",
            data_nascimento=date(1990, 1, 1),
            telefone="+5511999999999",
            avaliacao="Excelente cliente.",
            vendedor_fk=self.vendedor
        )

    def test_cliente_creation(self):
        """
        Testa a criação de um cliente.
        """
        cliente = Cliente.objects.get(username="cliente1")
        self.assertEqual(cliente.username, "cliente1")
        self.assertEqual(cliente.telefone, "+5511999999999")
        self.assertEqual(cliente.avaliacao, "Excelente cliente.")
        self.assertEqual(cliente.vendedor_fk, self.vendedor)

    def test_cliente_str(self):
        """
        Testa o método __str__ do modelo Cliente.
        """
        cliente = Cliente.objects.get(username="cliente1")
        self.assertEqual(str(cliente), cliente.username)

    def test_telefone_unique(self):
        """
        Testa se o campo telefone é único.
        """
        with self.assertRaises(Exception):
            Cliente.objects.create_user(
                username="cliente2",
                password="password123",
                data_nascimento=date(1992, 2, 2),
                telefone="+5511999999999",  # Telefone duplicado
                vendedor_fk=self.vendedor
            )

    def test_cliente_sem_avaliacao(self):
        """
        Testa a criação de um cliente sem avaliação.
        """
        cliente = Cliente.objects.create_user(
            username="cliente3",
            password="password123",
            data_nascimento=date(1993, 3, 3),
            telefone="+5511988888888",
            vendedor_fk=self.vendedor
        )
        self.assertEqual(cliente.avaliacao, None)

    def test_cliente_vendedor_relationship(self):
        """
        Testa a relação entre Cliente e Vendedor.
        """
        cliente = Cliente.objects.get(username="cliente1")
        self.assertEqual(cliente.vendedor_fk.username, "vendedor")
