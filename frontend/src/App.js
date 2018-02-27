import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

import { Provider, connect } from 'react-redux';
import HomeContainer from './components/home-container';
import store from './store';

class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <HomeContainer/>
      </Provider>
    );
  }
}


export default App;
