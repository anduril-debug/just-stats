import { createSlice } from '@reduxjs/toolkit';


export const matchesSlice = createSlice({
    name: "matches",
    initialState: {
        lastFive: [],
        lastFiveLoading: false,
        lastFiveHasErrors: false,
    },
    reducers: {
        getLastFive: state => {
            state.lastFiveLoading = true
        },


        getLastFiveSuccess: (state, { payload }) => {
            state.lastFiveLoading = false
            state.lastFive = payload
        },


        getLastFiveFailure: state => {
            state.lastFiveHasErrors = true
            state.lastFiveLoading = false
        }

    }
})


export function fetchLastFive() {
    return async dispatch => {
        dispatch(getLastFive())

        try {

            const res = await fetch(`http://localhost:5000/api/all_last_five`)
            const data = await res.json()

            dispatch(getLastFiveSuccess(data))

        } catch (err) {
            dispatch(getLastFiveFailure())
        }


    }

}


export const matchesSelector = state => state.matches

export const { getLastFive, getLastFiveSuccess, getLastFiveFailure } = matchesSlice.actions
export default matchesSlice.reducer