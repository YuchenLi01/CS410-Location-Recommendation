/* eslint-disable no-undef */

import { ADDWORD, REMOVEWORD, LOADINGQUERY, LOADEDQUERY, RESET, HIGHLIGHT } from '../actions/query-action';

const copyHelper = (obj) => {
  return JSON.parse(JSON.stringify(obj));
}

const compareHelper = (n1, n2) => {
  return Math.abs(n1 - n2) < 0.0000001
}

const defaultState = {
  keywords: ["beer", "drink"],
  resultObj: {},
  heatmapData: [],
  markers: [],
  tweets: [],
  queryInProgress: false,
}

const loadedQuery = (state, resultObj) => {
  return {
    ...state,
    resultObj: resultObj,
    heatmapData: resultObj.heatmapData,
    markers: resultObj.markers,
    tweets: resultObj.tweets,
    queryInProgress: false,
  }
}

const loadingQuery = (state) => {
  return {
    ...state,
    queryInProgress: true,
  }
}

const addWord = (state, curWord) => {
  let newKeywords = state.keywords.slice(); // copy
  newKeywords.push(curWord);
  return {
    ...state,
    keywords: newKeywords
  }
}

const removeWord = (state, curWord) => {
  let newKeywords = state.keywords.filter(e => e !== curWord);
  return {
    ...state,
    keywords: newKeywords
  }
}

const highlight = (state, tweet) => {
  let newMarkers = copyHelper(state.markers);
  for (let i = 0; i < newMarkers.length; i++) {
    let curMarker = newMarkers[i];
    if(compareHelper(tweet.lat, curMarker.position.lat) && compareHelper(tweet.lng, curMarker.position.lng)) {
      curMarker.highlight = true;
    }else {
      curMarker.highlight = false;
    }
  }
  return {
    ...state,
    markers: newMarkers
  }
}

export default function (state, action) {
  switch (action.type) {
    case ADDWORD:
      return addWord(state, action.curWord);
    case REMOVEWORD:
      return removeWord(state, action.curWord);
    case LOADINGQUERY:
      return loadingQuery(state);
    case LOADEDQUERY:
      return loadedQuery(state, action.resultObj);
    case HIGHLIGHT:
      return highlight(state, action.tweet);
    case RESET:
      return defaultState;
    default:
      return defaultState;
  }
}
