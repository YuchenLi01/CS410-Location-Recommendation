export const ADDWORD = 'ADDWORD';
export const REMOVEWORD = 'REMOVEWORD';
export const LOADQUERY = 'LOADQUERY';
export const LOADINGQUERY = 'LOADINGQUERY';
export const LOADEDQUERY = 'LOADEDQUERY';
export const RESET = 'RESET';

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
      dispatch(loadedQuery({result: "received"}))
    }, 2000); // just like API, taking time
  }
}
