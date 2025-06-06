# Projeto Clínica Odontológica 🦷

Este é um sistema web desenvolvido como Trabalho de Conclusão de Curso (TCC) para o curso técnico de Análise e Desenvolvimento de Sistemas, com foco no gerenciamento de uma clínica odontológica. O projeto permite o agendamento de consultas, cadastro de pacientes e profissionais, envio de e-mails automáticos, além de relatórios personalizados.

## 👨‍💻 Tecnologias Utilizadas

- Python 3.11+
- Django 4.x
- SQLite
- HTML5, CSS3 (com Bootstrap)
- JavaScript (básico)
- Biblioteca `smtplib` (para envio de e-mails)
- Pillow (para tratamento de imagens)
- PythonAnywhere (deploy)

## 📁 Estrutura do Projeto

O projeto contém as seguintes apps no Django:

- `cadastro_registro`: cadastro de pacientes e médicos
- `consulta`: exibição de consultas agendadas
- `marcar_consulta`: agendamento e formulário de consulta
- `esqueceu_senha`: recuperação de senha por e-mail
- `relatorios`: geração de relatórios PDF com dados de agendamentos

## ⚙️ Como Executar Localmente

1. **Clone o repositório:**

```bash
git clone https://github.com/KaueGracas/ProjetoClinica-KaueCardoso.git
cd ProjetoClinica-KaueCardoso
```

2. **Crie e ative um ambiente virtual:**

```bash
python -m venv venv
venv\Scripts\activate  # No Windows
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

4. **Aplique as migrações e crie o banco de dados:**

```bash
python manage.py migrate
```

5. **Crie um superusuário para acessar o admin:**

```bash
python manage.py createsuperuser
```

6. **Execute o servidor local:**

```bash
python manage.py runserver
```

7. **Acesse no navegador:**

```
http://127.0.0.1:8000/
```

## ✉️ Envio de E-mails

O sistema envia e-mails automaticamente em situações como:

- Criação de nova conta
- Redefinição de senha
- Confirmação de agendamento

> ⚠️ Use senhas de app específicas do Gmail para evitar bloqueios de segurança.

## 📊 Relatórios

No painel do administrador, é possível gerar relatórios em PDF com:

- Média de idade dos pacientes
- Porcentagem de homens e mulheres atendidos
- Porcentagem de exames realizados

## 👨‍🏫 Equipe

- Kaue Cardoso (Back-end Java / Python / Coordenação)


## 📄 Licença

Este projeto é de uso acadêmico, sem fins lucrativos.
