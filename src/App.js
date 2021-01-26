import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'
import './App.css';
import Landing from './Pages/landing';
import Home from './Pages/home';
import UnparPage from './Pages/unpar_sketch';

function App() {
  return (
    <div id="main">
      <Router>
        <Switch>
          <Route exact path="/" component={Landing} />
          <Route exact path="/home" component={Home} />
          <Route exact path="/unpar" component={UnparPage} />
        </Switch>
      </Router>
    </div>
  );
}

export default App;
