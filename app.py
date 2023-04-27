import streamlit as st

from database import query_db
from plotting import plot_wells

def app():
    st.title('Wells in the US')
    st.markdown('Select the minimum depth and gradient to display:')
    
    depth = st.number_input('Min depth', 0, 10000, step=500, value=5000)
    gradient = st.number_input('Min gradient', 0., 0.1, value=0.01, step=0.005, format='%0.3f')
    
    data = query_db(depth, gradient)
    st.write(f'Data size: {len(data)}')
    st.write(plot_wells(data))

if __name__ == '__main__':
    app()
