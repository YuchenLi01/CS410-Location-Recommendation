import React from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';

import { compose, withProps } from "recompose"
import { withScriptjs, withGoogleMap, GoogleMap, Marker } from "react-google-maps"

import mapStyle from '../mapStyle.json';

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
    defaultZoom={11}
    defaultCenter={{ lat: 34.0522, lng: -118.2437 }}
    defaultOptions={{ styles: mapStyle }}
  >
    {/* {props.isMarkerShown && <Marker position={{ lat: -34.397, lng: 150.644 }} onClick={props.onMarkerClick} />} */}
  </GoogleMap>
)

class MapContainer extends React.Component {
  render() {
    return (
      <div>
        <MyMapComponent
        />
      </div>
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

export default connect(mapStateToProps, mapDispatchToPropos)(MapContainer);
