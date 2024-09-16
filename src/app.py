import streamlit as st
from monty_hall import monty_hall_game
import time

st.title(":zap: Monty Hall Simulation")

st.image("https://static.scientificamerican.com/sciam/assets/media/interactive/monty-hall/stage_1-5.png", width=500)

n = st.number_input("Enter number of simulation",
                min_value=1, max_value=100000,
                value=100
)

col1, col2 = st.columns(2)
col1.subheader('Win percentage Without Switching') 
col2.subheader('Win percentage with Swiching')




chart1 = col1.line_chart(x=None, y=None, height=400)
chart2 = col2.line_chart(x=None, y=None, height=400)

wins_no_switch1 = 0
wins_switch1 = 0

for i in range(n):
    wins_no_switch = monty_hall_game(False, 1)
    wins_switch = monty_hall_game(True, 1)

    wins_no_switch1 += wins_no_switch
    wins_switch1 += wins_switch

    chart1.add_rows([wins_no_switch1 / (i + 1)])
    chart2.add_rows([wins_switch1 / (i + 1)])

    time.sleep(0.02)