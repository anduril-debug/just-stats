import { createSlice } from '@reduxjs/toolkit';


export const teamsSlice = createSlice({
    name: 'teams',
    initialState: {
        isLoading: false,
        hasError: false,
        teams: []
    },
    reducers: {
        getTeams: state => {
            state.isLoading = true
        },

        getTeamsSuccess: (state, { payload }) => {
            state.isLoading = false,
                state.hasError = false,
                state.teams = payload
        },

        getTeamsFailure: state => {
            state.isLoading = false,
                state.hasError = true
        }
    }

})

export function fetchTeams() {

    return async dispatch => {
        dispatch(getTeams())


        try {
            const res = await fetch('http://127.0.0.1:5000/api/teams')
            const data = await res.json()

            dispatch(getTeamsSuccess(data))
        } catch (err) {
            dispatch(getTeamsFailure(err))
        }
    }


}




export const { getTeams, getTeamsSuccess, getTeamsFailure } = teamsSlice.actions
export const teamsSelector = state => state.teams

export default teamsSlice.reducer