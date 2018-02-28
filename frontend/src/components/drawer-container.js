import React from 'react';
import {connect} from 'react-redux';
import {bindActionCreators} from 'redux';

import Drawer from 'material-ui/Drawer';
import AppBar from 'material-ui/AppBar';
import MenuItem from 'material-ui/MenuItem';
import TextField from 'material-ui/TextField';
import Divider from 'material-ui/Divider';
import Chip from 'material-ui/Chip';
import LinearProgress from 'material-ui/LinearProgress';
import {List} from 'material-ui/List';

import TweetPresenter from './tweet-presenter';
import  * as queryActions from '../actions/query-action';


const styles = {
  textFieldStyle: {
    marginLeft: 10,
    marginRight: 20,
  },

  buttonStyle: {
    textAlign: 'center',
  },

  chip: {
    margin: 4,
  },

  chipWrapper: {
    display: 'flex',
    flexWrap: 'wrap',
  }
}


class DrawerContainer extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      textInput: '',
    }
  }

  handleText = (event, value) => {
    if(value[0] === ' ' || value[0] === '\n') {
      this.setState({textInput: ''});
      return;
    }
    let newValue = value.replace('\n', ''); //strip \n
    let newList = newValue.split(' ');
    for(let idx = 0; idx < newList.length; idx += 1) {
      if(newList[idx] === ' ' || newList[idx] === '' || newList[idx] === '\n') {
        newList[idx] = '';
      }
    }
    newValue = newList.join(' ');
    this.setState({textInput: newValue});
  }

  handleKeyPress = (event) => {
    if(event.key === 'Enter') {
      if(this.state.textInput === '' || this.state.textInput[0] === '' || this.state.textInput[0] === ' ' || this.state.textInput[0] === '\n') {
        this.setState({textInput: ""});
      }else {
        let curWord = this.state.textInput.replace('\n', '');
        this.props.queryActions.addWord(curWord);
        this.setState({textInput: ''});
      }
    }
  }

  handleHover = (tweet) => {
    this.props.queryActions.highlight(tweet);
  }

  clearHover = () => {
    this.props.queryActions.highlight({position: {lat: 0, lng: 0}});
  }

  chipClick = (curWord) => {
    this.props.queryActions.removeWord(curWord);
  }

  renderChip = (curWord, curIdx) => {
    return (
      <Chip
        key={curIdx}
        onClick={() => this.chipClick(curWord)}
        style={styles.chip}
      >
        {curWord}
      </Chip>
    )
  }

  render() {
    return (
      <Drawer open={true} openSecondary={true} width={'15%'}>
        <AppBar showMenuIconButton={false}/>

        <div style={styles.chipWrapper}>
          {this.props.keywords.map(this.renderChip, this)}
        </div>

        <div style={styles.textFieldStyle}>
          <TextField
            hintText="Input keywords here"
            value={this.state.textInput}
            multiLine={true}
            fullWidth={true}
            underlineShow={false}
            onChange={this.handleText}
            onKeyPress={this.handleKeyPress}
          />
        </div>

        <Divider/>
        <MenuItem style={styles.buttonStyle} onClick={() => this.props.queryActions.loadQuery()}>Search</MenuItem>
        <Divider/>
        {this.props.queryInProgress ? <LinearProgress mode={'indeterminate'}/> : <div/>}
        <Divider/>
        <MenuItem style={styles.buttonStyle} onClick={() => this.props.queryActions.reset()}>Clear</MenuItem>
        <Divider/>
        <List>
          {this.props.tweets.map((tweet, index) => {
            return (
              <TweetPresenter
                key={index}
                tweet={tweet}
                onHover={this.handleHover}
                onLeave={this.clearHover}
              />
            )
          })}
        </List>
      </Drawer>
    )
  }
}

function mapStateToProps(state) {
  return {
    keywords: state.queryReducer.keywords,
    resultObj: state.queryReducer.resultObj,
    tweets: state.queryReducer.tweets,
    queryInProgress: state.queryReducer.queryInProgress,
  };
}

function mapDispatchToPropos(dispatch) {
  return {
    queryActions: bindActionCreators(queryActions, dispatch)
  };
}

export default connect(mapStateToProps, mapDispatchToPropos)(DrawerContainer);
