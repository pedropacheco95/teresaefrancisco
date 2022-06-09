from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from teresaefrancisco.models import Product

bp = Blueprint('main', __name__)

@bp.route('/', methods=('GET', 'POST'))
def index():
    return render_template('main/index.html')

@bp.route('/faqs', methods=('GET', 'POST'))
def faqs():
    q_and_as = [
        {
            'question':' Os noivos querem mesmo estes presentes que estão na lista ou escolherem uns a despachar?',
            'answer': 'Todos os presentes da lista foram escolhidos com MUITO cuidado para quando vierem a nossa casa poderem ver o presente que nos ofereceram com tanto amor e carinho! Se não quiserem vir a nossa casa podem sempre passar na nossa página da lua de mel, estamos ansiosos por poder fazer scuba diving na Asia outra vez ehehe.'
        },
        {
            'question':"Como posso chegar à Quinta do Ribeiro?",
            'answer': 'As coordenadas de gps estão na página principal, mas podem pesquisar diretamente no google maps “Quinta do Ribeiro, Guisande”'
        },
        {
            'question':"Como devo ir vestido/a?",
            'answer': 'Os homens são convidados a vir de fraque. As senhoras apenas devem ter cuidado com os tacões fininhos pois o cocktail será todo em relva'
        },
        {
            'question':"Qual a melhor logística para transporte/dormidas?",
            'answer': 'Não existe uber nos arredores por isso aconselhamos a agendar transporte caso queiram ficar a dormir perto da Quinta. Os hoteis mais perto são em Braga, a cerca de 12/15 minutos de carro. Para além disso, temos a sorte de ter uma madrinha fantástica que vai organizar uma camioneta para quem estiver disposto a partir tudo até às 5 da manhã. Podem contactá-la diretamente: (Beatriz Magalhães 918 533 723)'
        },
        {
            'question':'Quanto tempo demora a viagem para o Ribeiro?',
            'answer': 'Ora bem depende da velocidade obviamente. Em principio será perto dos 35 minutos.'
        },
        {
            'question':"Se eu tiver uma restrição alimentar daquelas que posso mesmo ir parar ao hospital?",
            'answer': 'Por favor enviem-nos mensagem! (Ines: 912913005, Pedro: 918966340)'
        },
        {
            'question':"Sendo que são os noivos que estão a escrever estas perguntas e respostas não é um bocado estranho estarem a referir-se a eles próprios como 'Os noivos'?",
            'answer': 'Sim, é um bocado estranho. Não sabemos bem como justificar. Foi assim que saiu.'
        },
    ]
    return render_template('main/faqs.html',q_and_as=q_and_as)
