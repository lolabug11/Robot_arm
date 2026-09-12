import streamlit as st
fCol1,fCol2,fCol3,fCol4,fCol5 = st.columns(5,border=True,gap=None)
if 'thumb_speed_mode' not in st.session_state:
    st.session_state['thumb_speed_mode'] = 3
if 'pointer_speed_mode' not in st.session_state:
    st.session_state['pointer_speed_mode'] = 3
if 'middle_speed_mode' not in st.session_state:
    st.session_state['middle_speed_mode'] = 3
if 'ring_speed_mode' not in st.session_state:
    st.session_state['ring_speed_mode'] = 3
if 'pinky_speed_mode' not in st.session_state:
    st.session_state['pinky_speed_mode'] = 3

with fCol1:
    st.write("THUMB SPEED")

    LC,MC,RC = st.columns(3)
    with MC:
        st.write(f"{st.session_state['thumb_speed_mode']}")

with fCol2:
    st.write("POINTER SPEED")

    LC,MC,RC = st.columns(3)
    with MC:
        st.write(f"{st.session_state['pointer_speed_mode']}")

with fCol3:
    st.write("MIDDLE SPEED")
    LC,MC,RC = st.columns(3)
    with MC:
        st.write(f"{st.session_state['middle_speed_mode']}")
with fCol4:
    st.write("RING SPEED")
    LC,MC,RC = st.columns(3)
    with MC:
        st.write(f"{st.session_state['ring_speed_mode']}")

with fCol5:
    st.write("PINKY SPEED")
    LC,MC,RC = st.columns(3)
    with MC:
        st.write(f"{st.session_state['pinky_speed_mode']}")
st.write('---')
rCol1,rCol2,rCol3 = st.columns([1,10,2],gap=None,border=False)
if 'selected' not in st.session_state:
    st.session_state['selected'] = None
if 'select' not in st.session_state:
    st.session_state['select'] = False
with rCol2:
    
    LC, MC1, RC = st.columns(3,gap=None)
    with MC1:
        a = st.container(border=True,width="stretch",height="content")
        

















        with a:


            col1,col2,col3 = st.columns(3,width='stretch',gap=None)
            with col1:



                if st.button("ch-"):
                    if st.session_state['selected']:
                        
                        if st.session_state['selected'] == 1:
                            if st.session_state['thumb_speed_mode'] > 1:
                                st.session_state['thumb_speed_mode'] -= 1
                        elif st.session_state['selected'] == 2:
                            if st.session_state['pointer_speed_mode'] > 1:
                                st.session_state['pointer_speed_mode'] -= 1
                        elif st.session_state['selected'] == 3:
                            if st.session_state['middle_speed_mode'] > 1:
                                st.session_state['middle_speed_mode'] -= 1
                        elif st.session_state['selected'] == 4:
                            if st.session_state['ring_speed_mode'] > 1:
                                st.session_state['ring_speed_mode'] -= 1
                        elif st.session_state['selected'] == 5:
                            if st.session_state['pinky_speed_mode'] > 1:
                                st.session_state['pinky_speed_mode'] -= 1
                        st.session_state['select'] = False
                        st.session_state['selected'] = None
                        st.rerun()
                if st.button("|<<"):
                    _ = None
                if st.button("0"):
                    _ = None
                if st.button("1"):
                    if st.session_state['select']:
                        st.session_state['select'] = False
                        st.session_state['selected'] = 1
                if st.button("4"):
                    if st.session_state['select']:
                        st.session_state['select'] = False
                        st.session_state['selected'] = 4
                if st.button("7"):
                    _ = None
            with col2:
                if st.button("ch"):
                    st.session_state['select'] = True
                if st.button(">>|"):
                    _ = None
                if st.button("+10"):
                    _ = None
                if st.button("2"):
                    if st.session_state['select']:
                        st.session_state['select'] = False
                        st.session_state['selected'] = 2
                if st.button("5"):
                    if st.session_state['select']:
                        st.session_state['select'] = False
                        st.session_state['selected'] = 5
                if st.button("8"):
                    _ = None


            with col3:
                if st.button("ch+"):
                    print(f"{st.session_state['selected']}")
                    if st.session_state['selected']:
                        print('FUCKFUCKFUCKFUCKFUCKFUCK')
                        if st.session_state['selected'] == 1:
                            if st.session_state['thumb_speed_mode'] < 5:
                                st.session_state['thumb_speed_mode'] += 1
                        elif st.session_state['selected'] == 2:
                            if st.session_state['pointer_speed_mode'] < 5:
                                st.session_state['pointer_speed_mode'] += 1
                        elif st.session_state['selected'] == 3:
                            if st.session_state['middle_speed_mode'] < 5:
                                st.session_state['middle_speed_mode'] += 1
                        elif st.session_state['selected'] == 4:
                            if st.session_state['ring_speed_mode'] < 5:
                                st.session_state['ring_speed_mode'] += 1
                        elif st.session_state['selected'] == 5:
                            if st.session_state['pinky_speed_mode'] < 5:
                                st.session_state['pinky_speed_mode'] += 1
                        st.session_state['select'] = False
                        st.session_state['selected'] = None
                        st.rerun()
                if st.button("|   |"):
                    _ = None
                if st.button("+20"):
                    _ = None
                if st.button("3"):
                    if st.session_state['select']:
                        st.session_state['select'] = False
                        st.session_state['selected'] = 3
                if st.button("6"):
                    _ = None
                if st.button("9"):
                    _ = None
