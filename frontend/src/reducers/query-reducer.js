import { ADDWORD, REMOVEWORD, LOADINGQUERY, LOADEDQUERY, RESET } from '../actions/query-action';

const defaultState = {
  keywords: [],
  resultObj: {},
}

const loadedQuery = (state, resultObj) => {
  return {
    ...state,
    resultObj: resultObj
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
      return defaultState;
    case LOADINGQUERY:
      return state;
    case LOADEDQUERY:
      return loadedQuery(state, action.resultObj);
    case RESET:
      return defaultState;
    default:
      return defaultState;
  }
}
