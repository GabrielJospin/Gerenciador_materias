import React, { Component } from 'react';
import logo from './logo.png';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Bem vindo ao Moodle </h2>
        </div>
        <p className="App-intro">
          Clique no menu acima para acessar o que deseja
        </p>
      </div>
    );
  }
}

export default App;
