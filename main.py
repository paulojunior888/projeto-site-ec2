from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    ano_atual = datetime.datetime.now().year
    return f"""
    <h1>Bem-vindo ao meu primeiro servidor na nuvem!</h1>
    <p>Projeto de estudos DevOps criado por Edson.</p>
    <p>Horario do servidor: {datetime.datetime.now().strftime('%H:%M:%S')}</p>
    <p>Ano atual: {ano_atual}</p>
    """

if __name__ == '__main__':
    # Roda na porta 8080 e aceita conexões externas
    app.run(host='0.0.0.0', port=8080)
