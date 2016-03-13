//main libs
import React from 'react';
import { render } from 'react-dom';
import { Router, Route, Link, BrowserHistory, Redirect, DefaultRoute } from 'react-router';

//Components
import State from './components/state';
import App from './components/app';

//App Logic
import history from './businessLogic/history';

//Style Import
import './styles/foundation.css';
import './styles/styles.scss';


//Needed for onTouchTap
import injectTapEventPlugin from 'react-tap-event-plugin';
injectTapEventPlugin();

let unlisten = history.listen(function(location) {
  if (location.pathname == '/' || !location.pathname) {
    history.pushState(null, '/state/default');
    return;
  }
});




render(
  <Router history={history}>
    <Route path="/" component={App}>
      <Route path="state/" component={State} />
      <Route path="*" component={State}/>
    </Route>
  </Router>
  , document.getElementById('app')
);
