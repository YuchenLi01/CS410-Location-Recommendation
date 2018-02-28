/* eslint-disable no-undef */

export const ADDWORD = 'ADDWORD';
export const REMOVEWORD = 'REMOVEWORD';
export const LOADQUERY = 'LOADQUERY';
export const LOADINGQUERY = 'LOADINGQUERY';
export const LOADEDQUERY = 'LOADEDQUERY';
export const RESET = 'RESET';
export const HIGHLIGHT = 'HIGHLIGHT';

google.maps.HeatmapLayer = google.maps.visualization.HeatmapLayer;

const fakeResultObj = {
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
      highlight: false,
    },
  ],
  tweets: [
    {
      user: 'username1',
      text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus fringilla egestas quam, vitae molestie ex pharetra et.',
      time: 'Feb 23 12:24',
      lat: 34.074182,
      lng: -118.292773
    },

    {
      user: 'username2',
      text: 'In ac tellus ac nisl placerat pharetra. Proin elementum tortor erat, tincidunt congue quam mattis ut. Sed sollicitudin vestibulum quam, id viverra purus congue sit amet. Suspendisse iaculis elit non tortor fermentum porttitor.',
      time: 'Feb 25 21:32',
      lat: 34.0522342,
      lng: -118.2436849
    },
  ],
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

export function highlight(tweet) {
  return {
    type: HIGHLIGHT,
    tweet: tweet,
  }
}
