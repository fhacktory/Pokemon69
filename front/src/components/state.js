//main libs
import React, { PropTypes } from 'react';

//Components


//App Logic
import history from '../businessLogic/history';

//Style Import
import RaisedButton from 'material-ui/lib/raised-button';
import TextField from 'material-ui/lib/text-field';
import Divider from 'material-ui/lib/divider';
import Paper from 'material-ui/lib/paper';
import FlatButton from 'material-ui/lib/flat-button';
import AutoComplete from 'material-ui/lib/auto-complete';
import CircularProgress from 'material-ui/lib/circular-progress';


import '../styles/components/state.scss';
import axios from 'axios';





var serverUrl = 'http://fhacktory-gsaynac.c9users.io/';



class State extends React . Component {

  constructor(props) {
    super(props);
    this.state = {
      dataSource: [],
      dataSourceCp: [],
      loading: false,
      metier:'',
      ville:'',
      liste: null
    };

    this._onClick = this._onClick.bind(this);
    this.getList = this.getList.bind(this);
    this.handleUpdateInput = this.handleUpdateInput.bind(this);
    this.handleUpdateInputCp = this.handleUpdateInputCp.bind(this);
  }

  componentDidMount() {
    //this.getList();
  }


  handleUpdateInput(t) {
    console.log('t', t);
    this.setState({
      dataSource: ['coiffeur', 'pub', 'plombier', 'restaurateur', 'moche', 'miche', 'mouche', 'mache']
    });
    this.setState({metier:t});
  }

  handleUpdateInputCp(t) {
    this.setState({
      dataSourceCp: ['lyon', 'Marseille', 'Caen', 'Rouen', 'organecity', 'Villeurbanne', 'nantes','paris']
    });
    this.setState({ville:t});
  }

  getList() {
    this.setState({
      loading: true
    });
    axios.get(serverUrl + 'search?city='+this.state.ville+'&job='+this.state.metier)
      .then((response) => {
        console.log('prout');
        console.log(response);

        this.setState({
          loading: false,
          liste:response.data.res
        });

      })
      .catch((response) => {
        console.log('prout 2');
        console.log(response);
        this.setState({
          loading: false
        });
      });
  }

  _onClick(event) {
    console.log('onclic');
    this.setState({liste:null});
    this.getList();
  }

  render() {
    var rendered ;
    var response = [];
    console.log('this.state.liste' + this.state.liste);
    if(this.state.liste){
        console.log('this.state.liste 2');
        console.log(this.state.liste)
        console.log('this.state.liste 2 end');
        this.state.liste.map((item, index, array)=>{
            console.log(item);
            response.push(
                <div key={index}> {item.name} - FB:{item.facebook.likes} - YELP:{item.yelp.rating}</div>);
        });
    }


    if (this.state.loading) {
        rendered = (<div><CircularProgress /></div>);
    } else {
        rendered = (
            <div><div>Hello dude !! </div>
            <AutoComplete
                hintText="Vous recherchez ? "
                dataSource={this.state.dataSource}
                onUpdateInput={this.handleUpdateInput}/>
            <AutoComplete
                hintText="Votre code postal "
                dataSource={this.state.dataSourceCp}
                onUpdateInput={this.handleUpdateInputCp}/>
            <RaisedButton label="Podium" primary={true} onClick={this._onClick} />
            <br/>
            {response}
            </div>);
    }

    return (<div>{rendered}</div>);
  }
}

export default State;
