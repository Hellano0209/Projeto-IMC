#### PROJETO IMC ####

import streamlit as st

st.title('Calculadora de Índice de Massa Corpórea (IMC)')

with st.expander('Saiba mais sobre o IMC'):
     st.write("""
         O IMC é um índice, criado na década de 30 por um estatístico belga, com o objetivo de medir de forma quantitativa aspéctos da saúde de um indivíduo.\n
         Em geral, pessoas com um índice de massa corporal mais alto têm mais gordura corporal, e é possível associá-lo às taxas de obesidade. Também é possível associar IMCs muito baixos e muito altos com uma maior taxa de mortalidade precoce.\n
         É importante salientar que a precisão e a utilidade do IMC envolvem muitos outros fatores, pois o índice não é capaz de calcular, por exemplo, qual porcentagem do peso de uma pessoa é composto por gordura, músculo ou osso. Por exemplo, os fisiculturistas tendem a ter um IMC alto, mas com pouca gordura corporal. Então o IMC é apenas **um** indicador que pode ser útil para avaliar a saúde de indivíduo se utilizados em conjunto com outros indicadores e exames.         
             """)

col1, col2, col3 = st.columns(3)

with col1:
    st.number_input('Altura em metros', min_value = 0.00, step = 0.5, key = 'altura')

with col2:
    st.number_input('Peso em kg', min_value = 0, key = 'kg')    

if (st.session_state.kg > 0 and st.session_state.altura > 0):
    imc = st.session_state.kg/pow(st.session_state.altura, 2)
    
    pmin = 18.5*pow(st.session_state.altura, 2)
    pmax = 24.9*pow(st.session_state.altura, 2)
    
    with col3:
        st.metric(label='Seu IMC é igual a', value = round(imc, 2))
    
    if imc < 18.5:
        st.write('Você está abaixo do peso. Para a sua altura o seu peso deve está entre: {} kg e {} kg'.format(round(pmin), round(pmax)))
    
    elif imc >= 18.5 and imc <=24.9:
        st.write('O seu peso pe considerado normal.')
    
    elif imc > 24.9 and imc < 29.9:
        st.write('Você está com excesso de peso. Para a sua altura o seu peso deve está entre: {} kg e {} kg'.format(round(pmin), round(pmax)))
    
    else:
        st.write('Você está obeso(a). Para a sua altura o seu peso deve está entre: {} kg e {} kg'.format(round(pmin), round(pmax)))
            
   
