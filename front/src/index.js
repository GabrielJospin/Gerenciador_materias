import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

ReactDOM.render(
  <App />,
  document.getElementById('root')
);

import ListarMaterias from "./webpages/listarMaterias"
import Header from "./components/Header"
import {Route, Router, Switch} from "react-router-dom";
import App from './App';

const Webpages = () => {
    return(
        <div>
            <Router>
                <Header />
                <Switch>
                    <Route exact path="/" component={App}/>
                    <Route path="/Materias" component={ListarMaterias}/>

                </Switch>

            </Router>
        </div>
    );
};