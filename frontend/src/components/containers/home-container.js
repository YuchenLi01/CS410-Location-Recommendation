import React from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';

import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import MenuItem from 'material-ui/MenuItem';
import Drawer from 'material-ui/Drawer';
import AppBar from 'material-ui/AppBar';

import { compose, withProps } from "recompose"
import { withScriptjs, withGoogleMap, GoogleMap, Marker } from "react-google-maps"

const MyMapComponent = compose(
  withProps({
    googleMapURL: "https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=geometry,drawing,places",
    loadingElement: <div style={{ height: "100%" }} />,
    containerElement: <div style={{ height: "850px" }} />,
    mapElement: <div style={{ height: "100%" }} />,
  }),
  withScriptjs,
  withGoogleMap
)((props) =>
  <GoogleMap
    defaultZoom={8}
    defaultCenter={{ lat: 34.0522, lng: -118.2437 }}
  >
    {/* {props.isMarkerShown && <Marker position={{ lat: -34.397, lng: 150.644 }} onClick={props.onMarkerClick} />} */}
  </GoogleMap>
)


const styles = {
  root: {
    marginRight: '15%',
    height: '80%',
    // paddingTop: '1%',
    // paddingLeft: '3%',
    // paddingRight: '3%',
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
            <MyMapComponent
            />
            {/* <withGoogleMap>
            <GoogleMap
              googleMapURL={"https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=geometry,drawing,places"}
              loadingElement={<div style={{ height: "100%" }} />}
              containerElement={<div style={{ height: "850px" }} />}
              mapElement={<div style={{ height: "100%" }} />}
              defaultZoom={8}
              defaultCenter={{ lat: 34.0522, lng: -118.2437 }}
            >
            </GoogleMap>
            </withGoogleMap> */}
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
