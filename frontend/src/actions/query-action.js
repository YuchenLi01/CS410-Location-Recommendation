/* eslint-disable no-undef */

export const ADDWORD = 'ADDWORD';
export const REMOVEWORD = 'REMOVEWORD';
export const LOADQUERY = 'LOADQUERY';
export const LOADINGQUERY = 'LOADINGQUERY';
export const LOADEDQUERY = 'LOADEDQUERY';
export const RESET = 'RESET';
google.maps.HeatmapLayer = google.maps.visualization.HeatmapLayer;

const fakeResultObj = {
  result: "received",
  heatmapData: [
    new google.maps.LatLng(34.0522342, -118.2436849),
    new google.maps.LatLng(34.0522342, -118.2436849),
    new google.maps.LatLng(34.0522342, -118.2436849),
  ],
  markers: [
    {
      position: new google.maps.LatLng(34.0522342, -118.2436849),
      highlight: false,
    },

    {
      position: new google.maps.LatLng(34.074182, -118.292773),
      highlight: true,
    },
  ],
  tweets: [],
}

export function addWord(curWord) {
  return {
    type: ADDWORD,
    curWord: curWord,
  }
}

export function removeWord(curWord) {
  return {
    type: REMOVEWORD,
    curWord: curWord,
  }
}

export function reset() {
  return {
    type: RESET,
  }
}

export function loadingQuery() {
  return {
    type: LOADINGQUERY,
  }
}

export function loadedQuery(resultObj) {
  return {
    type: LOADEDQUERY,
    resultObj: resultObj,
  }
}

export function loadQuery() {
  return function(dispatch) {
    dispatch(loadingQuery());
    return setTimeout(() => {
      dispatch(loadedQuery(fakeResultObj))
    }, 100); // just like API, taking time
  }
}
