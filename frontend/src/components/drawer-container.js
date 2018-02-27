import React from 'react';
import {connect} from 'react-redux';
import {bindActionCreators} from 'redux';

import Drawer from 'material-ui/Drawer';
import AppBar from 'material-ui/AppBar';
import MenuItem from 'material-ui/MenuItem';

class DrawerContainer extends React.Component {
  render() {
    return (
      <Drawer open={true} openSecondary={true} width={'15%'}>
        <AppBar showMenuIconButton={false}/>
        <MenuItem>A tweet</MenuItem>
      </Drawer>
    )
  }
}

function mapStateToProps(state) {
  return {};
}

function mapDispatchToPropos(dispatch) {
  return {};
}

export default connect(mapStateToProps, mapDispatchToPropos)(DrawerContainer);
