# Aplicação Django - Topics

Esta aplicação foi desenvolvida no âmbito da Unidade Curricular de Laboratório de Programação, utilizando a framework Django, e permite que os utilizadores criem, editem e façam a gestão dos tópicos e dos comentários. Esta aplicação é ideal para explorar funcionalidades básicas da framework Django, incluindo autenticação, manipulação de formulários e proteção de rotas, recorrendo ainda a bibliotecas de terceiros para adicionar funcionalidades ou até mesmo melhorar a experiência do utilizador.

## *Principais Funcionalidades*
1. *Listagem de Tópicos*
   - São apresentados todos os tópicos existentes, com o seu título e a respetiva descrição. 

2. *Detalhes de um Tópico*
   - São apresentados os detalhes do tópico e os comentários associados a este.

3. *Criação de Tópicos*
   - Formulário para a criação de novos tópicos.

4. *Adição de Comentários*
   - Formulário para a adição de comentários a um tópico existente.

5. *Edição e Remoção de Tópicos e Comentários*
   - O autor de um determinado tópico ou comentário, tem a opção de editar ou até mesmo remover o mesmo.

---

## *Requisitos*

Para dar run à aplicação, aconselha-se a criação de um ambiente virtual para se poder isolar as dependências do mesmo recorrendo ao comando:

`python -m venv venv`

Depois, para se ativar o mesmo coloca-se 'venv\Scripts\activate' e para se instalar as dependências necessárias coloca-se:

`pip install -r requirements.txt`