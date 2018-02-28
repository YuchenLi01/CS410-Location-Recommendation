import React from 'react';
import {connect} from 'react-redux';
import {bindActionCreators} from 'redux';

import Drawer from 'material-ui/Drawer';
import AppBar from 'material-ui/AppBar';
import MenuItem from 'material-ui/MenuItem';
import TextField from 'material-ui/TextField';
import Divider from 'material-ui/Divider';
import Chip from 'material-ui/Chip';


const styles = {
  textFieldStyle: {
    marginLeft: 10,
    marginRight: 20,
  },

  buttonStyle: {
    textAlign: 'center',
  },
}


class DrawerContainer extends React.Component {
  render() {
    return (
      <Drawer open={true} openSecondary={true} width={'15%'}>
        <AppBar showMenuIconButton={false}/>

        <div style={styles.textFieldStyle}>
          <TextField
            hintText="Input keywords here"
            multiLine={true}
            fullWidth={true}
            underlineShow={false}
          />
        </div>

        <Divider/>
        <MenuItem style={styles.buttonStyle}>Search</MenuItem>
        <Divider/>
        <MenuItem style={styles.buttonStyle}>Clear</MenuItem>
        <Divider/>
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
