import React from 'react';
import {connect} from 'react-redux';
import {bindActionCreators} from 'redux';

import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AppBar from 'material-ui/AppBar';

import MapContainer from './map-container';
import DrawerContainer from './drawer-container';

const styles = {
  mapStyle: {
    marginRight: '15%',
    height: window.innerHeight - 64, // 64 is the height of AppBar
  }
};

class HomeContainer extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      textAlign: "center",
      verticalAlign: "middle"
    }
  }

  render() {
    return (<MuiThemeProvider>
      <div>
        <AppBar title="TweetPortal"/>
        <DrawerContainer/>
        <div style={styles.mapStyle}>
          <MapContainer/>
        </div>
      </div>
    </MuiThemeProvider>)
  }
}

function mapStateToProps(state) {
  return {};
}

function mapDispatchToPropos(dispatch) {
  return {};
}

export default connect(mapStateToProps, mapDispatchToPropos)(HomeContainer);
