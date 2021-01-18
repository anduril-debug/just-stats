import React from 'react';
import './App.css';
import Navbar from './components/Navbar';
import TableSection from './components/TableSection';
import ContentSection from './components/ContentSection';

function App() {
  return (
    <div className="App">

      <Navbar />

      <div className="container fill">
        <div className="contnet row">
          <TableSection />
          <ContentSection />
        </div>
      </div>
    </div>
  );
}

export default App;
