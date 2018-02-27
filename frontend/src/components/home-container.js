import React from 'react';
import {connect} from 'react-redux';
import {bindActionCreators} from 'redux';

import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AppBar from 'material-ui/AppBar';

import MapContainer from './map-container';
import DrawerContainer from './drawer-container';

const styles = {
  map: {
    marginRight: '15%',
    height: '80%',
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
        <div style={styles.map}>
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
