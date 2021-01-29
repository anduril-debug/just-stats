import React, { useEffect } from 'react';
import './App.css';
import Navbar from './components/Navbar';
import Content from './components/Content';
import Table from './components/Table';
import { useDispatch } from 'react-redux';


import { fetchTeams } from './redux/teams/teamsSlice';



function App() {


  const dispatch = useDispatch()
  // const { isLoading, hasError, teams } = useSelector(teamsSelector)


  useEffect(() => {
    dispatch(fetchTeams())
  }, [dispatch])

  return (
    <div className="App">
      <Navbar />
      <div className="container">
        <Content />
        <Table />

      </div>
    </div>
  );
}

export default App;
