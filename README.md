Este projeto é uma plataforma de adoção de animais. Ele permite que os usuários cadastrem seus animais para adoção, bem como visualizem animais disponíveis para adoção.

O projeto é construído usando o framework Django para o back-end e Bootstrap para o front-end. Ele segue as melhores práticas de desenvolvimento web, incluindo validação de formulários, upload de imagens e gerenciamento de sessão de usuário.

O projeto inclui as seguintes funcionalidades:

Cadastro de animais para adoção, incluindo upload de imagem
Visualização de animais disponíveis para adoção
Sistema de gerenciamento de sessão de usuário para restringir o acesso a funcionalidades específicas
Validação de formulários para garantir que os dados fornecidos sejam válidos
Existem algumas melhorias planejadas para o projeto, incluindo:

Adição de um sistema de busca para ajudar os usuários a encontrar animais específicos
Adição de uma página de perfil de usuário para exibir animais que um usuário cadastrou para adoção
Adição de uma opção de contato para que os usuários possam entrar em contato com o dono do animal
Adição de uma seção de FAQ para responder perguntas comuns sobre o processo de adoção.
Este projeto é um trabalho em andamento, e qualquer contribuição é bem-vinda. Se você tiver alguma sugestão ou encontrar algum problema, por favor, abra uma issue no GitHub.

Instalação

Para instalar o projeto, siga os seguintes passos:

Clone o repositório: git clone https://github.com/seu-usuario/petmatch
Entre na pasta do projeto: cd petmatch
Instale as dependências: pip install -r requirements.txt
Rode as migrações: python manage.py migrate
Inicie o servidor: python manage.py runserver
Uso

Ao acessar a página inicial, apos fazer o cadastro é possível ver uma lista com todos os animais disponíveis para adoção. É possível filtrar essa lista por  raça e localização.

Também é possível cadastrar um animal perdido ou disponível para adoção. Para isso, basta acessar o menu "Quero divulgar" e preencher o formulário.

Além disso, é possível ver os animais que você já divulgou e excluí-los caso necessário.

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
