import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import time


if st.button("Press to continue"):
#    with st.spinner("Training ongoing"):
    st.balloons()
'''
# AI Checkers Quest


'''
st.write('An attempt of using Simple Reinforcement Q-learning for training AI to play italian checkers')
st.write()


st.title('Matias APP')
st.write("Here's our first attempt at using data to create a table:")
st.write(
    pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
    }))
"""
# My first app
Here's our first attempt at using data to create a table:
"""

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

df

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])

st.line_chart(chart_data)

map_data = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
                        columns=['lat', 'lon'])

st.map(map_data)

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'...and now we\'re done!'
