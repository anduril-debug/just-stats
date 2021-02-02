import { configureStore } from '@reduxjs/toolkit';
import counter from './redux/counter/counterSlice';
import teams from './redux/teams/teamsSlice';
import matches from './redux/matches/matchesSlice';


export default configureStore({
    reducer: {
        counter,
        teams,
        matches
    }
})