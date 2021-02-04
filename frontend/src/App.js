import React, { useEffect } from 'react';
import './App.css';
import Navbar from './components/Navbar';
import Content from './components/Content';
import { useDispatch } from 'react-redux';

import { fetchTeams } from './redux/teams/teamsSlice';
import { fetchLastFive } from './redux/matches/matchesSlice';

function App() {


  const dispatch = useDispatch()



  useEffect(() => {
    dispatch(fetchTeams())
    dispatch(fetchLastFive())
  }, [dispatch])

  return (
    <div className="App">
      <Navbar />
      <div className="container">
        <Content />

      </div>
    </div>
  );
}

export default App;
