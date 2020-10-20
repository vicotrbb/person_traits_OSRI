import streamlit as st
import numpy as np
import pandas as pd
import json

def main():
    load_data()
    st.title('Questionario - Open Sex Role Inventory')
    st.text(
        """
            Olá, bem vindo!
            
            Este questionario foi baseado em um estudo chamado Open Sex-Role Inventory, realizado originalmente por Sandra Bam e visava ser capaz de estudar e prever a 
            sexualidade das pessoas utilizando uma serie de perguntas. Atualmente, este questionario é muito mais amplo(apesar de parecer dubio) e mede a sexualidade de um
            individuo de forma mais complexa.
            
            A ideia deste questionario que você está prestes a fazer não tem nada haver com o objetivo original do teste, mas, em utilizar os dados fornecidos pelos 
            pesquisadores responsáveis para prever algumas outras informações da sua pessoa, sendo meramente um experimento envolvendo Estatística, Inteligencia Artificial 
            e Programação.
            
            Os dados informados aqui são completamente anónimos e utilizados apenas para propositos de medição da qualidade do modelo de decisão utilizado no experimento.
            
            O questionario deve ser respondido da seguinte forma: 
                Você será exposto a 44 perguntas que devem ser respondidas utilizando um slider de intensidade, onde o valor 1(mais baixo) representa total discordancia com a 
                afirmação, o valor 3(Médio) representa neutralidade sobre a pergunta e o valor 5(Mais alto) representa total concordancia com a pergunta.
            
            Dessa forma, você deve responder o questionario da forma mais honesta possível. Boa sorte!
            
            1 - Discordo totalmente;
            2 - Discordo;
            3 - Neutro;
            4 - Concordo;
            5 - Concordo totalmente.
        """
    )
    
    # Question sliders
    Q1 = st.slider(
        label='Eu estudei como ganhar apostando',
        min_value=1, 
        max_value=5,
        step=1)
    
    Q2 = st.slider(
        label='Eu penso em pintar meu cabelo',
        min_value=1, 
        max_value=5,
        step=1)
    
    Q3 = st.slider(
        label='Eu gosto de arremessar facas, machados e outras coisas cortantes',
        min_value=1, 
        max_value=5,
        step=1)
        
    Q4 = st.slider(
        label='Eu presenteio as pessoas com presentes feitos a mão',
        min_value=1, 
        max_value=5,
        step=1)
    
    Q5 = st.slider(
        label='Eu tenho sonhos em que estou salvando alguém de um prédio em chamas',
        min_value=1, 
        max_value=5,
        step=1)
        
    Q6 = st.slider(
        label='Eu fico envergonhado quando alguém lê algo que eu escrevi',
        min_value=1, 
        max_value=5,
        step=1)
            
    Q7 = st.slider(
        label='Eu ja estive/estou muito interessadas em guerras históricas',
        min_value=1, 
        max_value=5,
        step=1)
    
    Q8 = st.slider(
        label='Eu sei os aniversários dos meus amigos',
        min_value=1, 
        max_value=5,
        step=1)
    
    Q9 = st.slider(
        label='Eu gosto de armas de fogo',
        min_value=1, 
        max_value=5,
        step=1)
        
    Q10 = st.slider(
        label='Eu fico mais feliz quando estou na minha cama',
        min_value=1, 
        max_value=5,
        step=1)
    
    Q11 = st.slider(
        label='Eu não trabalhei/estudei muito no ensino médio',
        min_value=1, 
        max_value=5,
        step=1)
    
    Q12 = st.slider(
        label='Eu uso loção para minhas mãos',
        min_value=1, 
        max_value=5,
        step=1)
    
    Q13 = st.slider(
        label='Eu prefiro ter aulas de matemática do que aulas de artes manuais',
        min_value=1, 
        max_value=5,
        step=1)
    
    Q14 = st.slider(
        label='Eu danço quando estou sozinho',
        min_value=1, 
        max_value=5,
        step=1)
    
    Q15 = st.slider(
        label='Eu penso/pensei que seria muito excitante se tornar um fora da lei',
        min_value=1, 
        max_value=5,
        step=1)
    
    Q16 = st.slider(
        label='Quando eu era criança, eu costumava brincar de fingir que estava em uma banda com meus amigos',
        min_value=1, 
        max_value=5,
        step=1)
    
    Q17 = st.slider(
        label='Eu considero/considerei entrar para as forças armadas',
        min_value=1, 
        max_value=5,
        step=1)
    
    Q18 = st.slider(
        label='Eu fico tonto quando me levanto bruscamente',
        min_value=1, 
        max_value=5,
        step=1)
    
    Q19 = st.slider(
        label='Eu não considero normal ficar com raiva/triste ao ouvir sobre a morte de pessoas que você não conhece',
        min_value=1, 
        max_value=5,
        step=1)
    
    Q20 = st.slider(
        label='Algumas vezes eu choro quando fico com muita raiva',
        min_value=1, 
        max_value=5,
        step=1)
    
    Q21 = st.slider(
        label='Eu não lembro de datas de aniversários',
        min_value=1, 
        max_value=5,
        step=1)
    
    Q22 = st.slider(
        label='Eu guardo as cartas que eu recebo',
        min_value=1, 
        max_value=5,
        step=1)
    
    Q23 = st.slider(
        label='Eu brinco de xingar meus amigos e não me importo que façam o mesmo',
        min_value=1, 
        max_value=5,
        step=1)
    
    Q24 = st.slider(
        label='Sou contra experimentos médicos em animais',
        min_value=1, 
        max_value=5,
        step=1)
    
    Q25 = st.slider(
        label='Eu posso fazer uma quantidade incrível de flexões',
        min_value=1, 
        max_value=5,
        step=1)
    
    Q26 = st.slider(
        label='Eu pulo quando fico muito animado',
        min_value=1, 
        max_value=5,
        step=1)
    
    Q27 = st.slider(
        label='Eu penso que um desastre natural poderia ser divertido',
        min_value=1, 
        max_value=5,
        step=1)

    Q28 = st.slider(
        label='Eu ando com um cobertor pela casa',
        min_value=1, 
        max_value=5,
        step=1)
    
    Q29 = st.slider(
        label='Eu costumava/costumo queimar coisas com a luz do sol e uma lupa',
        min_value=1, 
        max_value=5,
        step=1)
    
    Q30 = st.slider(
        label='Eu acho o horóscopo divertido',
        min_value=1, 
        max_value=5,
        step=1)
    
    Q31 = st.slider(
        label='Eu não levo muita bagagem quando viajo',
        min_value=1, 
        max_value=5,
        step=1)
    
    Q32 = st.slider(
        label='Eu ja pensei/penso em me tornar vegetariano',
        min_value=1, 
        max_value=5,
        step=1)
    
    Q33 = st.slider(
        label='Eu odeio sair as compras',
        min_value=1, 
        max_value=5,
        step=1)
    
    Q34 = st.slider(
        label='Eu tenho/tive um diario pessoal que guardo até hoje',
        min_value=1, 
        max_value=5,
        step=1)
    
    Q35 = st.slider(
        label='Eu desmontei/desmonto maquinas apenas para ver como elas funcionam',
        min_value=1, 
        max_value=5,
        step=1)
    
    Q36 = st.slider(
        label='Eu tenho muitas fotos das coisas que eu fiz/faço',
        min_value=1, 
        max_value=5,
        step=1)
    
    Q37 = st.slider(
        label='Eu ja joguei/jogo muitos video games',
        min_value=1, 
        max_value=5,
        step=1)
    
    Q38 = st.slider(
        label='De vez em quando deixo boas mensagens para as pessoas',
        min_value=1, 
        max_value=5,
        step=1)
    
    Q39 = st.slider(
        label='Eu ja botei fogo em vários tipos de combustíveis apenas por diversão',
        min_value=1, 
        max_value=5,
        step=1)
    
    Q40 = st.slider(
        label='Eu realmente gosto de dançar',
        min_value=1, 
        max_value=5,
        step=1)
    
    Q41 = st.slider(
        label='Em uma escada, subo dois degraus de cada vez',
        min_value=1, 
        max_value=5,
        step=1)
    
    Q42 = st.slider(
        label='Eu cozinho doces e coisas gostosas para mim mesmo as vezes',
        min_value=1, 
        max_value=5,
        step=1)
    
    Q43 = st.slider(
        label='Eu penso que um desastre natural poderia ser divertido',
        min_value=1, 
        max_value=5,
        step=1)
    
    Q44 = st.slider(
        label='Eu decoro meus pertences(Ex: adesivos no notebook)',
        min_value=1, 
        max_value=5,
        step=1)
    
    # Features array
    features = [
        Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10,Q11,Q12,Q13,Q14,
        Q15,Q16,Q17,Q18,Q19,Q20,Q21,Q22,Q23,Q24,Q25,Q26,
        Q27,Q28,Q29,Q30,Q31,Q32,Q33,Q34,Q35,Q36,Q37,Q38,
        Q39,Q40,Q41,Q42,Q43,Q44
    ]
    
@st.cache
def load_data():
    pass

if __name__ == "__main__":
    main()
    
if __name__ != "__main__":
    main()
