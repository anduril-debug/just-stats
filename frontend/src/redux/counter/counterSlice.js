import { createSlice } from '@reduxjs/toolkit';



export const counterSlice = createSlice({
    name: 'counter',
    initialState: {
        value: 0,
        someTestString: "LUKA LORTK"
    },
    reducers: {
        increment: state => {
            state.value += 1
        },
        dicrement: state => {
            state.value -= 1
        },
        incrementByAmount: (state, amount) => {
            state.value += amount.payload
        }
    }
})

export const { increment, dicrement, incrementByAmount } = counterSlice.actions;

export const incrementAsync = amount => dispatch => {
    setTimeout(() => {
        dispatch(incrementByAmount(amount))
    }, 2000)
}

export const selectCount = state => state.counter.value;

export default counterSlice.reducer;