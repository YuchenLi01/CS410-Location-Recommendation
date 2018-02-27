const defaultState = {

}

export default function (state, action) {
  switch (action.type) {
    case "TEST":
      return defaultState
    default:
      return defaultState
  }
}
