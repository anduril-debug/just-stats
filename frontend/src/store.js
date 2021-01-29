import { configureStore } from '@reduxjs/toolkit';
import counter from './redux/counter/counterSlice';
import teams from './redux/teams/teamsSlice';


export default configureStore({
    reducer: {
        counter,
        teams
    }
})