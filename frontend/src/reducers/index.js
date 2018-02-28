import { combineReducers } from 'redux';

import TestReducer from './test-reducer';
import QueryReducer from './query-reducer';

export default combineReducers({
  QueryReducer,
  TestReducer,
});
