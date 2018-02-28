import React from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';

import { compose, withProps } from "recompose"
import { withScriptjs, withGoogleMap, GoogleMap, Marker } from "react-google-maps"
import HeatmapLayer from "react-google-maps/lib/components/visualization/HeatmapLayer";

import mapStyle from '../mapStyle.json';

const MapPresenter = withGoogleMap(props => (
  <GoogleMap
    defaultZoom={11}
    defaultCenter={{ lat: 34.0522, lng: -118.2437 }}
    defaultOptions={{ styles: mapStyle }}
  >
    <HeatmapLayer data={props.heatmapData}/>
    {props.markers.map((marker, index) => {
      return (
        <Marker
          key={index}
          position={marker.position}
          icon={marker.highlight ? 'http://maps.google.com/mapfiles/ms/icons/green-dot.png' : 'http://maps.google.com/mapfiles/ms/icons/red-dot.png'}
        >
        </Marker>
      )
    })}
  </GoogleMap>
))

class MapContainer extends React.Component {
  render() {
    return (
      <div>
        <MapPresenter
          containerElement={<div style={{ height: window.innerHeight - 64}} />}
          mapElement={<div style={{ height: "100%" }} />}
          heatmapData={this.props.heatmapData}
          markers={this.props.markers}
        />
      </div>
    )
  }
}

function mapStateToProps(state) {
  return {
    heatmapData: state.queryReducer.heatmapData,
    markers: state.queryReducer.markers,
  };
}

function mapDispatchToPropos(dispatch) {
  return {

  };
}

export default connect(mapStateToProps, mapDispatchToPropos)(MapContainer);
