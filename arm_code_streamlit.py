import streamlit as st
fCol1,fCol2,fCol3,fCol4,fCol5 = st.columns(5,border=True,gap=None)
thumb_speed_mode = 3
pointer_speed_mode = 3
middle_speed_mode = 3
ring_speed_mode = 3
pinky_speed_mode = 3
with fCol1:
    st.write("THUMB SPEED")

    LC,MC,RC = st.columns(3)
    with MC:
        st.write(f"{thumb_speed_mode}")

with fCol2:
    st.write("POINTER SPEED")

    LC,MC,RC = st.columns(3)
    with MC:
        st.write(f"{pointer_speed_mode}")

with fCol3:
    st.write("MIDDLE SPEED")
    LC,MC,RC = st.columns(3)
    with MC:
        st.write(f"{middle_speed_mode}")
with fCol4:
    st.write("RING SPEED")
    LC,MC,RC = st.columns(3)
    with MC:
        st.write(f"{ring_speed_mode}")

with fCol5:
    st.write("PINKY SPEED")
    LC,MC,RC = st.columns(3)
    with MC:
        st.write(f"{pinky_speed_mode}")
st.write('---')
rCol1,rCol2,rCol3 = st.columns(3)

with rCol2:
    
    LC, MC1, RC = st.columns(3,gap=None)
