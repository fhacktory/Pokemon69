//main libs
import React from 'react';
import { render } from 'react-dom';

//App Logic
import history from '../businessLogic/history';

//Style Import
import RaisedButton from 'material-ui/lib/raised-button';
import './../styles/components/app.scss';


class App extends React.Component {
  constructor(props) {
    super(props);
    this._testMethod = this._testMethod.bind(this);
    this.user = JSON.parse('{}');
    this.session = JSON.parse('{}');
  }

  getChildContext() {
    //check si user connecté
    //et si connecté le met dans le contexte
    return {
      user: this.user,
      session: this.session
    };
  }

  componentDidMount() {
    //at the start of the app, if no id -> go to state per default

  }

  _testMethod() {
    //history.replaceState(null, '/state/default');
  }



  render() {

    return (
      <div>
        <div className="row" id="app-container">
          {this.props.children}
        </div>
      </div>
    );
  }
}

// to have user in the context for the children of Component App
App.childContextTypes = {
  user: React.PropTypes.object,
  session: React.PropTypes.object,
  domain: React.PropTypes.string
};

export default App;
