/* eslint-disable no-undef */

import { ADDWORD, REMOVEWORD, LOADINGQUERY, LOADEDQUERY, RESET } from '../actions/query-action';

const defaultState = {
  keywords: ["asd", "qwe"],
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
    tweets: resultObj.markers,
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
    case RESET:
      return defaultState;
    default:
      return defaultState;
  }
}
