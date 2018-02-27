import React from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';

import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import MenuItem from 'material-ui/MenuItem';
import Drawer from 'material-ui/Drawer';
import AppBar from 'material-ui/AppBar';

const styles = {
  root: {
    marginLeft: '15%',
    paddingTop: '2%',
    paddingLeft: '3%',
    paddingRight: '3%',
  },
};

class Home extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      drawerOpen: true,
      textAlign: "center",
      verticalAlign: "middle",
    }
  }

  toggleDrawer = () => {
    // this.setState({drawerOpen: !this.state.drawerOpen})
  }

  render() {
    return (
      <MuiThemeProvider>
        <div>
          <AppBar
            title="TweetPortal"
            onLeftIconButtonClick={this.toggleDrawer}
          />
          <Drawer open={this.state.drawerOpen} openSecondary={true} width={'15%'}>
            <AppBar
              // title="TweetPortal"
              showMenuIconButton={false}
              // onLeftIconButtonClick={this.toggleDrawer}
            />
            <MenuItem>A tweet</MenuItem>
          </Drawer>
          <div style={styles.root}>
          </div>

        </div>
      </MuiThemeProvider>
    )
  }
}

function mapStateToProps(state) {
  return {

  };
}

function mapDispatchToPropos(dispatch) {
  return {

  };
}

export default connect(mapStateToProps, mapDispatchToPropos)(Home);
