import { createSlice } from "@reduxjs/toolkit";


export const matchesSlice = createSlice({
    name: "matches",
    initialState: {
        all_matches: [],
        isLoading: false,
        hasErrors: false
    },
    reducers: {

        getMatches: state => {
            state.isLoading = true
        },

        getMatchesSuccess: (state, { payload }) => {
            state.all_matches = payload
            state.isLoading = false
            state.hasErrors = false
        },


        getMatchesFailure: state => {
            state.hasErrors = true
        }
    }

})


export function fetchMatches() {
    return async dispatch => {
        dispatch(getMatches())

        try {
            const res = await fetch('http://localhost:5000/api/matches')
            const data = await res.json()

            dispatch(getMatchesSuccess(data))
        }
        catch (err) {
            console.log(err)
            dispatch(getMatchesFailure())
        }
    }
}

export const { getMatches, getMatchesSuccess, getMatchesFailure } = matchesSlice.actions
export default matchesSlice.reducer